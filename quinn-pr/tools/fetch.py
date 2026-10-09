#!/usr/bin/env python3
"""Polite public-page fetcher. Usage: fetch.py URL [--links] [--max N]
Honors robots.txt, 1.5s/domain delay (cross-process), caches to ../cache/, never retries blocks.
Prints a header line then readable text. Header: STATUS=<ok|blocked-by-network-policy|robots-disallowed|http-NNN|error> FETCHED=<date> URL=<url>"""
import sys, os, re, json, hashlib, subprocess, time, fcntl, datetime, html
from urllib.parse import urlparse, urljoin
from urllib import robotparser
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "cache"); os.makedirs(os.path.join(CACHE, ".last"), exist_ok=True)
UA = "QuinnPRResearchBot/1.0 (+https://meetquinn.ai; editorial-policy research, contact nandlal@meetquinn.ai)"
DELAY = 1.5

def wait_turn(dom):
    p = os.path.join(CACHE, ".last", dom)
    with open(p, "a+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.seek(0); s = f.read().strip()
        last = float(s) if s else 0
        w = DELAY - (time.time() - last)
        if w > 0: time.sleep(w)
        f.seek(0); f.truncate(); f.write(str(time.time())); f.flush()
        fcntl.flock(f, fcntl.LOCK_UN)

def curl(url):
    dom = urlparse(url).netloc
    wait_turn(dom)
    r = subprocess.run(["curl","-sS","-L","--max-time","25","--max-filesize","3000000","-A",UA,"-D","-","-o","-",url],
                       capture_output=True)
    out = r.stdout
    # split last header block
    parts = out.split(b"\r\n\r\n")
    hdrs, body, i = b"", out, 0
    while out.startswith(b"HTTP/"):
        h, _, rest = out.partition(b"\r\n\r\n")
        hdrs, out = h, rest
        if not out.startswith(b"HTTP/"): break
    return hdrs.decode("latin1"), out, r.returncode, r.stderr.decode("latin1")

def robots_ok(url):
    u = urlparse(url); ru = f"{u.scheme}://{u.netloc}/robots.txt"
    c = cached(ru)
    if c is None:
        h, b, rc, err = curl(ru)
        m = re.match(r"HTTP/\S+ (\d+)", h)
        code = int(m.group(1)) if m else 0
        c = {"status": code, "body": b.decode("utf-8","replace") if code == 200 else ""}
        store(ru, c)
    if c["status"] != 200: return True  # no robots / unreadable => allowed
    rp = robotparser.RobotFileParser(); rp.parse(c["body"].splitlines())
    return rp.can_fetch(UA, url) and rp.can_fetch("*", url)

def key(url): return os.path.join(CACHE, hashlib.sha1(url.encode()).hexdigest()+".json")
def cached(url):
    try: return json.load(open(key(url)))
    except Exception: return None
def store(url, d):
    d["url"] = url; d.setdefault("fetched", datetime.date.today().isoformat())
    json.dump(d, open(key(url), "w"))

class T(HTMLParser):
    def __init__(s, base):
        super().__init__(); s.out=[]; s.skip=0; s.base=base; s.href=None; s.links=[]
    def handle_starttag(s, t, a):
        a = dict(a)
        if t in ("script","style","noscript","svg","head"): s.skip += 1
        if t in ("p","div","br","li","h1","h2","h3","h4","tr","section","article"): s.out.append("\n")
        if t == "a" and a.get("href"):
            s.href = urljoin(s.base, a["href"])
            if "cf-email" in (a.get("class") or "") or "email-protection" in a["href"]:
                s.out.append(" [obfuscated - see page] ")
            if a["href"].startswith("mailto:"): s.out.append(f" [mailto:{a['href'][7:].split('?')[0]}] ")
        if t == "meta" and a.get("name") in ("description","date","article:published_time") : s.out.append(f"\n[meta {a.get('name')}: {a.get('content')}]\n")
        if t == "meta" and a.get("property") in ("article:published_time","article:modified_time","og:updated_time"): s.out.append(f"\n[meta {a.get('property')}: {a.get('content')}]\n")
        if t == "time" and a.get("datetime"): s.out.append(f" [time {a['datetime']}] ")
    def handle_endtag(s, t):
        if t in ("script","style","noscript","svg","head") and s.skip: s.skip -= 1
        if t == "a" and s.href: s.links.append(s.href); s.href=None
    def handle_data(s, d):
        if not s.skip and d.strip(): s.out.append(d.strip()+" ")

def main():
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    url = a[0]; links = "--links" in a
    mx = int(a[a.index("--max")+1]) if "--max" in a else 20000
    c = cached(url)
    if c is None:
        if not robots_ok(url):
            c = {"status":"robots-disallowed","text":"","links":[]}
        else:
            h, b, rc, err = curl(url)
            m = re.match(r"HTTP/\S+ (\d+)", h); code = int(m.group(1)) if m else 0
            if code == 403 and re.search(r"x-deny-reason", h, re.I) or "CONNECT tunnel failed" in err:
                c = {"status":"blocked-by-network-policy","text":"","links":[]}
            elif code != 200:
                c = {"status": f"http-{code}" if code else "error", "text": err[:200], "links":[]}
            else:
                txt = b.decode("utf-8","replace")
                ctype = re.search(r"content-type:\s*([^\r\n;]+)", h, re.I)
                if ctype and "html" not in ctype.group(1).lower():
                    c = {"status":"ok","text":txt[:200000],"links":[]}
                else:
                    p = T(url); p.feed(txt)
                    t = html.unescape("".join(p.out)); t = re.sub(r"\n\s*\n+","\n",t)
                    c = {"status":"ok","text":t,"links":list(dict.fromkeys(p.links))}
        store(url, c)
    print(f"STATUS={c['status']} FETCHED={c['fetched']} URL={url}")
    print(c["text"][:mx])
    if links and c["links"]:
        print("\n--- LINKS ---"); print("\n".join(c["links"][:300]))
main()

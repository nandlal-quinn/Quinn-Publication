#!/usr/bin/env python3
"""Merge research/*.csv -> master.csv (schema cols + derived cols). Deterministic; re-run any time."""
import csv, glob, re, os, json
from urllib.parse import urlparse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA = "name,url,industry,tier,audience,circulation_or_subs,content_types,typical_length,guidelines_url,contact_name,contact_email_or_form,cost,editorial_rules,relevance_1_5,suggested_angle,last_content_date,source_urls,status".split(",")
EXTRA = ["rank","score","flags","deadline","also_listed_as"]
TODAY = "2026-10-09"; CUTOFF = "2025-10-09"
LABEL = {  # normalise agent labels
 "Trade Schools / Technical Education":"Trade Schools",
 "Adjacent (Plumbing/Electrical/Home Services/FSM/Workforce/L&D)":"Adjacent (plumbing, electrical, home services, FSM, workforce, L&D)"}
rows = []
for f in sorted(glob.glob(f"{ROOT}/research/*.csv")):
    for r in csv.DictReader(open(f, encoding="utf-8")):
        r["industry"] = LABEL.get(r["industry"].strip(), r["industry"].strip()); r["_src"] = os.path.basename(f)
        rows.append(r)
dropped = [r for r in rows if r["url"].strip().lower() in ("not found","") ]
rows = [r for r in rows if r not in dropped]

def host(u): return urlparse(u).netloc.lower().removeprefix("www.")
def depth0(u): return urlparse(u).path.strip("/") == ""
def first(n): return re.sub(r"[^a-z0-9 ]","",n.lower()).split()[0]
SR = {"verified":3,"unverified":2,"blocked-by-network-policy":1,"inactive":0,"paywalled":1}
def nkey(n): return re.sub(r"[^a-z0-9]","",re.sub(r"\(.*","",n.lower()))
def ukey(r):
    u = r["url"]
    return host(u) if depth0(u) and False else u.rstrip("/").lower().removeprefix("https://").removeprefix("http://").removeprefix("www.")
parent = list(range(len(rows)))
def find(i):
    while parent[i]!=i: parent[i]=parent[parent[i]]; i=parent[i]
    return i
seen = {}
for i,r in enumerate(rows):
    ks = [("n",nkey(r["name"])),("u",ukey(r))]
    if depth0(r["url"]): ks.append(("h",host(r["url"])+"|"+first(r["name"])))
    for k in ks:
        if k in seen: parent[find(i)] = find(seen[k])
        else: seen[k] = i
groups = {}
for i,r in enumerate(rows): groups.setdefault(find(i), []).append(r)
merged = []
for g in groups.values():
    g.sort(key=lambda r: (SR.get(r["status"],0), len(r["editorial_rules"])), reverse=True)
    p = dict(g[0]); inds = []; 
    for r in g:
        for i in r["industry"].split("; "):
            if i not in inds: inds.append(i)
    p["industry"] = "; ".join(inds)
    p["relevance_1_5"] = str(max(int(r["relevance_1_5"] or 0) for r in g))
    p["also_listed_as"] = " | ".join(r["name"] for r in g[1:] if r["name"] != p["name"])
    merged.append(p)

FIXES = [  # agent-written pitch titles that stated numbers Quinn has not published
 ("Training 400+ roofing crews without hiring trainers","Training roofing crews without hiring trainers"),
 ("400-employee-scale trades op","446-employee trades op"),
 ("what a 3-day course launch taught a 446-person pest company","what a 446-person pest company learned rolling out 226 courses"),
 ("an 446-employee","a 446-employee")]
for p in merged:
    for a,b in FIXES: p["suggested_angle"] = p["suggested_angle"].replace(a,b)
UNCACHED_EMAILS = ["editor@clomedia.com","help@mcaa.org","ifma@ifma.org","jrose@automate.org"]  # not found in any fetched page text
for p in merged:
    for e in UNCACHED_EMAILS:
        if e in p["contact_email_or_form"] and "not read on the outlet's page" not in p["contact_email_or_form"]:
            p["contact_email_or_form"] += f" [{e}: not found in any page text fetched by this run (likely search snippet); confirm on the outlet's site]"
            if p["status"] == "verified" and e in p["contact_email_or_form"].split("[")[0] and False: pass
def ym(s):
    m = re.match(r"(\d{4})-(\d{2})(?:-(\d{2}))?", s.strip()); return m.group(0) if m else None
for p in merged:  # stale => inactive
    d = ym(p["last_content_date"])
    p["_stale"] = bool(d and d < CUTOFF[:len(d)] ) 
    if p["_stale"] and p["status"] != "inactive": p["status"] = "inactive"; p["editorial_rules"] += f" [merge: last content {d} is >12 months old, set inactive]"
    p["_nodate"] = d is None

COMPETITOR = re.compile(r"Restoration Playbook|Smart Buildings Academy", re.I)
SW_BAN = re.compile(r"^(FacilitiesNet|Building Operating Management|Healthcare Facilities Today)", re.I)
VENDOR = re.compile(r"VENDOR BAN|bans? (vendor|company)|rejects? (product|vendor)|vendor-neutral|non-?promotional|no (sales|product|company|commercial|promotion)|not accept[^.]{0,60}(vendor|product|software)|no vendor|product-neutral|no references to products|commercial language|without (sales|product)", re.I)
AI = re.compile(r"(bans?|banned|prohibit\w*|no|not)\s+(generative\s+)?AI|NOT AI-generated|AI[- ]generated|generative AI|\d+%\s*(of )?(AI|content)|AI (cap|disclos|policy:)|AI use|disclos\w+ (of )?AI|AI (content )?(is )?(not |never )", re.I)
EXCL = re.compile(r"EXCLUSIVE|exclusive to|exclusivity (for|of|period|across|window)|\d+-?\s?(day|month)s? exclusiv|first-run|must be exclusive|original, unpublished", re.I)
DEADLINE = [("RIA International Restoration Convention","2026-10-16 (convention call for presentations closes)"),
            ("IEC Business Summit","2026-11-06 (call for content closes)"),
            ("ACTE Techniques","2026-12-01 (proposals for Mar/Apr 2027 issue)")]
for p in merged:
    f = []
    if SW_BAN.match(p["name"]): f.append("software-vendor-ban")
    if COMPETITOR.search(p["name"]): f.append("competitor")
    if VENDOR.search(p["editorial_rules"]) and "software-vendor-ban" not in f: f.append("vendor-restricted")
    if AI.search(p["editorial_rules"]) and not re.search(r"AI policy not found", p["editorial_rules"]) : f.append("ai-policy")
    if EXCL.search(p["editorial_rules"]): f.append("exclusivity")
    if p["status"] == "inactive": f.append("inactive")
    if p["status"] == "blocked-by-network-policy": f.append("blocked")
    if p["_nodate"] and p["status"] != "inactive": f.append("recency-unconfirmed")
    if re.search(r"paywall|subscriber[- ]only|members?[- ]only", p["editorial_rules"]+p["cost"], re.I) or p["status"]=="paywalled": f.append("paywall/members-only?")
    p["flags"] = "; ".join(f)
    p["deadline"] = next((d for n,d in DEADLINE if p["name"].startswith(n)), "")
    contact = p["contact_email_or_form"].strip().lower() not in ("not found","")
    s = int(p["relevance_1_5"])*10 + {"verified":12,"unverified":0}.get(p["status"],-6) + (5 if p["tier"]=="free" else 0) + (2 if contact else 0)
    s += (-25 if "software-vendor-ban" in f else 0) + (-4 if "vendor-restricted" in f else 0) + (-3 if "ai-policy" in f else 0) + (-2 if "exclusivity" in f else 0)
    s += (4 if p["deadline"] else 0) + (-3 if "recency-unconfirmed" in f else 0)
    p["score"] = s
    p["_rankable"] = not ({"competitor","inactive"} & set(f))
rk = sorted([p for p in merged if p["_rankable"]], key=lambda p: -p["score"])
for i,p in enumerate(rk,1): p["rank"] = i
for p in merged:
    p.setdefault("rank","")
merged.sort(key=lambda p: (p["rank"]=="", p["rank"] if p["rank"] else 0, p["name"]))
with open(f"{ROOT}/master.csv","w",newline="",encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=SCHEMA+EXTRA, extrasaction="ignore"); w.writeheader(); w.writerows(merged)
json.dump({"dropped":[(r["name"],r["_src"]) for r in dropped],"input_rows":len(rows)+len(dropped)}, open(f"{ROOT}/research/_merge_meta.json","w"))
print("input",len(rows)+len(dropped),"dropped(no url)",len(dropped),"master",len(merged),"ranked",len(rk))

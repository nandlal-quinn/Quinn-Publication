#!/usr/bin/env python3
import csv, json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = list(csv.DictReader(open(f"{ROOT}/master.csv", encoding="utf-8")))
data = json.dumps(rows, ensure_ascii=False).replace("</", "<\\/")
html = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Quinn PR targets</title>
<style>
:root{--bg:#fff;--fg:#1b1f24;--mut:#5d6773;--line:#d9dee4;--hd:#f3f5f7;--acc:#0b5fff;--ok:#157f3b;--warn:#a15c00;--bad:#b42318}
@media(prefers-color-scheme:dark){:root{--bg:#14171a;--fg:#e7eaee;--mut:#9aa5b1;--line:#2c333a;--hd:#1c2126;--acc:#6ea2ff;--ok:#4cc17a;--warn:#e0a24a;--bad:#ff7b6e}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:14px/1.4 system-ui,sans-serif}
header{padding:14px 16px;border-bottom:1px solid var(--line)}h1{margin:0 0 2px;font-size:18px}.sub{color:var(--mut);font-size:12px}
.bar{display:flex;flex-wrap:wrap;gap:8px;padding:10px 16px;border-bottom:1px solid var(--line);background:var(--hd);position:sticky;top:0;z-index:3}
.bar input,.bar select,.bar button{font:inherit;padding:5px 8px;border:1px solid var(--line);border-radius:6px;background:var(--bg);color:var(--fg)}
.bar input[type=search]{min-width:220px;flex:1}.wrap{overflow:auto;padding:0 16px 24px}
table{border-collapse:collapse;width:100%;min-width:980px}th,td{border-bottom:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}
th{position:sticky;top:50px;background:var(--hd);cursor:pointer;white-space:nowrap;user-select:none;z-index:2}th.s-asc::after{content:" \25B2"}th.s-desc::after{content:" \25BC"}
tr.row{cursor:pointer}tr.row:hover{background:var(--hd)}td.n a{color:var(--acc);font-weight:600;text-decoration:none}
.tag{display:inline-block;padding:0 6px;margin:1px 2px 1px 0;border:1px solid var(--line);border-radius:10px;font-size:11px;color:var(--mut)}
.verified{color:var(--ok)}.unverified{color:var(--warn)}.inactive,.blocked-by-network-policy,.paywalled{color:var(--bad)}
.tag.sw,.tag.competitor,.tag.inactive,.tag.blocked{color:var(--bad);border-color:var(--bad)}.tag.ai-policy,.tag.exclusivity,.tag.vendor-restricted{color:var(--warn);border-color:var(--warn)}
tr.det td{background:var(--hd)}.det dl{margin:0;display:grid;grid-template-columns:150px 1fr;gap:4px 12px}.det dt{color:var(--mut)}.det dd{margin:0;word-break:break-word}
.cnt{margin-left:auto;color:var(--mut);align-self:center}
</style></head><body>
<header><h1>Quinn PR targets: trades publications &amp; podcasts</h1>
<div class="sub">Source: master.csv, built 2026-10-09. Click a column to sort, a row for details. "unverified" rows are leads, not confirmed facts. No external dependencies.</div></header>
<div class="bar">
<input type="search" id="q" placeholder="Search all fields (name, rules, angle, contact)…">
<select id="fi"><option value="">All industries</option></select>
<select id="ft"><option value="">Free + paid</option><option>free</option><option>paid</option></select>
<select id="fs"><option value="">All statuses</option><option>verified</option><option>unverified</option><option>blocked-by-network-policy</option><option>inactive</option><option>paywalled</option></select>
<select id="fr"><option value="0">Any relevance</option><option value="5">Relevance 5</option><option value="4">Relevance 4+</option><option value="3">Relevance 3+</option></select>
<select id="fg"><option value="">Any flags</option><option value="!">No flags</option><option>software-vendor-ban</option><option>vendor-restricted</option><option>ai-policy</option><option>exclusivity</option><option>competitor</option><option>inactive</option><option>blocked</option><option>recency-unconfirmed</option></select>
<label><input type="checkbox" id="hide"> hide inactive/competitor</label>
<button id="dl">Download CSV (filtered)</button><span class="cnt" id="cnt"></span></div>
<div class="wrap"><table><thead><tr id="hr"></tr></thead><tbody id="tb"></tbody></table></div>
<script>
const DATA=__DATA__;
const COLS=[["rank","#","num"],["name","Outlet"],["industry","Industry"],["tier","Tier"],["relevance_1_5","Rel","num"],["status","Status"],["flags","Flags"],["contact_email_or_form","Contact route"],["cost","Cost"],["last_content_date","Last content"],["deadline","Deadline"]];
const FIELDS=["name","url","industry","tier","audience","circulation_or_subs","content_types","typical_length","guidelines_url","contact_name","contact_email_or_form","cost","editorial_rules","relevance_1_5","suggested_angle","last_content_date","source_urls","status","rank","score","flags","deadline","also_listed_as"];
const $=id=>document.getElementById(id);let sk="rank",sd=1,open=new Set();
const inds=[...new Set(DATA.flatMap(r=>r.industry.split(";").map(s=>s.trim())))].sort();
inds.forEach(i=>{const o=document.createElement("option");o.textContent=i;$("fi").appendChild(o)});
$("hr").innerHTML=COLS.map(c=>`<th data-k="${c[0]}" data-t="${c[2]||""}">${c[1]}</th>`).join("");
const esc=s=>String(s??"").replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const linkify=s=>esc(s).replace(/(https?:\/\/[^\s|)<]+)/g,'<a href="$1" target="_blank" rel="noopener noreferrer">$1</a>');
function val(r,k,num){let v=r[k];if(num){v=parseFloat(v);return isNaN(v)?(k==="rank"?1e9:-1):v}return String(v||"").toLowerCase()}
function filtered(){const q=$("q").value.toLowerCase(),fi=$("fi").value,ft=$("ft").value,fs=$("fs").value,fr=+$("fr").value,fg=$("fg").value,h=$("hide").checked;
return DATA.filter(r=>{if(fi&&!r.industry.split(";").map(s=>s.trim()).includes(fi))return false;if(ft&&r.tier!==ft)return false;if(fs&&r.status!==fs)return false;
if(+r.relevance_1_5<fr)return false;if(fg==="!"?r.flags:fg&&!r.flags.includes(fg))return false;if(h&&/inactive|competitor/.test(r.flags))return false;
return !q||FIELDS.some(k=>String(r[k]||"").toLowerCase().includes(q))})}
function flagTags(f){return f.split(";").map(s=>s.trim()).filter(Boolean).map(s=>`<span class="tag ${s.includes("ban")?"sw":s.split("/")[0]}">${esc(s)}</span>`).join("")}
function render(){const t=COLS.find(c=>c[0]===sk)?.[2]==="num";const rs=filtered().sort((a,b)=>{const x=val(a,sk,t),y=val(b,sk,t);return(x<y?-1:x>y?1:0)*sd});
$("cnt").textContent=rs.length+" of "+DATA.length+" outlets";
document.querySelectorAll("th").forEach(th=>th.className=th.dataset.k===sk?(sd>0?"s-asc":"s-desc"):"");
$("tb").innerHTML=rs.map((r,i)=>{const id=r.name+r.url,o=open.has(id);
let h=`<tr class="row" data-id="${esc(id)}"><td>${esc(r.rank)}</td><td class="n"><a href="${esc(r.url)}" target="_blank" rel="noopener noreferrer">${esc(r.name)}</a></td><td>${esc(r.industry)}</td><td>${esc(r.tier)}</td><td>${esc(r.relevance_1_5)}</td><td class="${esc(r.status)}">${esc(r.status)}</td><td>${flagTags(r.flags)}</td><td>${esc(r.contact_email_or_form)}</td><td>${esc(r.cost)}</td><td>${esc(r.last_content_date)}</td><td>${esc(r.deadline)}</td></tr>`;
if(o)h+=`<tr class="det"><td colspan="${COLS.length}"><dl>${["suggested_angle","editorial_rules","audience","circulation_or_subs","content_types","typical_length","guidelines_url","contact_name","also_listed_as","source_urls"].map(k=>`<dt>${k}</dt><dd>${linkify(r[k])}</dd>`).join("")}</dl></td></tr>`;return h}).join("")}
$("hr").onclick=e=>{const k=e.target.dataset?.k;if(!k)return;sd=(sk===k)?-sd:1;sk=k;render()};
$("tb").onclick=e=>{if(e.target.tagName==="A")return;const tr=e.target.closest("tr.row");if(!tr)return;const id=tr.dataset.id;open.has(id)?open.delete(id):open.add(id);render()};
["q","fi","ft","fs","fr","fg","hide"].forEach(i=>$(i).addEventListener("input",render));
$("dl").onclick=()=>{const q=s=>'"'+String(s??"").replace(/"/g,'""')+'"';const csv=[FIELDS.map(q).join(",")].concat(filtered().map(r=>FIELDS.map(k=>q(r[k])).join(","))).join("\n");
const a=document.createElement("a");a.href=URL.createObjectURL(new Blob([csv],{type:"text/csv"}));a.download="quinn-pr-filtered.csv";a.click()};
render();
</script></body></html>'''
open(f"{ROOT}/index.html", "w", encoding="utf-8").write(html.replace("__DATA__", data))
print(os.path.getsize(f"{ROOT}/index.html"))

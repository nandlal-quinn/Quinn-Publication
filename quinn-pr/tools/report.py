#!/usr/bin/env python3
"""Build report.md from master.csv (tables are generated; narrative is inline)."""
import csv, os, re, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = list(csv.DictReader(open(f"{ROOT}/master.csv", encoding="utf-8")))
def esc(s, n=None):
    s = re.sub(r"\s+", " ", s or "").replace("|", "/").strip()
    return (s[:n-1].rstrip() + "…") if n and len(s) > n else s
CORE = ["HVAC","Pest Control","Mechanical Contracting","Facilities Maintenance","Roofing","Landscaping","Restoration","Trade Schools"]
QUINN_LISTED = ["Building Automation","Fire and Life Safety","Industrial Automation"]
ADJ = "Adjacent (plumbing, electrical, home services, FSM, workforce, L&D)"
ORDER = CORE + QUINN_LISTED + [ADJ]
live = [r for r in rows if "inactive" not in r["flags"]]
def inds(r): return [i.strip() for i in r["industry"].split(";")]
def route(r):
    c = r["contact_email_or_form"]; return esc(c, 70) if c.strip().lower() != "not found" else "not found"
def src1(r):
    m = re.search(r"https?://\S+", r["source_urls"]); return m.group(0).rstrip("|);,") if m else ""
out = []; w = out.append
cnt = collections.Counter(r["status"] for r in rows)
w("# Quinn PR & content-distribution targets (trades): research report")
w(f"\nBuilt 2026-10-09 from `master.csv` ({len(rows)} unique outlets merged from 244 research rows across 12 industry passes). Facts were read from each publication's own pages with a polite fetcher (robots.txt honored, 1.5s/domain delay, cached to `cache/`). Status counts: "
  + ", ".join(f"{v} {k}" for k, v in cnt.most_common()) + ".")
w("\n**How to read status.** `verified` = the research agent read that outlet's own page text. `unverified` = page unreadable (403, bot-check, empty render, PDF) or the facts came from search snippets/aggregators; treat every unverified row as a lead, not a fact. `blocked-by-network-policy` = this environment's network policy denied the host; not worked around. `inactive` = no content in the last 12 months (since 2025-10-09). Nothing is invented: unknown prices, editors and emails are `not found`; obfuscated emails say `obfuscated - see page`.")
w("\n**Quinn facts used** come from `context.md` (supplied by Quinn, copied from meetquinn.ai). meetquinn.ai renders client-side, so this run could confirm only page meta descriptions, including the White Knight line \"cut technician attrition costs by $1M a year with Quinn. 97% workforce participation, 96% course completion\". Founder/exec names were not available to me; pitches below say \"Quinn exec\" and need a named byline holder.")

# --- 1. master ranked
w("\n## 1. Master list: best first move (ranked)\n")
w("Score = fit (relevance x10) + verified read (+12) + free route (+5) + a public contact route (+2) + open deadline (+4); minus software-vendor ban (-25), vendor/promo restriction (-4), AI-policy (-3), exclusivity (-2), recency unconfirmed (-3), unread/blocked (-6). Competitors and inactive outlets are excluded from the ranking (see section 4). The score is a heuristic for ordering, not a prediction.\n")
w("| # | Outlet | Industry | Tier | Rel | Status | Route (as listed publicly) | Flags | Deadline | First move |")
w("|---|---|---|---|---|---|---|---|---|---|")
for r in [x for x in rows if x["rank"]][:40]:
    w(f"| {r['rank']} | {esc(r['name'],55)} | {esc(r['industry'],40)} | {r['tier']} | {r['relevance_1_5']} | {r['status']} | {route(r)} | {esc(r['flags'])} | {esc(r['deadline'])} | {esc(r['suggested_angle'],230)} |")
w("\nFull ranked list (all 204 rankable outlets) is in `master.csv` (`rank` column) and `index.html`.")

# --- 2. per-industry
w("\n## 2. Summary by industry\n")
w("Sorted by relevance (5 first), then free before paid, then verified before unverified. Outlets in several industries appear in each. Inactive outlets are omitted here (see section 4). Targets were 10-15 Tier 1 (relevance 4-5) and 5-8 Tier 2 (relevance 2-3) per core industry.\n")
for ind in ORDER:
    rs = [r for r in live if ind in inds(r)]
    rs.sort(key=lambda r: (-int(r["relevance_1_5"]), r["tier"] != "free", r["status"] != "verified", r["name"]))
    t1 = sum(int(r["relevance_1_5"]) >= 4 for r in rs); t2 = sum(2 <= int(r["relevance_1_5"]) <= 3 for r in rs)
    t1v = sum(int(r["relevance_1_5"]) >= 4 and r["status"] == "verified" for r in rs)
    kind = "core" if ind in CORE else "Quinn-listed" if ind in QUINN_LISTED else "adjacent"
    w(f"\n### {ind} ({kind}): {len(rs)} live outlets; Tier 1 (rel 4-5): {t1} ({t1v} verified); Tier 2 (rel 2-3): {t2}\n")
    w("| Outlet | Tier | Rel | Status | Contact route | Cost | Flags | Last content |")
    w("|---|---|---|---|---|---|---|---|")
    for r in rs:
        w(f"| [{esc(r['name'],60)}]({r['url']}) | {r['tier']} | {r['relevance_1_5']} | {r['status']} | {route(r)} | {esc(r['cost'],60)} | {esc(r['flags'])} | {esc(r['last_content_date'],18)} |")

# --- 3. angles
w("""
## 3. Five repurposable article angles (built from Quinn's real proof points)

Rules for all five: human-written and disclosed where an outlet requires it (many ban or cap AI text, see section 4); vendor-neutral body, Quinn named only in the byline/bio; customer data and quotes only with the customer's written approval; Quinn benchmarks labeled as Quinn benchmarks. Pitch one outlet per sibling group at a time (exclusivity table, section 4).

**Angle 1: "What 97% participation looks like: rolling out training to a 446-person pest control company"** (case study)
- Proof: White Knight Pest Control: 446 employees, 226 courses, 97% workforce participation, 96% completion (meetquinn.ai/results/white-knight).
- Shape: ops-leader-voiced story (White Knight co-byline or as-told-to), 800-1,500 words: why they started, how courses were built from existing SOPs, what drove participation. Needs White Knight's sign-off.
- Best fits: PCT, PMP, PestWorld (NPMA), Pest Control Millionaire/Bug Bux podcasts; trimmed versions for Roofing Contractor/Contracting Business as "lessons for other trades".

**Angle 2: "The $1M question: what technician attrition really costs a service company"** (data/thought-leadership)
- Proof: the White Knight results page states technician attrition costs were cut by $1M a year (page meta). Quinn benchmark: ~20% lower turnover (Quinn-reported).
- Shape: vendor-neutral cost-of-turnover framework (replacement cost, ramp, lost revenue) with White Knight as the worked example. Strong for owners/GMs.
- Best fits: ACHR News guest column (lead with a contractor co-author; ACHR is "highly selective" on AI/software pitches), Contracting Business Best Practices, Roofing Contractor Guest Column, Construction Executive, IndustryWeek Talent.

**Angle 3: "Your best tech's knowledge is trapped in their head"** (how-to)
- Proof: Quinn's core theme; SOPs, videos and call recordings become courses and roleplay; 3 days to launch; 0 new trainers needed (Quinn-reported).
- Shape: 5-step playbook for capturing tribal knowledge (ride-along recordings, SOP gaps, scenario roleplay, mid-job answers) with no product references. Strong for training managers and ops.
- Best fits: BUILDINGS (vendor-neutral, 90-day exclusivity), CONTRACTOR (case-study/Best Practices, 20% AI cap), Plant Services/Reliable Plant (maintenance training), AutomatedBuildings.com (technician skill-set series), Training Magazine/Training Industry (no product mentions).

**Angle 4: "Measuring ramp time: how to know when a new hire is actually ready"** (framework)
- Proof: ~40% faster ramp and 94% completion (Quinn benchmarks); readiness scored by person, role, branch and skill.
- Shape: define "ready" by skill, score it, compare branches, fix drift. Include a simple worksheet; cite benchmarks as Quinn-reported.
- Best fits: Training Industry, Chief Learning Officer, Training Magazine, IFMA FMJ (non-advertorial abstract, 1,250-2,000 words), NALP Edge blog (ELEVATE 2027 session pitch with a customer operator), IEC Business Summit (owner-level workshop, call closes 2026-11-06).

**Angle 5: "Prove graduates can do the job"** (education/workforce)
- Proof: trade-school positioning on meetquinn.ai (instructors and program directors prove graduates can do the job; employers get a hiring signal); UTI is a named customer. Do not claim UTI outcomes without their approval.
- Shape: how programs can use scenario-based assessment and competency maps to give employers a trustworthy signal; co-byline with a school partner if UTI agrees.
- Best fits: ACTE Techniques (proposal for Mar/Apr 2027 closes 2026-12-01), Career Education Review (CECU), Community College Daily, NCCER newsroom; Inside Higher Ed/EdSurge require AI and ed-tech affiliation disclosure; Higher Ed Dive bans generative AI in op-eds.
""")

# --- 4. flags
def lst(title, rs, note=""):
    w(f"\n### {title} ({len(rs)})\n"); 
    if note: w(note + "\n")
    for r in rs: w(f"- **{esc(r['name'],70)}** ({esc(r['industry'],40)}; {r['status']}): {esc(r['editorial_rules'],260) if 'flags' else ''} [{src1(r)}]")
w("## 4. Flagged outlets")
w("\n### Sibling-outlet exclusivity (pitch one per group per piece)\n")
w("""Parent companies below are as reported on the outlets' own pages by the research agents unless marked unconfirmed. Re-check before pitching.

| Parent / group | Outlets in this list | Rule seen |
|---|---|---|
| Endeavor Business Media | Contracting Business, CONTRACTOR (parent not text-verified on its own page), BUILDINGS, Plant Services, IndustryWeek, Automation World, Control Design, EC&M, Pro Remodeler, EHS Today, SecurityInfoWatch/Security Business | Each title exclusive (Contracting Business and CONTRACTOR: exclusive, 20% AI cap); BUILDINGS 90-day exclusivity; no cross-brand rule stated for IndustryWeek family, but do not shop one piece to several |
| BNP Media | ACHR News, Plumbing & Mechanical, Engineered Systems (ES NEWS), Restoration & Remediation, Roofing Contractor, Maintenance Sales News | ACHR guest columns exclusive and product-neutral; coordinate HVAC, restoration and roofing pitches |
| Trade Press Media Group | FacilitiesNet, Building Operating Management, Facility Maintenance Decisions, Healthcare Facilities Today | One set of contributed-content rules; articles exclusive; **software providers banned** |
| Informa TechTarget / Industry Dive | Construction Dive, Facilities Dive, Higher Ed Dive, Education Dive, HR Dive, Workforce Dive | Shared opinion rules: exclusivity (Construction Dive 30 days) and **generative AI banned in op-eds**; Higher Ed Dive and Education Dive share one opinion form |
| WTWH Media / Arrowfly (name differs between guidelines and site footer) | Plant Engineering, Control Engineering, Consulting-Specifying Engineer | One piece exclusive across all three |
| GIE Media | Lawn & Landscape, Golf Course Industry (PMP/PCT parent unconfirmed: seed says GIE Media, a third-party listing says North Coast Media) | Landscape Management parent unconfirmed: pitch it or Lawn & Landscape, not both |
| Training Industry Inc. | Training Industry, Chief Learning Officer | Siblings; AI text and product mentions prohibited |
| Emerald | Security Sales & Integration | 4-month exclusivity after publication |
| NRCA | Professional Roofing, RoofTalk | Same association; coordinate |
| Campus Technology / THE Journal | siblings | Coordinate |
""")
lst("Software-vendor bans / vendor-restricted (Quinn is a software company)", [r for r in rows if "software-vendor-ban" in r["flags"]],
    "Hard bans. Quinn's routes there are paid Branded Features or a customer-authored byline. Soft restrictions (\"vendor-restricted\" flag, e.g. ACHR News 'highly selective' on AI/software, ACCA no-sales-pitch, RIA non-proprietary, University Business rejects product/case-study content, Consulting-Specifying Engineer rejects vendor-focused articles, DRJ and Claims Journal ban company mentions) are in the `flags` and `editorial_rules` columns of `master.csv`.")
ai = [r for r in rows if "ai-policy" in r["flags"] and "inactive" not in r["flags"]]
w(f"\n### AI-content policies (Quinn is an AI company): {len(ai)} outlets mention one\n")
w("Hard or notable ones: Higher Ed Dive, Construction Dive, Facilities Dive and HR Dive ban generative AI in op-eds; Contracting Business and CONTRACTOR cap AI at 20% (Contracting Business requires disclosure); IndustryWeek caps AI at 10% with disclosure; Training Industry prohibits AI-generated text; EHS Today: no AI-written articles; Inside Higher Ed and EdSurge require disclosure; ASHRAE prohibits entering its content into AI tools; ACHR News is highly selective on AI pitches. Full per-outlet text is in `editorial_rules`. Flag matched by keyword; verify against the cited source before relying on it.\n")
lst("Competitors (do not pitch)", [r for r in rows if "competitor" in r["flags"]])
lst("Inactive (no content in last 12 months)", [r for r in rows if "inactive" in r["flags"]])
lst("Blocked by network policy", [r for r in rows if "blocked" in r["flags"]], "Recorded and not worked around; retry from an environment where the host is allowed.")
pw = [r for r in rows if "paywall/members-only?" in r["flags"]]
w(f"\n### Possible paywall/members-only language ({len(pw)}; keyword match, verify)\n")
for r in pw: w(f"- {esc(r['name'],70)}: cost/rules mention paywall or members-only. [{src1(r)}]")
w("\n### Time-sensitive\n")
for r in [x for x in rows if x["deadline"]]: w(f"- **{esc(r['name'],80)}**: {r['deadline']}. [{src1(r)}]")
w("- Several 2026 conference speaker calls already closed (IFMA World Workplace, SMRP, International Roofing Expo 2027 closed 2026-04-18, TICE 2027 closed 2026-10-02); the next windows are spring 2027. PestWorld's Technology Adopter Award reopens spring 2027 (White Knight is a natural nominee).")

# --- 5. gaps
unv = [r for r in rows if r["status"] == "unverified" and "inactive" not in r["flags"] and int(r["relevance_1_5"]) >= 4]
w("\n## 5. Gaps remaining\n")
w("**Tier-1 shortfalls (relevance 4-5 outlets, live), versus the 10-15 target:** " + "; ".join(
    f"{i}: {sum(int(r['relevance_1_5'])>=4 for r in live if i in inds(r))} ({sum(int(r['relevance_1_5'])>=4 and r['status']=='verified' for r in live if i in inds(r))} verified)" for i in CORE) + ". Several fall short because few outlets in the trade accept contributed content, not only because of access limits.")
w("\n**High-fit outlets still unverified (need a human or a less restricted network):**\n")
for r in unv: w(f"- {esc(r['name'],70)} ({esc(r['industry'],30)}): {esc(r['editorial_rules'],160)}")
w("""
**Known unresolved items from the brief:**
- PCT (pctonline.com): bot-check/empty responses; no guidelines, dates or contacts read. PMP (mypmp.net): 403 on every page. Neither bypassed. Pitch by phone/email from their public contact pages.
- Lawn & Landscape, Landscape Management, Turf, Total Landscape Care, Green Industry Pros: 403 or empty render; no guidelines page confirmed.
- Professional Roofing: no public author-guidelines page exists on the site, sitemap or about page; the CSV lists the editor contact route only.
- Facility Executive: 403 on all URLs. It may be the renamed Today's Facility Manager (search snippet only).
- Training Magazine: guidelines available only by emailing the address on its page (/faq returns 404).
- MCAA (highest-fit mechanical outlet), RSES, ESCO Group, AHRI, Control Engineering, ASIS, AFSA: 403; nothing verified.
- NFPA Journal and NFPA Conference & Expo: no readable page or call for proposals. NAFED and NFSA magazine: robots.txt disallows.
- NCCER guidelines page returned 410; td.org (ATD, TD Magazine) returned 429.
- Podcast contact info: most podcasts publish no guest policy, only a host name or form. Contacts in the CSV are only those listed publicly; confirm each before outreach.
- Parent-company facts for PMP, PCT, Landscape Management and CONTRACTOR are unconfirmed.
- Prices: most rate cards are gated or PDFs that did not parse; `cost` says `not found` where not read. Only AutomatedBuildings.com sponsorship (from $2,400/yr, per its page) is a concrete figure in the building-automation file.
- Not covered: state/regional association magazines beyond TPCA/FPMA/FRSA, Canadian outlets, Spanish-language trade media, LinkedIn newsletters and creator channels, award programs beyond those listed.
- Quinn side: meetquinn.ai is client-rendered so only meta descriptions were machine-readable; customer approvals, named founder/exec bylines and bios are still needed. The White Knight $1M figure comes from the page meta description and should be confirmed with Quinn before publishing.
- 3 research rows had no URL and were dropped from the master (see `research/_merge_meta.json`).
""")
open(f"{ROOT}/report.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
print(len(out), "lines")

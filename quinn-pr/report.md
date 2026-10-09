# Quinn PR & content-distribution targets (trades): research report

Built 2026-10-09 from `master.csv` (214 unique outlets merged from 244 research rows across 12 industry passes). Facts were read from each publication's own pages with a polite fetcher (robots.txt honored, 1.5s/domain delay, cached to `cache/`). Status counts: 137 verified, 64 unverified, 8 inactive, 5 blocked-by-network-policy.

**How to read status.** `verified` = the research agent read that outlet's own page text. `unverified` = page unreadable (403, bot-check, empty render, PDF) or the facts came from search snippets/aggregators; treat every unverified row as a lead, not a fact. `blocked-by-network-policy` = this environment's network policy denied the host; not worked around. `inactive` = no content in the last 12 months (since 2025-10-09). Nothing is invented: unknown prices, editors and emails are `not found`; obfuscated emails say `obfuscated - see page`.

**Quinn facts used** come from `context.md` (supplied by Quinn, copied from meetquinn.ai). meetquinn.ai renders client-side, so this run could confirm only page meta descriptions, including the White Knight line "cut technician attrition costs by $1M a year with Quinn. 97% workforce participation, 96% course completion". Founder/exec names were not available to me; pitches below say "Quinn exec" and need a named byline holder.

## 1. Master list: best first move (ranked)

Score = fit (relevance x10) + verified read (+12) + free route (+5) + a public contact route (+2) + open deadline (+4); minus software-vendor ban (-25), vendor/promo restriction (-4), AI-policy (-3), exclusivity (-2), recency unconfirmed (-3), unread/blocked (-6). Competitors and inactive outlets are excluded from the ranking (see section 4). The score is a heuristic for ordering, not a prediction.

| # | Outlet | Industry | Tier | Rel | Status | Route (as listed publicly) | Flags | Deadline | First move |
|---|---|---|---|---|---|---|---|---|---|
| 1 | IEC Business Summit 2027 - Call for Content (Independe… | Adjacent (plumbing, electrical, home se… | free | 5 | verified | kmessenger@ieci.org |  | 2026-11-06 (call for content closes) | Workshop co-led with an electrical/mechanical customer: 'Build a training system owners can run in 3 days' (94% completion, 3-day launch). Submit before Nov 6. |
| 2 | ACHR News NEWSmakers Podcast | HVAC; Mechanical Contracting | free | 5 | verified | dylankurt@achrnews.com |  |  | Pitch a contractor ops leader + Quinn exec episode: 'Why best-tech knowledge stays trapped in heads and how 3-day launch training (94% completion, ~40% faster ramp - Quinn benchmark) fixes ramp time'. Pair with a customer GM |
| 3 | NALP The Edge Magazine + Edge blog (National Associati… | Landscaping | free | 5 | verified | NALP HQ, Fairfax VA, 703-736-9666; email obfuscated - see page |  |  | Pitch ELEVATE/Edge piece: 'Turning your best crew leader's know-how into onboarding: what a 446-person company learned' using White Knight: 446 employees, 226 courses, 97% participation, 96% completion, reported ~$1M/yr technicia… |
| 4 | RIA International Restoration Convention - Call for Pr… | Restoration | free | 5 | verified | Online submission form (SUBMIT HERE button on call page); RIA info@re… | vendor-restricted | 2026-10-16 (convention call for presentations closes) | Session: 'Ramping restoration techs faster: turning your best PM's job-site knowledge into trainable SOPs' (Talent Development track) using White Knight: 446 employees, 226 courses, 97% participation, 96% completion, reported ~$1… |
| 5 | RoofersCoffeeShop (RCS) incl. Roofing Road Trips with… | Roofing | free | 5 | verified | Contact form https://rooferscoffeeshop.com/contact-us ; phone (877) 4… |  |  | Roofing Road Trips / Coffee Conversations guest spot, then a partner webinar; angle: 'best installer's knowledge trapped in one head' with White Knight numbers (relevant to Roofing Talent America workforce effort) |
| 6 | Career Education Review (CECU) | Trade Schools | free | 5 | verified | obfuscated - see page (Contact Us page) |  |  | Byline: 'What AI can't do in trade school - and what it can: closing the gap between classroom and the first 90 days on the job,' with employer data (White Knight (446 employees, 226 courses, 97% participation, 96% completion, re… |
| 7 | Roofing Contractor (BNP Media) | Roofing | free | 5 | verified | aisnera@bnpmedia.com; kernt@bnpmedia.com; sotoservinp@bnpmedia.com (l… | ai-policy |  | Guest Column / Best of Success podcast pitch: 'Training roofing crews without hiring trainers' using White Knight: 446 employees, 226 courses, 97% participation, 96% completion, reported ~$1M/yr technician attrition cost reductio… |
| 8 | ACTE Techniques | Trade Schools | free | 5 | verified | lmilgram@acteonline.org or Techniques submission form | vendor-restricted; ai-policy | 2026-12-01 (proposals for Mar/Apr 2027 issue) | Pitch a practitioner-voice proposal with a school partner for the Mar/Apr 2027 (messaging) or the fall 2027 Emerging Technology Pathways issue: how SOP-to-course AI and roleplay sims shorten ramp time in trades programs, citing W… |
| 9 | Plant Services (Endeavor) | Industrial Automation; Facilities Maint… | free | 5 | verified | obfuscated - see page (editor email shown on contact page) | vendor-restricted |  | Pitch Anna Townshend a Workforce case study or Great Question podcast guest spot: how a maintenance organization turns SOPs and tribal knowledge into role-based training and mid-job answers; White Knight (446 employees, 226 cours… |
| 10 | ACCA conference and educational programs (speaker call) | HVAC | free | 5 | verified | events@acca.org; proposal form on guidelines page | vendor-restricted |  | Contractor-led session co-presented by a Quinn customer ops leader: 'Cutting technician ramp time with SOP-based training' (White Knight data, 3-day launch); zero product demo |
| 11 | PestWorld Magazine (NPMA) | Pest Control | free | 5 | verified | npma@pestworld.org (general NPMA, listed on page); ad sales via YGS G… | vendor-restricted |  | Pitch an Ask the Expert / workforce feature: how a pest company turned SOPs into courses and AI coaching to cut technician attrition, using White Knight Pest Control: 446 employees, 226 courses, 97% participation, 96% completion,… |
| 12 | Contracting Business (contributed content) | HVAC; Mechanical Contracting | free | 5 | verified | obfuscated - see page (email pitch per guidelines page) | ai-policy; exclusivity |  | Best Practices column co-bylined with a customer: 'Starting an in-house training program without hiring trainers' (guidelines literally list in-house training center); use White Knight numbers (446 employees, 226 courses, 96% com… |
| 13 | IndustryWeek (Endeavor) | Industrial Automation | free | 5 | verified | obfuscated - see page (contributor email on guidelines page); pitch a… | ai-policy; exclusivity |  | Talent-section column: 'Your best technician's knowledge is walking out the door' - how operators capture veteran know-how and cut ramp time without adding trainers; use White Knight (446 employees, 226 courses, 97% participation… |
| 14 | Restoration & Remediation (R&R) magazine - contributed… | Restoration | free | 5 | verified | mcgowank@bnpmedia.com | ai-policy; exclusivity |  | Email pitch to Kayla for a Training & Education byline: 'What a 3-day course launch taught a 446-person pest company about technician ramp' reframed for restoration, citing White Knight and Quinn's ~40% faster ramp benchmark (lab… |
| 15 | CONTRACTOR (Contractor Magazine) | HVAC; Mechanical Contracting; Adjacent… | free | 5 | verified | obfuscated - see page | vendor-restricted; ai-policy |  | Mechanical/plumbing-hydronics angle: 'Cross-training techs on boilers, hydronics and heat pumps without pulling them off the truck' using Quinn Ask-Quinn mid-job SOP answers; or Under 30 All-Stars nomination of a customer's young… |
| 16 | AutomatedBuildings.com | Building Automation | free | 5 | verified | sponsors@automatedbuildings.com (sponsorship); no public editorial pi… | vendor-restricted; ai-policy |  | Byline on the technician skills gap: 'The Skill Set Is Changing' (Kelly Sinclair, 2026-10-06) frames what AI means for BAS people - pitch the training/ramp-time counterpart: how the White Knight rollout (446 employees 226 courses… |
| 17 | IFMA FMJ (Facility Management Journal) | Facilities Maintenance | free | 5 | verified | fmj@ifma.org; Proposal Submission Form (https://ifma.org/publications… | vendor-restricted; ai-policy |  | Abstract: 'Competency-based readiness for FM technicians: how organizations close the knowledge gap when top performers hold the know-how' written in third person with White Knight data (White Knight Pest Control: 446 employees,… |
| 18 | BUILDINGS (Endeavor Business Media) | Facilities Maintenance; Building Automa… | free | 5 | verified | obfuscated - see page (https://buildings.com/contributors-guidelines)… | vendor-restricted; ai-policy; exclusivity |  | Educational how-to byline by a Quinn exec or customer: 'Getting facilities technicians productive faster: turning SOPs into field-ready training' with vendor-neutral method plus anonymized proof (White Knight Pest Control: 446 em… |
| 19 | Training Magazine (Lakewood Media Group) | Adjacent (plumbing, electrical, home se… | free | 4 | verified | Grace@TrainingMag.com (guidelines on request) / Lorri@TrainingMag.com |  |  | Email Grace for guidelines, then pitch an online article / Leadership Development Case Study using White Knight data (226 courses, 446 employees, 96% completion). Also consider Training MVP / Network Choice awards nominations. |
| 20 | SMACNA (Fab Forum / Annual Convention / podcasts) | Mechanical Contracting; HVAC | free | 4 | verified | https://www.smacna.org/about-smacna/contact-smacna |  |  | Offer a member-contractor + Quinn session on onboarding sheet-metal fabricators with SOP-based courses; pitch podcast / Technology Playbook contribution |
| 21 | NALP ELEVATE conference (Nov 8-11, 2026, Tampa) | Landscaping | free | 4 | verified | form/email not found |  |  | Propose a 2027 session with a landscaping customer operator on SOP-to-course rollout and ramp time (Quinn benchmark ~40% faster ramp). Ask NALP education team about the 2027 call. |
| 22 | Pest Control Millionaire (podcast, Jonas Olson) | Pest Control | free | 4 | verified | not found (Buzzsprout page lists no email) |  |  | Guest: 'Why growth stalls at 30-50 techs: training and consistency' with Quinn proof; fits owner-operator audience, less enterprise |
| 23 | RIA Restoration Blog | Restoration | free | 4 | verified | hgardyasz@restorationindustry.org (media room contact) ; info@restora… |  |  | By-lined post 'Why your restoration SOPs live in the heads of your top 5 techs' with the White Knight 446-employee/226-course result; or Partner Insights spotlight if joining affinity program. |
| 24 | Roofing Contractor - Best of Success Podcast Show | Roofing | free | 4 | verified | aisnera@bnpmedia.com; kernt@bnpmedia.com |  |  | Episode: 'How roofing companies turn SOPs and best-crew know-how into onboarding' (200+ ops teams; 3-day launch; ~40% faster ramp, Quinn benchmark) |
| 25 | Roofing (roofingmagazine.com) | Roofing | free | 4 | verified | obfuscated - see page (https://roofingmagazine.com/contact/); phone (… |  |  | Business Sense column pitch: 'Why roofing crews forget the SOP by week 3 - and how to measure readiness' with White Knight data |
| 26 | NRCA (events, IRE speaker calls, member channels) | Roofing | free | 4 | verified | IRE call: submission form via Informa Markets (link on NRCA notice) |  |  | Submit a 2028 IRE session in spring 2027: 'Ramping new roofing crews in weeks: a contractor case study' with a customer co-presenter, no product pitch |
| 27 | Roofing Insights Podcast (Dmitry Lipinskiy) | Roofing | free | 4 | verified | not found on page read |  |  | Guest interview with a Quinn exec on turning SOPs into roleplay sims for roofing sales/crews; White Knight proof |
| 28 | Western Roofing (WSRCA official publication; Dodson Pu… | Roofing | free | 4 | verified | info@westernroofing.net |  |  | Contributed article 'Keeping crew skills consistent across branches' by a Quinn exec with roofing customer |
| 29 | Community College Daily (AACC) | Trade Schools | free | 4 | verified | mdembicki@aacc.nche.edu |  |  | Pitch Dembicki a news-style story on community college trades programs using AI roleplay/readiness scoring with an employer partner; lead with White Knight (446 employees, 226 courses, 97% participation, 96% completion, reported… |
| 30 | NCCER Newsroom (blog / guest writers) | Trade Schools | free | 4 | verified | media@nccer.org |  |  | Guest blog on turning contractor SOPs into craft-training modules aligned to NCCER credentials. |
| 31 | Landscape Management | Landscaping | free | 5 | unverified | form/email not found |  |  | Same operations/training angle as Lawn & Landscape but pitch only one at a time until parent is confirmed: ramp-time and attrition story from White Knight: 446 employees, 226 courses, 97% participation, 96% completion, reported ~… |
| 32 | Green Industry Podcast (Paul Jamison) | Landscaping | free | 5 | unverified | not found (libsyn page lists no guest form) |  |  | Guest episode: 'How a 446-employee company got 97% participation in training' with White Knight: 446 employees, 226 courses, 97% participation, 96% completion, reported ~$1M/yr technician attrition cost reduction (meetquinn.ai/re… |
| 33 | Construction Executive (ABC) | Mechanical Contracting | free | 4 | verified | editor@constructionexec.com | exclusivity |  | Workforce development / training byline (Workforce, Training categories): 'Why SOPs trapped in senior techs' heads cost contractors a year of ramp time' using White Knight metrics and Quinn ~40% faster ramp benchmark; third-perso… |
| 34 | Pest Management Professional (PMP) | Pest Control | free | 5 | unverified | Mail only per search snippet: PMP Magazine, 1360 E. 9th St., 10th Flo… |  |  | Contributed technical/ops column or Q&A on SOP-to-training and technician retention using White Knight Pest Control: 446 employees, 226 courses, 97% participation, 96% completion, reported ~$1M/yr technician attrition cost reduct… |
| 35 | Bug Bux Podcast (Allan Draper) | Pest Control | free | 4 | verified | not found |  |  | Expert guest on building a training system that scales: 226 courses and 96% completion at White Knight; offer P&L framing (attrition cost) |
| 36 | Automation World (Endeavor) | Industrial Automation | free | 4 | verified | obfuscated - see page (Chris McNamara email on contact page) | ai-policy |  | Pitch Chris McNamara: 'Why Industry 4.0 hasn't scaled is a people problem' - tie to AW coverage of digital transformation; frame training/ramp-time data (Quinn benchmark ~40% faster ramp, 94% completion) as the workforce layer of… |
| 37 | R&R Ask the Expert podcast | Restoration | free | 4 | verified | mcgowank@bnpmedia.com (guests/topics); Balzanod@bnpmedia.com (sponsor… | ai-policy |  | Guest spot on technician onboarding/training ('Field Notes'-style topic for technicians) with White Knight proof and 3-day launch. |
| 38 | Professional Roofing (NRCA) | Roofing | free | 4 | verified | areid@nrca.net; chanus@nrca.net; kberns@nrca.net; professionalroofing… | ai-policy |  | Ask Reid for an editorial-calendar and contributor fit call; offer a contractor-co-authored feature on workforce training/onboarding (NRCA Executive Leadership Bilingual Program and recruitment tool featured Oct 2026) using White… |
| 39 | Inside Higher Ed - Views / Careers | Trade Schools | free | 4 | verified | opinion@insidehighered.com; editor@insidehighered.com | ai-policy |  | Disclosed-affiliation Views piece: 'What community colleges can learn from how top trades employers onboard technicians' using White Knight (446 employees, 226 courses, 97% participation, 96% completion, reported ~$1M/yr technici… |
| 40 | EC&M (Electrical Construction & Maintenance) | Adjacent (plumbing, electrical, home se… | free | 4 | verified | obfuscated - see page | vendor-restricted |  | Thought-leadership piece (500-1,500w) on 'Safety and training': how electrical contractors keep code/NEC knowledge from living only in senior electricians' heads; author a Quinn customer/ops leader or technical lead. |

Full ranked list (all 204 rankable outlets) is in `master.csv` (`rank` column) and `index.html`.

## 2. Summary by industry

Sorted by relevance (5 first), then free before paid, then verified before unverified. Outlets in several industries appear in each. Inactive outlets are omitted here (see section 4). Targets were 10-15 Tier 1 (relevance 4-5) and 5-8 Tier 2 (relevance 2-3) per core industry.


### HVAC (core): 24 live outlets; Tier 1 (rel 4-5): 12 (12 verified); Tier 2 (rel 2-3): 12

| Outlet | Tier | Rel | Status | Contact route | Cost | Flags | Last content |
|---|---|---|---|---|---|---|---|
| [ACCA conference and educational programs (speaker call)](https://www.acca.org/education/accacallforpresenters) | free | 5 | verified | events@acca.org; proposal form on guidelines page | Free to speak but ACCA membership required; speakers get re… | vendor-restricted | 2026-10-07 |
| [ACHR News NEWSmakers Podcast](https://www.achrnews.com/media/podcasts/2904) | free | 5 | verified | dylankurt@achrnews.com | Free guest slot (earned). Vendor-hosted episodes appear to… |  | 2026-09-30 |
| [CONTRACTOR (Contractor Magazine)](https://www.contractormag.com/) | free | 5 | verified | obfuscated - see page | Free (earned). Fee-based Sponsored Content / 'Preferred Med… | vendor-restricted; ai-policy | 2026-10-09 |
| [Contracting Business (contributed content)](https://www.contractingbusiness.com/) | free | 5 | verified | obfuscated - see page (email pitch per guidelines page) | Free (earned); paid media kit/content marketing via Endeavo… | ai-policy; exclusivity | 2026-10-07 |
| [ACHR News (guest columns and contributed articles)](https://www.achrnews.com/) | free | 4 | verified | mariataylor@achrnews.com (guest column pitch); dylankurt@achrnews.com… | Free (earned). Paid Sponsored Content, webinars, eBlasts ex… | vendor-restricted; exclusivity | 2026-10-09 |
| [HVAC Chats podcast (Contracting Business)](https://www.contractingbusiness.com/podcasts/hvac-chats) | free | 4 | verified | no podcast-guest form found; route via editor pitch (email obfuscated… | not found | vendor-restricted | 2026-10-07 |
| [SMACNA (Fab Forum / Annual Convention / podcasts)](https://www.smacna.org) | free | 4 | verified | https://www.smacna.org/about-smacna/contact-smacna | Free to propose; membership/associate membership or Premier… |  | 2026-10-07 |
| [ACCA partnership, advertising, ACCA Now magazine, HVAC Blog](https://www.acca.org/about/partner-and-advertise) | paid | 4 | verified | Start Now form on page | Strategic Partnership from $36,000; other advertising price… |  | 2026-10-07 |
| [HVAC School (podcast, site, Symposium)](https://hvacrschool.com/) | paid | 4 | verified | contact page: https://hvacrschool.com/contact/ (no email read) | Sponsorship price not found; site funded by named partners… |  | 2026-10-08 |
| [HVACR Business magazine](https://www.hvacrbusiness.com/) | paid | 4 | verified | emails listed on contact page (roles not captured): ttanker@hvacrbusi… | Media kit with rates by form; price not found | ai-policy | 2026-10 |
| [Plumbing & Mechanical (BNP Media)](https://www.pmmag.com) | paid | 4 | verified | Advertising inquiry form (see page); contributor contact not found | Not found (rate card not public) |  | 2026-10 |
| [Service World Expo / Service Nation (Service Roundtable)](https://serviceworldexpo.com) | paid | 4 | verified | sponsorship brochure by form | not found (brochure) |  | 2026-10 |
| [ACCA Awards Program](https://www.acca.org/about/awards) | free | 3 | verified | see awards page | No application fee |  | 2026-10 |
| [High-Performance HVAC Today (National Comfort Institute)](https://hvactoday.com/) | free | 3 | verified | form on contribute page | Free; guest authors get printed issue copy. Advertising for… | ai-policy | 2026-09 |
| [ServiceTitan blog, podcast and Pantheon](https://www.servicetitan.com/blog) | free | 3 | verified | not found | Not found |  | 2026-10 |
| [HVAC Know It All podcast](https://www.hvacknowitall.com/) | paid | 3 | verified | gary@hvacknowitall.com | sponsor pricing not found |  | 2026-10-06 |
| [PHCC Solutions magazine and eNewsletter (Plumbing-Heating-C…](https://www.phccweb.org) | paid | 3 | verified | jboulka@thewymancompany.com | Not found; associate-member discounts mentioned |  | 2026-10-08 |
| [HVAC & Refrigeration Insider (hvacinsider.com)](https://hvacinsider.com/) | free | 2 | verified | https://hvacinsider.com/contact-us/ | Free news posting apparent; ad rates PDF on advertising page | recency-unconfirmed | 2026 |
| [AHRI](https://www.ahrinet.org/) | free | 2 | unverified | not found | not found | recency-unconfirmed | not found |
| [ESCO Group (ESCO Institute, Did You Know? podcast)](https://escogroup.org/DidYouKnow.aspx) | free | 2 | unverified | not found | not found | recency-unconfirmed | not found |
| [Jobber Academy / blog](https://getjobber.com/academy/) | free | 2 | unverified | not found | not found | recency-unconfirmed | not found |
| [RSES Journal / RSES](https://www.rses.org/) | free | 2 | unverified | not found | not found | recency-unconfirmed | not found |
| [HARDI (HVACR distributors)](https://www.hardinet.org/) | paid | 2 | verified | not found | not found (sponsorship guide PDF) |  | 2026-09 |
| [Nexstar Network (blog, Super Meeting)](https://www.nexstarnetwork.com/) | paid | 2 | verified | https://www.nexstarnetwork.com/contact | not found |  | 2026-09 |

### Pest Control (core): 16 live outlets; Tier 1 (rel 4-5): 8 (4 verified); Tier 2 (rel 2-3): 7

| Outlet | Tier | Rel | Status | Contact route | Cost | Flags | Last content |
|---|---|---|---|---|---|---|---|
| [PestWorld Magazine (NPMA)](https://www.npmapestworld.org/your-business/pestworld-magazine/26-5-september-october-2026/) | free | 5 | verified | npma@pestworld.org (general NPMA, listed on page); ad sales via YGS G… | Editorial route: not found. Ad Rates page returned HTTP 403… | vendor-restricted | 2026-10 |
| [Pest Control Technology (PCT)](https://www.pctonline.com) | free | 5 | unverified | not found (site contact page returned a bot-check block) | Not found; advertising/media kit exists per site nav (not r… | recency-unconfirmed | not found |
| [Pest Management Professional (PMP)](https://www.mypmp.net) | free | 5 | unverified | Mail only per search snippet: PMP Magazine, 1360 E. 9th St., 10th Flo… | Advertising and 'Word from our sponsor' sponsored content e… |  | 2026-06 |
| [Bug Bux Podcast (Allan Draper)](https://bugbuxpodcast.buzzsprout.com/) | free | 4 | verified | not found | Not found |  | 2026-10-08 |
| [Pest Control Millionaire (podcast, Jonas Olson)](https://www.buzzsprout.com/2092423) | free | 4 | verified | not found (Buzzsprout page lists no email) | Not found (guest spots appear free; network may sell sponso… |  | 2026-10-06 |
| [Pest Control Legends (podcast, Dan Leibrandt)](https://www.castfox.net/podcast/pest-control-legends-7042708) | free | 4 | unverified | not found (official site blocked by network policy) | Not found |  | 2026-10-07 |
| [Pest in Class (FieldRoutes / ServiceTitan podcast)](https://fieldroutes.com/resources/podcast) | free | 4 | unverified | not found | Not found | recency-unconfirmed | not found |
| [NPMA PestWorld 2026 / Technology Adopter Award](https://www.npmapestworld.org/attend/industry-events-calendar/pestworld-2026/) | paid | 4 | verified | npma@pestworld.org | Exhibit/sponsor cost not found; award application free (no… |  | 2026-10 |
| [BugBytes Podcast (NPMA)](https://www.npmapestworld.org/your-business/latest-news/argentine-ants-house-mice-and-asian-tiger-mosquitoes-featured-on-bugbytes/) | free | 3 | verified | training@pestworld.org (listed for BugBytes feedback) | Free (no fee stated) |  | 2026-10-01 |
| [Texas Pest Control Association (TPCA)](https://www.texaspest.org/advertising) | paid | 3 | verified | Phone (512) 954-9664; email obfuscated - see page | Newsletter ad rates linked from page, not read |  | 2026-10 |
| [PestPac / WorkWave Blog](https://www.pestpac.com/blog) | free | 2 | verified | https://www.pestpac.com/contact-us (form, general) | Not found |  | 2026-03-13 |
| [FieldRoutes Blog](https://www.fieldroutes.com/blog/page/1) | free | 2 | unverified | not found | Not found |  | 2026-10 |
| [Pest Control Marketing Domination Podcast (Casey Lewis)](https://castbox.fm/channel/Pest-Control-Marketing-Domination-Podcast-id5019066) | free | 2 | unverified | phone listed 925-464-8383 on aggregator; no email | Not found |  | 2026-10-03 |
| [QualityPro (NPMA-endorsed accreditation)](https://www.qualitypro.org) | free | 2 | unverified | QualityPro@PestWorld.org | Not found | recency-unconfirmed | not found |
| [Florida Pest Management Association (FPMA) - Pest Perspecti…](https://flpma.org) | paid | 2 | unverified | https://flpma.org/contact-fpma (page exists, not read) | EXPO sponsor/exhibitor info page exists; rates not read | recency-unconfirmed | 2026 |
| [Pest Management Podcast (pestmanagementpodcast.com)](https://www.pestmanagementpodcast.com) | free | 1 | blocked-by-network-policy | not found | not found | blocked; recency-unconfirmed | not found |

### Mechanical Contracting (core): 17 live outlets; Tier 1 (rel 4-5): 9 (7 verified); Tier 2 (rel 2-3): 7

| Outlet | Tier | Rel | Status | Contact route | Cost | Flags | Last content |
|---|---|---|---|---|---|---|---|
| [ACHR News NEWSmakers Podcast](https://www.achrnews.com/media/podcasts/2904) | free | 5 | verified | dylankurt@achrnews.com | Free guest slot (earned). Vendor-hosted episodes appear to… |  | 2026-09-30 |
| [CONTRACTOR (Contractor Magazine)](https://www.contractormag.com/) | free | 5 | verified | obfuscated - see page | Free (earned). Fee-based Sponsored Content / 'Preferred Med… | vendor-restricted; ai-policy | 2026-10-09 |
| [Contracting Business (contributed content)](https://www.contractingbusiness.com/) | free | 5 | verified | obfuscated - see page (email pitch per guidelines page) | Free (earned); paid media kit/content marketing via Endeavo… | ai-policy; exclusivity | 2026-10-07 |
| [ACHR News (guest columns and contributed articles)](https://www.achrnews.com/) | free | 4 | verified | mariataylor@achrnews.com (guest column pitch); dylankurt@achrnews.com… | Free (earned). Paid Sponsored Content, webinars, eBlasts ex… | vendor-restricted; exclusivity | 2026-10-09 |
| [Construction Executive (ABC)](https://www.constructionexec.com) | free | 4 | verified | editor@constructionexec.com | Free (does not pay for contributed content); sponsored cont… | exclusivity | 2026-10-07 |
| [SMACNA (Fab Forum / Annual Convention / podcasts)](https://www.smacna.org) | free | 4 | verified | https://www.smacna.org/about-smacna/contact-smacna | Free to propose; membership/associate membership or Premier… |  | 2026-10-07 |
| [Electrical Contractor (ECmag, NECA)](https://www.ecmag.com) | free | 4 | unverified | not found | not found | recency-unconfirmed | not found |
| [United Association (UA) training](https://www.ua.org) | free | 4 | blocked-by-network-policy | not found | not found | blocked; recency-unconfirmed | not found |
| [Plumbing & Mechanical (BNP Media)](https://www.pmmag.com) | paid | 4 | verified | Advertising inquiry form (see page); contributor contact not found | Not found (rate card not public) |  | 2026-10 |
| [Construction Dive (opinion)](https://www.constructiondive.com) | free | 3 | verified | submission form on page; email obfuscated - see page | Free (op-ed). Paid: content marketing/Playbooks via adverti… | ai-policy; exclusivity | 2026-10 |
| [Consulting-Specifying Engineer (csemag.com)](https://www.csemag.com/) | free | 3 | verified | obfuscated - see page (ARozgus at wtwhmedia.com as shown on guideline… | Free (contributed) | ai-policy; exclusivity | 2026-09 |
| [Engineered Systems (ES NEWS)](https://www.esmagazine.com) | free | 3 | verified | Submit a Letter form (no guideline page found) | Free route not confirmed; advertise page https://www.esmaga… |  | 2026-10 |
| [PHCC Solutions magazine and eNewsletter (Plumbing-Heating-C…](https://www.phccweb.org) | paid | 3 | verified | jboulka@thewymancompany.com | Not found; associate-member discounts mentioned |  | 2026-10-08 |
| [ASHRAE Journal](https://www.ashrae.org/technical-resources/ashrae-journal) | free | 2 | verified | letters@ashrae.org (letters); submission portal via guidelines page | Free | ai-policy; recency-unconfirmed | not found |
| [ASPE Pipeline (American Society of Plumbing Engineers)](https://aspe.org/pipeline/) | free | 2 | verified | gpienta@aspe.org | Free; ASPE holds copyright, author keeps nonexclusive licen… |  | 2026-09-24 |
| [Plumbing Engineer](https://www.pemag.com) | free | 2 | blocked-by-network-policy | not found | not found | blocked; recency-unconfirmed | not found |
| [ForConstructionPros](https://www.forconstructionpros.com) | free | 1 | unverified | not found | not found | recency-unconfirmed | not found |

### Facilities Maintenance (core): 22 live outlets; Tier 1 (rel 4-5): 9 (8 verified); Tier 2 (rel 2-3): 13

| Outlet | Tier | Rel | Status | Contact route | Cost | Flags | Last content |
|---|---|---|---|---|---|---|---|
| [BUILDINGS (Endeavor Business Media)](https://buildings.com/) | free | 5 | verified | obfuscated - see page (https://buildings.com/contributors-guidelines)… | Free for contributed content; advertising via buildings.com… | vendor-restricted; ai-policy; exclusivity | 2026-09-23 (homep… |
| [IFMA FMJ (Facility Management Journal)](https://fmj.ifma.org/) | free | 5 | verified | fmj@ifma.org; Proposal Submission Form (https://ifma.org/publications… | Contributed articles free; paid: FMJ advertising/sponsored… | vendor-restricted; ai-policy | 2026-10 (site pro… |
| [Plant Services (Endeavor)](https://www.plantservices.com/) | free | 5 | verified | obfuscated - see page (editor email shown on contact page) | Free to pitch editor; paid: advertising, webinars, eHandboo… | vendor-restricted | 2026-10-09 |
| [BUILDINGS Podcast](https://buildings.com/podcasts) | free | 4 | verified | obfuscated - see page | Free | vendor-restricted | 2026-10-05 |
| [Facilities Dive (Informa TechTarget)](https://www.facilitiesdive.com/) | free | 4 | verified | Submission form on page; questions email obfuscated - see page | Opinion free; content marketing/ads paid via https://www.fa… | vendor-restricted; ai-policy; exclusivity | 2026-10-08 |
| [IFMA Connected FM Podcast](https://podcast.ifma.org/) | free | 4 | verified | communications@ifma.org (press inquiries, listed on page); no guest-p… | Free (no sponsorship pricing found for podcast) | vendor-restricted; recency-unconfirmed | 2026 (episodes un… |
| [Reliable Plant / Machinery Lubrication (Noria)](https://www.reliableplant.com/) | free | 4 | verified | Online submission form on guidelines page; sales@noria.com for paid p… | Free for unpaid educational articles/case studies; paid: co… | vendor-restricted; ai-policy | 2026-10-02 |
| [Facility Executive (Group C Media; formerly Today's Facilit…](https://facilityexecutive.com/) | free | 4 | unverified | not found | not found | recency-unconfirmed | not found |
| [IFMA World Workplace conference (speaker/sponsor)](https://worldworkplace.ifma.org/) | paid | 4 | verified | ifma@ifma.org per search snippet only (not read); see page [ifma@ifma… | Speaking slots free of fees but no honorarium (per CFP poli… |  | 2026-10 (2026 eve… |
| [APPA Facilities Manager (magazine)](https://www.appa.org/fmmagazine) | free | 3 | verified | publications@appa.org (subject 'Facilities Manager'); advertising mar… | Editorial free; ads: spread member rate from $7,500, non-me… | ai-policy; exclusivity | 2026-07 (July iss… |
| [Health Facilities Management (ASHE / American Hospital Asso…](https://www.hfmmagazine.com/) | free | 3 | verified | mhrickiewicz@aha.org, 312-893-6813; jmorgan@aha.org (products) | Free (contributed); subscription via ASHE | vendor-restricted | 2026-09-16 |
| [Uptime Magazine / Reliabilityweb.com](https://reliabilityweb.com/) | free | 3 | verified | crm@reliabilityweb.com; Article Submission Form on page | Articles free; marketing/sponsorship inquiries via crm@reli… |  | 2026-07 (About pa… |
| [AFE (Association for Facilities Engineering)](https://www.afe.org/) | free | 3 | unverified | not found | not found | recency-unconfirmed | not found |
| [Maintenance Technology (mtonline.com)](https://www.mtonline.com/) | free | 3 | unverified | not found | not found | vendor-restricted; recency-unconfirmed | not found |
| [Building Operating Management and Facility Maintenance Deci…](https://www.reachfms.com/) | paid | 3 | verified | https://www.reachfms.com/contact.aspx (form/sales reps); editorial da… | Paid programs only for Quinn; rates not found (request via… | software-vendor-ban; exclusivity | 2026-10 (Oct 2026… |
| [FacilitiesNet (Trade Press Media Group)](https://www.facilitiesnet.com/) | paid | 3 | verified | dave.lubach@tradepress.com (proposals); fnproducts@tradepress.com (pr… | Contributed articles free; paid routes: Branded Features, w… | software-vendor-ban; ai-policy; exclusivity | 2026-10 (webcasts… |
| [SMRP (Society for Maintenance & Reliability Professionals)](https://www.smrp.org/) | paid | 3 | verified | https://smrp.org/contact/ (form); no editorial contact found | Speaking free (abstract); sponsorship/exhibit rates not fou… | ai-policy | 2026-10-05 (site… |
| [RFMA Facilitator (Restaurant Facility Management Associatio…](https://www.rfmaonline.com/) | paid | 3 | unverified | not found | Ads per media kit (not read) | recency-unconfirmed | not found |
| [CMMS vendor blogs (Limble, UpKeep, Fiix, MAPCON)](https://mapcon.com/us-en/maintenance-management-blog-index) | free | 2 | unverified | not found | not found | recency-unconfirmed | not found |
| [Facilities Management Journal (UK, fmj.co.uk)](https://www.fmj.co.uk/) | free | 2 | unverified | not found | not found | recency-unconfirmed | not found |
| [BOMA International (BOMA/BOMI newsletters and publications)](https://www.boma.org/) | paid | 2 | verified | obfuscated - see page (ad sales emails on https://boma.org/advertise-… | Rates in media kits (PDF not read); paid only |  | 2026-10-07 (site… |
| [Healthcare Facilities Today (Trade Press Media Group)](https://www.healthcarefacilitiestoday.com/) | paid | 2 | verified | dan.hounsell@tradepressmedia.com (proposals); FNproducts@tradepress.c… | Articles free; Branded Features paid (rates not found; cont… | software-vendor-ban; ai-policy; exclusivity | 2026-11 (upcoming… |

### Roofing (core): 22 live outlets; Tier 1 (rel 4-5): 8 (8 verified); Tier 2 (rel 2-3): 13

| Outlet | Tier | Rel | Status | Contact route | Cost | Flags | Last content |
|---|---|---|---|---|---|---|---|
| [RoofersCoffeeShop (RCS) incl. Roofing Road Trips with Heidi…](https://rooferscoffeeshop.com/) | free | 5 | verified | Contact form https://rooferscoffeeshop.com/contact-us ; phone (877) 4… | Free forum/article participation and podcast guests exist;… |  | 2026-09 |
| [Roofing Contractor (BNP Media)](https://www.roofingcontractor.com/) | free | 5 | verified | aisnera@bnpmedia.com; kernt@bnpmedia.com; sotoservinp@bnpmedia.com (l… | Guest Column/podcast pitch: free via editor. Paid: Sponsore… | ai-policy | 2026-10 |
| [NRCA (events, IRE speaker calls, member channels)](https://nrca.net/) | free | 4 | verified | IRE call: submission form via Informa Markets (link on NRCA notice) | Free to propose; IRE 2027 call deadline was April 18, 2026… |  | 2026-10 |
| [Professional Roofing (NRCA)](https://www.professionalroofing.net/) | free | 4 | verified | areid@nrca.net; chanus@nrca.net; kberns@nrca.net; professionalroofing… | Editorial route free (invitation/pitch). Paid: advertising… | ai-policy | 2026-10-01 |
| [Roofing (roofingmagazine.com)](https://www.roofingmagazine.com/) | free | 4 | verified | obfuscated - see page (https://roofingmagazine.com/contact/); phone (… | Editorial pitch free; media kit/digital rates via advertise… |  | 2026-10-07 |
| [Roofing Contractor - Best of Success Podcast Show](https://www.roofingcontractor.com/media/podcasts/5077) | free | 4 | verified | aisnera@bnpmedia.com; kernt@bnpmedia.com | Free guest spot if editors accept (no guest process publish… |  | 2026-10 |
| [Roofing Insights Podcast (Dmitry Lipinskiy)](https://roofinginsightspodcast.buzzsprout.com) | free | 4 | verified | not found on page read | Free guest spots (no published process) |  | 2026-05-18 |
| [Western Roofing (WSRCA official publication; Dodson Publica…](https://www.westernroofing.net/) | free | 4 | verified | info@westernroofing.net | Editorial route free; advertising page https://www.westernr… |  | 2026-09-25 |
| [Construction Dive - Opinion (Informa TechTarget)](https://www.constructiondive.com/opinion/submit-opinion) | free | 3 | verified | Online submission form on page | Free | ai-policy; exclusivity | 2026-07 |
| [RoofTalk with NRCA (podcast)](https://nrcarooftalk.podbean.com/) | free | 3 | verified | kberns@nrca.net; areid@nrca.net (from Professional Roofing about page… | Free if invited; no guest application found |  | 2026-09-18 |
| [Roofing Success Podcast (Jim Ahlin / Roofer Marketers)](https://www.buzzsprout.com/2187966) | free | 3 | verified | not found on page read | Free guest spots (no public process) |  | 2026-10-06 |
| [Toolbox for the Trades (ServiceTitan podcast)](https://servicetitan.com/blog/best-roofing-podcasts) | free | 3 | unverified | not found | not found | recency-unconfirmed | 2026 |
| [Florida Roofing Magazine (FRSA)](https://www.floridaroof.com/frm) | paid | 3 | verified | Contact via https://www.floridaroof.com (contact link on page) | Advertising; rates in media kit (not found); 12x one-page c… | recency-unconfirmed | 2026 |
| [RCAT - Roofing Contractors Association of Texas (Texas Roof…](https://rcat.net/) | paid | 3 | verified | Contact page https://rcat.net/contact-us.html | Associate membership / exhibiting likely required; fees not… |  | 2026-10 |
| [Roofing Contractor - Webinars (BNP Events)](https://www.roofingcontractor.com/events/category/2621-webinar) | paid | 3 | verified | webinars@bnpmedia.com | Paid sponsorship; price not found |  | 2026-10 |
| [AccuLynx blog (roofing software vendor)](https://acculynx.com/blog) | free | 2 | verified | not found | not found |  | 2026-04 |
| [IIBEC Interface (formerly RCI Interface) technical journal](https://iibec.org/hub/interface/) | free | 2 | verified | acooper@iibec.org; submission form on Interface page | Technical papers free; advertising packages roughly $750-$4… | vendor-restricted | 2026-09-30 |
| [JobNimbus blog (roofing software vendor)](https://www.jobnimbus.com/blog) | free | 2 | verified | not found | not found |  | 2026-10-05 |
| [Roofing Business Builder Podcast (Daniel Lakstins)](https://roofingbusinessbuilder.buzzsprout.com/818962) | free | 2 | unverified | not found | not found | recency-unconfirmed | not found |
| [Roofing Roundtable](https://podcasts.apple.com/us/podcast/the-roofing-roundtable/id1685463581) | free | 2 | unverified | not found | not found | recency-unconfirmed | not found |
| [Win the Storm (event)](https://roofingcontractor.com/events/4315-win-the-storm-2025) | paid | 2 | unverified | not found | not found |  | 2026-10 |
| [ForConstructionPros - Expert Columns](https://www.forconstructionpros.com/22106209) | free | 1 | unverified | not found | not found | recency-unconfirmed | not found |

### Landscaping (core): 18 live outlets; Tier 1 (rel 4-5): 6 (2 verified); Tier 2 (rel 2-3): 10

| Outlet | Tier | Rel | Status | Contact route | Cost | Flags | Last content |
|---|---|---|---|---|---|---|---|
| [NALP The Edge Magazine + Edge blog (National Association of…](https://blog.landscapeprofessionals.org/) | free | 5 | verified | NALP HQ, Fairfax VA, 703-736-9666; email obfuscated - see page | Contributed route: not found (no public guidelines located)… |  | 2026-10-06 |
| [Green Industry Podcast (Paul Jamison)](https://greenindustrypodcast.libsyn.com/) | free | 5 | unverified | not found (libsyn page lists no guest form) | Free (guest). Sponsorship: not found |  | 2026-10-09 |
| [Landscape Management](https://www.landscapemanagement.net/) | free | 5 | unverified | form/email not found | not found |  | 2026-06 |
| [Lawn & Landscape (GIE Media)](https://www.lawnandlandscape.com/) | free | 5 | unverified | form/email not found | Editorial: not found. Paid: sponsored podcasts, webinars, a… | vendor-restricted | 2026-07 |
| [NALP ELEVATE conference (Nov 8-11, 2026, Tampa)](https://www.landscapeprofessionals.org/) | free | 4 | verified | form/email not found | Speaker route: no public 2026 call found (selection process… |  | 2026-10-06 |
| [Turf Magazine (Group C Media)](https://turfmagazine.com/) | free | 4 | unverified | form on Yardstick page; contact page returned http-403 | Free (earned). Advertising: not found | ai-policy; recency-unconfirmed | not found |
| [Arborist News (ISA) - tree care adjacent](https://www.isa-arbor.com/Publications/Arborist-News) | free | 3 | verified | email obfuscated - see page; mail: PO Box 191, Annapolis Junction MD… | Free (submission). Advertising via ISA Media Kit | ai-policy | 2026-09-29 |
| [Aspire Software blog (landscape software vendor)](https://www.youraspire.com/blog) | free | 3 | verified | not found | Free; cost not found |  | 2026-10-08 |
| [Green Industry Pros (GreenIndustryPros.com)](https://www.greenindustrypros.com/) | free | 3 | unverified | not found | not found | recency-unconfirmed | not found |
| [Total Landscape Care](https://www.totallandscapecare.com/) | free | 3 | unverified | not found | not found | recency-unconfirmed | not found |
| [Equip Exposition (OPEI), Oct 20-23, 2026](https://www.equipexposition.com/) | paid | 3 | unverified | not found | Exhibitor application: cost not found |  | 2026-10-09 |
| [Greenhouse Grower (Meister Media) - nursery adjacent](https://greenhousegrower.com/) | free | 2 | verified | form on https://www.greenhousegrower.com/contact/; Meister Media, 442… | Advertise page exists; rates not found |  | 2026-07-21 |
| [Golf Course Industry (GIE Media)](https://www.golfcourseindustry.com/) | free | 2 | unverified | not found | Free | recency-unconfirmed | not found |
| [Jobber blog](https://www.jobber.com/blog/) | free | 2 | unverified | not found | not found | vendor-restricted; recency-unconfirmed | not found |
| [LMN blog](https://www.lmnapp.com/blog) | free | 2 | unverified | not found | not found | recency-unconfirmed | not found |
| [LawnSite forum](https://www.lawnsite.com/) | free | 2 | unverified | login required | Free |  | 2026-10-09 |
| [American Nurseryman](https://americannursery.com/) | free | 1 | unverified | not found | not found | recency-unconfirmed | not found |
| [Irrigation Today (Irrigation Association)](https://irrigationtoday.org/) | free | 1 | unverified | not found | Advertise link exists; rates not found |  | 2026-05-15 |

### Restoration (core): 20 live outlets; Tier 1 (rel 4-5): 8 (6 verified); Tier 2 (rel 2-3): 10

| Outlet | Tier | Rel | Status | Contact route | Cost | Flags | Last content |
|---|---|---|---|---|---|---|---|
| [RIA International Restoration Convention - Call for Present…](https://convention.restorationindustry.org/) | free | 5 | verified | Online submission form (SUBMIT HERE button on call page); RIA info@re… | Free to submit; speaker perks not stated on current page. 2… | vendor-restricted | 2026-10 |
| [Restoration & Remediation (R&R) magazine - contributed arti…](https://www.randrmagonline.com/) | free | 5 | verified | mcgowank@bnpmedia.com | Free for editorial; Sponsored Content, webinars, eBlasts, I… | ai-policy; exclusivity | 2026-10 |
| [Cleaning & Restoration (C&R) Magazine](https://www.candrmagazine.com/) | free | 5 | unverified | not found | Free to read; submission cost not found | recency-unconfirmed | not found |
| [Cleanfax (ISSA) - editorial content submissions](https://cleanfax.com/) | free | 4 | verified | Contact form: https://cleanfax.com/contact-us/ ; submission method on… | Free editorial; paid Sponsored Content/advertising exists (… | vendor-restricted; ai-policy | 2026-09 |
| [R&R Ask the Expert podcast](https://www.randrmagonline.com/media/podcasts) | free | 4 | verified | mcgowank@bnpmedia.com (guests/topics); Balzanod@bnpmedia.com (sponsor… | Free guest spot; sponsorship is paid | ai-policy | 2026-09 |
| [RIA Restoration Blog](https://www.restorationindustry.org/restoration-blog) | free | 4 | verified | hgardyasz@restorationindustry.org (media room contact) ; info@restora… | Free for outside-author posts seen (e.g. by-lined posts fro… |  | 2026-09-22 |
| [Take 5 With Cleanfax (video/podcast)](https://cleanfax.com/multimedia-resources/podcasts/) | free | 4 | verified | obfuscated - see page | Free (participation invited) | vendor-restricted | 2026-09 |
| [Restoration Today podcast (Michelle Blevins)](https://apple.co/3lyOqwL) | free | 4 | unverified | not found | Standard guest spot: not found; some series are sponsor-fun… |  | 2026-10-06 |
| [RIA Media Room / RIA Beyond podcast](https://www.restorationindustry.org/restoration-industry-media) | free | 3 | verified | hgardyasz@restorationindustry.org; Press & Media Request Form on page | Free to request; affinity partnership is a paid vendor prog… |  | 2026-04 |
| [Restoration Rundown Podcast](https://rephonic.com/podcasts/restoration-rundown-podcast) | free | 3 | unverified | not found | not found |  | 2026-09-18 |
| [Cleanfax advertising and Sponsored Content](https://cleanfax.com/advertise-with-us/) | paid | 3 | verified | https://cleanfax.com/contact-us/ | not found |  | 2026-09 |
| [R&R advertising and Sponsored Content (BNP Media)](https://www.randrmagonline.com/advertise) | paid | 3 | verified | help@randrmagonline.com; Balzanod@bnpmedia.com (podcast sponsorship) | not found (media kit download, rates not read) |  | 2026-10 |
| [RIA sponsorship and year-round advertising](https://www.restorationindustry.org/ria-mission/sponsorship-year-round-advertising) | paid | 3 | verified | abray@restorationindustry.org; 856-437-4750 | not found (prospectus/media kit linked, not read) |  | 2026-10 |
| [The Experience (R&R / Violand conference)](https://www.theexperienceshow.com/) | paid | 3 | unverified | not found | not found | recency-unconfirmed | not found |
| [Claims Journal (bylined articles)](https://www.claimsjournal.com/) | free | 2 | verified | editorial@claimsjournal.com; (619) 584-1100 x121 | Free | vendor-restricted; exclusivity | 2026-10 |
| [Albiware blog (restoration software vendor)](https://www.albiware.com/blog/) | free | 2 | unverified | not found | not found |  | 2026-06 |
| [IICRC (IICRCToday newsletter / Clean Trust)](https://www.iicrc.org/news) | free | 2 | unverified | not found | not found | recency-unconfirmed | not found |
| [The Restoration Marketing Experts Podcast](https://iheart.com/podcast/84197803/) | free | 2 | unverified | not found | not found |  | 2026-10-01 |
| [Disaster Recovery Journal (DRJ)](https://drj.com/) | free | 1 | verified | jon@drj.com | Free editorial; sponsored content paid (Bob Arnold bob@drj.… | vendor-restricted | 2026-09 |
| [The Restoration Playbook Podcast (KnowHow) - COMPETITOR](https://restorationplaybook.transistor.fm/) | free | 1 | verified | not found | not found | competitor | 2026-04-10 |

### Trade Schools (core): 25 live outlets; Tier 1 (rel 4-5): 8 (6 verified); Tier 2 (rel 2-3): 17

| Outlet | Tier | Rel | Status | Contact route | Cost | Flags | Last content |
|---|---|---|---|---|---|---|---|
| [ACTE Techniques](https://www.acteonline.org/publications/techniques/) | free | 5 | verified | lmilgram@acteonline.org or Techniques submission form | Free to contribute; advertising via advertisingsales@acteon… | vendor-restricted; ai-policy | 2026-09-14 |
| [Career Education Review (CECU)](https://www.careereducationreview.net/) | free | 5 | verified | obfuscated - see page (Contact Us page) | Free to contribute (per snippet); advertising page exists,… |  | 2026-09-25 |
| [Community College Daily (AACC)](https://www.ccdaily.com/) | free | 4 | verified | mdembicki@aacc.nche.edu | Free earned; ads via YGS Group (Laura Gaenzle, Laura.gaenzl… |  | 2026-10-08 |
| [Higher Ed Dive - Opinion](https://www.highereddive.com/opinion/submit-opinion/) | free | 4 | verified | Submission form on page | Free; ads via advertise page (media kit) | ai-policy; exclusivity | 2026-10-02 |
| [Inside Higher Ed - Views / Careers](https://www.insidehighered.com/content/general-guidelines-submissions-inside-higher-ed) | free | 4 | verified | opinion@insidehighered.com; editor@insidehighered.com | Free | ai-policy | 2026-10-09 |
| [NCCER Newsroom (blog / guest writers)](https://www.nccer.org/newsroom/) | free | 4 | verified | media@nccer.org | Free (NCCER does not pay for content, per snippet) |  | 2026-10-09 |
| [ATD (Association for Talent Development)](https://www.td.org/) | free | 4 | unverified | not found | Not found | recency-unconfirmed | not found |
| [CECU (Career Education Colleges and Universities)](https://www.cecu.edu/) | paid | 4 | blocked-by-network-policy | not found | Not found | blocked; recency-unconfirmed | not found |
| [ACCT Trustee Quarterly](https://www.acct.org/publications-media/trustee-quarterly) | free | 3 | verified | not found | Not found |  | 2026-10 |
| [Campus Technology](https://campustechnology.com/pages/pr-guidelines.aspx) | free | 3 | verified | obfuscated - see page | Free for editorial; paid ads/sponsored content via advertis… |  | 2026-10-08 |
| [Education Dive](https://www.educationdive.com/) | free | 3 | verified | Submission form (shared with Higher Ed Dive) | Free; ads via advertise page |  | 2026-10 |
| [Technical Education Post (techedmagazine.com)](https://www.techedmagazine.com/) | free | 3 | verified | publisher@techedmagazine.com | Free for news releases; ad rates not found |  | 2026-09-01 |
| [University Business](https://universitybusiness.com/write-for-us) | free | 3 | verified | obfuscated - see page; phone 646-978-9578 on page | Free (no payment for columns); paid custom media for though… | vendor-restricted | 2026-10 |
| [AACC 21st-Century Center](https://www.aacc21stcenturycenter.org/?p=98) | free | 3 | unverified | not found | Free (unconfirmed) | recency-unconfirmed | not found |
| [ACTE Corporate Partnerships / Sponsorship / CTU & STEM Smar…](https://www.acteonline.org/partners/) | paid | 3 | verified | mwertz@smartbrief.com; advertisingsales@acteonline.org | Not found (rates in media kit PDF; text not readable) |  | 2026-10-07 |
| [SkillsUSA TECHSPO / Industry Partner](https://www.skillsusa.org/support-skillsusa/exhibit-advertise/) | paid | 3 | verified | not found | Not found |  | 2026-01-27 |
| [ACTE Events (CareerTech VISION, Postsecondary CTE Summit, W…](https://www.acteonline.org/events-calendar/) | paid | 3 | unverified | not found | Not found (speaker call/exhibit terms not read) |  | 2026-10-09 |
| [ACCT Podcast](https://www.acct.org/publications-media/podcast) | free | 2 | verified | not found | Not found |  | 2025-10-24 |
| [ACTE CTE Policy Watch Blog](https://www.acteonline.org/cte-policy-watch/) | free | 2 | verified | not found | Free (earned/ quoted only) |  | 2026-10-07 |
| [EdSurge - Contribute (Voices)](https://www.edsurge.com/submission-guidelines) | free | 2 | verified | voices@edsurge.com | Free | ai-policy | 2026-10 |
| [SkillsUSA Podcast](https://www.skillsusa.org/resources/news-room/podcasts/) | free | 2 | verified | not found | Not found | recency-unconfirmed | 2026 |
| [THE Journal](https://thejournal.com/) | free | 2 | verified | not found | Not found (ads at converge360.com/pages/advertising/the.asp… |  | 2026-10-08 |
| [Ohio College Tech Prep Podcast](https://techprepemail.podbean.com) | free | 2 | unverified | not found | Free | recency-unconfirmed | not found |
| [UPCEA Blogs / Corporate Member Blog Series](https://upcea.edu/blogs/) | paid | 2 | verified | not found | Corporate membership required (cost not found) |  | 2026-09-17 |
| [Tech Directions](https://www.techdirections.com/) | paid | 2 | unverified | matt@techdirections.com | Not found | recency-unconfirmed | not found |

### Building Automation (Quinn-listed): 11 live outlets; Tier 1 (rel 4-5): 3 (2 verified); Tier 2 (rel 2-3): 8

| Outlet | Tier | Rel | Status | Contact route | Cost | Flags | Last content |
|---|---|---|---|---|---|---|---|
| [AutomatedBuildings.com](https://www.automatedbuildings.com/) | free | 5 | verified | sponsors@automatedbuildings.com (sponsorship); no public editorial pi… | Free route: contributing editor / editorial-board-reviewed… | vendor-restricted; ai-policy | 2026-10-08 |
| [BUILDINGS (Endeavor Business Media)](https://buildings.com/) | free | 5 | verified | obfuscated - see page (https://buildings.com/contributors-guidelines)… | Free for contributed content; advertising via buildings.com… | vendor-restricted; ai-policy; exclusivity | 2026-09-23 (homep… |
| [Facility Executive (Group C Media; formerly Today's Facilit…](https://facilityexecutive.com/) | free | 4 | unverified | not found | not found | recency-unconfirmed | not found |
| [BACnet International - Journal of Building Automation](https://bacnetinternational.org/journals/) | free | 3 | verified | marycatherine@bacnetinternational.org (listed on submission page) | Free to submit; advertising per Journal Media Plan (rates n… | ai-policy | 2026-06 |
| [Consulting-Specifying Engineer (csemag.com)](https://www.csemag.com/) | free | 3 | verified | obfuscated - see page (ARozgus at wtwhmedia.com as shown on guideline… | Free (contributed) | ai-policy; exclusivity | 2026-09 |
| [Engineered Systems (ES NEWS)](https://www.esmagazine.com) | free | 3 | verified | Submit a Letter form (no guideline page found) | Free route not confirmed; advertise page https://www.esmaga… |  | 2026-10 |
| [Smart Buildings Academy Podcast (Phil Zito)](https://podcast.smartbuildingsacademy.com) | free | 3 | unverified | Contact section on https://www.smartbuildingsacademy.com (form; no gu… | not found | competitor; ai-policy | 2026-10-08 |
| [ASHRAE Journal](https://www.ashrae.org/technical-resources/ashrae-journal) | free | 2 | verified | letters@ashrae.org (letters); submission portal via guidelines page | Free | ai-policy; recency-unconfirmed | not found |
| [Memoori (smart building research)](https://www.memoori.com/) | free | 2 | verified | obfuscated - see page ([email protected] on about page) | not found | ai-policy | 2026-10-09 |
| [Control Engineering (WTWH Media / Arrowfly)](https://www.controleng.com/) | free | 2 | unverified | obfuscated - see page (MHoske at wtwhmedia.com per shared guidelines… | Free (contributed) | recency-unconfirmed | not found |
| [Realcomm / IBcon (Realcomm Webinars and conferences)](https://www.realcomm.com/) | paid | 2 | verified | ithompson@realcomm.com (webinar deliverables, listed on page); lwoods… | Sponsorship/exhibitor pricing not found (prospectus PDFs ex… | ai-policy | 2026-10 |

### Fire and Life Safety (Quinn-listed): 12 live outlets; Tier 1 (rel 4-5): 4 (1 verified); Tier 2 (rel 2-3): 8

| Outlet | Tier | Rel | Status | Contact route | Cost | Flags | Last content |
|---|---|---|---|---|---|---|---|
| [Security Sales & Integration (SSI)](https://www.securitysales.com/) | free | 4 | verified | obfuscated - see page (phone 914-383-9030 listed) | Free (earned/contributed); Advertise With Us page exists, r… | vendor-restricted; ai-policy; exclusivity | 2026-10 |
| [NFSA (National Fire Sprinkler Association) blog / NFS magaz…](https://nfsa.org/category/blog/) | free | 4 | unverified | https://nfsa.org/contact-us/ (contact page linked) | Membership/sponsorship rates not found |  | 2026-10-08 |
| [AFSA Sprinkler Age (American Fire Sprinkler Association)](https://firesprinkler.org/) | paid | 4 | unverified | Request pricing form on media kit page | Paid (request pricing). Editorial/contribution route not fo… | ai-policy | 2026-10 (media ki… |
| [NAFED (National Association of Fire Equipment Distributors)](https://www.nafed.org/) | paid | 4 | unverified | not found | not found | recency-unconfirmed | not found |
| [EHS Today (contributed articles)](https://www.ehstoday.com/) | free | 3 | verified | obfuscated - see page | Free (earned). Webinars/advertising are paid via Advertise… | vendor-restricted; exclusivity | 2026-10-07 |
| [Occupational Health & Safety (OH&S)](https://ohsonline.com/) | free | 3 | verified | obfuscated - see page | Free (earned). Advertising via Converge360 (rates not found) | ai-policy | 2026-10-08 |
| [SecurityInfoWatch / Security Business / Security Executive](https://www.securityinfowatch.com/) | free | 3 | verified | obfuscated - see page; press releases: submitnews@securityinfowatch.c… | Free for press release/pitch; paid advertising/sponsored co… |  | 2026-10 |
| [NFPA Conference & Expo](https://www.nfpa.org/conference) | free | 3 | unverified | not found | Speaker route free if accepted; exhibiting is paid (rates n… |  | 2026-06 |
| [NFPA Journal](https://www.nfpa.org/news-blogs-and-articles/nfpa-journal) | free | 3 | unverified | not found | not found | recency-unconfirmed | not found |
| [Fire Engineering](https://www.fireengineering.com/submissions/) | free | 2 | verified | email submission (address not read) | Free; Advertise link exists | exclusivity | 2026-10-05 |
| [Fire Protection Engineering (SFPE)](https://www.sfpe.org/publications/periodicals/fpemagazine) | free | 2 | verified | jreichert@sfpe.org; info@sfpe.org | Free (contributed). Advertising Opportunities page exists,… | ai-policy; recency-unconfirmed | 2026 |
| [FireRescue1 / ASIS Security Management (responder and secur…](https://www.firerescue1.com/) | free | 2 | unverified | not found | not found | recency-unconfirmed | not found |

### Industrial Automation (Quinn-listed): 15 live outlets; Tier 1 (rel 4-5): 5 (5 verified); Tier 2 (rel 2-3): 10

| Outlet | Tier | Rel | Status | Contact route | Cost | Flags | Last content |
|---|---|---|---|---|---|---|---|
| [IndustryWeek (Endeavor)](https://www.industryweek.com/) | free | 5 | verified | obfuscated - see page (contributor email on guidelines page); pitch a… | Free (contributed); advertising via Advertise page (rates n… | ai-policy; exclusivity | 2026-10-07 |
| [Plant Services (Endeavor)](https://www.plantservices.com/) | free | 5 | verified | obfuscated - see page (editor email shown on contact page) | Free to pitch editor; paid: advertising, webinars, eHandboo… | vendor-restricted | 2026-10-09 |
| [Automation World (Endeavor)](https://www.automationworld.com/) | free | 4 | verified | obfuscated - see page (Chris McNamara email on contact page) | Free for editorial pitch/podcast; paid: sponsored content,… | ai-policy | 2026-10-07 |
| [Plant Engineering (WTWH Media / Arrowfly)](https://www.plantengineering.com/) | free | 4 | verified | obfuscated - see page (ARozgus at wtwhmedia.com per shared guidelines… | Free (contributed); advertising available via advertise lin… | ai-policy; exclusivity; recency-unconfirmed | 2026 |
| [Reliable Plant / Machinery Lubrication (Noria)](https://www.reliableplant.com/) | free | 4 | verified | Online submission form on guidelines page; sales@noria.com for paid p… | Free for unpaid educational articles/case studies; paid: co… | vendor-restricted; ai-policy | 2026-10-02 |
| [Control Design (Endeavor)](https://www.controldesign.com/) | free | 3 | verified | obfuscated - see page (editor emails on contact page); sales emails @… | Free to pitch; paid via sales (Mitch Brian, VP Sales) |  | 2026-10-05 |
| [ISA InTech / Automation.com (International Society of Autom…](https://www.isa.org/intech-home) | free | 3 | verified | rbassett@isa.org (listed on guidelines page); 919-990-9250 | Free (contributed); sponsorship/advertising via Automation.… | vendor-restricted; ai-policy; exclusivity; recency-unconfirmed | 2026 (InTech foot… |
| [The Manufacturing Institute (NAM)](https://themanufacturinginstitute.org/) | free | 3 | verified | not found (contact not read on pages fetched) | Free for earned/partner exposure; sponsorships/membership n… |  | 2026-10-02 |
| [Manufacturing.net](https://www.manufacturing.net/) | free | 3 | unverified | not found | Free | recency-unconfirmed | not found |
| [TD magazine (ATD - Association for Talent Development)](https://www.td.org/magazines/td-magazine) | free | 3 | unverified | not found | Free | recency-unconfirmed | not found |
| [Industry Today](https://industrytoday.com/) | paid | 3 | verified | editorialdesk@industrytoday.com (article outline pitch) | Paid placement is the main route (banners, dedicated emails… | ai-policy | 2026-10-08 |
| [SME - Manufacturing Engineering magazine / AdvancedManufact…](https://www.sme.org/smemedia/sme-media/) | free | 2 | verified | Speaker interest form on speaking-opportunities page; SME Media conta… | Free to apply to speak; sponsorship/advertising rates not f… | ai-policy; recency-unconfirmed | not found |
| [A3 - Association for Advancing Automation (Automate, Automa…](https://www.automate.org/) | free | 2 | unverified | jrose@automate.org listed as media contact in Sept 2025 press release… | not found | recency-unconfirmed | not found |
| [Control Engineering (WTWH Media / Arrowfly)](https://www.controleng.com/) | free | 2 | unverified | obfuscated - see page (MHoske at wtwhmedia.com per shared guidelines… | Free (contributed) | recency-unconfirmed | not found |
| [Podomation (ISA podcast)](https://www.isa.org/about-isa/podomation) | paid | 2 | verified | podomation@isa.org (advertising inquiries); media@isa.org (interview… | Advertising route listed (rate not found); guest route appe… |  | 2026-06 |

### Adjacent (plumbing, electrical, home services, FSM, workforce, L&D) (adjacent): 27 live outlets; Tier 1 (rel 4-5): 8 (7 verified); Tier 2 (rel 2-3): 18

| Outlet | Tier | Rel | Status | Contact route | Cost | Flags | Last content |
|---|---|---|---|---|---|---|---|
| [CONTRACTOR (Contractor Magazine)](https://www.contractormag.com/) | free | 5 | verified | obfuscated - see page | Free (earned). Fee-based Sponsored Content / 'Preferred Med… | vendor-restricted; ai-policy | 2026-10-09 |
| [IEC Business Summit 2027 - Call for Content (Independent El…](https://ieci.org/call-for-content/) | free | 5 | verified | kmessenger@ieci.org | Free to submit (speaker compensation not found) |  | 2026-07-30 |
| [EC&M (Electrical Construction & Maintenance)](https://www.ecmweb.com) | free | 4 | verified | obfuscated - see page | Free for editorial; fee-based sponsored content available | vendor-restricted | 2026-07-31 |
| [Training Industry (website articles + Training Industry Mag…](https://trainingindustry.com) | free | 4 | verified | editor@trainingindustry.com (submission form linked on guidelines pag… | Free; authors assign rights to Training Industry. Media kit… | vendor-restricted; ai-policy; exclusivity | 2026-09 |
| [Training Magazine (Lakewood Media Group)](https://trainingmag.com) | free | 4 | verified | Grace@TrainingMag.com (guidelines on request) / Lorri@TrainingMag.com | Free for editorial (per old listing, unpaid online articles… |  | 2026-09 |
| [Electrical Contractor (ECmag, NECA)](https://www.ecmag.com) | free | 4 | unverified | not found | not found | recency-unconfirmed | not found |
| [Plumbing & Mechanical (BNP Media)](https://www.pmmag.com) | paid | 4 | verified | Advertising inquiry form (see page); contributor contact not found | Not found (rate card not public) |  | 2026-10 |
| [Service World Expo / Service Nation (Service Roundtable)](https://serviceworldexpo.com) | paid | 4 | verified | sponsorship brochure by form | not found (brochure) |  | 2026-10 |
| [Chief Learning Officer (CLO) magazine](https://www.chieflearningofficer.com) | free | 3 | verified | Submission form linked from guidelines page (not read); older listing… | Free for practitioner contributions; sponsorship/advertise… | ai-policy; exclusivity | 2026-10 |
| [Field Service News (Copperberg AB)](https://www.fieldservicenews.com) | free | 3 | verified | contact form on https://www.fieldservicenews.com/contact-us/ | Press-partner/paid campaign pricing not found |  | 2026-10-09 |
| [HR Dive (Informa TechTarget) - opinion section](https://www.hrdive.com) | free | 3 | verified | obfuscated - see page (submission form on page) | Free | ai-policy; exclusivity | 2026-10-01 |
| [Jobs for the Future (JFF)](https://www.jff.org) | free | 3 | verified | https://www.jff.org/contact-us/ (form) | Free |  | 2026-10-08 |
| [Learning Solutions (The Learning Guild)](https://www.learningguild.com) | free | 3 | verified | obfuscated - see page | Free to authors and readers | vendor-restricted; ai-policy | 2026-10 |
| [ServiceTitan blog, podcast and Pantheon](https://www.servicetitan.com/blog) | free | 3 | verified | not found | Not found |  | 2026-10 |
| [Training Industry - The Business of Learning podcast](https://trainingindustry.com/writing-for-training-industry/) | free | 3 | verified | editor@trainingindustry.com | Free |  | 2026-09 |
| [Training Industry Conference & Expo (TICE) 2027 call for pr…](https://trainingindustry.com/tice/training-industry-conference-expo-call-for-presenters/) | free | 3 | verified | Submission form linked on page | Free to submit; unpaid speaking, complimentary registration… |  | 2026-07 |
| [TD magazine (ATD - Association for Talent Development)](https://www.td.org/magazines/td-magazine) | free | 3 | unverified | not found | Free | recency-unconfirmed | not found |
| [Workforce Dive (Informa TechTarget)](https://www.workforcedive.com) | free | 3 | blocked-by-network-policy | not found | not found | blocked; recency-unconfirmed | not found |
| [IEC Insights magazine](https://ieci.org/insights/advertise/) | paid | 3 | verified | contact via ieci.org/contact-us | Full page print+digital $5,500; spread $7,000; half page $5… |  | 2026-10-08 |
| [PHCC Solutions magazine and eNewsletter (Plumbing-Heating-C…](https://www.phccweb.org) | paid | 3 | verified | jboulka@thewymancompany.com | Not found; associate-member discounts mentioned |  | 2026-10-08 |
| [ASPE Pipeline (American Society of Plumbing Engineers)](https://aspe.org/pipeline/) | free | 2 | verified | gpienta@aspe.org | Free; ASPE holds copyright, author keeps nonexclusive licen… |  | 2026-09-24 |
| [National Skills Coalition](https://nationalskillscoalition.org) | free | 2 | verified | info@nationalskillscoalition.org | Free |  | 2026-10-08 |
| [Pro Remodeler (Endeavor Business Media)](https://www.proremodeler.com) | free | 2 | verified | https://www.proremodeler.com/contact-us | Free editorial; advertise page exists (price not found) |  | 2026-08-06 |
| [Housecall Pro podcast and Tradewire newsletter](https://www.housecallpro.com/podcasts/) | free | 2 | unverified | https://www.housecallpro.com/contact-us/ | Free |  | 2026-04 |
| [eLearning Industry](https://elearningindustry.com) | paid | 2 | verified | contact email obfuscated - see page (about-us) | Original article $788-$1,099; republished article $788-$1,0… |  | 2026-10 |
| [Field Service USA / Field Service Next (WBR Insights)](https://fieldserviceusa.wbresearch.com) | paid | 2 | unverified | not found | not found | recency-unconfirmed | not found |
| [Workiz blog](https://www.workiz.com/blog/) | free | 1 | unverified | not found | Free |  | 2026-10 |

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

## 4. Flagged outlets

### Sibling-outlet exclusivity (pitch one per group per piece)

Parent companies below are as reported on the outlets' own pages by the research agents unless marked unconfirmed. Re-check before pitching.

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


### Software-vendor bans / vendor-restricted (Quinn is a software company) (3)

Hard bans. Quinn's routes there are paid Branded Features or a customer-authored byline. Soft restrictions ("vendor-restricted" flag, e.g. ACHR News 'highly selective' on AI/software, ACCA no-sales-pitch, RIA non-proprietary, University Business rejects product/case-study content, Consulting-Specifying Engineer rejects vendor-focused articles, DRJ and Claims Journal ban company mentions) are in the `flags` and `editorial_rules` columns of `master.csv`.

- **Building Operating Management and Facility Maintenance Decisions (Tra…** (Facilities Maintenance; verified): SIBLING EXCLUSIVITY/VENDOR BAN: editorial for both magazines goes through the same FacilitiesNet contributed-content rules (no software providers; exclusive to FacilitiesNet) so one pitch covers the whole Trade Press family and cannot be shopped to HFT or oth… [https://www.facilitiesnet.com/advertise]
- **FacilitiesNet (Trade Press Media Group)** (Facilities Maintenance; verified): VENDOR BAN: 'We do not accept articles from product manufacturers or software providers' and 'solutions should not be brand-specific' (quoted from guidelines page). Quinn is a software provider so direct byline is barred; only route is a practitioner or custo… [https://www.facilitiesnet.com/site/page.aspx?id=38391]
- **Healthcare Facilities Today (Trade Press Media Group)** (Facilities Maintenance; verified): VENDOR BAN: 'we do not accept articles from product manufacturers or software designers'. 300-word synopsis first; EXCLUSIVE to HFT. Sibling of FacilitiesNet/BOM/FMD (same parent Trade Press Media Group). No AI policy found [https://www.healthcarefacilitiestoday.com/pages/Contributing-to-Healthcare-Facilities-Today--622?source=nav]

### AI-content policies (Quinn is an AI company): 46 outlets mention one

Hard or notable ones: Higher Ed Dive, Construction Dive, Facilities Dive and HR Dive ban generative AI in op-eds; Contracting Business and CONTRACTOR cap AI at 20% (Contracting Business requires disclosure); IndustryWeek caps AI at 10% with disclosure; Training Industry prohibits AI-generated text; EHS Today: no AI-written articles; Inside Higher Ed and EdSurge require disclosure; ASHRAE prohibits entering its content into AI tools; ACHR News is highly selective on AI pitches. Full per-outlet text is in `editorial_rules`. Flag matched by keyword; verify against the cited source before relying on it.


### Competitors (do not pitch) (2)

- **Smart Buildings Academy Podcast (Phil Zito)** (Building Automation; unverified): No guest/pitch policy found. FLAG: Smart Buildings Academy sells BAS technician training/workforce development programs, so it is a direct competitor to Quinn's training value prop - expect resistance or vendor-vs-vendor positioning; no AI policy found [https://www.smartbuildingsacademy.com/]
- **The Restoration Playbook Podcast (KnowHow) - COMPETITOR** (Restoration; verified): VENDOR CONFLICT: run by KnowHow, a restoration workforce training/onboarding platform that directly competes with Quinn; also tied to R&R and RIA Cost of Doing Business Survey. Do not pitch. Guests are customers/operators. [https://restorationplaybook.transistor.fm/]

### Inactive (no content in last 12 months) (8)

- **D and A Pest Control Podcast** (Pest Control; inactive): Newest episode visible Nov 2024; no content in last 12 months [https://dandapestpodcast.buzzsprout.com/874597]
- **Field Technologies Online** (Adjacent (plumbing, electrical, home se…; inactive): Vendor/supplier/technology-partner content NOT accepted even if non-promotional; AI-written text must be reworked, AI-generated images not accepted. Audience is life sciences, not trades. Newest visible dates 2024. [https://www.fieldtechnologiesonline.com/doc/guest-expert-article-guidelines-0001]
- **Grounds Maintenance** (Landscaping; inactive): Domain is now a premium domain for sale (DomainMarket); no publication content. [https://www.groundsmaintenance.com/]
- **Landscaper's Business Growth Podcast (John Giaccotto)** (Landscaping; inactive): Only aggregator page read; newest episode shown 2024-12-30, so appears inactive (no content within 12 months seen). [https://rephonic.com/podcasts/the-landscapers-business-growth-podcast]
- **LonMark International** (Building Automation; inactive): Homepage last modified 2025-07-29; no content dated since 2025-10-09 seen; no contributor policy found; chaired by Tracy Markie of Engenuity Systems (per AutomatedBuildings media kit) [https://lonmark.org/]
- **MCAA (Mechanical Business magazine, Inside MCAA podcast, events)** (Mechanical Contracting; inactive): mcaa.org returned HTTP 403 to fetcher - nothing verified. Do not conflate with Marie Curie Alumni Association results [merge: last content 2025-03 is >12 months old, set inactive] [https://www.mcaa.org/news/inside-mcaa-the-blueprint-for-mechanical-contracting-ep-5-the-evolution-of-technology-in-the-mechanical-industry]
- **Pest Control Marketing Podcast (Hal Coleman and Mike Stewart)** (Pest Control; inactive): Newest listed episode 2025-01-12 says show is not ending but changing focus; no content in last 12 months seen [https://podcasts.apple.com/podcast/id1020838126]
- **The Restoration Revolution Podcast (Hazard Clean)** (Restoration; inactive): Company marketing podcast; no episode since July 2025. [https://www.buzzsprout.com/2286310]

### Blocked by network policy (5)

Recorded and not worked around; retry from an environment where the host is allowed.

- **United Association (UA) training** (Mechanical Contracting; blocked-by-network-policy): blocked-by-network-policy; apprenticeship/training angle remains strategically valuable (training directors, JATCs) [https://www.ua.org]
- **CECU (Career Education Colleges and Universities)** (Trade Schools; blocked-by-network-policy): Domain blocked by network policy; CER is CECU-owned (see CER row). Convention highlights page 2026 exists on CER site. [https://www.cecu.edu/]
- **Workforce Dive (Informa TechTarget)** (Adjacent (plumbing, electrical, home se…; blocked-by-network-policy): Blocked by network policy; same parent as HR Dive (exclusivity and AI-ban rules probably shared; unconfirmed). [https://www.workforcedive.com/]
- **Plumbing Engineer** (Mechanical Contracting; blocked-by-network-policy): blocked-by-network-policy [https://www.pemag.com]
- **Pest Management Podcast (pestmanagementpodcast.com)** (Pest Control; blocked-by-network-policy): Domain blocked-by-network-policy; existence unconfirmed [https://www.pestmanagementpodcast.com]

### Possible paywall/members-only language (0; keyword match, verify)


### Time-sensitive

- **IEC Business Summit 2027 - Call for Content (Independent Electrical Contractors)**: 2026-11-06 (call for content closes). [https://ieci.org/call-for-content/]
- **RIA International Restoration Convention - Call for Presentations**: 2026-10-16 (convention call for presentations closes). [https://convention.restorationindustry.org/call-presentations]
- **ACTE Techniques**: 2026-12-01 (proposals for Mar/Apr 2027 issue). [https://www.acteonline.org/publications/techniques/techniques-editorial-calendar/]
- Several 2026 conference speaker calls already closed (IFMA World Workplace, SMRP, International Roofing Expo 2027 closed 2026-04-18, TICE 2027 closed 2026-10-02); the next windows are spring 2027. PestWorld's Technology Adopter Award reopens spring 2027 (White Knight is a natural nominee).

## 5. Gaps remaining

**Tier-1 shortfalls (relevance 4-5 outlets, live), versus the 10-15 target:** HVAC: 12 (12 verified); Pest Control: 8 (4 verified); Mechanical Contracting: 9 (7 verified); Facilities Maintenance: 9 (8 verified); Roofing: 8 (8 verified); Landscaping: 6 (2 verified); Restoration: 8 (6 verified); Trade Schools: 8 (6 verified). Several fall short because few outlets in the trade accept contributed content, not only because of access limits.

**High-fit outlets still unverified (need a human or a less restricted network):**

- Landscape Management (Landscaping): Fetch returned http-403 so nothing read. Search shows 2026 issues listed through June 2026. Parent unresolved: historical mastheads show Questex (2011-12) and…
- Green Industry Podcast (Paul Jamison) (Landscaping): Show description read; no guest policy or AI policy published. Independent host, not tied to a magazine group (no sibling conflict found). Latest episode 2026-…
- Pest Management Professional (PMP) (Pest Control): mypmp.net returned HTTP 403 for all pages, so nothing was read. Seed said Gie Media; third-party FeedSpot listing names North Coast Media LLC as publisher (old…
- Pest Control Technology (PCT) (Pest Control): UNRESOLVED seed: pctonline.com returned empty/bot-challenge (Incapsula) responses to the fetch tool, so no guidelines, dates or contacts could be read. Parent…
- Lawn & Landscape (GIE Media) (Landscaping): UNRESOLVED/UNVERIFIED: site returned empty text to fetcher, so no policy read. Parent: GIE Media (Valley View, OH) per search results. Sibling exclusivity: GIE…
- Cleaning & Restoration (C&R) Magazine (Restoration): candrmagazine.com returned HTTP 403 to the fetcher; not worked around. Info only from RIA page. Columns 'with industry thought leaders'. Owned by Blevins who a…
- NFSA (National Fire Sprinkler Association) blog / NFS magazine (Fire and Life Safety): NFSA magazine page (app.nfsa.org) disallowed by robots.txt; no contributor guidelines found. Pitch NFSA education/training staff for seminar or webinar guest s…
- Pest Control Legends (podcast, Dan Leibrandt) (Pest Control): Official site pestcontrollegends.com blocked-by-network-policy; facts come from third-party aggregator only. Aggregator tag says 'Accepts Guests' (search resul…
- Restoration Today podcast (Michelle Blevins) (Restoration): Read via Apple Podcasts listing only. Vendor guests appear (Verisk, DocuSketch), some in sponsor-branded series so vendor appearances may be sponsorship-gated.…
- Electrical Contractor (ECmag, NECA) (Adjacent (plumbing, electrica…): ecmag.com returned HTTP 403; submission policy unread. Search snippet only says NECA publishes it.
- Facility Executive (Group C Media; formerly Today's Facility Manager) (Facilities Maintenance; Build…): Could not read: site returned HTTP 403. Search result shows Facility Executive is the renamed Today's Facility Manager (same outlet), Group C Media, Red Bank N…
- Pest in Class (FieldRoutes / ServiceTitan podcast) (Pest Control): Vendor-owned show (FieldRoutes, a ServiceTitan company). Guests are customer operators; episode topics include SOPs and technician retention. Quinn builds Fiel…
- ATD (Association for Talent Development) (Trade Schools): Fetch returned HTTP 429; not read. (Note: atd.org is American Truck Dealers, not this.) Likely AI/ vendor rules exist; check manually.
- Turf Magazine (Group C Media) (Landscaping): Pages returned http-403 to fetcher, details from search snippets only. Parent: Group C Media (acquired 2018 per 2019 editor's letter; current ownership unconfi…
- AFSA Sprinkler Age (American Fire Sprinkler Association) (Fire and Life Safety): Dedicated eblast has 100% share of voice (no exclusivity conflict); no AI policy found.
- NAFED (National Association of Fire Equipment Distributors) (Fire and Life Safety): nafed.org disallowed by robots.txt; not read. Association mission includes technical competence of members, a direct training fit.

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


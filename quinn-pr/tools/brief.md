# Research brief (shared by all industry subagents)

Client: Quinn (meetquinn.ai) - AI operational-readiness platform for the skilled trades (SOP->courses, roleplay sims, text-based "Ask Quinn", readiness scoring, ServiceTitan/FieldRoutes practice replicas, career pathing). Read ./context.md. Quinn is an AI company, so AI-content policies matter. Goal: get Quinn founders/execs PUBLISHED (bylines, expert commentary, case studies, podcast/webinar guest spots) in outlets reaching owners, GMs, ops leaders, training managers, school administrators. Today is 2026-10-09.

## How to work (HARD RULES)
- Working dir: /home/user/Quinn-Publication/quinn-pr. Read pages ONLY with: `python3 tools/fetch.py <URL> [--links] [--max N]`. It honors robots.txt, rate-limits 1.5s/domain, caches to ./cache/ (so never fetch the same URL twice; re-running is free), and prints `STATUS=... FETCHED=... URL=...`. Do NOT use raw curl/WebFetch on target sites. Use WebSearch (standard mode) only for discovery (finding URLs of guidelines pages, outlets, podcasts, associations).
- Public pages only. No logins, no paywall/bot-check circumvention, no form submissions.
- If STATUS is blocked-by-network-policy, robots-disallowed, or any http-4xx/5xx: do NOT work around it. Record that outlet with status "blocked-by-network-policy" (or "unverified" for other failures), put "not found" in unread fields, move on. Don't try alternate mirrors/archives.
- Extract contact details ONLY if the publication itself lists them publicly on a page you read. Obfuscated -> write "obfuscated - see page". Never guess an address or name. Never invent prices, circulation, editor names: write "not found".
- status=verified ONLY if you read that outlet's page text yourself (guidelines or about/advertise page). Otherwise unverified. inactive = no content dated within last 12 months (since 2025-10-09). paywalled = content/guidelines behind paywall.
- Every fact about submission policy, pricing, circulation or contact needs a source URL. In source_urls use the format `fact: URL (fetched YYYY-MM-DD)` separated by " | ". Check recency: find the date of the newest article/episode you can see on the site (last_content_date, YYYY-MM-DD or YYYY-MM). Drop outlets with nothing in last 12 months into the CSV with status=inactive (they get flagged, not ranked).
- Search each industry for: "write for us", contributor/author guidelines, editorial submissions, podcast guest, newsletter sponsorship, advertise/media kit, association magazine, awards/events with speaker calls. Check relevant trade associations. Flag: exclusivity conflicts between sibling outlets (same parent company - note parent), software-vendor bans, vendor-neutral/no-commercial-content rules, AI-content/AI-disclosure policies.
- Be efficient: don't read more than needed (guidelines page + one about/advertise page + homepage/recent-article for date per outlet). Spend your effort on breadth of correctly verified outlets, not prose.
- Targets: for a CORE industry 10-15 Tier 1 (best fit, realistic first moves) + 5-8 Tier 2 outlets. For adjacent/smaller industries aim 8-12 total. Quality over quantity: if fewer genuinely active outlets exist, say so in your final note.

## Output
Write research/<industry>.csv (proper CSV quoting, UTF-8, header row exactly):
name,url,industry,tier,audience,circulation_or_subs,content_types,typical_length,guidelines_url,contact_name,contact_email_or_form,cost,editorial_rules,relevance_1_5,suggested_angle,last_content_date,source_urls,status
- tier: "free" (earned/contributed/guest, no payment) or "paid" (sponsorship, advertising, paid placement required). Outlets with both: choose the route that matters for Quinn's first move and mention the other in cost/editorial_rules.
- industry: your industry label (use the same label on every row).
- relevance_1_5: fit for Quinn's buyers (5 = ops/training leaders at trade companies, active contributed-content channel).
- suggested_angle: one concrete pitch grounded in Quinn's real proof (White Knight: 446 employees, 226 courses, 97% participation, 96% completion, reported ~$1M/yr technician attrition cost reduction per meetquinn.ai/results/white-knight; 200+ ops teams; 3-day launch; 94% completion; ~40% faster ramp (Quinn benchmark)). Don't invent customer quotes.
- Validate the CSV parses with python3 (csv module) before finishing.
Final reply (<=150 words): file path, row count, counts by status, top 3 first moves, any blocked domains, any gaps.

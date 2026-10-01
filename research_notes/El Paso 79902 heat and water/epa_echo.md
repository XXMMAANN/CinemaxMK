# EPA ECHO / SDWA / CWA Compliance: El Paso Water and ZIP 79902 facilities

**Note on method (read first):** I could not reach any primary EPA or TCEQ data source from this research environment. The egress proxy blocked every one of these hosts with a CONNECT 403 or EGRESS_BLOCKED error, through both curl and WebFetch:
- `https://echodata.epa.gov/echo/sdw_rest_services.get_systems?output=JSON&p_pwsid=TX0710002` (ECHO SDW REST)
- `https://echo.epa.gov/detailed-facility-report?fid=TX0710002` (ECHO DFR)
- `https://data.epa.gov/efservice/VIOLATION/PWSID/TX0710002/JSON` (Envirofacts SDWIS VIOLATION table)
- `www.tceq.texas.gov` (TCEQ agenda backup PDFs), `www.env.nm.gov` (NMED), `mytapwater.org`, `elpasomatters.org`

Everything below therefore comes from web-search result snippets and summaries, not from reading the pages in full. Search snippets can be wrong or out of context, so the report writer should treat the specific numbers as **unverified** unless a primary source confirms them. ECHO-specific fields could not be retrieved at all: quarters in noncompliance, effluent exceedance counts, Serious Violator / SNC flags, and the ECHO compliance status.

## Q1: SDWA record for El Paso Water (PWSID TX0710002)

### Takeaway
I found no evidence of a recent health-based drinking-water violation. Third-party aggregators built on SDWIS say the system's violations in the last 3 years were all monitoring/reporting violations. The only drinking-water enforcement I could document is a small TCEQ fine in 2022 for the utility's water-hauling (truck) facility. I could not retrieve ECHO's own status fields.

### Cited Findings
- PWSID TX0710002 ("El Paso Water Utilities Public Service B[oard]") is a community water system serving about 672,538 people, with surface water as its primary source. — [Search summary citing mytapwater.org](https://mytapwater.org/pws/tx0710002/el-paso-water-utilities-public-service-b/el-paso-tx/)
- One aggregator reports 12 violations in the past 3 years, **0 health-based and 12 monitoring/reporting**, and 69 EPA violations on record, the most recent in 2024. — [tapwater.org](https://www.tapwater.org/texas/el-paso) / [tapsafetyreport.com](https://tapsafetyreport.com/texas/el-paso) (aggregators; exact attribution among the result pages is unclear)
- A different aggregator snippet reports 858 violations on record, 192 of them health-based, and 234 violations in the past 5 years. — search summary of [mytapwater.org](https://mytapwater.org/pws/tx0710002/el-paso-water-utilities-public-service-b/el-paso-tx/) / [waterverge.com](https://www.waterverge.com/cities/el-paso-tx/). **This conflicts with the "69 violations" figure above.** It may be counting all-time records, other systems, or rule-level rows. Do not use it without checking SDWIS.
- Aggregators report that UCMR 5 testing detected 7 PFAS compounds. One aggregator claims some levels exceed the EPA MCLs. — [tapwater.org](https://www.tapwater.org/texas/el-paso). The PFAS MCLs are not yet enforceable (compliance begins 2029; EPA has proposed extending some), so this would **not** be an SDWA violation. Treat the claim with caution.
- **Enforcement:** TCEQ fined El Paso Water $7,728 (approved around July 2022) for six violations of state drinking-water safety rules. The violations were found in a September 2020 TCEQ compliance inspection of the utility's water-hauling facility. — [El Paso Matters, 2022-07-14](https://elpasomatters.org/2022/07/14/tceq-fines-el-paso-utility-for-drinking-water-truck-health-safety-violations/)

### Inferences
- If the aggregators are mirroring SDWIS correctly, ECHO probably shows TX0710002 without a current health-based violation and without Serious Violator status. This needs confirmation from the ECHO DFR.

### Gaps
- I could not retrieve violation codes, contaminants, compliance-period dates, RTC status or enforcement actions from SDWIS/ECHO, because echo.epa.gov, echodata.epa.gov and data.epa.gov were all blocked.
- I could not retrieve the Serious Violator flag or the current ECHO compliance status.
- I did not identify which rules the 12 monitoring/reporting violations fall under (for example, Lead and Copper, DBP or Total Coliform).

## Q2: CWA / NPDES and wastewater enforcement (Haskell R. Street, Bustamante, Hickerson, Fred Hervey; Frontera force main)

### Takeaway
The main wastewater enforcement case of 2021–2026 is the Frontera Force Main emergency. From August 2021 to January 2022, about 1.2 billion gallons of raw sewage were diverted to the Rio Grande. TCEQ resolved it with a 2022 Agreed Order: a $2,016,000 penalty offset by a Supplemental Environmental Project. New Mexico's separate $1.2M fine was later withdrawn. Plant spills after that (2025–2026) are documented in news reports, but I found no resulting enforcement orders.

### Cited Findings
- **TCEQ Docket 2022-0310-MWD-E** (El Paso Water Utilities Public Service Board): On August 27, 2021, a sewer main break near 4134 Doniphan Drive caused a sanitary sewer overflow. From August 27, 2021 through January 10, 2022, the utility diverted all raw sewage at the Frontera Lift Station into the storm sewer and on to the Rio Grande at the Doniphan Outfall. The estimated rate was 9 MGD, about 1.2 billion gallons in total. The order also cites alleged unauthorized discharges of 350,000, 450,000 and 310,000 gallons of raw sewage. — [TCEQ agenda backup 2022-0310-MWD-E](https://www.tceq.texas.gov/downloads/agency/decisions/agendas/backup/2022/2022-0310-mwd-e.pdf) (search snippet only; the PDF was blocked)
- The TCEQ Agreed Order set an administrative penalty of $2,016,000, offset by the utility performing a SEP. EPWater says it spent about $7 million or more on cleanup and cooperated with TCEQ from the start. — [KFOX14](https://kfoxtv.com/news/local/el-paso-water-fined-2-million-for-dumping-wastewater-into-rio-grande); [KTSM](https://www.ktsm.com/local/el-paso-news/ep-water-fined-2m-for-frontera-wastewater-dump-into-rio-grande/)
- **NMED:** In June 2022, the New Mexico Environment Department fined EPWater $1.2M and issued two Administrative Compliance Orders under NM surface/groundwater regulations, because the discharge entered the river at Sunland Park, NM. EPWater appealed and sued in Texas courts. NMED later **withdrew the fine and all allegations** as part of a settlement, after its attorneys concluded the case would not succeed. EPWater agreed to keep supplying information to NMED. — [NMED release](https://www.env.nm.gov/el-paso-water-fined-for-discharging-1-1-billion-gallons-of-raw-sewage-into-the-rio-grande-river-in-sunland-park-new-mexico/); [Source NM](https://sourcenm.com/briefs/nm-officials-withdraw-1-2-million-fine-against-el-paso-water/); [KRQE](https://www.krqe.com/news/new-mexico/new-mexico-withdraws-1-2m-fine-against-el-paso-water-in-sewage-discharge-case/); [EPWater](https://www.epwater.org/about-us/newsroom/nmed-withdraws-fine-against-epwater)
- **Roberto Bustamante WWTP** (10001 Pan American Dr): A 36-inch line broke on April 17, 2025, spilling about 800,000 gallons of wastewater. The spill was contained on plant property. A separate 560,000-gallon spill at the same plant is also reported, date not confirmed. — [KVIA 2025-04-18](https://kvia.com/news/texas/2025/04/18/800000-gallons-of-wastewater-spill-in-lower-valley/); [KFOX14 560K](https://kfoxtv.com/news/local/el-paso-water-contains-560000-gallon-spill-at-bustamante-plant-cleanup-underway)
- **John T. Hickerson WWTP** (West El Paso): Four contractor pumps failed on March 24, 2026, spilling about 670,000 gallons. Most of it was contained on site, but a "minimal amount" reached the mostly dry Rio Grande bed. The spill was reported to TCEQ. — [KVIA 2026-03-24](https://kvia.com/news/top-stories/2026/03/24/670000-gallons-of-wastewater-spill-contained-to-john-t-hickerson-treatment-facility/); [EPWater](https://www.epwater.org/about-us/newsroom/wastewater-spill-contained-at-john-t-hickerson-treatment-facility)
- **Collection system:** About 950,000 gallons spilled on Railroad Drive in Northeast El Paso in April 2026, reported to TCEQ Region 6. — [KFOX14](https://kfoxtv.com/news/local/el-paso-water-contains-950000-gallon-wastewater-spill-in-northeast); [Hoodline](https://hoodline.com/2026/04/railroad-drive-reek-950-000-gallon-sewage-spill-slams-northeast-el-paso/)

### Inferences
- The SSOs/unauthorized discharges would likely show up in ECHO as CWA violations for the collection system / TPDES permits. That cannot be confirmed here.
- I found no reports of EPA federal enforcement (as opposed to state enforcement) against EPWater under the CWA for 2021–2026.

### Gaps
- I could not obtain NPDES/TPDES permit IDs, quarters in noncompliance, DMR effluent exceedances or SNC status for Haskell R. Street, Bustamante, Hickerson or Fred Hervey (ECHO blocked).
- I found nothing specific on the Haskell R. Street or Fred Hervey plants.
- I don't know whether TCEQ issued NOVs or orders for the 2025–2026 spills, or whether the 2022 SEP has been completed.
- One search snippet said "10 million gallons" for the Frontera event. That appears to be a misreading of the roughly 9–10 MGD rate; the documented total is about 1.2 billion gallons.

## Q3: ECHO-listed facilities in ZIP 79902

### Takeaway
I could not run the ECHO facility search by ZIP. **The former ASARCO smelter is not in 79902.** Its address is 2301 W. Paisano Dr, El Paso, TX **79922**. Its lead and arsenic legacy does reach 79902 neighborhoods such as Kern Place, through the EPA "El Paso County Metals" residential soil cleanup.

### Cited Findings
- ASARCO site address: Texas Custodial Trust, 2301 West Paisano Drive, El Paso, TX 79922. The site is under custodial trust (trustee PathForward), with remediation overseen by TCEQ and EPA. Contaminants include lead, arsenic, cadmium and others, in soil and groundwater. — [Recasting the Smelter doc](http://www.recastingthesmelter.com/wp-content/themes/recastingasarco/downloads/site_documents/Review-of-ASARCO-El-Paso-Smelting-Processes-Report-FINAL.pdf); [TCEQ ASARCO](https://www.tceq.texas.gov/remediation/sites/asarco)
- As of July 2026, the site is still restricted to commercial use only. — [Hoodline 2026-07](https://hoodline.com/2026/07/toxic-ghost-lot-west-el-paso-s-asarco-site-still-too-hot-for-homes/)
- EPA's El Paso County Metals Survey sampled more than 3,900 residential properties in west El Paso. EPA and Asarco removed contaminated soil at over 1,000 of them in 2002–2009. — [EPA response.epa.gov](https://response.epa.gov/elpasocountymetals)
- A 2001 Texas DSHS report found high arsenic and lead in soil around Kern Place (which is in 79902). — [Wikipedia: Kern Place](https://en.wikipedia.org/wiki/Kern_Place) (secondary source)
- El Paso Plating Works is a state Superfund site where cleanup is complete; it was deleted from the registry in 2015. Its ZIP is unverified. — [TCEQ](https://www.tceq.texas.gov/remediation/superfund/state/elpasopw.html)

### Inferences
- In ECHO, 79902 facilities are likely dominated by small RCRA generators, air permits and EPWater infrastructure. I could not confirm which facilities have violations.

### Gaps
- No ECHO all-media list for 79902, and no violation flags for individual facilities.
- I did not verify UTEP's ZIP; it may be 79968 rather than 79902.
- I did not verify whether any EPWater wastewater plant or the Frontera/Doniphan outfall falls inside 79902.

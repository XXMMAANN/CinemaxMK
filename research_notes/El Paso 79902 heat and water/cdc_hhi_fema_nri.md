# CDC Heat & Health Index and FEMA National Risk Index: ZIP 79902 (El Paso, TX)

> **Access caveat (read first):** This research session's network egress proxy blocked every primary data host needed for the record-level values. WebFetch and curl both returned "EGRESS_BLOCKED" / HTTP 403 CONNECT for: www2.census.gov (ZCTA-to-tract relationship file), atsdr.cdc.gov / www.atsdr.cdc.gov (HHI page and data download), onemap.cdc.gov (the HHI ArcGIS FeatureServer, `Hosted/The_Heat_And_Health_Index/FeatureServer`), ephtracking.cdc.gov, data.cdc.gov, hazards.fema.gov, www.fema.gov (OpenFEMA NRI page and PDFs), services.arcgis.com (FEMA NRI Census Tracts FeatureServer), hub/opendata.arcgis.com, api.census.gov, tigerweb.geo.census.gov, gis.elpasotexas.gov, datacommons.org, zipdatamaps.com, eenews.net, web.archive.org, zenodo, figshare. The GitHub code-search API was also unavailable because this session is limited to its own repository. Only web-search snippets came back. **So this file does NOT contain the actual HHI rank for ZCTA 79902 or tract-level NRI Heat Wave values. None were found in any search snippet, and none have been invented.** It covers how each index works, which versions are current, the county-level numbers that secondary sources cite, and the exact queries to run once someone has access.

## Q1. CDC Heat & Health Index (HHI): ZCTA 79902 overall rank and module scores

### Takeaway
The HHI ranks every U.S. ZCTA (ZIP Code Tabulation Area) by percentile, using 25 indicators in 4 modules. The current file is "HHI Data 2024 United States", and the HHI page was last updated September 4, 2025. Because the data hosts were blocked, the actual overall and module percentiles for ZCTA 79902 could not be retrieved. No secondary source found reports them.

### Cited Findings
- The HHI is "the first nationwide tool to combine ZIP code level data on heat-related illness, pre-existing health conditions, sociodemographic factors, and natural and built environment factors". It gives "a single ranking for each ZIP code". — [CDC/ATSDR HHI Fact Sheet (Sept 2025)](https://atsdr.cdc.gov/place-health/media/pdfs/2025/09/CDC-ATSDR-HHI-Fact-Sheet-508.pdf); [Nextgov, May 2024 launch coverage](https://www.nextgov.com/digital-government/2024/05/hhs-launches-online-tool-identify-communities-hit-hardest-extreme-heat/397043/)
- There are 25 indicators in 4 modules:
  - Historical Heat and Health Burden: past local experience with heat.
  - Sensitivity: pre-existing health conditions.
  - Sociodemographic: social and demographic characteristics.
  - Natural and Built Environment.

  — [HHI 2024 Release Technical Documentation](https://www.atsdr.cdc.gov/place-health/media/pdfs/2024/07/HHI-2024-Release-Technical-Documentation-508.pdf); [CDC stacks: HHI Technical Documentation](https://stacks.cdc.gov/view/cdc/158548); [HHI FAQs (Sept 2025)](https://www.atsdr.cdc.gov/place-health/media/pdfs/2025/09/CDC-ATSDR-HHI-FAQS-508.pdf)
- The method is percentile ranking. The HHI "provides percentile ranks for all indicators, modules, and for the overall HHI". A rank is the share of ZCTAs above or below the ZCTA of interest. ZCTAs are the unit of analysis. — [HHI 2024 Technical Documentation](https://www.atsdr.cdc.gov/place-health/media/pdfs/2024/07/HHI-2024-Release-Technical-Documentation-508.pdf) (via search snippet)
- An extreme heat day is a day when a ZCTA's temperature exceeded the 95th percentile of that ZCTA's own 1991–2020 historical values. (The brief said "90th percentile", but the snippet says 95th; verify against the full document.) — [HHI 2024 Technical Documentation](https://www.atsdr.cdc.gov/place-health/media/pdfs/2024/07/HHI-2024-Release-Technical-Documentation-508.pdf) (via search snippet)
- The page was last updated September 4, 2025. The download has two Excel files, "HHI Data 2024 United States" (all indicators and percentile rankings) and "Data Dictionary 2024". It is reached through the "Data Download" button on the HHI page. — [CDC/ATSDR Heat & Health Index page](https://atsdr.cdc.gov/place-health/php/hhi/index.html) (via search snippet); [How to Filter the HHI (Sept 2025)](https://atsdr.cdc.gov/place-health/media/pdfs/2025/09/CDC-ATSDR-HHI-Top-Decile-Filter-508.pdf)
- CDC's own guide shows how to filter for ZIP codes in the top decile (90th percentile and above) of the overall HHI. — [How to Filter the HHI](https://atsdr.cdc.gov/place-health/media/pdfs/2025/09/CDC-ATSDR-HHI-Top-Decile-Filter-508.pdf)
- HHI data is also served as an ArcGIS FeatureServer at `onemap.cdc.gov/onemapservices/rest/services/Hosted/The_Heat_And_Health_Index/FeatureServer`, and it is carried in PolicyMap. — [onemap.cdc.gov layers](https://onemap.cdc.gov/onemapservices/rest/services/Hosted/The_Heat_And_Health_Index/FeatureServer/layers); [PolicyMap HHI source page](https://www.policymap.com/data/sources/centers-for-disease-control-and-prevention-cdc-heat-and-health-index-hhi)
- E&E News reported on CDC's top-ranked places for heat risk; its headline says they "might surprise you". The article text could not be fetched, so it is unknown whether El Paso is named. — [E&E News](https://www.eenews.net/articles/cdc-ranked-the-top-places-for-heat-risk-they-might-surprise-you/)
- Local context: ZIP 79902 has about 20,071 people, lies entirely in El Paso County, and covers the UTEP, Kern Place and Sunset Heights areas. — [zip-codes.com 79902](https://www.zip-codes.com/zip-code/79902/zip-code-79902.asp) (via search snippet); [city-data Sunset Heights](https://www.city-data.com/neighborhood/Sunset-Heights-El-Paso-TX.html)

### Inferences
- The HHI's own documentation describes national percentile ranks. A "within Texas" rank would probably have to be computed by filtering the national file to Texas ZCTAs and re-ranking. That is an inference; the snippets do not confirm a state-level rank field exists.
- 79902 is a dense, older urban core with high impervious cover in parts and a desert climate. That suggests elevated scores in the Natural & Built Environment and Historical Heat Burden modules. This is speculation and must not be reported as a finding.

### Gaps
- The actual overall HHI percentile for ZCTA 79902, plus its four module percentiles and indicator values, could not be retrieved. No secondary source citing them was found.
- To fill this gap, run either of these:
  - (a) Download the zip from https://atsdr.cdc.gov/place-health/php/hhi/index.html, open "HHI Data 2024 United States.xlsx", and filter ZCTA = 79902.
  - (b) Query `https://onemap.cdc.gov/onemapservices/rest/services/Hosted/The_Heat_And_Health_Index/FeatureServer/0/query?where=ZCTA='79902'&outFields=*&returnGeometry=false&f=json`. The field name ZCTA has not been verified; check `/0?f=json` first.
- Whether a newer HHI release than the 2024 data (page updated Sept 2025) exists as of October 2026 is unverified.

## Q2. FEMA National Risk Index (NRI): census tracts making up 79902, Heat Wave and overall ratings

### Takeaway
The current NRI is v1.20 (December 2025), and its heat wave period runs to November 2024. FEMA retired the standalone NRI web app and moved the data into RAPT (Resilience Analysis and Planning Tool) on December 15, 2025. Because Census and FEMA hosts were blocked, the list of tracts that make up 79902 and their tract-level Heat Wave values could not be retrieved.

### Cited Findings
- Version: **NRI v1.20 (December 2025)**. Its technical documentation is titled "National Risk Index Data Technical Documentation December 2025 – v1.20". — [FEMA NRI Technical Documentation v1.20](https://www.fema.gov/sites/default/files/documents/fema_national-risk-index_technical-documentation.pdf); [NRI Data Version and Update Documentation, Dec 2025](https://www.fema.gov/sites/default/files/documents/fema_national-risk-index_data-version-update-documentation.pdf)
- Heat wave changes in v1.20.0:
  - The data period was extended from Nov 12, 2005–Oct 6, 2022 (in v1.19.0) to **Nov 12, 2005–Nov 12, 2024**.
  - The method was updated, including changes to the Iowa Mesonet source data.
  - CDC's Compressed Mortality File (1996–2018) is now used as a nationwide target for fatality estimates in population Expected Annual Loss.

  — [NRI Data Version and Update Documentation, Dec 2025](https://www.fema.gov/sites/default/files/documents/fema_national-risk-index_data-version-update-documentation.pdf) (via search snippet)
- **Methodology change (important for comparisons):** v1.20 dropped CDC/ATSDR SVI as its Social Vulnerability component and switched to the **U.S. Census Bureau Community Resilience Estimates**. Social vulnerability ratings from v1.20 are therefore not directly comparable with older versions. — [NRI Data Version and Update Documentation, Dec 2025](https://www.fema.gov/sites/default/files/documents/fema_national-risk-index_data-version-update-documentation.pdf) (via search snippet); [NACCHO blog](https://www.naccho.org/blog/articles/fema-updates-national-risk-index-other-agency-tools)
- On December 15, 2025, FEMA moved NRI data into RAPT. The "National Risk Index application is no longer available", so the hazards.fema.gov/nri map viewer has been retired. — [FEMA NRI page](https://www.fema.gov/flood-maps/products-tools/national-risk-index); [RAPT NRI user guide 2025](https://www.fema.gov/sites/default/files/documents/fema_national-risk-index-rapt-user-guide_2025.pdf); [NRI FAQ Dec 2025](https://www.fema.gov/sites/default/files/documents/fema_national-risk-index_faq-page-documentation.pdf)
- FEMA also removed the NRI "Future Risk" index. — [Harvard EELP rollback tracker](https://eelp.law.harvard.edu/tracker/rollback-fema-removed-future-risk-index/)
- Tract-level NRI is also published as the "National Risk Index Census Tracts" ArcGIS dataset on NOAA's Climate Resilience portals, and OpenFEMA lists NRI data downloads. — [resilience.climate.gov NRI Census Tracts](https://resilience.climate.gov/datasets/FEMA::national-risk-index-census-tracts/about); [CRIS NRI Census Tracts](https://cris.climate.gov/content/9da4eeb936544335a6db0cd7a8448a51); [OpenFEMA NRI Data](https://www.fema.gov/about/openfema/data-sets/national-risk-index-data)
- FEMA publishes a separate map layer, "National Risk Index Annualized Frequency Heat Wave". — [FEMA Resilience hub map](https://resilience-fema.hub.arcgis.com/maps/014e8bbbc9be4ba7965612d59af522cb)
- An El Paso city GIS layer of 2020 census tracts exists; it could be used to determine which tracts fall in 79902. — [El Paso GIS 2020 Census Tracts](https://gis.elpasotexas.gov/dev/rest/services/planning/2020_Census_Tracts/FeatureServer/info/iteminfo)

### Inferences
- In NRI CSVs, the tract IDs for 79902 would be 11-digit GEOIDs beginning 48141 (TRACTFIPS). The relevant fields are:

  | Field | Meaning |
  |---|---|
  | `HWAV_RISKS` | Heat Wave risk score |
  | `HWAV_RISKR` | Heat Wave risk rating |
  | `HWAV_EALR` | Heat Wave Expected Annual Loss (EAL) rating |
  | `HWAV_AFREQ` | Heat Wave annualized frequency |
  | `SOVI_RATNG` | Social vulnerability rating |
  | `RESL_RATNG` | Community resilience rating |
  | `RISK_RATNG` | Overall risk rating |
  | `NRI_VER` | NRI version |

  These names come from memory of the NRI data dictionary and were not checked this session. Confirm them against the v1.20 data dictionary.
- Heat wave events in the NRI are recorded per county zone, and frequency is assigned through NWS forecast zones. The tracts in 79902 are therefore likely to share similar Heat Wave annualized frequency and differ mainly in exposure, social vulnerability and resilience. This is an unverified inference.

### Gaps
- The list of 2020 tracts intersecting ZCTA 79902 could not be retrieved. Get it from `tab20_zcta520_tract20_natl.txt` on www2.census.gov by filtering `GEOID_ZCTA5_20 = 79902`, or from HUD's ZIP–tract crosswalk.
- Per-tract Heat Wave score and rating, EAL rating, annualized frequency, social vulnerability, community resilience and overall NRI rating were all unavailable.
- To retrieve them, use either of these:
  - RAPT
  - The FEMA NRI Census Tracts FeatureServer on services.arcgis.com, queried with `STATEABBRV='TX' AND COUNTYFIPS='141'`

## Q3. Comparison with El Paso County and Texas

### Takeaway
Only secondary aggregator figures were found for the county, and they disagree with each other. Their NRI version is unclear and probably older than v1.20. They describe El Paso County's overall NRI as "Relatively High" and its heat risk as "Relatively High". Treat these as provisional until checked against v1.20.

### Cited Findings
- KRGV/ValleyCentral, citing FEMA, reported an overall El Paso County NRI score of **35.67**, rated "relatively high". It was the 8th highest in Texas, and 98.7% of U.S. counties scored lower. The article date was not visible and appears to predate v1.20. — [ValleyCentral: These Texas counties face greatest risk of disaster](https://www.valleycentral.com/news/local-news/these-texas-counties-face-greatest-risk-of-disaster-fema-indicates/)
- DisasterAware, an aggregator citing FEMA, rated the El Paso County heat risk "Relatively High". It gave estimated annual loss of about **$14M**, "48 events recorded in proximity", an overall EAL rating of "Relatively Moderate", social vulnerability "Very High" and community resilience "Relatively Low". The NRI version was not stated; the "Very High" social vulnerability likely reflects the older SVI-based method. — [DisasterAware: Natural Hazard Risks in El Paso, TX](https://explore.disasteraware.com/risks/el-paso-tx/) (via search snippet)
- ClimateRiskCheck gives an "extreme heat" score of 9.9/10 for El Paso. These are proprietary 0–10 scores, not NRI ratings, and two snippets from the same source gave different benchmarks: one said Texas 7.7 and U.S. 5.6, the other Texas 5.6 and U.S. 4.5. This source is low reliability for the purpose. — [ClimateRiskCheck El Paso](https://www.climateriskcheck.com/risk/texas/el-paso)
- First Street rates heat risk in El Paso as "very high". It projects days above 101.8°F rising from about 7 per year (around 1990) to about 40 per year by 2050. This is a non-federal model, included for context only. — [First Street: El Paso heat](https://firststreet.org/city/el-paso-tx/4824000_fsid/heat)
- Inside Climate News (August 2025) reported record heat deaths in El Paso. — [Inside Climate News, Aug 17, 2025](https://insideclimatenews.org/news/17082025/el-paso-extreme-heat-illness-death/)

### Inferences
- With the v1.20 switch to Census Community Resilience Estimates and the extended heat wave period to 2024, county ratings may differ from the figures above. Report county numbers with a version caveat.
- A Texas-wide HHI comparison would mean ranking the share of Texas ZCTAs in the national top decile. Texas-wide NRI is usually expressed through state-level ratings or the county distribution. Neither was retrievable.

### Gaps
- Official v1.20 El Paso County (FIPS 48141) Heat Wave risk score and rating, HWAV EAL, annualized frequency, and overall, SOVI and RESL ratings were not verified from FEMA directly.
- No Texas state-level NRI heat wave values were found.
- No Texas or El Paso County HHI summary statistics were found.
- Recommended follow-up from an environment with access to cdc.gov, fema.gov, census.gov and arcgis.com: run the queries listed in the Q1 and Q2 Gaps sections.

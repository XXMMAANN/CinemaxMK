# CDC Heat & Health Index and FEMA National Risk Index for ZCTA 79902 (El Paso, TX): primary-source values

> Retrieved October 1, 2026. Every value below was pulled directly from primary federal files or services in this session, and each is tagged **[PRIMARY-VERIFIED]**. Values computed from primary data are tagged **[DERIVED]**. Things that could not be retrieved are listed under Gaps. www.fema.gov and hazards.fema.gov still returned HTTP 403 / SSL errors, so FEMA values come from FEMA's own authoritative ArcGIS feature services (owner `FEMA_NationalRiskIndex`). The FEMA PDFs and CSV download could not be fetched.

## Q1. Census tracts overlapping ZCTA 79902

### Takeaway
ZCTA 79902 (2020 ZCTA) overlaps **9 El Paso County 2020 census tracts**. About 80% of its land area falls in five of them: 15.01, 15.02, 14, 22.01 and 16. [PRIMARY-VERIFIED]

### Cited Findings
- Source: the 2020 ZCTA-to-tract relationship file, filtered to `GEOID_ZCTA5_20 = 79902`. ZCTA land area is 16,915,468 m², and the sum of the parts matches it exactly. — [Census tab20_zcta520_tract20_natl.txt](https://www2.census.gov/geo/docs/maps-data/data/rel2020/zcta520/tab20_zcta520_tract20_natl.txt)

| Tract GEOID | Tract | Land in 79902 (m²) | % of ZCTA 79902 land | % of tract's land inside 79902 |
|---|---|---|---|---|
| 48141001501 | 15.01 | 5,647,857 | 33.4% | 96.4% |
| 48141001502 | 15.02 | 2,665,431 | 15.8% | 100% |
| 48141001400 | 14 | 2,466,935 | 14.6% | 31.0% |
| 48141002201 | 22.01 | 2,101,555 | 12.4% | 93.0% |
| 48141001600 | 16 | 1,310,376 | 7.7% | 89.1% |
| 48141002202 | 22.02 | 1,173,050 | 6.9% | 100% |
| 48141001115 | 11.15 | 1,034,163 | 6.1% | 33.2% |
| 48141001111 | 11.11 | 358,655 | 2.1% | 3.1% |
| 48141001700 | 17 | 157,446 | 0.9% | 14.0% |

- Shares are by land area, not population. The relationship file has no population.

### Inferences
- Tracts 11.11 (3% inside 79902) and 17 (14% inside) contribute only marginally. Their NRI values describe areas that lie mostly outside the ZIP.

### Gaps
- No population-weighted ZCTA-to-tract shares are available from this file. HUD's ZIP–tract crosswalk would add residential or address ratios, but it was not retrieved.

## Q2. CDC Heat & Health Index (HHI): ZCTA 79902

### Takeaway
ZCTA 79902 has an **overall HHI national percentile rank of 0.921 (92.1st percentile)**. That puts it in CDC's top decile nationally. [PRIMARY-VERIFIED]

Its module ranks are uneven:

| Module | National percentile rank |
|---|---|
| Natural & Built Environment | 0.9414 |
| Sociodemographic | 0.8991 |
| Historical Heat & Health Burden | 0.7879 |
| Sensitivity | 0.3497 |

Re-ranked within Texas only, 79902 is at about the **72nd percentile** [DERIVED]. Among roughly 30 El Paso County ZCTAs it ranks **15th** [DERIVED].

### Cited Findings: dataset and version
- The HHI page metadata says "updated: September 4, 2025". The download is `HHI_Data.zip`, which holds "HHI Data 2024 United States.xlsx" (32,195 ZCTA rows, 75 columns) and "HHI Data Dictionary 2024.xlsx". — [CDC/ATSDR HHI page](https://www.atsdr.cdc.gov/place-health/php/hhi/index.html); [HHI_Data.zip](https://www.atsdr.cdc.gov/place-health/media/files/2024/08/HHI_Data.zip) [PRIMARY-VERIFIED]
- The same record is served, field for field, by the ArcGIS FeatureServer layer "Heat And Health Index", which has 32,657 features. The 79902 record from the service matched the xlsx exactly. — [onemap.cdc.gov HHI FeatureServer/0](https://onemap.cdc.gov/onemapservices/rest/services/Hosted/The_Heat_And_Health_Index/FeatureServer/0/query?where=zcta5ce10%3D%2779902%27&outFields=*&returnGeometry=false&f=json) [PRIMARY-VERIFIED]
- The HHI uses **2010 ZCTA geography** (fields `ZCTA`/`GEOID10` = 4879902; `zcta5ce10` in the service). It reports a population of 21,236 for 79902. — [HHI_Data.zip](https://www.atsdr.cdc.gov/place-health/media/files/2024/08/HHI_Data.zip) [PRIMARY-VERIFIED]

### Cited Findings: ZCTA 79902 values
All values below are [PRIMARY-VERIFIED] from the [HHI 2024 xlsx](https://www.atsdr.cdc.gov/place-health/media/files/2024/08/HHI_Data.zip). Field definitions come from the bundled Data Dictionary 2024.

| Field | Description | Value |
|---|---|---|
| OVERALL_SCORE | Mean of the module ranks | 0.7445 |
| **OVERALL_RANK** | National percentile | **0.921** |
| HHB_SCORE / **HHB_RANK** | Historical Heat & Health Burden | 0.7317 / **0.7879** |
| SEN_SCORE / **SEN_RANK** | Sensitivity | 0.1667 / **0.3497** |
| SOCIODEM_SCORE / **SOCIODEM_RANK** | Sociodemographic | 0.6654 / **0.8991** |
| NBE_SCORE / **NBE_RANK** | Natural & Built Environment | 0.6994 / **0.9414** |
| P_NEHD | Number of extreme heat days, 5-yr average 2018–2022 | **15.6 days**; PR_NEHD 0.7134 |
| PR_HRI | Percentile rank of heat-related EMS activations reported to NEMSIS (0–100 scale) | **68**; F_HRI (quartile) 0.75; LOW_EMS 0 (not a low-count ZCTA) |
| P_IMPERV | % impervious surface (NLCD) | **43.29%**; PR 0.9152 |
| P_TREEC | % tree canopy (USFS) | **0.72%**; PR 0.9226 (low canopy ranks as high vulnerability) |
| P_OZONE | Annual mean days above the O3 standard, 2018–2020 | 7; PR 0.9673 |
| P_PM25 | Days above the PM2.5 standard | 0; PR 0 |
| P_NOVEH | % of households with no vehicle | 17.2; PR 0.9452 |
| P_RENT | % renters | 60.13; PR 0.9478 |
| P_MOBILE | % mobile homes | 0.5; PR 0.1976 |
| P_POV | Poverty | 37.08%; PR 0.8581 |
| P_UNINSUR | Uninsured | 20.7%; PR 0.9398 |
| P_UNEMP | Unemployed | 6.6%; PR 0.7392 |
| P_NOHSDP | No high-school diploma | 20.0%; PR 0.8407 |
| P_ISO | Adults living alone | 20.70%; PR 0.8645 |
| P_ELP | Speak English "less than well" | 14.93%; PR 0.9749 |
| P_DISABL | Disability | 13.7%; PR 0.4673 |
| P_ODW | Outdoor-type occupations | 5.08%; PR 0.1513 |
| P_AGE65 | Age 65+ | 17.7%; PR 0.4882 |
| P_AGE5 | Age under 5 | 4.4%; PR 0.3298 |
| Sensitivity (PLACES) | CHD 6.4%, obesity 36.1%, **diabetes 15.2% (PR 0.8907, the only flagged indicator)**, COPD 6.2%, asthma 9.1%, poor mental health 16.7% | F_SEN_COUNT = 1 |

### Cited Findings: methodology confirmed from the technical documentation
- **Extreme heat day = the 95th percentile, not the 90th.** The documentation says "days where the temperature in a ZCTA exceeded the 95th percentile of all values for that ZCTA from 1991-2020". The source is NLDAS-2 modeled data from the CDC Tracking Network. P_NEHD is the 5-year average for 2018–2022, derived from census-tract counts. The threshold is relative, so an extreme heat day in a northwestern ZCTA can be about 10 degrees cooler than one in the Southwest. — [HHI 2024 Release Technical Documentation](https://www.atsdr.cdc.gov/place-health/media/pdfs/2024/07/HHI-2024-Release-Technical-Documentation-508.pdf) [PRIMARY-VERIFIED]
- **Heat-related EMS.** NEMSIS supplied only percentile ranks of 3-year (2020–2022) average heat-related EMS activation rates per 100,000. No raw rates are shared. — [HHI Technical Documentation](https://www.atsdr.cdc.gov/place-health/media/pdfs/2024/07/HHI-2024-Release-Technical-Documentation-508.pdf); Data Dictionary 2024 [PRIMARY-VERIFIED]
- **Ranking method.** Ranks use dplyr `percent_rank()` across all U.S. ZCTAs. OVERALL_SCORE is the mean of the 4 module ranks, which is then percentile ranked into OVERALL_RANK. SEN_SCORE = F_SEN_COUNT × 1/6. A value of -999 means null. — Data Dictionary 2024 in [HHI_Data.zip](https://www.atsdr.cdc.gov/place-health/media/files/2024/08/HHI_Data.zip) [PRIMARY-VERIFIED]
- **Documentation discrepancy.** The dictionary gives HHB_SCORE = (PR_NEHD + PR_HRI)/n. In the actual file, HHB_SCORE equals (PR_NEHD + F_HRI)/2 for 100% of valid ZCTAs, and matches PR_HRI/100 for only 0.4%. For 79902: (0.7134 + 0.75)/2 = 0.7317. The EMS term therefore enters the score as a quartile (0.25/0.5/0.75/1.0), not as the raw percentile. [DERIVED from primary data]

### Cited Findings: Texas-only and El Paso comparisons (all [DERIVED])
All computed from the [HHI 2024 xlsx](https://www.atsdr.cdc.gov/place-health/media/files/2024/08/HHI_Data.zip).

**Texas-only percentile.** Method: re-run `percent_rank` on each score among the 1,900 Texas ZCTAs (STATEFP10 = 48), excluding -999.

| Measure | Texas-only percentile |
|---|---|
| **Overall** | **0.719** |
| HHB score | 0.556 |
| Sensitivity score | 0.289 |
| Sociodemographic score | 0.735 |
| NBE score | 0.835 |
| Extreme heat days | 0.550 |
| Impervious surface | 0.852 |
| Low tree canopy | 0.859 |

- 533 Texas ZCTAs have a higher national overall rank than 79902, which makes it about **534th of 1,900** in Texas.
- 613 Texas ZCTAs sit in the national top decile (OVERALL_RANK ≥ 0.90).
- The national check reproduces: 92.06% of ZCTAs have a lower overall score.

**El Paso County ZCTAs.** The county was identified with the [Census 2010 ZCTA–county relationship file](https://www2.census.gov/geo/docs/maps-data/data/rel/zcta_county_rel_10.txt), GEOID 48141. ZCTA 88063 was excluded because only 0.21% of its population is in the county. That leaves 30 ZCTAs, and **79902 ranks 15th of 30** on OVERALL_RANK.

| Order | ZCTAs (national OVERALL_RANK) |
|---|---|
| Ranked above 79902 | 79901 (0.9994), 79905 (0.9954), 79915 (0.9900), 79838 (0.9798), 79907 (0.9788), 79930 (0.9776), 79903 (0.9635), 79904 (0.9567), 79924 (0.9567), 79853 (0.9514), 79927 (0.9384), 79835 (0.9366), 79849 (0.9311), 79821 (0.9308) |
| Ranked just below | 79836 (0.9160), 79925 (0.9003), 79935 (0.8728) |
| Lowest | 79911 (0.2835) |

- 79902's NBE rank (0.9414) is among the higher values in the county.
- Its Sensitivity rank (0.3497) is in the lower half: one flag, for diabetes.
- Extreme heat days are nearly uniform countywide, at roughly 14.7 to 15.9 days.
- 79902's tree canopy is 0.72% and its impervious surface 43%. By comparison, 79901 (downtown) has 84% impervious surface and 6.2% canopy.

### Inferences
- 79902's high overall rank comes from its built environment (heavy impervious surface, almost no canopy, many carless and renter households, ozone) and from sociodemographic factors (limited English, uninsured, poverty). Health sensitivity contributes less.
- Extreme heat days are measured against a local 95th-percentile threshold. So 15.6 days does not mean El Paso has "fewer hot days" than cooler places; it measures departures from the local climate.

### Gaps
- No HHI release newer than the 2024 data was found on the HHI page. The page was last updated Sept 4, 2025, and the zip path is still `/2024/08/`.
- The HHI uses 2010 ZCTAs and the tract list uses 2020 ZCTAs, so the boundaries may differ slightly.
- Raw heat-related EMS rates are not published (NEMSIS shares ranks only).

## Q3. FEMA National Risk Index v1.20: tracts in 79902 and El Paso County, heat wave

### Takeaway
All 9 tracts carry **NRI_VER = "December 2025"** (v1.20.0). [PRIMARY-VERIFIED]
- **Heat wave risk ratings:**
  - Tracts 11.11 and 15.01 are "Relatively High". 15.01 is the largest share of 79902.
  - Six tracts are "Relatively Moderate".
  - Tract 17 is "Relatively Low".
- **Social vulnerability:** "Very High" in most tracts.
- **Community resilience:** "Very Low" in every tract.
- **Overall NRI risk:** mostly "Relatively Low". The exception is tract 15.02, which is "Relatively High" and is the only such tract in El Paso County.
- **El Paso County heat wave risk:** "Relatively High", score 98.68. That ranks it 42nd of 3,114 rated counties nationally and 6th of 254 in Texas [DERIVED].

### Cited Findings: dataset and fields
- The ArcGIS item "National Risk Index Census Tracts" (id 9da4eeb936544335a6db0cd7a8448a51, owner FEMA_NationalRiskIndex) states "National Risk Index Data Version: December 2025 (1.20.0)". It covers 18 hazards, now including inland flooding. — [ArcGIS item](https://www.arcgis.com/home/item.html?id=9da4eeb936544335a6db0cd7a8448a51); [NRI Census Tracts FeatureServer](https://services.arcgis.com/XG15cJAlne2vxtgt/arcgis/rest/services/National_Risk_Index_Census_Tracts/FeatureServer/0) [PRIMARY-VERIFIED]
- Field names and aliases were verified from the service schema (469 fields). They match the expected NRI dictionary names.

| Field | Alias |
|---|---|
| HWAV_RISKS | Heat Wave – Hazard Type Risk Index Score |
| HWAV_RISKR | Heat Wave – Hazard Type Risk Index Rating |
| HWAV_RISKV | Heat Wave – Hazard Type Risk Index Value |
| HWAV_EALS | Heat Wave – Expected Annual Loss Score |
| HWAV_EALR | Heat Wave – Expected Annual Loss Rating |
| HWAV_EALT | Heat Wave – Expected Annual Loss Total |
| HWAV_EALP | Heat Wave – Expected Annual Loss Population (fatalities/yr) |
| HWAV_EVNTS | Heat Wave – Number of Events |
| HWAV_AFREQ | Heat Wave – Annualized Frequency |
| HWAV_ALR_NPCTL | Heat Wave – EAL Rate National Percentile |
| HWAV_HLRR | Heat Wave – Historic Loss Ratio Total Rating |
| RISK_RATNG | Composite risk rating |
| SOVI_RATNG | Social Vulnerability rating |
| RESL_RATNG | Community Resilience rating |
| NRI_VER | NRI version |

  This check used the service schema, not the FEMA data-dictionary CSV, which was blocked. — [service schema](https://services.arcgis.com/XG15cJAlne2vxtgt/arcgis/rest/services/National_Risk_Index_Census_Tracts/FeatureServer/0?f=json)
- The layer's data was last edited at epoch 1765870818438, which is 2025-12-16 UTC. — same source

### Cited Findings: per-tract values
All values below are [PRIMARY-VERIFIED] from the [NRI Census Tracts query (El Paso, STATEFIPS 48, COUNTYFIPS 141)](https://services.arcgis.com/XG15cJAlne2vxtgt/arcgis/rest/services/National_Risk_Index_Census_Tracts/FeatureServer/0/query?where=STATEFIPS%3D%2748%27+AND+COUNTYFIPS%3D%27141%27&outFields=*&returnGeometry=false&f=json).

| Tract (% of 79902) | Pop 2020 | **HWAV Risk score / rating** | HWAV EAL score / rating | HWAV EAL total $/yr | HWAV AFREQ (events/yr) | Overall RISK score / rating | SOVI score / rating | RESL score / rating |
|---|---|---|---|---|---|---|---|---|
| 15.01 (33.4%) | 4,929 | **85.25 / Relatively High** | 74.98 / Relatively Moderate | 79,481 | 8.790 | 39.73 / Relatively Low | 94.56 / Very High | 1.38 / Very Low |
| 15.02 (15.8%) | 2,627 | **68.43 / Relatively Moderate** | 53.80 / Relatively Moderate | 42,374 | 8.789 | 84.66 / **Relatively High** | 89.02 / Very High | 1.38 / Very Low |
| 14 (14.6%) | 2,664 | **59.84 / Relatively Moderate** | 54.27 / Relatively Moderate | 42,910 | 8.723 | 4.88 / Very Low | 63.32 / Relatively High | 1.38 / Very Low |
| 22.01 (12.4%) | 2,984 | **71.22 / Relatively Moderate** | 58.29 / Relatively Moderate | 48,160 | 8.802 | 53.25 / Relatively Low | 86.69 / Very High | 1.38 / Very Low |
| 16 (7.7%) | 4,079 | **78.87 / Relatively Moderate** | 69.11 / Relatively Moderate | 65,775 | 8.789 | 55.73 / Relatively Low | 85.02 / Very High | 1.38 / Very Low |
| 22.02 (6.9%) | 3,832 | **66.99 / Relatively Moderate** | 67.00 / Relatively Moderate | 61,792 | 8.790 | 36.99 / Relatively Low | 47.03 / Relatively Moderate | 1.38 / Very Low |
| 11.15 (6.1%) | 3,859 | **76.81 / Relatively Moderate** | 67.24 / Relatively Moderate | 62,225 | 8.789 | 7.18 / Very Low | 82.94 / Very High | 1.38 / Very Low |
| 11.11 (2.1%) | 5,084 | **85.82 / Relatively High** | 75.86 / Relatively Moderate | 81,985 | 8.794 | 26.81 / Relatively Low | 94.60 / Very High | 1.38 / Very Low |
| 17 (0.9%) | 1,165 | **41.48 / Relatively Low** | 27.34 / Relatively Low | 18,790 | 8.789 | 48.68 / Relatively Low | 89.05 / Very High | 1.38 / Very Low |

Additional tract fields (same source):
- HWAV_EVNTS is about 154.7–156.2 events for every tract.
- HWAV_HLRR is "Relatively Moderate" for all 9 tracts.
- HWAV_ALR_NPCTL ranges from 33.7 (tract 11.15) to 63.5 (tract 15.02).
- Heat wave EAL is almost entirely population-equivalence loss. HWAV_EALP (fatalities per year) ranges from 0.0014 to 0.0060 per tract.
- RESL_SCORE is identical (1.376614) for all El Paso tracts, so community resilience appears to be assigned at county level in v1.20. That is consistent with the switch to Census Community Resilience Estimates noted in earlier notes; the inference is unverified against the FEMA documentation, which was blocked.
- RISK_SPCTL (labelled "State Percentile") equals RISK_SCORE to every decimal for these tracts and for the county. This looks like a service artifact or a field-labelling issue, so do not cite RISK_SPCTL as a state percentile.

### Cited Findings: El Paso County (C48141) and national context
County values are [PRIMARY-VERIFIED] from the [NRI Counties FeatureServer](https://services.arcgis.com/XG15cJAlne2vxtgt/arcgis/rest/services/National_Risk_Index_Counties/FeatureServer/0/query?where=STATEFIPS%3D%2748%27+AND+COUNTYFIPS%3D%27141%27&outFields=*&returnGeometry=false&f=json), NRI_VER December 2025.

| Field | El Paso County value |
|---|---|
| HWAV_RISKS / HWAV_RISKR | **98.68 / Relatively High** |
| HWAV_EALS / HWAV_EALR | 98.13 / **Relatively High** |
| HWAV_EALT | **$13.98M/yr** (HWAV_EALP 1.02 fatalities/yr) |
| HWAV_AFREQ | 7.28 events/yr (HWAV_EVNTS 130.5) |
| HWAV_ALR_NPCTL | 14.2 |
| Overall RISK_SCORE / RISK_RATNG | 95.45 / **Relatively High** |
| EAL composite | 92.45 / Relatively Moderate |
| SOVI | 85.18 / **Very High** |
| RESL | 4.07 / **Very Low** |
| Population | 864,454 |

County comparisons below are [DERIVED] from all 3,232 county records in the same service:
- **Heat wave risk rank:** 42nd of 3,114 counties with a score nationally, and 6th of 254 in Texas. The Texas counties ahead of El Paso are Dallas (99.94, Very High), Harris (99.71, Very High), Tarrant, Bexar and Hidalgo.
- **National county HWAV_RISKR distribution:**

  | Rating | Counties |
  |---|---|
  | Very High | 11 |
  | Relatively High | 98 |
  | Relatively Moderate | 551 |
  | Relatively Low | 1,246 |
  | Very Low | 1,156 |
  | No Rating | 52 |

- **Annualized frequency:** El Paso's 7.28 is below the Texas county median (10.05) but above the national county median (4.58). Its high heat wave risk score therefore reflects exposure (population), social vulnerability and resilience more than frequency.

Among El Paso County's 188 tracts [DERIVED]:
- **HWAV_RISKR distribution:** 44 Relatively High, 129 Relatively Moderate, 13 Relatively Low, 2 Very Low.
- **Median HWAV_RISKS** is 77.28.
- **Where the 79902 tracts rank** (by HWAV_RISKS): 11.11 is 29th of 188, 15.01 is 38th, 16 is 82nd, 11.15 is 99th, 22.01 is 135th, 15.02 is 142nd, 22.02 is 148th, 14 is 170th and 17 is 183rd.
- **Overall RISK_RATNG distribution:** 87 Very Low, 87 Relatively Low, 13 Relatively Moderate, and only 1 Relatively High (tract 15.02, in 79902).

National tract HWAV_RISKR distribution [PRIMARY-VERIFIED], from a statistics query on the tract service:

| Rating | Tracts |
|---|---|
| Very High | 2,917 |
| Relatively High | 10,157 |
| Relatively Moderate | 24,019 |
| Relatively Low | 32,675 |
| Very Low | 13,078 |
| Insufficient Data | 1,238 |
| No Rating | 1,070 |

### Inferences
- **Inside 79902, heat wave risk is "Relatively Moderate to Relatively High".** The 15.01 tract, about a third of the ZIP's land, is Relatively High. A land-area-weighted average of HWAV_RISKS over the 9 tracts is about 74, which would sit in the Relatively Moderate band. This is rough, illustrative arithmetic and not an official FEMA ZIP value.
- **Annualized frequency is nearly identical across tracts** (8.72–8.80), so differences between tracts come mainly from exposure (population/building value) and social vulnerability.
- **Older aggregator figures differ from v1.20.** Earlier notes cited a county overall score of 35.67 and a heat EAL of about $14M. The v1.20 county overall score is 95.45 on the 0–100 percentile scale. The 35.67 was probably an old-version "RISK_VALUE"-style or older-scale number. The v1.20 heat wave EAL ($13.98M) is consistent with the "~$14M" aggregator figure.

### Gaps
- www.fema.gov (HTTP 403) and hazards.fema.gov (SSL error) were still blocked. So the v1.20 technical documentation, the data-dictionary CSV and the `NRI_Table_CensusTracts` CSV were not fetched directly. All values come from FEMA's ArcGIS feature services, which are labelled v1.20.0 / "December 2025".
- RAPT was not queried.
- Texas state-level heat wave values (NRI States layer) were not retrieved.
- The meaning of the RISK_SPCTL anomaly is unresolved.

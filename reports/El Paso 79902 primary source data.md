# Primary data puts 79902 in heat's top decile

Primary federal data rank ZIP 79902 (ZCTA 79902: Kern Place, Rim Road, UTEP, Sunset Heights and the north edge of downtown El Paso) at the **92.1st national percentile on CDC's Heat & Health Index**. The rank comes mainly from its built environment (43% impervious surface, 0.72% tree canopy) and from sociodemographic factors, not from residents' health conditions. FEMA's National Risk Index v1.20 (December 2025) rates heat-wave risk **"Relatively High" in tract 15.01**, the largest third of the ZIP, and "Relatively Moderate" in most of the rest. El Paso County as a whole is **"Relatively High" (score 98.68)**, and every tract is rated "Very Low" for community resilience. The ZIP's own heat signal is a neighborhood split: hillside Rim Road and Kern Place are older and wealthier, while Sunset Heights (tract 16) and the Montana/El Paso High tracts (22.01, 22.02) sit at the **98th–99th national SVI percentile**, with up to 36% of households carless and most homes built before 1950. NOAA's July 10, 2020 heat map puts 79902 right at the citywide median, about 104°F in the afternoon, with a 4–6°F gap between the cooler foothills and the hotter Sunset Heights and Mesa corridor in the morning and evening. The tap water is a different story: El Paso Water's 2023–2025 reports show **no MCL or action-level exceedance**, EPA records show **no health-based drinking-water violation since at least 2015**, and the utility has found **zero lead service lines**. The water risk that remains is concentrated in 79902, though. Querying the utility's own public map shows about **1,513 service lines of unknown material (27% of the ZIP's lines, versus 5% systemwide)**, roughly 14% of all unknowns in the system. Every figure below was re-pulled from primary files or APIs on October 1, 2026, and it supersedes the earlier snippet-based report. Values computed from primary data are marked **[DERIVED]**.

## CDC ranks 79902 in the national top decile because of pavement and poverty, not sickness

The CDC/ATSDR Heat & Health Index file ("HHI Data 2024 United States", page last updated September 4, 2025) gives ZCTA 79902 an **overall national percentile rank of 0.921**. The ArcGIS service returns the identical record ([CDC/ATSDR HHI_Data.zip](https://www.atsdr.cdc.gov/place-health/media/files/2024/08/HHI_Data.zip); [CDC HHI FeatureServer](https://onemap.cdc.gov/onemapservices/rest/services/Hosted/The_Heat_And_Health_Index/FeatureServer/0/query?where=zcta5ce10%3D%2779902%27&outFields=*&returnGeometry=false&f=json)). No newer release exists. The HHI uses 2010 ZCTA boundaries and a 2010-era population of 21,236.

| HHI module | National percentile rank | What drives it |
|---|---|---|
| **Natural & Built Environment** | **0.9414** | 43.29% impervious surface (PR 0.915), 0.72% tree canopy (PR 0.923), 7 ozone-exceedance days/yr (PR 0.967) |
| **Sociodemographic** | **0.8991** | Limited English 14.9% (PR 0.975), renters 60.1% (PR 0.948), no vehicle 17.2% (PR 0.945), uninsured 20.7% (PR 0.940), poverty 37.1% (PR 0.858) |
| Historical Heat & Health Burden | 0.7879 | 15.6 extreme-heat days/yr, 2018–22 (PR 0.713); heat-related EMS activations at the 68th percentile |
| Sensitivity | 0.3497 | Only one flagged condition: diabetes 15.2% (PR 0.891) |
| **Overall** | **0.921** | Mean of the four module ranks, re-ranked nationally |

Two points from CDC's [HHI 2024 Technical Documentation](https://www.atsdr.cdc.gov/place-health/media/pdfs/2024/07/HHI-2024-Release-Technical-Documentation-508.pdf) shape how to read this table. First, it settles a definitional question from the earlier round: an "extreme heat day" is a day **above the 95th percentile** of that ZCTA's own 1991–2020 temperatures, not the 90th. So 79902's 15.6 days measure departures from El Paso's already-hot normal, not raw hotness. Second, NEMSIS shares only percentile ranks of heat-related EMS activations, never raw rates. In the actual file, the EMS term enters the burden score as a quartile (0.75 for 79902), not as the raw percentile the data dictionary describes **[DERIVED: (0.7134 + 0.75)/2 = 0.7317, which matches HHB_SCORE]**.

Against narrower comparison groups the ranking softens. Re-running CDC's `percent_rank` method within Texas's 1,900 ZCTAs puts 79902 at about the **72nd percentile, roughly 534th in the state [DERIVED]**. That happens because 613 Texas ZCTAs sit in the national top decile. Within El Paso County, 79902 ranks **15th of 30 ZCTAs [DERIVED]**, well behind 79901 downtown (0.9994), 79905 (0.9954) and 79915 (0.9900). Extreme-heat days are nearly uniform countywide (about 14.7–15.9), so the county ranking depends on pavement, canopy and social factors rather than climate.

## Nine tracts split the ZIP between a hillside and some of America's most vulnerable blocks

The Census Bureau's [2020 ZCTA-to-tract relationship file](https://www2.census.gov/geo/docs/maps-data/data/rel2020/zcta520/tab20_zcta520_tract20_natl.txt) shows that 79902 (16.9 km² of land, about 6.5 sq mi) overlaps **nine** El Paso County tracts. Five form its core, with at least 89% of their land inside it. Two, 14 and 11.15, are partial, and two are slivers. The neighborhood labels come from [Census Geocoder](https://geocoding.geo.census.gov/geocoder/geographies/onelineaddress?address=500%20W%20University%20Ave%2C%20El%20Paso%2C%20TX%2079968&benchmark=Public_AR_Current&vintage=Census2020_Current&layers=Census%20Tracts&format=json) placements of landmark addresses. They are informal; no city crosswalk exists. This changes one earlier claim: **807 Kern Dr geocodes to tract 15.01, not 15.02**, so Kern Place straddles both tracts. UTEP and 1505 Rim Rd are in 15.02. Mission Hills could not be pinned to a tract from a primary source.

FEMA's NRI v1.20 values come from FEMA's own ArcGIS feature service, labelled "December 2025 (1.20.0)" ([NRI Census Tracts query, El Paso County](https://services.arcgis.com/XG15cJAlne2vxtgt/arcgis/rest/services/National_Risk_Index_Census_Tracts/FeatureServer/0/query?where=STATEFIPS%3D%2748%27+AND+COUNTYFIPS%3D%27141%27&outFields=*&returnGeometry=false&f=json)). fema.gov itself remained blocked. SVI 2022 values are from [CDC's US tract file](https://svi.cdc.gov/Documents/Data/2022/csv/states/SVI_2022_US.csv).

| Tract (neighborhood, informal) | % of 79902 land | % of tract in 79902 | **NRI heat-wave risk score / rating** | Heat-wave EAL $/yr | NRI overall risk | NRI social vulnerability | SVI 2022 (US pctl) |
|---|---|---|---|---|---|---|---|
| 15.01 (north Kern Place, Scenic Dr hillside) | 33.4% | 96.4% | **85.25 / Relatively High** | 79,481 | Relatively Low | Very High | 0.64 |
| 15.02 (Kern Place south, Rim Rd, UTEP) | 15.8% | 100% | 68.43 / Relatively Moderate | 42,374 | **Relatively High** (only one in county) | Very High | 0.49 |
| 14 (I-10 / river corridor) | 14.6% | 31.0% | 59.84 / Relatively Moderate | 42,910 | Very Low | Relatively High | 0.93 |
| 22.01 (El Paso High area) | 12.4% | 93.0% | 71.22 / Relatively Moderate | 48,160 | Relatively Low | Very High | **0.99** |
| 16 (Sunset Heights) | 7.7% | 89.1% | 78.87 / Relatively Moderate | 65,775 | Relatively Low | Very High | **0.98** |
| 22.02 (Montana Ave, north of downtown) | 6.9% | 100% | 66.99 / Relatively Moderate | 61,792 | Relatively Low | Relatively Moderate | **0.99** |
| 11.15 (N Mesa, near UTEP) | 6.1% | 33.2% | 76.81 / Relatively Moderate | 62,225 | Very Low | Very High | 0.85 |
| 11.11 (sliver, west side) | 2.1% | 3.1% | 85.82 / Relatively High | 81,985 | Relatively Low | Very High | 0.52 |
| 17 (sliver, downtown edge) | 0.9% | 14.0% | 41.48 / Relatively Low | 18,790 | Relatively Low | Very High | 0.97 |

Every tract's community resilience is "Very Low", and every tract carries the identical RESL score of 1.38. That suggests v1.20 assigns resilience at the county level, but the FEMA documentation that would confirm it was blocked. Annualized heat-wave frequency is nearly identical everywhere (8.72–8.80 events/yr), so tract differences reflect exposure and social vulnerability rather than climate. Among El Paso County's 188 tracts, 15.01 ranks 38th on heat-wave risk and 15.02 ranks 142nd [DERIVED]. Weighting the nine tract scores by land area gives about **74, which falls in the Relatively Moderate band [DERIVED]**. This is illustrative arithmetic only; FEMA publishes no ZIP value.

At county level, El Paso is **"Relatively High" for heat wave (score 98.68)**, with **$13.98M in expected annual loss** and about one fatality-equivalent per year. Overall NRI risk is "Relatively High" (95.45), social vulnerability "Very High" and resilience "Very Low" ([NRI Counties query](https://services.arcgis.com/XG15cJAlne2vxtgt/arcgis/rest/services/National_Risk_Index_Counties/FeatureServer/0/query?where=STATEFIPS%3D%2748%27+AND+COUNTYFIPS%3D%27141%27&outFields=*&returnGeometry=false&f=json)). Across the service's 3,232 county records, that heat-wave score ranks **42nd of 3,114 rated counties nationally and 6th of 254 in Texas [DERIVED]**, behind Dallas, Harris, Tarrant, Bexar and Hidalgo. The earlier report's county overall score of "35.67" came from an older NRI version or scale and should be discarded. The "~$14M" heat expected annual loss holds up.

### ACS 2020–2024 shows old housing, carless renters and an elderly core

ACS 5-year 2020–2024 data, taken from the Census Bureau's [table-based Summary File](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/), confirm the earlier Census Reporter figures exactly: population 19,031, median age 40.0, poverty 22.5%, median household income $50,873, foreign-born 24.4%. Simplemaps' $38,274 income figure was an older vintage. The ZIP's distinguishing traits are **housing age (43.7% built before 1950, against 7.0% countywide)**, **renters (58.0% vs 35.8%)**, **carless households (16.4% vs 6.4%)** and **seniors (21.5% vs 13.1%)**.

| Geography | Pop. | % 65+ | Median HH income | % poverty | % uninsured | % renter | % no vehicle | % built pre-1950 | Median yr built |
|---|---|---|---|---|---|---|---|---|---|
| **ZCTA 79902** | 19,031 | 21.5 | $50,873 | 22.5 | 23.4 | 58.0 | 16.4 | **43.7** | 1954 |
| Tr 15.01 | 4,400 | 23.4 | $77,008 | 15.4 | 20.9 | 28.2 | 8.0 | 15.0 | 1964 |
| Tr 15.02 | 2,900 | 26.4 | $111,436 | 7.2 | 17.1 | 29.0 | 1.2 | 65.6 | ≤1939 |
| Tr 14 | 2,152 | 7.7 | $46,306 | 32.6 | 27.2 | 88.2 | 18.5 | 12.8 | 1974 |
| Tr 22.01 | 2,758 | 26.9 | $41,228 | 23.6 | 23.4 | 58.2 | 10.8 | 30.6 | 1962 |
| **Tr 16 (Sunset Heights)** | 4,200 | 21.2 | **$25,887** | 25.7 | 17.5 | 88.1 | **35.9** | 52.1 | 1949 |
| Tr 22.02 | 3,555 | 19.0 | $35,167 | 32.5 | 35.3 | 81.2 | 22.1 | **70.1** | ≤1939 |
| Tr 11.15 | 3,965 | 7.4 | $57,301 | 16.3 | 37.5 | 89.3 | 4.7 | 2.7 | 1990 |
| Tr 11.11 (sliver) | 5,498 | 9.9 | $63,125 | 17.2 | 24.7 | 73.5 | 5.6 | 4.0 | 1985 |
| Tr 17 (sliver) | 1,018 | 11.2 | $18,264 | 66.7 | 33.1 | 98.2 | 45.8 | 68.7 | ≤1939 |
| El Paso County | 870,779 | 13.1 | $59,806 | 18.7 | 21.6 | 35.8 | 6.4 | 7.0 | 1988 |
| Texas | 30,188,424 | 13.4 | $78,476 | 13.8 | 17.1 | 37.4 | 5.4 | 5.8 | 1992 |

Many tract margins of error are wide. Tract 16's income is ±$15,433, for example, so compare tracts only where the gaps are large. Tracts 11.15 and 14 border UTEP, and their young median ages and roughly 89% renter shares fit student housing. Tract populations sum to 30,446, against 19,031 for the ZCTA, because four tracts extend mostly outside it. **Use the ZCTA row for 79902 as a whole and the tract rows only for sub-areas.** The ACS does not measure air conditioning. The pattern that matters for heat runs through Sunset Heights and the 22.0x tracts: pre-war housing, renters who cannot install AC themselves, and households without a car to reach cooling centers. This is where FEMA's tract heat scores are only "moderate" but SVI is at the national extreme.

## NOAA's heat map puts 79902 at the city median, with cool foothills and hot fringes

NOAA's own image services name the El Paso rasters `HINDX.*.20200710.El_Paso`. They timestamp the traverses at 6–7 AM, 3–4 PM and 7–8 PM MDT on **July 10, 2020** ([NOAA Afternoon Air Temperature ImageServer](https://gis.nnvl.noaa.gov/arcgis/rest/services/HINDZ/Afternoon_Air_Temperature_in_Cities/ImageServer)). That settles the date: [CAPA's "July 11" post](https://www.capastrategies.com/city-of-el-paso-maps-hottest-places-in-region) refers to "Friday's extreme heat," and July 10 was the Friday. NWS El Paso had an **Excessive Heat Warning** in effect that day for "temperatures reaching or exceeding 110" ([IEM archive of NWS text](https://mesonet.agron.iastate.edu/api/1/nwstext/202007101109-KEPZ-WWUS74-NPWEPZ)), and the airport hit 109°F with an 83°F low ([RCC-ACIS](https://data.rcc-acis.org/StnData)).

Sampling the modeled rasters across the city and across the ZCTA polygon gives the figures below **[DERIVED: researcher grid sampling of primary rasters; about 500 m spacing citywide, 523 valid points at about 150 m in 79902]**.

| Period (MDT) | Citywide range (median) | 79902 range (mean) | Coolest 79902 spot | Hottest 79902 spots |
|---|---|---|---|---|
| Morning 6–7 AM | 74.3–85.5°F (83.2) | 79.7–85.6°F (83.3) | Rim Rd/Scenic Dr foothill, about 80.3°F | Lower UTEP / I-10 / Mesa, about 85.2–85.6°F |
| Afternoon 3–4 PM | 100.2–106.4°F (104.5) | 102.7–106.1°F (104.4) | Foothill, about 103.3°F | Mission Hills and Sunset Heights, about 104.9°F; east edge 106.1°F |
| Evening 7–8 PM | 92.0–105.4°F (103.6) | 101.1–104.9°F (103.4) | Foothill, about 101–102°F | Sunset Heights east / downtown edge and Mesa corridor, about 104.4–104.9°F |

Two conclusions follow. **79902 is not one of El Paso's hottest pockets.** Its mean sits within about a degree of the city median in every period. The citywide extremes are on the far west side near I-10/Resler and in east-central El Paso, and the cool extreme is the irrigated Upper Valley. Inside the ZIP, the **Franklin Mountains foothills run 3–4°F cooler than Sunset Heights at dawn**, which fits cold air draining off the slopes, but that edge shrinks to about 1.5°F by afternoon. Nearly all of 79902 was still at **101–105°F at 7–8 PM**, so on the hottest days overnight relief is minimal everywhere in the ZIP. One caveat: the downtown core (San Jacinto Plaza) and the airport returned NoData because they lay outside the mapped footprint. "Downtown is the hottest part of 79902" therefore cannot be claimed from these maps. The rasters are single-day statistical models, so the relative pattern matters more than the absolute degrees.

## NWS records show 2023 as the outlier and 2026 as the long burn

All four 79902 neighborhood points fall in NWS forecast zone **TXZ418, "Western El Paso County"**; the airport is in TXZ419 ([api.weather.gov zone TXZ418](https://api.weather.gov/zones/forecast/TXZ418)). The IEM VTEC archive counts heat products for TXZ418 as follows ([IEM VTEC by WFO, EPZ](https://mesonet.agron.iastate.edu/json/vtec_events_bywfo.py?wfo=EPZ&year=2023)). Alert-day counts are **[DERIVED]**: days with a non-cancelled product in effect between 10 AM and 8 PM.

| Year | Heat Advisories | Excessive Heat Warnings | Watches | ~Alert days | ELP days ≥100°F | Days ≥105°F | Nights ≥75°F |
|---|---|---|---|---|---|---|---|
| 2020 | 9 | 1 (Jul 10–13) | 0 | 17 | **57** | 18 | 52 |
| 2021 | 2 | 0 | 0 | 6 | 20 | 4 | 14 |
| 2022 | 3 | 0 | 0 | 6 | 34 | 8 | 27 |
| **2023** | 10 | **4** | 4 | **39** | **70** (record) | **33** | **68** |
| 2024 | 11 | 1 (Jun 13–15) | 1 | 20 | 55 | 16 | 59 |
| 2025 | 6 | 0 | 0 | 13 | 37 | 15 | 39 |
| 2026 (thru Sep 30) | 7 | 0 | 0 | 12 | 52 | 10 | 50 |

The temperature columns are computed from ACIS daily data for the threaded El Paso record ([RCC-ACIS StnData, ELPthr](https://data.rcc-acis.org/StnData)), and the NWS's own table reproduces the 100°F counts for 2015–2024 ([NWS El Paso 100-degree FAQ](https://www.weather.gov/epz/elpaso_100_degree_page)). EPZ publishes no numeric criteria page; weather.gov/epz/heat returns 404. Issued products cite **105–108°F for advisories and about 110°F for warnings** (2023), and as low as **103–107°F** for a July 2026 advisory ([IEM NWS text, July 2026](https://mesonet.agron.iastate.edu/api/1/nwstext/202607290334-KEPZ-WWUS74-NPWEPZ)). **No "Extreme Heat" watch or warning has been issued for TXZ418 since the 2025 rename.**

The climate record adds context. 2023 still holds the 100°F-day record (70) and the **44-day 100°F streak (June 16 – July 29)**. 2024 is **tied for 4th** in 100°F days, with 1980 [DERIVED from ACIS ranking], and is the **warmest year on record by mean temperature (69.8°F)** ([NWS 2024 Annual Review](https://www.weather.gov/media/epz/climat/2024AnnualReview.pdf)). 2026 produced a different kind of heat: a record **108-day streak of 90°F days, June 6 – September 21**, beating 106 days in 2015 [DERIVED from ACIS], and the warmest January–September on record. It brought only seven advisories and ten days at or above 105°F. [El Paso Matters](https://elpasomatters.org/2026/09/21/el-paso-record-108-consecutive-days-90-degree-heat/) counts 50 100°F days inside the streak, while ACIS shows 52; treat the figure as 50–52. For 79902, the trend in nights matters most: **nights at or above 75°F roughly doubled, from 26–31 a year in 2015–17 to 50–68 in 2020, 2023, 2024 and 2026.** Combined with the 7–8 PM map readings, that points to shrinking overnight recovery in a ZIP where one resident in five is over 65.

Heat deaths come from a single source, and the earlier report's "conflict" over them was not real. The El Paso Matters article is a republication of the Inside Climate News investigation. It reports that **state data attribute 26 deaths (2023) and a record 39 deaths (2024) in El Paso County directly or indirectly to heat**, while the reporters could identify **26 individual victims by autopsy across both years combined, 19 of them migrants** ([El Paso Matters / Inside Climate News, Aug. 21, 2025](https://elpasomatters.org/2025/08/21/el-paso-weather-extreme-heat-illness-deaths/)). The same piece documents one Franklin Mountains hiker death per year from 2022 to 2024; those trailheads border 79902 off Rim Road and Scenic Drive. It also notes that the city "does not track heat-related illnesses." No 2025 county total and no ZIP-level data exist publicly.

## El Paso Water's tap water is clean on paper; the gap is unknown pipes

EPWater (PWSID TX0710002, **747,168 people served**) labels its reports by data year: the "2024 Drinking Water Report" ([2024 CCR](https://www.epwater.org/ep-water/uploads/2024-ccr.pdf)) covers calendar 2024 and was released in May 2025, and the "2025" report ([2025 CCR](https://www.epwater.org/ep-water/uploads/Documents/2025-ccr-web.pdf)) covers 2025 and was released in June 2026. The [2023 report](https://www.epwater.org/ep-water/uploads/dwr_2023.pdf) adds a third year.

| Parameter (limit) | 2023 data | 2024 data | 2025 data |
|---|---|---|---|
| **Arsenic** avg (max) (MCL 10 ppb) | 5.5 (9.7) ppb | **4.3 (9.1) ppb** | 3.4 (**13.0**) ppb* |
| **TTHM** highest LRAA (MCL 80 ppb) | 70.45 ppb | **71.03 ppb** | 51.03 ppb |
| **HAA5** highest LRAA (MCL 60 ppb) | 34.05 ppb | **35.43 ppb** | 19.23 ppb |
| **Lead** 90th pctl (max) (AL 15 ppb) | 1.5 (4.3) ppb, 2022 sampling | 1.16 (6.6) ppb | 0 as printed (**12.9**) ppb |
| Copper 90th pctl (AL 1.3 ppm) | 0.39 ppm | 0.476 ppm | 0.472 ppm |
| Nitrate as N (MCL 10 ppm) | 0.92 ppm | 1.06 ppm | 0.74 ppm |
| Fluoride avg (natural) | 0.63 ppm | 0.29 ppm | 0.58 ppm |
| Uranium avg (MCL 30 ppb) | 4.4 ppb | 5.2 ppb | 1.5 ppb |
| PFOS max (2024 MCL 4.0 ppt, not yet enforced) | **6.05 ppt** | **4.27 ppt** | below reporting limit |
| Violations listed | Chlorite M/R (May), RTCR monitoring (Feb) | Chlorite M/R (Mar) | None |

\*In 2025, arsenic compliance used an approved alternative plan based on the distribution-system average, so a single sample above 10 ppb was not a violation.

Several earlier aggregator figures are now resolved. **No CCR contains "6.6 ppb arsenic"**: 6.6 ppb is the 2024 *lead* maximum, misattributed. **No CCR contains "21 ppb"**, so that figure is unsupported. **HAA5's "0.06 mg/L" was the MCL itself**; the real 2024 result is 35.43 ppb, about 59% of the limit. TTHM at 71 ppb was the item closest to its limit (89%) until it fell to 51 ppb in 2025. Byproducts likely dropped because a short 2025 Rio Grande season meant less organic-rich surface water was chlorinated, but the CCR does not say so. Individual PFOS detections in 2023–24 exceeded the 4.0 ppt MCL that EPA set in 2024. They are not violations, because compliance rests on running annual averages and enforcement has not begun, and all 2025 samples were below the reporting limit. The maximum lead and copper results stayed below the action levels in every year, which implies **zero sites above the action level [DERIVED from printed ranges; CCRs do not state site counts]**. The 2025 lead maximum of 12.9 ppb, however, was about double 2024's. EPWater publishes no current TDS, sodium or hardness data. Its only sheet, from 2017, shows the Lower Valley/Central wells that feed "Downtown Central" off-season at **862 mg/L TDS and 283 mg/L chloride** ([EPWater chemical analysis](https://www.epwater.org/ep-water/uploads/chemanalysis.pdf)). The aggregator figures for hardness (207 ppm) and TDS (2,080 maximum) appear in no EPWater document. Utility documents point to the **Robertson/Umbenhauer "Canal Street" plant** (Rio Grande water, March–September) as the supplier for Central and West El Paso, which includes 79902 ([Robertson/Umbenhauer fact sheet](https://www.epwater.org/ep-water/uploads/robertson-umbenhauer-water-plant.pdf)). In 2025 its units posted the system's highest turbidity readings (0.38 and 0.36 NTU), but no violation.

**Lead service lines.** The 2025 CCR states that "**No lead service lines** have been identified" and counts **192 "galvanized requiring replacement"** lines after more than 100,000 meters were assessed. EPWater posts no downloadable inventory for TX0710002, so this research queried the backend of the utility's public [120Water service-line map](https://pws-ptd.120wateraudit.com/ElPaso-TX) directly. The 79902 tally below is a researcher aggregation, not a published EPWater figure **[DERIVED]**.

| Area | Service lines | Non-lead | Lead | Unknown | Galvanized (GRR) |
|---|---|---|---|---|---|
| Systemwide | ~220,280 | 208,982 | 0 | 11,108 (5.0%) | 190 |
| **ZIP 79902** (address ZIP field) | ~5,538 | 4,019 (72.6%) | 0 | **1,513 (27.3%)** | 6 |

Three things stand out. 79902 has about 2.5% of the system's lines but **about 14% of its unknowns [DERIVED]**. Most of those unknowns (1,175) are unknown on both the utility and the customer side, which suggests the premises have never been inspected in the field. The six galvanized lines are all in pre-war central blocks: 215 Prospect St, 501 N Oregon St, 1911 N Kansas St, 2007 N Florence St, 1661 Rim Rd and 709 Blacker Ave. No 79902 record carries a verification date after September 2025, so field work there appears to have paused or the map has not been updated since. EPWater's [Lead Awareness page](https://www.epwater.org/our-water/water-quality/lead-awareness) says unknown-line customers were to receive notices by December 2025 and annually after that. Whether the notices went out is unconfirmed. These figures fit the housing data: a ZIP where 44% of homes predate 1950 holds a disproportionate share of the pipes nobody has looked at.

**EPA ECHO.** ECHO's detailed facility report lists TX0710002 as "No Violation Identified" (as of 03/31/2026). It is not a serious violator, with 2 noncompliance quarters in three years, 0 formal actions and $0 in penalties ([ECHO DFR API, TX0710002](https://echodata.epa.gov/echo/dfr_rest_services.get_dfr?output=JSON&p_id=TX0710002&p_system=SDWIS)). EPA's SDWIS copy holds **54 violation rows, all monitoring/reporting, none health-based**. Forty-nine of them come from a single missed SOC/VOC sampling quarter in 2018, logged one row per contaminant, so the record collapses to **six distinct events from 2015 to 2024** ([Envirofacts VIOLATION](https://data.epa.gov/efservice/VIOLATION/PWSID/TX0710002/JSON)). Neither the aggregators' "69 violations" nor "858 violations / 192 health-based" matches EPA records; the 858 figure should be discarded. SDWIS also logs state public-notice actions for **E. coli at EPWater wells in November 2024, January 2025 and November 2025**, with no associated violation ([Envirofacts ENFORCEMENT_ACTION](https://data.epa.gov/efservice/ENFORCEMENT_ACTION/PWSID/TX0710002/JSON)). EPWater's enforcement problems are on the wastewater side, and none of its plants is in 79902. The **Bustamante WWTP** (79927) is currently in violation, with E. coli and TSS exceedances of 400–500%+ in 2025–26, two significant-noncompliance quarters, and a February 2026 EPA order whose milestones are still unmet ([ECHO DFR API, TX0101605](https://echodata.epa.gov/echo/dfr_rest_services.get_dfr?output=JSON&p_id=TX0101605&p_system=NPDES)). The Frontera sewage order carried a **$2,016,000 penalty, fully offset by a SEP, so $0 was paid** ([TCEQ docket 2022-0310-MWD-E](https://www.tceq.texas.gov/downloads/agency/decisions/agendas/backup/2022/2022-0310-mwd-e.pdf)). An ECHO search of ZIP 79902 itself returns 135 facilities with **0 current violations, 0 formal actions in five years and $0 in penalties** ([ECHO all-media search, ZIP 79902](https://echodata.epa.gov/echo/echo_rest_services.get_facilities?output=JSON&p_zip=79902)). The one facility with recent violations, Quail Run MHP, is registered at a 79902 mailing address but sits in far-east El Paso. The ZIP's EPA-visible burden is legacy contamination, such as El Paso Plating Works, an ASARCO tract and old dry-cleaner sites, not active permit violations.

## What changed from the earlier snippet-based report

| Earlier claim | Primary-verified finding |
|---|---|
| Arsenic "6.6 ppb average, up to 21 ppb" | 2024 average **4.3 ppb** (max 9.1). 6.6 ppb was the 2024 lead maximum; 21 ppb appears in no CCR |
| HAA5 "0.06 mg/L" | That is the MCL. 2024 highest LRAA was **35.43 ppb** |
| Violation counts "69" / "858, 192 health-based" | EPA SDWIS: **54 rows, 0 health-based, 6 distinct events** (2015–2024) |
| 2020: 56 days ≥100°F (earlier notes) | **57** (ACIS and NWS) |
| 2024 rank "2nd or 4th" | **Tied 4th** with 1980 for 100°F days; warmest by mean temperature |
| 90°F streak began June 22 (earlier notes) | Began **June 6**. June 22 was the start of a separate El Paso Matters statistic |
| Heat-death "conflict" (26/39 vs 26) | Not a conflict: one ICN investigation reporting state-data totals (26, 39) and 26 autopsy-identified victims over both years |
| Kern Place = tract 15.02 (via 807 Kern Dr) | 807 Kern Dr is in **15.01**; Kern Place straddles 15.01 and 15.02 |
| Only one tract identified | **Nine tracts**, with land shares from the Census relationship file |
| County NRI overall "35.67" | v1.20 overall score **95.45** (Relatively High); heat-wave score 98.68 |
| Population served 672,538 vs 747,168 | **747,168** (ECHO/SDWIS) |
| Traverse date July 10 vs July 11 | **July 10, 2020**, confirmed by NOAA raster metadata |
| Extreme heat day = 90th percentile | **95th percentile** (HHI technical documentation) |

## Remaining gaps and how to fill them

| Gap | Why it is missing | How to fill it |
|---|---|---|
| CAPA El Paso final report figures (41 volunteers, 66,000+ readings, 100 vs 105 sq mi) and heat-index rasters | heat.gov and cpo.noaa.gov return CloudFront 403; heat-index rasters not sampled | Request the report from the City of El Paso Office of Climate & Sustainability or CAPA; sample the VizLab "Heat Index in Cities" image services the same way the air-temperature rasters were sampled |
| TCEQ lead/copper sample counts, sites above action level, TCEQ-side service line inventory | The new Drinking Water Viewer's API returns HTTP 500 outside a browser session | Open https://dwv.tceq.texas.gov/ manually, search TX0710002, and read the Lead & Copper and Service Line Inventory tabs |
| 2025 (and 2026) heat deaths, county and ZIP | DSHS heat pages return 404; ME report article gives no heat line | Request DSHS heat-related death data by county; obtain the El Paso County Medical Examiner 2025 annual report PDF |
| FEMA NRI documentation, data dictionary, CSV; RAPT | fema.gov 403, hazards.fema.gov SSL error | Fetch from an unrestricted network; confirm the county-level RESL assignment and the RISK_SPCTL anomaly (it equals RISK_SCORE) |
| Population-weighted tract shares | The relationship file has land area only | Join 2020 PL 94-171 block counts to the block-to-ZCTA assignment, or use HUD's ZIP–tract crosswalk residential ratios |
| Whether unknown-line notices were sent; post-2025 field verification in 79902 | No EPWater statement; map shows no 79902 verifications after Sept 2025 | Ask EPWater directly; re-query the 120Water map later to track changes |
| Current TDS, sodium, hardness by source; plant-to-ZIP mapping | Latest EPWater sheet is from 2017 | Request current source-water chemistry and pressure-zone maps from EPWater |
| Mission Hills tract assignment | No primary city crosswalk | City of El Paso neighborhood GIS layer overlaid on TIGER tracts |

## Conclusion

The primary data change the shape of the risk more than its size. 79902's top-decile HHI rank is real, but it reflects a city-scale climate plus local pavement and poverty, not an unusually hot microclimate. On the July 2020 map the ZIP is average for El Paso, and within Texas it falls to about the 72nd percentile. The sharper signal is internal and social. The same six square miles contain a hillside tract FEMA rates highest for heat and lowest for poverty, and three tracts at the 98th–99th national SVI percentile that FEMA rates only "moderate" for heat. A ZIP-level index blurs exactly that contrast, so heat interventions such as cooling access, night-time checks on seniors living alone, and help for carless renters belong in Sunset Heights and the Montana/El Paso High tracts, not spread evenly across 79902. The 2026 season, with a record 90°F streak but few warnings, shows that the advisory system tracks peak days while the persistent harm builds overnight.

On water, the evidence supports a confident "safe at the tap, by every regulatory measure" for 2023–2025. The one live exposure question is pipes, not the utility's chemistry. 79902 holds a seventh of the system's unverified service lines and 44% of its housing predates 1950. A finding of zero lead lines among mostly *unverified* old premises is a measure of inspection progress, not proof that no lead exists. Field verification of those roughly 1,500 lines is the highest-value next step.

# Census Tracts and ACS Demographics of ZCTA 79902 (El Paso, TX): Primary-Source Verification

> **Provenance.** Every figure below comes from files I downloaded from census.gov or cdc.gov on 2026-10-01 and processed locally. Each is marked **[PV]** (primary-verified). This file replaces the snippet-based notes in `El Paso 79902 heat and water/census_tracts.md`. Access notes: the Census Data API (api.census.gov) now answers, but data queries without a key redirect to `missing_key.html`. I therefore took the ACS values from the **official ACS 5-year table-based Summary File** on www2.census.gov, which holds the same published estimates as the API, and checked the variable labels against the API's `variables.json` (that metadata endpoint needs no key). **Latest vintage available: ACS 5-year 2020-2024**. The 2019-2023 fallback was not needed.

## Which 2020 census tracts overlap ZCTA 79902, and what share of each lies in it?

### Takeaway
ZCTA 79902 (16,915,468 m² of land, about 6.53 sq mi) overlaps **9** 2020 census tracts, all in El Paso County (48141). Five make up its core, either lying entirely inside it or with ≥89% of their land inside: 15.01, 15.02, 16, 22.01 and 22.02. Two contribute a substantial partial share: 14 and 11.15. Two are slivers: **11.11** has only 3.1% of its land in 79902, and **17** (downtown) has 14.0% of its land in 79902, which is 0.9% of the ZCTA. Tract 15.02 (Kern Place / Rim / UTEP) is confirmed, and its whole land area lies in 79902.

### Cited Findings
- Source file: Census Bureau 2020 ZCTA5-to-census-tract relationship file, filtered to `GEOID_ZCTA5_20 = 79902`. The 9 tract parts sum exactly to the ZCTA land area (16,915,468 m²). ZCTA water area is 30,595 m², all of it in tract 22.01. **[PV]** — [tab20_zcta520_tract20_natl.txt (2020 Census geography)](https://www2.census.gov/geo/docs/maps-data/data/rel2020/zcta520/tab20_zcta520_tract20_natl.txt)

| GEOID | Tract | Tract land (m²) | Land in 79902 (m²) | % of tract land in 79902 | % of 79902 land | Sliver flag (<5%) |
|---|---|---|---|---|---|---|
| 48141001111 | Census Tract 11.11 | 11,576,614 | 358,655 | 3.1 | 2.1 | yes (tract share) |
| 48141001115 | Census Tract 11.15 | 3,112,241 | 1,034,163 | 33.2 | 6.1 | no |
| 48141001400 | Census Tract 14 | 7,957,689 | 2,466,935 | 31.0 | 14.6 | no |
| 48141001501 | Census Tract 15.01 | 5,857,753 | 5,647,857 | 96.4 | 33.4 | no |
| 48141001502 | Census Tract 15.02 | 2,665,431 | 2,665,431 | 100.0 | 15.8 | no |
| 48141001600 | Census Tract 16 | 1,470,079 | 1,310,376 | 89.1 | 7.7 | no |
| 48141001700 | Census Tract 17 | 1,127,843 | 157,446 | 14.0 | 0.9 | yes (ZCTA share) |
| 48141002201 | Census Tract 22.01 | 2,260,325 | 2,101,555 | 93.0 | 12.4 | no |
| 48141002202 | Census Tract 22.02 | 1,173,050 | 1,173,050 | 100.0 | 6.9 | no |

- Tract land areas and internal points, from the Census 2020 Gazetteer (ALAND in m²; lat/long are internal points): 11.11 (4.47 sq mi; 31.828, -106.501), 11.15 (1.202 sq mi; 31.807, -106.512), 14 (3.072 sq mi; 31.788, -106.522), 15.01 (2.262 sq mi; 31.794, -106.496), 15.02 (1.029 sq mi; 31.776, -106.500), 16 (0.568 sq mi; 31.764, -106.498), 17 (0.435 sq mi; 31.760, -106.487), 22.01 (0.873 sq mi; 31.779, -106.481), 22.02 (0.453 sq mi; 31.770, -106.484). **[PV]** — [2020 Gazetteer, Texas tracts](https://www2.census.gov/geo/docs/maps-data/data/gazetteer/2020_Gazetteer/2020_gaz_tracts_48.txt)
- The same file was used to produce the CSV at `research_notes/El Paso 79902 primary source data/tracts_79902.csv`. **[PV]**

### Inferences
- Summing the nine tracts' ACS populations gives 30,446, against 19,031 for the ZCTA itself. That gap is expected, because 11.11, 11.15, 14 and 17 extend mostly outside 79902. **Use tract figures to describe sub-areas. Do not add or average them to stand in for the ZCTA.** The ZCTA-level ACS estimate is the right number for 79902 as a whole.
- The shares here are land-area shares, not population shares. Tract 14 includes the I-10 / Rio Grande corridor and is probably sparse in parts, so its land share probably overstates its population share. (Not verified.)
- Practical weighting: treat 15.01, 15.02, 16, 22.01 and 22.02 as "core 79902". Treat 11.15 and 14 as partial, and 11.11 and 17 as negligible.

### Gaps
- Population-weighted tract shares. These would need 2020 block-level PL 94-171 counts joined to the 2020 block-to-ZCTA assignment. Not computed.

## Key ACS 2020-2024 indicators for ZCTA 79902, each tract, El Paso County, and Texas

### Takeaway
ZCTA 79902 (ACS 2020-2024): population **19,031**, median age **40.0**, **21.5% aged 65+**, **only 2.4% under 5**, median household income **$50,873**, poverty **22.5%**, uninsured **23.4%**, Hispanic **75.6%**, foreign-born **24.4%**, limited-English households **13.9%**, renters **58.0%**, households with no vehicle **16.4%**. The housing is very old: **43.7% built before 1950**, **85.9% before 1980**, median year built **1954**. Disability rate is **13.0%**.

Compared with El Paso County (median year built 1988, 7.0% built before 1950, 35.8% renters, 6.4% with no vehicle, 13.1% aged 65+), 79902 is far older in both housing stock and population, much more renter-heavy and car-free, and lower-income. Its poverty rate is somewhat higher than the county's. It is less Hispanic than the county (75.6% vs 82.7%) and has a lower limited-English share (13.9% vs 17.6%).

Tract differences are large. **Tract 17** (downtown sliver), **16** (Sunset Heights) and **22.02** stand out on poverty, no-vehicle households, renting and pre-1950 housing. **Tract 15.02** (Kern Place / Rim) is affluent ($111k) but has the oldest housing.

### Cited Findings
All rows are **[PV]**. Source: ACS 5-year 2020-2024 table-based Summary File, files `acsdt5y2024-<table>.dat` at [www2.census.gov ACS SF 2024 5YRData](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/). Variable labels were checked against [api.census.gov/data/2024/acs/acs5/variables.json](https://api.census.gov/data/2024/acs/acs5/variables.json). GEO_IDs: 860Z200US79902; 1400000US48141xxxxxx; 0500000US48141; 0400000US48.

**Table A: population, age, income, poverty, insurance** (estimate ± 90% MOE)

| Geography | Total pop | Median age | % 65+ | % under 5 | Median HH income | % in poverty | % uninsured |
|---|---|---|---|---|---|---|---|
| ZCTA 79902 | 19,031 ± 1,433 | 40.0 ± 2.2 | 21.5 ± 2.7 | 2.4 ± 0.9 | $50,873 ± 7,890 | 22.5 ± 4.0 | 23.4 ± 3.1 |
| Tr 11.11 (sliver) | 5,498 ± 650 | 30.7 ± 2.7 | 9.9 ± 2.6 | 4.7 ± 2.3 | $63,125 ± 7,615 | 17.2 ± 9.6 | 24.7 ± 7.6 |
| Tr 11.15 | 3,965 ± 1,362 | 30.2 ± 2.5 | 7.4 ± 1.3 | 7.5 ± 6.8 | $57,301 ± 10,945 | 16.3 ± 4.7 | 37.5 ± 14.7 |
| Tr 14 | 2,152 ± 336 | 29.8 ± 2.8 | 7.7 ± 4.3 | 2.2 ± 2.0 | $46,306 ± 15,826 | 32.6 ± 10.5 | 27.2 ± 8.4 |
| Tr 15.01 | 4,400 ± 611 | 44.7 ± 7.7 | 23.4 ± 6.1 | 2.9 ± 2.4 | $77,008 ± 23,791 | 15.4 ± 7.5 | 20.9 ± 6.7 |
| Tr 15.02 | 2,900 ± 518 | 40.8 ± 8.4 | 26.4 ± 7.2 | 3.6 ± 3.1 | $111,436 ± 14,857 | 7.2 ± 5.2 | 17.1 ± 6.4 |
| Tr 16 | 4,200 ± 671 | 35.6 ± 3.4 | 21.2 ± 7.0 | 0.6 ± 1.0 | $25,887 ± 15,433 | 25.7 ± 9.1 | 17.5 ± 7.2 |
| Tr 17 (sliver) | 1,018 ± 161 | 36.2 ± 6.1 | 11.2 ± 6.1 | 4.8 ± 8.4 | $18,264 ± 9,409 | 66.7 ± 21.7 | 33.1 ± 2.8 |
| Tr 22.01 | 2,758 ± 442 | 43.9 ± 8.6 | 26.9 ± 5.7 | 2.5 ± 2.2 | $41,228 ± 8,217 | 23.6 ± 11.3 | 23.4 ± 9.2 |
| Tr 22.02 | 3,555 ± 746 | 39.3 ± 8.1 | 19.0 ± 6.4 | 1.6 ± 1.5 | $35,167 ± 14,439 | 32.5 ± 11.2 | 35.3 ± 8.5 |
| El Paso County | 870,779 ± 0 | 33.6 ± 0.1 | 13.1 ± 0.3 | 6.6 ± 0.0 | $59,806 ± 1,141 | 18.7 ± 0.6 | 21.6 ± 0.5 |
| Texas | 30,188,424 ± 0 | 35.6 ± 0.1 | 13.4 ± 0.0 | 6.4 ± 0.0 | $78,476 ± 263 | 13.8 ± 0.1 | 17.1 ± 0.1 |

**Table B: ethnicity, nativity, language, tenure, vehicles, disability** (estimate ± 90% MOE)

| Geography | % Hispanic | % foreign-born | % limited-English HHs | Occupied HUs | % renter-occ. | % HHs no vehicle | % with disability |
|---|---|---|---|---|---|---|---|
| ZCTA 79902 | 75.6 ± 4.8 | 24.4 ± 2.9 | 13.9 ± 3.2 | 8,494 ± 660 | 58.0 ± 4.4 | 16.4 ± 4.6 | 13.0 ± 2.1 |
| Tr 11.11 (sliver) | 73.7 ± 7.9 | 15.4 ± 4.6 | 24.8 ± 11.5 | 2,760 ± 283 | 73.5 ± 6.4 | 5.6 ± 4.9 | 10.6 ± 4.1 |
| Tr 11.15 | 81.4 ± 17.7 | 35.3 ± 17.8 | 38.7 ± 12.0 | 1,843 ± 287 | 89.3 ± 8.2 | 4.7 ± 3.3 | 6.6 ± 1.8 |
| Tr 14 | 74.5 ± 5.6 | 32.4 ± 8.2 | 11.0 ± 6.1 | 964 ± 184 | 88.2 ± 8.1 | 18.5 ± 9.8 | 14.7 ± 5.1 |
| Tr 15.01 | 69.1 ± 9.8 | 17.9 ± 4.5 | 16.9 ± 8.3 | 2,109 ± 279 | 28.2 ± 7.6 | 8.0 ± 6.3 | 17.5 ± 6.0 |
| Tr 15.02 | 54.8 ± 9.0 | 21.7 ± 5.6 | 3.9 ± 3.6 | 1,024 ± 214 | 29.0 ± 10.4 | 1.2 ± 2.4 | 10.3 ± 3.9 |
| Tr 16 | 83.5 ± 8.1 | 24.1 ± 7.4 | 18.2 ± 8.6 | 2,312 ± 353 | 88.1 ± 8.1 | 35.9 ± 13.8 | 13.2 ± 5.1 |
| Tr 17 (sliver) | 82.2 ± 15.8 | 28.6 ± 18.1 | 55.4 ± 12.3 | 325 ± 76 | 98.2 ± 2.4 | 45.8 ± 4.7 | 31.8 ± 10.1 |
| Tr 22.01 | 90.1 ± 6.2 | 30.2 ± 7.9 | 19.5 ± 8.1 | 1,019 ± 133 | 58.2 ± 10.0 | 10.8 ± 7.3 | 14.0 ± 6.1 |
| Tr 22.02 | 79.8 ± 9.5 | 27.0 ± 3.7 | 18.9 ± 6.0 | 1,700 ± 331 | 81.2 ± 11.4 | 22.1 ± 10.3 | 14.3 ± 5.1 |
| El Paso County | 82.7 ± 0.0 | 23.1 ± 0.5 | 17.6 ± 0.7 | 299,637 ± 1,051 | 35.8 ± 0.7 | 6.4 ± 0.4 | 13.8 ± 0.3 |
| Texas | 39.7 ± 0.0 | 17.6 ± 0.1 | 6.8 ± 0.1 | 10,992,816 ± 15,813 | 37.4 ± 0.2 | 5.4 ± 0.1 | 12.3 ± 0.1 |

**Table C: housing age** (estimate ± 90% MOE)

| Geography | Housing units | % built pre-1950 | % built pre-1980 | Median yr built |
|---|---|---|---|---|
| ZCTA 79902 | 9,650 ± 659 | 43.7 ± 5.6 | 85.9 ± 6.1 | 1954 ± 3 |
| Tr 11.11 (sliver) | 3,059 ± 311 | 4.0 ± 3.7 | 38.0 ± 10.6 | 1985 ± 3 |
| Tr 11.15 | 2,123 ± 238 | 2.7 ± 2.9 | 34.4 ± 12.0 | 1990 ± 9 |
| Tr 14 | 1,160 ± 153 | 12.8 ± 8.3 | 76.8 ± 17.0 | 1974 ± 3 |
| Tr 15.01 | 2,335 ± 249 | 15.0 ± 7.7 | 83.3 ± 15.7 | 1964 ± 5 |
| Tr 15.02 | 1,151 ± 184 | 65.6 ± 14.6 | 93.0 ± 14.1 | 1939 or earlier* |
| Tr 16 | 2,492 ± 351 | 52.1 ± 15.6 | 91.9 ± 16.3 | 1949 ± 5 |
| Tr 17 (sliver) | 419 ± 85 | 68.7 ± 12.6 | 89.5 ± 12.1 | 1939 or earlier* |
| Tr 22.01 | 1,204 ± 93 | 30.6 ± 9.3 | 84.5 ± 17.0 | 1962 ± 5 |
| Tr 22.02 | 2,208 ± 331 | 70.1 ± 12.0 | 82.0 ± 11.5 | 1939 or earlier* |
| El Paso County | 323,571 ± 169 | 7.0 ± 0.4 | 38.9 ± 0.9 | 1988 ± 1 |
| Texas | 12,128,515 ± 1,574 | 5.8 ± 0.1 | 33.2 ± 0.1 | 1992 ± 1 |

\* For tracts 15.02, 17 and 22.02 the median falls in the open-ended "Built 1939 or earlier" category. The summary file stores the estimate as 1938, and the MOE annotation code -333333333 means the median is in the lowest interval. Report it as "1939 or earlier".

**Exact definitions (table / variables). Derived percentages use the Census Bureau's ACS MOE approximation formulas: root-sum-of-squares for sums, and the proportion formula, switching to the ratio formula when the term under the radical is negative. County and state MOEs coded -555555555 (controlled estimate) were treated as 0.**
- Total population: B01003_001. Median age: B01002_001.
- % 65+: B01001 _020–_025 + _044–_049, divided by _001. % under 5: B01001 (_003 + _027) / _001.
- Median household income (2024 inflation-adjusted dollars): B19013_001.
- Poverty rate: B17001_002 / B17001_001 (population for whom poverty status is determined).
- % uninsured: B27010 (_017 + _033 + _050 + _066) / _001 (civilian noninstitutionalized population).
- % Hispanic: B03003_003 / _001. % foreign-born: B05002_013 / _001.
- % limited-English-speaking households: C16002 (_004 + _007 + _010 + _013) / _001.
- % renter-occupied: B25003_003 / _001. % households with no vehicle: B25044 (_003 owner + _010 renter) / _001.
- % built before 1950: B25034 (_010 + _011) / _001. % built before 1980: B25034 (_007…_011) / _001. Median year built: B25035_001.
- Disability rate: B18101, sum of the 12 "With a disability" cells (_004, _007, _010, _013, _016, _019, _023, _026, _029, _032, _035, _038), divided by _001 (civilian noninstitutionalized population).

**Corrections to the earlier snippet-based notes:**
- The Census Reporter figures in the earlier notes **match ACS 2020-2024 exactly**: population 19,031 (±1,433), median age 40 (±2.2), poverty 22.5% (±4.0), median household income $50,873 (±7,890), foreign-born 24.4% (±2.9), households 8,494 (±660). So those were ACS 2020-2024 values, and they are now **[PV]**. — [ACS SF 2024](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/)
- The Simplemaps figure of "$38,274 (2021)" for median household income is **not** the current estimate. Disregard it, since it is an older vintage.
- Pre-1950 housing in 79902 is **43.7%**, against **7.0%** for El Paso County and **5.8%** for Texas. Median year built is 1954 for 79902, 1988 for the county and 1992 for Texas. **[PV]**

### Inferences
- **College-student artifact:** Tracts 11.15 and 14 border UTEP. Both have median age around 30, renter shares of 88-89%, and few people aged 65+, which is consistent with student housing. Treat their poverty and income figures with caution.
- **Tract 17:** population about 1,018 (±161), poverty 66.7% (±21.7), 98% renters, 45.8% with no vehicle, 31.8% with a disability. It may include group-quarters or supportive housing downtown. Only about 0.9% of 79902's land lies in it, so do not attribute these figures to 79902 as a whole.
- **Tract 16 (Sunset Heights):** 35.9% of households have no vehicle, 88% rent, median household income is $25.9k (±15.4k) and 52% of homes were built before 1950. These are strong heat-exposure risk markers: old uninsulated stock, no car to reach cooling centers, and renters who have limited ability to install AC.
- Many tract MOEs are large; some exceed half the estimate, as with tract 17's under-5 share and tract 16's income. Compare tracts only where the intervals do not overlap.
- ACS does not measure air conditioning. Treat that as a gap and use a proxy.

### Gaps
- Some indicators on the original wish list were not pulled: limited-English *persons* (rather than households), and S-table versions such as S2701 and S1810. The B and C detailed tables above are the underlying data for those S-tables.
- I did not produce a separate 2019-2023 vintage. 2020-2024 was available, so it was not needed.

## CDC/ATSDR SVI 2022 overall percentile (RPL_THEMES) for the 79902 tracts

### Takeaway
SVI 2022 was downloaded from svi.cdc.gov in both versions: the Texas file, which ranks tracts within Texas, and the US file, which ranks them nationally. Six of the nine tracts are in the top quintile nationally (≥0.80): 11.15, 14, 16, 17, 22.01 and 22.02. Tract 15.02 is the least vulnerable, at 0.49 nationally and 0.38 within Texas.

### Cited Findings
- SVI 2022 is built from ACS 2018-2022 data. Columns: RPL_THEMES is the overall percentile. Themes are 1 socioeconomic, 2 household characteristics, 3 racial and ethnic minority status, and 4 housing type and transportation. **[PV]** — [SVI 2022 US tract CSV](https://svi.cdc.gov/Documents/Data/2022/csv/states/SVI_2022_US.csv); [SVI 2022 Texas tract CSV](https://svi.cdc.gov/Documents/Data/2022/csv/states/Texas.csv)

| GEOID | Tract | RPL_THEMES (US) | RPL_THEMES (TX) | Theme 1 US | Theme 2 US | Theme 3 US | Theme 4 US |
|---|---|---|---|---|---|---|---|
| 48141001111 | 11.11 (sliver) | 0.5229 | 0.4123 | 0.7464 | 0.0659 | 0.8555 | 0.4337 |
| 48141001115 | 11.15 | 0.8502 | 0.8050 | 0.9365 | 0.7416 | 0.9082 | 0.4851 |
| 48141001400 | 14 | 0.9337 | 0.8823 | 0.9948 | 0.2977 | 0.9176 | 0.9138 |
| 48141001501 | 15.01 | 0.6436 | 0.4799 | 0.6553 | 0.7972 | 0.8268 | 0.2836 |
| 48141001502 | 15.02 | 0.4942 | 0.3772 | 0.4198 | 0.4119 | 0.7242 | 0.5190 |
| 48141001600 | 16 | 0.9843 | 0.9461 | 0.9811 | 0.8800 | 0.9432 | 0.9343 |
| 48141001700 | 17 (sliver) | 0.9718 | 0.9669 | 0.9891 | 0.4709 | 0.8991 | 0.9844 |
| 48141002201 | 22.01 | 0.9874 | 0.9564 | 0.9609 | 0.9382 | 0.9169 | 0.9521 |
| 48141002202 | 22.02 | 0.9874 | 0.9739 | 0.9963 | 0.9877 | 0.8926 | 0.7435 |

### Inferences
- Within the core of 79902, tracts 16, 22.01 and 22.02 are at the 98th-99th percentile nationally. Those are among the most socially vulnerable tracts in the US. Kern Place / Rim (15.02) and the hillside tract 15.01 sit near or below the middle.

### Gaps
- SVI 2022 uses ACS 2018-2022 data, so it lags the ACS 2020-2024 profile above. No ZCTA-level SVI exists.

## Mapping tracts to neighborhoods (Kern Place, Sunset Heights, Mission Hills, Rim-University/UTEP, downtown edge)

### Takeaway
The Census Geocoder (2020 tracts) places these landmark addresses: **UTEP (500 W University Ave) and 1505 Rim Rd in 15.02**; **807 Kern Dr in 15.01**, near the 15.01/15.02 line; **Sunset Heights (715 Upson Dr, 1000 W Yandell Dr) in 16**; **El Paso High (800 E Schuster Ave) in 22.01**; **1211 Montana Ave in 22.02**; **downtown San Jacinto Plaza (114 W Mills Ave, ZIP 79901) in 17**; **4301 N Mesa St in 11.15**. Mission Hills could not be pinned to a tract from a primary source.

### Cited Findings
- Geocoder results (benchmark Public_AR_Current, vintage Census2020_Current, layer Census Tracts). **[PV]** — [Census Geocoder API](https://geocoding.geo.census.gov/geocoder/geographies/onelineaddress?address=500%20W%20University%20Ave%2C%20El%20Paso%2C%20TX%2079968&benchmark=Public_AR_Current&vintage=Census2020_Current&layers=Census%20Tracts&format=json)
  - 500 W University Ave (UTEP), matched as ZIP 79902 → 48141001502
  - 1505 Rim Rd → 48141001502; 3000 N Stanton St → 48141001502
  - 807 Kern Dr → **48141001501**. This contradicts the earlier secondary claim (ClustrMaps) that 807 Kern Dr is in 001502. Kern Place probably straddles 15.01 and 15.02.
  - 715 Upson Dr and 1000 W Yandell Dr (Sunset Heights) → 48141001600
  - 800 E Schuster Ave (El Paso High School) → 48141002201
  - 1211 Montana Ave → 48141002202
  - 114 W Mills Ave (San Jacinto Plaza, ZIP 79901) → 48141001700
  - 4301 N Mesa St (79902) → 48141001115; 5000 N Mesa St (79912) → 48141001111
- Tract bounding boxes from TIGERweb (Census 2020 tracts layer, WGS84): 15.02 spans lon -106.510 to -106.486 and lat 31.765 to 31.788; 16 spans -106.508 to -106.489 and 31.758 to 31.771; 17 spans -106.495 to -106.479 and 31.754 to 31.767; 22.01 spans -106.497 to -106.469 and 31.770 to 31.792; 22.02 spans -106.494 to -106.473 and 31.765 to 31.776; 15.01 spans -106.511 to -106.479 and 31.782 to 31.806. **[PV]** — [TIGERweb tigerWMS_Census2020 MapServer layer 6](https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_Census2020/MapServer/6)

### Inferences (neighborhood labels are informal; not a primary crosswalk)
- **15.02**: Rim Road / Kern Place south side, plus UTEP's campus. Note that UTEP has its own ZIP, 79968, but its campus land lies in tract 15.02 and the geocoder matched the address to ZIP 79902.
- **15.01**: northern Kern Place and the hillside up to the Franklin Mountains (Scenic Dr area). Older, owner-occupied (72% owners), with the highest income in the ZCTA after 15.02.
- **16**: Sunset Heights.
- **17**: downtown edge (sliver).
- **22.01**: area around El Paso High / Mesa–Stanton north of downtown, extending east. **Mission Hills is probably 22.01 and/or 15.01, but this is unverified.**
- **22.02**: the Montana Ave / Golden Hill-type area just north of downtown.
- **11.15 and 14**: the UTEP-adjacent N Mesa / west-side corridor and I-10 / river corridor, mostly outside 79902.

### Gaps
- No official City of El Paso neighborhood-to-tract crosswalk was retrieved. Mission Hills and Manhattan Heights boundaries were not verified against a primary map.

# Census Tracts and Demographics of ZCTA 79902 (El Paso, TX)

> **Important data-access caveat (read first):** In this research session, the network egress proxy blocked every primary Census data host: api.census.gov, www2.census.gov (relationship files), data.census.gov, tigerweb/geocoding.geo.census.gov, plus censusreporter.org, datacommons.org, CDC/ATSDR SVI (svi.cdc.gov, data.cdc.gov), City of El Paso GIS (gis.elpasotexas.gov), NHGIS, and MCDC. Neither the ZCTA-to-tract relationship file nor any ACS API table could be downloaded. The only figures below come from **search-engine excerpts** of secondary pages, mainly Census Reporter, which repackages ACS 5-year data. These are noted as such. Treat every number here as provisional until someone checks it against the primary URLs listed under "Gaps". Nothing below was invented. Anything not found is listed as a gap.

## Which 2020 census tracts (El Paso County FIPS 48141) overlap ZCTA 79902, and what share of each lies in it?

### Takeaway
I could not get the authoritative tract list. The Census 2020 ZCTA-to-tract relationship file was blocked. One tract is confirmed by secondary sources: **Census Tract 15.02 (GEOID 48141001502)**, which covers Kern Place / Rim Road. The other tracts and the area shares are still unknown.

### Cited Findings
- Properties in Kern Place are assigned to census tract 001502, i.e., GEOID 48141001502. This comes from a search excerpt of a property-records page, so it is secondary. — [Kern Place (Wikipedia/search excerpt)](https://en.wikipedia.org/wiki/Kern_Place); [807 Kern Dr public record (ClustrMaps)](https://clustrmaps.com/a/1gg1p4/)
- A listing for 1505 Rim Rd, El Paso, TX 79902 gives "Census Tract Code 1502". — [Dave Perry-Miller listing](https://www.daveperrymiller.com/realestate/details/106629914/1505-rim-road-el-paso-tx-79902)
- ZCTA 79902 lies entirely within El Paso County. — [Simplemaps 79902](https://simplemaps.com/us-zips/79902/) (search excerpt)
- The City of El Paso runs a "2020_Census_Tracts" ArcGIS FeatureServer that could be used for the overlay. It was blocked from this environment. — [City of El Paso GIS item info](https://gis.elpasotexas.gov/dev/rest/services/planning/2020_Census_Tracts/FeatureServer/info/iteminfo)
- Authoritative source, not retrievable here: https://www2.census.gov/geo/docs/maps-data/data/rel2020/zcta520/tab20_zcta520_tract20_natl.txt (filter `GEOID_ZCTA5_20 == 79902`. Use `AREALAND_PART / AREALAND_TRACT_20` for the share of each tract that falls in the ZCTA.)

### Inferences
- 79902 is a central/west-central El Paso ZCTA of about 19,000 people. Tracts typically hold about 2,500 to 5,000 people, so it most likely contains or touches roughly 5 to 10 tracts, some of them only slivers. This is an estimate, not a finding.
- Other tracts very likely include those around UTEP, Sunset Heights, Mission Hills, and the edge of downtown. 2020 El Paso tract numbers in the teens (e.g., 15.01/15.02 and neighbors) are plausible, but **none apart from 15.02 could be verified**. The report should not list any others without checking the relationship file.

### Gaps
- Full list of overlapping tract GEOIDs and their AREALAND_PART shares. Download the relationship file above, or use the Census Geocoder / TIGERweb, from an environment with access to census.gov.
- Population-weighted shares. These need the 2020 block-to-ZCTA assignment or block populations (PL 94-171). Not obtained.

## Key ACS indicators for ZCTA 79902 and each tract

### Takeaway
Only a handful of ZCTA-level values surfaced, through Census Reporter excerpts with an unconfirmed ACS vintage: about 19,000 people, median age about 40, poverty about 22.5%, median household income about $50.9k, foreign-born about 24.4%. I found no tract-level values. Most requested indicators (65+, under 5, uninsured, Hispanic, limited English, renters, no vehicle, housing age, disability, AC) are still gaps.

### Cited Findings (ZCTA 79902)
- Total population **19,031**, density about 2,915 per sq mi. Simplemaps, which generally uses ACS 5-year data; vintage not stated in the excerpt. — [Simplemaps 79902](https://simplemaps.com/us-zips/79902/)
- Median age **40 ± 2.2 years**. — [Census Reporter 79902 profile](https://censusreporter.org/profiles/86000US79902-79902/) (search excerpt; Census Reporter normally shows the latest ACS 5-year, likely 2019-2023 or 2020-2024, but this was not confirmed)
- Persons below poverty: **22.5% ± 4%** (3,983 ± 777 persons). — [Census Reporter 79902 profile](https://censusreporter.org/profiles/86000US79902-79902/)
- Median household income **$50,873 ± $7,890**. The MOE is about ±15.5%, which is large. — [Census Reporter 79902 profile](https://censusreporter.org/profiles/86000US79902-79902/)
  - Conflicting figure: **$38,274 (labeled 2021)**. — [Simplemaps 79902](https://simplemaps.com/us-zips/79902/) (search excerpt). The gap probably reflects different vintages (an older ACS vs. a newer one) and income growth plus inflation. It needs confirmation against ACS table B19013 / DP03_0062E.
- Foreign-born: **24.4% ± 2.9%** (4,645 ± 659 persons). — [Census Reporter 79902 profile](https://censusreporter.org/profiles/86000US79902-79902/)
- Households: **8,494** (search-engine summary; source page and vintage unclear). — [Point2Homes / search summary](https://www.point2homes.com/US/Neighborhood/TX/El-Paso-Demographics.html). Low confidence.
- City-wide context only, not 79902: El Paso's median year built is 1984. About 4.7% of homes were built before 1940 and another 3.4% in 1940-1949. — [Point2Homes El Paso](https://www.point2homes.com/US/Neighborhood/TX/El-Paso-Demographics.html) (search excerpt)

### Cited Findings (tracts)
- None obtained. All tract-level ACS values are gaps.

### Inferences
- The poverty rate (~22.5%) is well above the U.S. rate, and the population is older (median ~40), which matters for heat vulnerability. Large MOEs at ZCTA scale mean tract-level figures will be noisier still.
- 79902 includes some of El Paso's oldest neighborhoods (Sunset Heights, early 1900s, and Kern Place, platted in the 1910s). So the share of housing built before 1950/1980 is very likely far higher than the city-wide 8%. **This is not quantified** and needs B25034 / DP04_0017P-DP04_0026P.
- The UTEP student population probably inflates the renter share and possibly the poverty rate in the UTEP-area tract(s). This is a common ACS artifact for college tracts and should be noted when the profile is interpreted.

### Gaps (with exact tables/variables to pull; ACS 5-year 2020-2024 should be the latest as of Oct 2026, otherwise 2019-2023)
Not retrieved: api.census.gov was blocked. Suggested calls (no key needed for small queries):
- ZCTA profile: `https://api.census.gov/data/2024/acs/acs5/profile?get=NAME,DP05_0001E,DP05_0018E,DP05_0024PE,DP05_0005PE,DP03_0062E,DP03_0099PE,DP02_0094PE,DP02_0115PE,DP04_0047PE,DP04_0058PE,DP04_0017PE,...&for=zip%20code%20tabulation%20area:79902`. Verify variable numbers against `/variables.json` because DP numbering shifts between years. Note that ZCTA queries no longer nest within state.
- Tracts: same call with `&for=tract:001502,...&in=state:48%20county:141`.
- Total population (DP05_0001), median age (DP05_0018), % 65+ (DP05_0024P), % under 5 (DP05_0005P). Values needed; none found except ZCTA median age.
- % Hispanic (DP05 "Hispanic or Latino (of any race)" percent, ~DP05_0076P/0073P depending on year). Not found.
- Limited English: % speaking English less than "very well" (DP02_0115P area; or S1601), plus limited-English-speaking households (S1602). Not found. Foreign-born is above.
- Uninsured (DP03_0099P / S2701). Not found.
- Poverty (S1701_C03_001). ZCTA value above; tracts not found.
- % renter-occupied (DP04_0047P). Not found.
- % households with no vehicle (DP04_0058P). Not found.
- Year built distribution (B25034 / DP04_0017P-0026P) and median year built (B25035). Not found.
- Disability (S1810 / DP02_0072P). Not found.
- % without air conditioning: **ACS does not collect this.** AC availability exists only in the American Housing Survey (metro level, and El Paso is not a separately published AHS metro) or modeled products. Plan on a gap or proxy.
- CDC/ATSDR SVI 2022 tract percentiles (RPL_THEMES etc.) for 48141001502 and the other tracts. svi.cdc.gov / ATSDR were blocked, so not obtained.

## Neighborhoods covered by ZIP 79902

### Takeaway
Secondary real-estate and neighborhood sources confirm that Sunset Heights, Kern Place, Mission Hills, and Rim-University (the UTEP area) are in 79902. Manhattan Heights is **not** confirmed: it is generally associated with 79903, though that was not verified here.

### Cited Findings
- 79902 is described as El Paso's "institutional and cultural core", anchored by UTEP, the museum district, and historic neighborhoods such as Kern Place and Sunset Heights. — [Texas Ally 79902](https://www.texasally.com/neighborhoods/el-paso/el-paso/79902)
- Sunset Heights is in ZIP 79902 and lies near UTEP and downtown. — [Texas Ally Sunset Heights](https://www.texasally.com/neighborhoods/el-paso/el-paso/sunset-heights-homes-2); [Homes.com Sunset Heights guide](https://www.homes.com/local-guide/el-paso-tx/sunset-heights-neighborhood/)
- Mission Hills is in ZIP 79902. — [City-Data Mission Hills](https://www.city-data.com/neighborhood/Mission-Hills-El-Paso-TX.html); [Texas Ally Mission Hills](https://www.texasally.com/neighborhoods/el-paso/el-paso/mission-hills-homes-3)
- Rim-University neighborhood is covered by ZIP 79902. — [ZipDataMaps Rim-University](https://www.zipdatamaps.com/neighborhood/texas/el-paso/rim-university)
- Kern Place is next to UTEP's campus, east of UTEP and north of downtown, and falls in tract 15.02. — [Kern Place (Wikipedia)](https://en.wikipedia.org/wiki/Kern_Place); [Homes.com Kern Place](https://www.homes.com/local-guide/el-paso-tx/kern-place-neighborhood/)
- Texas Ally also lists other named areas in 79902: Angel's Triangle, Arlington Park, Collingsworth, the Downtown Historic District (part), and Stone Ridge. This is a real-estate source and its neighborhood boundaries are informal. — [Texas Ally 79902](https://www.texasally.com/neighborhoods/el-paso/el-paso/79902)
- NeighborhoodScout lists an "El Paso High" neighborhood in 79902, the area around El Paso High School and Sunset Heights / Upper Mesa. — [NeighborhoodScout El Paso High](https://www.neighborhoodscout.com/tx/el-paso/el-paso-high)

### Inferences
- The ZCTA runs from the southern Franklin Mountains foothills (Rim Rd / Kern Place / Mission Hills) down through UTEP and Sunset Heights to the western edge of downtown. That is a mix of affluent hillside housing, student housing, and older, lower-income historic housing stock. Tract-level heterogeneity is likely to be large, so ZCTA averages will hide pockets of high vulnerability.

### Gaps
- Manhattan Heights: not confirmed in 79902. Verify against a ZIP boundary map. It is commonly placed in 79903.
- Official City of El Paso neighborhood boundaries and the tract-to-neighborhood crosswalk were not retrievable (city GIS blocked).

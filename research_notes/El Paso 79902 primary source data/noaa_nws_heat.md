# NOAA 2020 El Paso Urban Heat Island Mapping, NWS El Paso Heat Products, ELP Climate Records and Heat Deaths: primary-source verification for ZIP 79902

Research date: 2026-10-01. **Verification labels:**
- **[PRIMARY-VERIFIED]**: pulled directly from a NOAA, NWS, IEM, ACIS or UTEP server in this session. Where values are computed, the method is stated.
- **[SECONDARY]**: from news or other non-primary reporting, read in full text this session unless noted otherwise.

All computations were done by this researcher from raw primary data, and the scripts are reproducible from the URLs given. **Still blocked this session:** heat.gov, cpo.noaa.gov/nihhis (CloudFront 403), insideclimatenews.org (403), and the DSHS heat pages (404).

---

## 1. NOAA/NIHHIS–CAPA 2020 El Paso Heat Watch campaign: date, scale, temperature ranges, and what the maps show for 79902

### Takeaway
The campaign date is **July 10, 2020**, confirmed by the raster file names and timestamps on NOAA's own image services.
- The morning traverse ran 06:00–07:00 MDT, the afternoon 15:00–16:00 MDT and the evening 19:00–20:00 MDT.
- NWS El Paso had an **Excessive Heat Warning** in effect for central El Paso that day, and ELP hit 109°F.

From the NOAA/CAPA modeled air-temperature rasters:
- **Citywide spread:** about 74–86°F in the morning (about 12°F), about 100–106°F in the afternoon (about 6°F), and about 92–105°F in the evening (about 13°F).
- **79902 overall:** close to the citywide median in every period. Its mean was 83.3°F in the morning, 104.4°F in the afternoon and 103.4°F in the evening.
- **Within 79902** there is a clear internal gradient:
  - The Rim Road / Scenic Drive foothills are the coolest part, about 80°F in the morning and about 102°F in the evening.
  - Sunset Heights, the edge of downtown, and the Mission Hills / Mesa St. corridor run hottest, about 105°F in the afternoon and about 104–105°F in the evening.
- **Coverage gaps:** the downtown core (San Jacinto Plaza) and the airport were **outside the mapped footprint** and have no data.

### Cited Findings
**Date, timing and partners**
- NOAA's ArcGIS image services name the El Paso rasters `HINDX.morning.20200710.El_Paso.float`, `HINDX.afternoon.20200710.El_Paso.float` and `HINDX.evening.20200710.El_Paso.float`. The catalog start/end times convert to 2020-07-10 06:00–07:00 MDT (morning), 15:00–16:00 MDT (afternoon) and 19:00–20:00 MDT (evening). Units are °F. Sensors are tagged "Car-Mounted Weather Gauge" and the source is "NOAA/CAPA Strategies". **[PRIMARY-VERIFIED]**
  - Services: [Morning](https://gis.nnvl.noaa.gov/arcgis/rest/services/HINDZ/Morning_Air_Temperature_in_Cities/ImageServer), [Afternoon](https://gis.nnvl.noaa.gov/arcgis/rest/services/HINDZ/Afternoon_Air_Temperature_in_Cities/ImageServer), [Evening](https://gis.nnvl.noaa.gov/arcgis/rest/services/HINDZ/Evening_Air_Temperature_in_Cities/ImageServer)
  - ArcGIS items: [El Paso Morning](https://www.arcgis.com/home/item.html?id=80ffd96d6ca744c4a66c6db2dbd4d4b1), [Afternoon](https://www.arcgis.com/home/item.html?id=83e8009738f641e083bd7a01555549eb), [Evening](https://www.arcgis.com/home/item.html?id=2983321f9dcb48ebb7c2e2fedacc2d29) (owner tiffany.small_noaa)
- UTEP SEGA Lab (Dr. Chakraborty) says volunteers drove "designated routes and collect[ed] temperature/humidity measurements over three one-hour periods on July 10, 2020." The partners it names are the City of El Paso Community & Human Development and Public Health Departments, NWS El Paso and Border 2020. **[PRIMARY-VERIFIED, UTEP]** — [UTEP SEGA Lab](https://www.utep.edu/liberalarts/sega/environmental-injustice-hurricane-harvey-in-greater-houston12.html)
- **Resolving July 10 vs July 11:** the CAPA web post is dated "July 11, 2020" and says "The city of El Paso took advantage of **Friday's** extreme heat." July 10, 2020 was a Friday, so July 11 is the post date, not the traverse date. The city's sustainability coordinator is quoted: "We actually selected this day on conjunction with the National Weather Service in El Paso." **[PRIMARY-VERIFIED, CAPA page read in full]** — [CAPA Strategies](https://www.capastrategies.com/city-of-el-paso-maps-hottest-places-in-region)

**Conditions on the campaign day**
- NWS El Paso issued an Excessive Heat Warning for TXZ418/TXZ419 at 5:09 AM MDT Friday, July 10, 2020. It ran from 6 AM that day to 6 AM Sunday, and said "temperatures reaching or exceeding 110". The text upgraded the existing Heat Advisory. The zone header lists "Downtown El Paso, West El Paso, Upper Valley…". **[PRIMARY-VERIFIED]** — [IEM NWS text 202007101109-KEPZ-WWUS74-NPWEPZ](https://mesonet.agron.iastate.edu/api/1/nwstext/202007101109-KEPZ-WWUS74-NPWEPZ)
- ELP (threaded El Paso record) observed a high of **109°F and a low of 83°F** on 2020-07-10, and 108°F / 82°F on July 11. **[PRIMARY-VERIFIED]** — [RCC-ACIS StnData, sid ELPthr](https://data.rcc-acis.org/StnData)

**Campaign-wide context**
- CAPA's Sept. 1, 2020 post says the 2020 cohort "engaged over 600 volunteers … gathering over a million unique measurements," and that all cities finished by mid-August. **[PRIMARY-VERIFIED, CAPA]** — [CAPA Strategies page (same page, "Sensor Data to Heat Maps" post)](https://www.capastrategies.com/city-of-el-paso-maps-hottest-places-in-region)
- The El Paso-specific "41 volunteers / 66,000+ readings / 105 sq mi" figures could **not** be re-verified from a primary NOAA or CAPA document this session. They remain **[SECONDARY]**, sourced to the City of El Paso climate page and earlier snippets. — [City of El Paso Climate & Sustainability](https://www.elpasotexas.gov/strategic-and-legislative-affairs/climate-action)
- The raster catalog footprint polygon for El Paso covers about 0.139 sq-degree. At 31.8°N that is about 600 sq mi of **bounding raster area** (centroid -106.40, 31.80). This is the extent of the modeled raster, not the traversed study area, so it cannot confirm "100 vs 105 sq mi". **[PRIMARY-VERIFIED, raster metadata]**

**Citywide temperature ranges**
Method: grid of 1,208 valid samples at about 500 m spacing across the El Paso raster, using the ImageServer `getSamples` endpoint locked to the El Paso raster, °F. **[PRIMARY-VERIFIED data; statistics computed by researcher]**

| Period (MDT) | Min | 10th pct | Median | Mean | 90th pct | Max | Spread |
|---|---|---|---|---|---|---|---|
| Morning 06–07 | 74.3 | 79.1 | 83.2 | 82.5 | 84.2 | 85.5 | ~11°F |
| Afternoon 15–16 | 100.2 | 103.5 | 104.5 | 104.3 | 105.1 | 106.4 | ~6°F |
| Evening 19–20 | 92.0 | 102.4 | 103.6 | 103.3 | 104.3 | 105.4 | ~13°F |

A separate `computeStatisticsHistograms` call over the full raster footprint gave a morning range of 73.1–86.4°F (mean 82.4), which agrees with the grid.

- **Coolest areas citywide:**
  - **Afternoon and evening:** the **Upper Valley / Rio Grande corridor** in the far northwest, near -106.59, 31.83–31.84. It read 100.2°F in the afternoon and as low as 92.0°F in the evening, which suggests irrigated farmland and orchards cooling fast after sunset.
  - **Morning:** the **far east / southeast edge** of the raster, near -106.22, 31.76–31.77, at about 74.3°F.
- **Hottest areas citywide:**
  - **Afternoon:** about 106.1–106.4°F at points on the **west side near -106.57, 31.86** (around the I-10 / Redd Rd–Resler corridor) and **east-central near -106.33, 31.74**.
  - **Evening:** about 105.2–105.4°F at **-106.53, 31.82** (west side, north of 79902) and **east El Paso near -106.38/-106.39** (around 31.74 and 31.79).

  *Street-level place names are researcher interpretation of coordinates.*

**What the maps show for 79902**
- ZIP boundary: Census TIGERweb ZCTA5 79902 polygon, bbox -106.523 to -106.473, 31.759 to 31.809. **[PRIMARY-VERIFIED]** — [TIGERweb ZCTA query](https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/PUMA_TAD_TAZ_UGA_ZCTA/MapServer/1/query?where=ZCTA5%3D%2779902%27&outFields=ZCTA5&outSR=4326&f=geojson)
- 523 of 720 grid points (about 150 m spacing) inside the ZCTA had data. The **downtown core and parts of the Franklin Mountains slopes returned NoData**, meaning they were outside the modeled area. **[PRIMARY-VERIFIED; computed]**

**79902 summary statistics, °F** **[PRIMARY-VERIFIED data; computed]**

| Period | Min | 10th pct | Median | Mean | 90th pct | Max |
|---|---|---|---|---|---|---|
| Morning | 79.7 | 82.0 | 83.5 | 83.3 | 84.3 | 85.6 |
| Afternoon | 102.7 | 103.7 | 104.4 | 104.4 | 105.0 | 106.1 |
| Evening | 101.1 | 102.6 | 103.4 | 103.4 | 104.1 | 104.9 |

**Neighborhood point values**
Method: mean of a 3×3 sample block about 150 m across, same rasters, °F. Neighborhood coordinates were chosen by the researcher. **[PRIMARY-VERIFIED data; computed]**

| Location (approx. coords) | Morning | Afternoon | Evening |
|---|---|---|---|
| Kern Place core (-106.5048, 31.7745) | 83.8 | 103.8 | 103.1 |
| Kern Place lower / Stanton (-106.5000, 31.7720) | 83.8 | 104.1 | 103.4 |
| UTEP campus center (-106.5070, 31.7703) | 84.2 | 104.0 | 103.7 |
| Rim Rd / Scenic Dr foothill (-106.4985, 31.7826) | **80.3** | 103.3 | **102.1** |
| Mission Hills (-106.4950, 31.7880) | 82.7 | **104.9** | 104.1 |
| Sunset Heights, Upson Dr (-106.4935, 31.7640) | 84.3 | **104.9** | 103.8 |
| Sunset Heights east, Yandell/Stanton (-106.4880, 31.7650) | 84.2 | 104.8 | **104.4** |
| Manhattan Heights edge (-106.4780, 31.7800) | 83.9 | 103.3 | 103.3 |
| Downtown, San Jacinto Plaza (-106.4875, 31.7590) | NoData | NoData | NoData |
| ELP airport (-106.3776, 31.8073) | NoData | NoData | NoData |

- **79902 internal extremes:**
  - **Coolest:** in the morning, 79.7–80.0°F around -106.498/-106.499 between 31.777 and 31.783 (the Rim Rd / Scenic Dr / Murchison Park foothill band). In the evening, 101.1°F at the same band.
  - **Hottest:** in the morning, 85.2–85.6°F at the lower UTEP / I-10 / Mesa area (-106.505 to -106.510, 31.765–31.771). In the afternoon, 106.1°F at the east edge (-106.4736, 31.7755). In the evening, 104.9°F near northern Sunset Heights / downtown edge (-106.4856, 31.765) and along the Mesa St. corridor (-106.511, 31.797). **[PRIMARY-VERIFIED data; computed]**
- **Earlier qualitative claim, still [SECONDARY]:** "the majority of the heat map is in yellow and red … areas closer to natural landscapes are cooler." It cited the upper east side and Lower Valley as cooler. — [KTSM](https://www.ktsm.com/news/hottest-areas-of-el-paso-how-water-company-prepares-for-drought-conditions/). The primary rasters partly support it: the coolest spots are the irrigated Upper Valley and the eastern edge. The rasters were not checked against the specific "upper east side" claim.

### Inferences
- **79902 is not one of El Paso's hottest pockets.** On the campaign day its mean sat within about 0.1–1°F of the citywide median in every period. The ZIP's real story is an **internal gradient of about 4–6°F in morning and evening**: foothills are cooler; Sunset Heights, the downtown edge and Mesa corridor are hotter.
- The foothill advantage is largest **at night and early morning** (about 3–4°F cooler than Sunset Heights at 6–7 AM), which fits cold-air drainage off the Franklin Mountains. It nearly disappears in the afternoon (about 1.5°F).
- **Evening temperatures stayed at about 101–105°F at 7–8 PM across almost all of 79902**, and the ELP low that night was 83°F. Overnight relief was minimal on this Excessive Heat Warning day.
- Because downtown proper was unmapped, statements like "downtown is the hottest part of 79902" **cannot be supported** from these data. The hottest mapped 79902 cells are at its fringes.
- CAPA rasters are statistical models trained on traverse points from a single day. Absolute values describe July 10, 2020 only. The relative pattern is the durable finding.

### Gaps
- The CAPA El Paso final report PDF and the heat.gov campaign page could not be retrieved (heat.gov and cpo.noaa.gov return CloudFront 403 from this environment). The El Paso volunteer and reading counts (41 / 66,000+) and study area (100 vs 105 sq mi) remain unverified against a primary document.
- Raw traverse-point data (individual car readings) were not located. Only the modeled rasters were sampled.
- Heat-index rasters exist (VizLab_noaa "Morning/Afternoon/Evening Heat Index in Cities" image services, e.g. [item a65b708…](https://www.arcgis.com/home/item.html?id=a65b70804bf64db5ae18cbbbd5eee2b1)) but were not sampled.

---

## 2. NWS El Paso (EPZ) heat products for central El Paso: criteria and issuance history 2020–2026

### Takeaway
ZIP 79902 lies in NWS public zone **TXZ418 "Western El Paso County"**. Its products list "Downtown El Paso, West El Paso, Upper Valley." The IEM VTEC archive gives these TXZ418 counts:

| Year | Heat Advisory events | Excessive Heat Warnings | Excessive Heat Watches | Days with daytime heat products |
|---|---|---|---|---|
| 2020 | 9 | 1 | 0 | ~17 |
| 2021 | 2 | 0 | 0 | ~6 |
| 2022 | 3 | 0 | 0 | ~6 |
| 2023 | 10 | 4 | 4 | ~39 |
| 2024 | 11 | 1 | 1 | ~20 |
| 2025 | 6 | 0 | 0 | ~13 |
| 2026 YTD | 7 | 0 | 0 | ~12 |

**No Extreme Heat Watch or Warning (XH.A/XH.W) has been issued for TXZ418 since the 2025 rename.** EPZ has not published a formal numeric criteria page; issued products cite forecast highs of about 103–108°F for advisories and about 110°F for warnings.

### Cited Findings
**Zone assignment** **[PRIMARY-VERIFIED]**
- api.weather.gov points lookups for Kern Place (31.776,-106.508), UTEP/Rim (31.770,-106.500), Sunset Heights (31.764,-106.493) and Mission Hills (31.785,-106.495) all return forecast zone **TXZ418**, county TXC141. ELP airport (31.807,-106.378) returns **TXZ419** "Eastern/Central El Paso County". — [api.weather.gov/points](https://api.weather.gov/points/31.7700,-106.5000); [zone TXZ418](https://api.weather.gov/zones/forecast/TXZ418); [zone TXZ419](https://api.weather.gov/zones/forecast/TXZ419)
- Product headers read "Western El Paso County-Eastern/Central El Paso County - Including the cities of Downtown El Paso, West El Paso, Upper Valley, East and Northeast El Paso, Socorro, and Fort Bliss". TXZ418 and TXZ419 are almost always issued together. — [IEM text 202307080140-KEPZ-WWUS74-NPWEPZ](https://mesonet.agron.iastate.edu/api/1/nwstext/202307080140-KEPZ-WWUS74-NPWEPZ)

**Criteria, as stated in issued products** **[PRIMARY-VERIFIED product text]**
- **July 7, 2023:** "For the Heat Advisory, temperatures of 105 to 108 degrees. For the Excessive Heat Warning, dangerously hot conditions with temperatures near 110 degrees possible." — [IEM 202307080140](https://mesonet.agron.iastate.edu/api/1/nwstext/202307080140-KEPZ-WWUS74-NPWEPZ)
- **July 10, 2020:** the EH.W cited "temperatures reaching or exceeding 110". — [IEM 202007101109](https://mesonet.agron.iastate.edu/api/1/nwstext/202007101109-KEPZ-WWUS74-NPWEPZ)
- **July 28, 2026 (HT.Y #7):** "Hot temperatures 103 to 107 degrees expected … Hot temperatures may cause heat illnesses." This shows the post-2025, HeatRisk-era advisory threshold reaching down to 103°F. — [IEM 202607290334](https://mesonet.agron.iastate.edu/api/1/nwstext/202607290334-KEPZ-WWUS74-NPWEPZ)
- Weather.gov/epz/heat and /epz/wwa_criteria return **404**. No official EPZ local-criteria page was found. The earlier "105°F high / 75°F low" rule of thumb remains **[SECONDARY]** — [AOL/El Paso Times](https://www.aol.com/articles/major-heat-risk-triggers-heat-141114000.html). The national HeatRisk-based Extreme Heat naming also remains **[SECONDARY/national]** — [NWS HeatRisk](https://www.wpc.ncep.noaa.gov/heatrisk/)

**Issuance history, TXZ418, from IEM VTEC by-WFO JSON** **[PRIMARY-VERIFIED]**
Source: `https://mesonet.agron.iastate.edu/json/vtec_events_bywfo.py?wfo=EPZ&year=YYYY`, for [2020](https://mesonet.agron.iastate.edu/json/vtec_events_bywfo.py?wfo=EPZ&year=2020) through [2026](https://mesonet.agron.iastate.edu/json/vtec_events_bywfo.py?wfo=EPZ&year=2026).
- Times are MDT (UTC−6).
- An "event" is a VTEC event ID. Some advisories were cancelled or upgraded early; these are marked "(cxl/upg)".
- "Days" counts calendar days on which a non-cancelled HT.Y/EH.W/XH.W was in effect between 10 AM and 8 PM. This is a researcher computation.

- **2020: 9 HT.Y, 1 EH.W, 0 watches; about 17 alert days, 3 of them under EH.W.**
  - HT.Y: Jun 4–6, Jun 22, Jul 8–10 (upgraded), Jul 12 (cxl/replaced), Jul 13–15, Jul 30–31, Aug 11–15, Aug 12 (cxl), Aug 21.
  - **EH.W: Jul 10 06:00 – Jul 13 06:00**, which covers the UHI campaign day.
- **2021: 2 HT.Y, about 6 days.** Jun 10–13 and Jun 19–21.
- **2022: 3 HT.Y, about 6 days.** Jun 10–14, Jul 19–20 and Jul 21.
- **2023: 10 HT.Y, 4 EH.A, 4 EH.W; about 39 alert days, 11 under EH.W.** First Jun 18, last Sep 9.
  - **EH.W:** Jun 26–27, Jul 9–13, Jul 18–21 and Aug 6–8.
  - **HT.Y:** Jun 18–21, Jun 21–26, Jun 28–Jul 1, Jul 5–9, Jul 13–18, Jul 21–22, Jul 25–28, Aug 4–6, Sep 8 and Sep 9.
- **2024: 11 HT.Y, 1 EH.A, 1 EH.W; about 20 alert days.**
  - **EH.W:** Jun 13 06:00 – Jun 15 06:00.
  - **HT.Y:** Jun 5–7, Jun 12–13, Jun 15 (two segments), Jun 15–18, Jun 19–20, Jun 24–27, Jun 28–30, Jul 4, Jul 7–8, Aug 2–3 and Aug 16–18.
  - Event #2 appears twice in the IEM output, so the count of 11 may include one re-issued segment; 10 distinct periods is also defensible.
- **2025: 6 HT.Y, 0 warnings or watches, about 13 days.** Jun 8, Jun 14–18, Jun 19, Jul 11, Aug 4–9 and Aug 9.
- **2026 (through Sep 30): 7 HT.Y on TXZ418, 0 warnings or watches, about 12 days.**
  - Jun 22, Jun 23–25, Jul 24, Jul 27–28, Jul 29–31, Aug 4 and Aug 25.
  - TXZ419 (east/central, including the airport) had **9** HT.Y in 2026. Two early-season EPZ advisories, #1 and #2, did not include TXZ418.
- **No XH.A or XH.W** (the new "Extreme Heat" codes) appear anywhere in EPZ's 2025–2026 VTEC data. **[PRIMARY-VERIFIED]**

### Inferences
- 2023 stands far above every other year: about 39 heat-alert days and 4 Excessive Heat Warnings. That is roughly double 2020 or 2024 and about six times 2021–22.
- 2026 set a record 90°F streak (Section 3) but produced only 7 advisories and no warnings for 79902's zone. This year's heat was persistent rather than extreme-peak: only 10 days reached 105°F or more, against 33 in 2023.
- The earlier note's 2024 example dates (Jun 5–6, Jun 24–26) and 2026 example (Jun 22–24) are **confirmed and expanded** by the VTEC record.

### Gaps
- No official numeric EPZ heat-product criteria page was found. Products and media imply a threshold of about 103–105°F for advisories and about 110°F for warnings.
- Day counts are approximate because the method uses a daytime window. Cancelled and replaced segments were excluded heuristically.

---

## 3. ELP climate: 100°F days, records, warmest years and the 2026 streak

### Takeaway
The ACIS threaded El Paso record **confirms** these figures:
- 70 days of 100°F or more in 2023, the record.
- 55 in 2024.
- 37 in 2025.
- **52 so far in 2026, the 6th most on record.** No 100°F day has occurred since Aug 31, so this is effectively the final count.
- A **108-day 90°F streak, Jun 6 – Sep 21, 2026**, the longest on record. It beat 106 days in 2015.

**Corrections to the earlier notes:**
- **2020 had 57 days of 100°F or more** (NWS and ACIS), not 56.
- The 108-day streak began **June 6**, not June 22. The "June 22" in the earlier notes is the start of a separate El Paso Matters statistic, "every summer day Jun 22–Sep 21 reached 90°F."

Warmest years by annual mean temperature: 2024, then 2023, then 2025. 2026 is the warmest Jan–Sep on record.

### Cited Findings
**Days at or above 100°F per year, ELP (threaded record "El Paso Area", ELPthr 9, POR 1887–)** **[PRIMARY-VERIFIED, computed from daily maxima]** — [RCC-ACIS StnData](https://data.rcc-acis.org/StnData), request `{"sid":"ELPthr","sdate":"por","edate":"2026-09-30","elems":[{"name":"maxt"},{"name":"mint"}]}`. No missing days 2015–2026.

| Year | Days at or above 100°F |
|---|---|
| 2015 | 18 |
| 2016 | 38 |
| 2017 | 23 |
| 2018 | 46 |
| 2019 | 47 |
| 2020 | **57** |
| 2021 | 20 |
| 2022 | 34 |
| 2023 | **70** |
| 2024 | **55** |
| 2025 | **37** |
| 2026 (through Sep 30) | **52** |

- **NWS cross-check:** the NWS EPZ 100-degree FAQ table gives the same 2015–2024 values: 18, 38, 23, 46, 47, 57, 20, 34, 70 and 55. **[PRIMARY-VERIFIED]** — [NWS EPZ 100-degree FAQ](https://www.weather.gov/epz/elpaso_100_degree_page)
- **All-time ranking** of 100°F days per year (ACIS, computed):
  1. 2023 (70)
  2. 1994 (62)
  3. 2020 (57)
  4. 2024 and 1980, tied (55)
  5. 2026 (52)
  6. 2011 (50)
  7. 2019 (47)
  8. 2018 (46)
  9. 2016 (38)
  10. 2025 (37)

  This makes 2024 **tied for 4th**. That resolves the "4th vs 2nd" conflict in the earlier notes in favor of "4th (tied)". 2025 ranks 11th by distinct position, consistent with El Paso Matters' "11th most". **[PRIMARY-VERIFIED; computed]**
- **Other figures from the NWS FAQ (David Hefner, WFO El Paso):** **[PRIMARY-VERIFIED]** — [NWS EPZ FAQ](https://www.weather.gov/epz/elpaso_100_degree_page)
  - 2,193 days of 100°F or more, 1887–2024.
  - Long-term average of 16 per year. The 1991–2020 normal is 26 per year.
  - Record 44 consecutive days of 100°F or more, Jun 16 – Jul 29, 2023.
  - Earliest 100°F day: May 7, 2020. Latest: Sep 27, 2024.
  - Monthly records: July 30 (2023), August 20 (2020), September 10 (2023).

**Records** **[PRIMARY-VERIFIED]**
- All-time high is **114°F on Jun 30, 1994**. 2023's 112°F on Aug 6 is the highest since 1994. — [NWS EPZ FAQ](https://www.weather.gov/epz/elpaso_100_degree_page); [ACIS](https://data.rcc-acis.org/StnData)
- Longest 100°F streaks (ACIS): 44 days (Jun 16 – Jul 29, 2023), 23 (1994), 21 (1980), 18 (Jul 3–20, 2020) and 16 (2016).
- Longest 90°F streaks (ACIS): **108 days (Jun 6 – Sep 21, 2026)**, 106 (May 27 – Sep 9, 2015), 91 (2020), 89 (2019) and 82 (2023). **[PRIMARY-VERIFIED; computed]**
- El Paso Matters (Sep 21, 2026) reports: 108th consecutive 90°F day; "The last day El Paso's temperature didn't reach at least 90 degrees was June 5"; "Fifty days in that stretch saw temperatures of 100 degrees or more"; average high Jun 22 – Sep 21 of 98.7°F (3rd highest) and average low 74°F (4th highest). **[SECONDARY, full text read]** — [El Paso Matters 2026-09-21](https://elpasomatters.org/2026/09/21/el-paso-record-108-consecutive-days-90-degree-heat/)
  - **Discrepancy:** ACIS shows **52** days of 100°F or more inside the streak, and all 52 of 2026's 100°F days fell Jun 6 – Aug 31 (June 17, July 15, August 20). El Paso Matters says 50. This may reflect preliminary versus quality-controlled data or a different count window. Treat it as "50–52".

**Per-year detail, 2015–2026 (ACIS, computed)** **[PRIMARY-VERIFIED]**

| Year | Annual max | Days at or above 105°F | Nights with low at or above 75°F | Nights with low at or above 80°F |
|---|---|---|---|---|
| 2015 | 104 | 0 | 28 | 0 |
| 2016 | 108 | 10 | 31 | 4 |
| 2017 | 111 | 5 | 26 | 2 |
| 2018 | 108 | 10 | 49 | 5 |
| 2019 | 106 | 2 | 47 | 7 |
| 2020 | 110 (Jul 13) | 18 | 52 | 14 |
| 2021 | 109 | 4 | 14 | 5 |
| 2022 | 108 | 8 | 27 | 5 |
| 2023 | 112 (Aug 6) | **33** | **68** | **18** |
| 2024 | 109 (Jun 13) | 16 | 59 | 17 |
| 2025 | 109 (Jun 15) | 15 | 39 | 6 |
| 2026 YTD | 108 (Jul 31) | 10 | 50 | 5 |

**Warmest years by annual mean of (max+min)/2** **[PRIMARY-VERIFIED; computed from threaded record]**
1. 2024: 69.86°F. This agrees with the NWS 2024 Annual Review (69.8°F) and El Paso Matters (69.9°F) as the warmest year.
2. 2023: 69.18°F.
3. 2025: 69.05°F. This confirms "third-warmest".
4. 2017: 68.58°F.
5. 2020: 68.33°F.

Supporting source for the 2024 figure: [NWS 2024 Annual Review](https://www.weather.gov/media/epz/climat/2024AnnualReview.pdf)

**Jan–Sep mean temperature:** 2026 is 72.94°F, ahead of 2024 (72.77), 2023 (72.42), 2018 (72.39) and 2020 (71.95). This confirms 2026 is running warmest-to-date, by about 0.2°F through September. The earlier note said 0.4°F, measured at a different date. **[PRIMARY-VERIFIED; computed]**

### Inferences
- **Fully confirmed:** 2023 (70), 2024 (55), 2025 (37), the 44-day streak, and the 108-day 90°F streak.
- **Corrected:** 2020 is 57 days, not 56. 2024 is tied 4th for 100°F days. The 90°F streak began Jun 6.
- **Night heat is the 79902-relevant signal.** Nights at or above 75°F roughly doubled from 26–31 per year (2015–17) to 50–68 per year (2020, 2023, 2024, 2026). Combined with the UHI map's 101–105°F readings at 7–8 PM, this points to reduced overnight relief.

### Gaps
- 2026 data after about mid-September may be preliminary in ACIS. Final rank comparisons should be rechecked after NCEI quality control.
- ACIS "ELPthr" is the threaded El Paso record and matches the official ELP values used by NWS for 2015–2024.

---

## 4. Heat-related deaths in El Paso County, 2023–2025

### Takeaway
No primary DSHS or City/County surveillance data could be retrieved: the DSHS heat pages return 404, and the city told reporters it "does not track heat-related illnesses." The El Paso Matters and Inside Climate News figures **do not conflict**. They come from the **same Inside Climate News investigation**, republished by El Paso Matters, and measure different things:
- **26 (2023) and 39 (2024):** deaths "directly or indirectly" attributed to heat, per **state data**.
- **26 people over 2023–2024 combined (19 migrants, 7 U.S. residents):** individuals Inside Climate News could **identify by name through autopsies**. Non-autopsied heat deaths are not public record.

No final 2025 count was found.

### Cited Findings
**From the Inside Climate News investigation as republished by El Paso Matters** **[SECONDARY, full text read]** — [El Paso Matters 2025-08-21](https://elpasomatters.org/2025/08/21/el-paso-weather-extreme-heat-illness-deaths/)
- The article was published by El Paso Matters "Special to El Paso Matters", August 21, 2025. Its text identifies it as Inside Climate News reporting: "El Paso's health information exchange denied a request from Inside Climate News…".
- Quotes: "a record 39 deaths were attributed directly or indirectly to heat in El Paso County during 2024. The previous record was set in 2023, when the heat directly or indirectly killed 26 people, according to state data."
- "Inside Climate News was only able to identify individuals for whom autopsies were conducted… The identities of individuals who died from the heat in Texas and did not receive autopsies are not public record." "Inside Climate News identified 26 people who died in the heat during 2023 and 2024 in El Paso County. Nineteen were migrants… Seven were U.S. residents. The youngest victim was 19 and the oldest 88."
- "So far in 2025, fewer heat deaths have been reported than in the previous two years." The first 2025 death was an 85-year-old woman found outside her home in Canutillo on June 12, when the high was 103°F.
- "The city of El Paso said it does not track heat-related illnesses." Neither the city nor the county shares the state's weekly heat-illness data with the public. PHIX declined the data request.
- History: in 2002, 10 heat-stroke deaths plus 11 heat-contributed deaths led to creation of the Extreme Weather Task Force. "Between 2005 and 2021, El Paso recorded fewer than 10 direct heat deaths a year."
- U.S. resident victims included one male hiker per year in the **Franklin Mountains** (2022–2024), two elderly men living alone, and a 75-year-old man in a northeast El Paso trailer that was 85°F inside at 8:23 PM on June 11, 2024 (outside high 102°F).
- Statewide: 334 Texas heat deaths in 2023, the deadliest year on record. In 2024, 171 deaths directly attributed to heat plus 281 contributing, per preliminary state data.
- A 2016 UTHealth paper found elderly mortality risk 4.70 times greater during heat waves in El Paso County (2006–2011), the strongest correlation in Texas.
- The ME's 2025 annual report (El Paso Matters, 2026-06-21) covers 7,200 county deaths, with 1,145 accepted by the ME. **The article text read this session gives no heat/hyperthermia figure.** **[SECONDARY]** — [El Paso Matters 2026-06-21](https://elpasomatters.org/2026/06/21/deaths-el-paso-county-medical-examiner-report-overdoses-car-accidents/)

### Inferences
- **Recommended phrasing:** "State data show 26 heat-related deaths (direct and indirect) in El Paso County in 2023 and a record 39 in 2024. An Inside Climate News review could identify 26 individual victims by autopsy across both years, most of them migrants."
- For 79902 the documented local exposure pathways are:
  - **Franklin Mountains hikers.** The trailheads off Rim Rd and Scenic Dr border the ZIP.
  - **Elderly residents living alone or unable to run AC overnight.**
  - **Unhoused people near downtown.** This group is inferred, not documented in the article.

### Gaps
- **Not retrieved:** DSHS primary heat-death tables by county, the ME annual report PDF heat line, and 2025 and 2026 county totals.
- No ZIP-level (79902) heat illness or death data exists publicly, according to the reporting above.

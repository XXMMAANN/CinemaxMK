# EPA ECHO / SDWIS / ICIS compliance: El Paso Water (TX0710002), EPWater wastewater plants, and ZIP 79902 facilities (primary-verified)

**Method:** Every finding below marked **[PV]** (primary-verified) comes straight from EPA's own APIs, queried on 2026-10-01. Data extract dates: SDWIS 07/09/2026 (ECHO DFR); ECHO SDWA status current as of 03/31/2026; CWA SNC status as of 06/30/2026. One TCEQ primary PDF was also read in full. The earlier notes (`../El Paso 79902 heat and water/epa_echo.md`) relied on search snippets; these notes replace them where they conflict.

The API calls used (all returned HTTP 200):
- `https://data.epa.gov/efservice/VIOLATION/PWSID/TX0710002/JSON` (Envirofacts SDWIS VIOLATION, 54 rows)
- `https://data.epa.gov/efservice/ENFORCEMENT_ACTION/PWSID/TX0710002/JSON` (64 rows)
- `https://echodata.epa.gov/echo/dfr_rest_services.get_dfr?output=JSON&p_id=TX0710002&p_system=SDWIS`
- `https://echodata.epa.gov/echo/cwa_rest_services.get_facilities?output=JSON&p_st=TX&p_ct=EL%20PASO&p_maj=Y` → `get_qid` (QueryID 935)
- `https://echodata.epa.gov/echo/cwa_rest_services.get_facilities?output=JSON&p_st=TX&p_ct=EL%20PASO&p_fn=EL%20PASO%20WATER` → `get_qid` (QueryID 852)
- `https://echodata.epa.gov/echo/dfr_rest_services.get_dfr?output=JSON&p_id={TX0087149|TX0101605|TX0026751}&p_system=NPDES`
- `https://echodata.epa.gov/echo/case_rest_services.get_case_report?output=JSON&p_id={06-2022-1705|06-2026-1751|TX-2022-0310-MWD-E|06-2026-3506}`
- `https://echodata.epa.gov/echo/echo_rest_services.get_facilities?output=JSON&p_zip=79902` → `get_qid` (QueryID 16, 135 rows)
- `https://echodata.epa.gov/echo/dfr_rest_services.get_dfr?output=JSON&p_id=110013277863` (Quail Run)
- `https://www.tceq.texas.gov/downloads/agency/decisions/agendas/backup/2022/2022-0310-mwd-e.pdf`

Note: `sdw_rest_services.get_systems?p_pwsid=TX0710002` **ignores the p_pwsid parameter**. It returned "Rows Returned would be 434040 … Queryset Limit would be exceeded". The DFR and Envirofacts endpoints were used instead.

Human-readable equivalents: ECHO DFR `https://echo.epa.gov/detailed-facility-report?fid=TX0710002` (SDWA); `https://echo.epa.gov/detailed-facility-report?fid=110064621226` (Bustamante); case reports at `https://echo.epa.gov/enforcement-case-report?id=<case>`.

## Q1: SDWA record for El Paso Water Utilities, PWSID TX0710002

### Takeaway
**[PV]** The system is in compliance and is not a serious violator. ECHO shows "No Violation Identified" (as of 03/31/2026), CurrentSNC = "No", 2 quarters in noncompliance and 0 in SNC over the last 3 years, 0 formal actions, $0 penalties. SDWIS (Envirofacts) holds **54 violation records for TX0710002, all monitoring/reporting (MR/MON), and none health-based** (2015-12 to 2024-03). Fifty of those 54 rows come from just two events: one missed SOC/VOC sampling quarter in 2018 (49 rows, one per contaminant) and one Lead & Copper Rule period. Neither the "69" nor the "858" aggregator figure matches the EPA records.

### Cited Findings
- **[PV] System profile:** Community water system, local-government owner, primary source surface water. ECHO/SDWIS lists population served as **747,168**; the aggregators' 672,538 is out of date. FRS Registry ID 110013278540. — [ECHO DFR API TX0710002](https://echodata.epa.gov/echo/dfr_rest_services.get_dfr?output=JSON&p_id=TX0710002&p_system=SDWIS)
- **[PV] Current status:**
  - SDWA CurrentStatus "No Violation Identified"; QtrsInNC = 2, QtrsInSNC = 0 (3-year window 04/01/2023–03/31/2026).
  - InformalActions = 16; FormalActions = none; TotalPenalties $0 (5-year window 04/01/2021–03/31/2026).
  - ComplianceSummary: CurrentSNC "No", CurrentAsOf 03/31/2026. This means the system **is not** a Serious Violator.
  - Source: [ECHO DFR API](https://echodata.epa.gov/echo/dfr_rest_services.get_dfr?output=JSON&p_id=TX0710002&p_system=SDWIS)
- **[PV] 13-quarter history (04/2023–06/2026):** Violation in Q2-2023 and Q1-2024; "No Violation" in every other quarter. The rule violated in both cases was the Stage 1 Disinfectants & Disinfection Byproducts Rule (MR), with periods 05/01–05/31/2023 and 03/01–03/31/2024. — [ECHO DFR API](https://echodata.epa.gov/echo/dfr_rest_services.get_dfr?output=JSON&p_id=TX0710002&p_system=SDWIS)
- **[PV] Full SDWIS violation list (Envirofacts, 54 rows):** every row has is_health_based_ind = "N", compliance_status_code = "R" (returned to compliance), and primacy agency TX. — [Envirofacts VIOLATION](https://data.epa.gov/efservice/VIOLATION/PWSID/TX0710002/JSON)

  | Violation ID(s) | Code / category | Rule (code) | Contaminant | Compliance period | RTC date |
  |---|---|---|---|---|---|
  | 100069164 | 66 / MR | Lead & Copper (350) | 5000 Lead & Copper Rule | begins 2015-12-30 | 2016-02-09 |
  | 100070465–100070485 (21 rows) | 03 / MR (monitoring, regular) | VOCs (310) | 21 individual VOCs (e.g., 2378 1,2,4-trichlorobenzene, 2955 xylenes, 2964 dichloromethane, 2977 1,1-dichloroethylene, 2976 vinyl chloride) | 2018-04-01 to 2018-06-30, facility_id 131378 | 2019-03-18 |
  | 100070486–100070513 (28 rows) | 03 / MR | SOCs (320) | 28 individual SOCs (e.g., 2005 endrin, 2010 lindane, 2050 atrazine, 2039 DEHA/2306 benzo(a)pyrene etc.) | 2018-04-01 to 2018-06-30, facility_id 131378 | 2019-03-18 / 2019-04-23 |
  | 100070591 | 53 / MR | Lead & Copper (350) | 5000 | 2020-01-01 to 2020-06-30 | 2021-12-31 |
  | 100070830 | 3A / MON | Revised Total Coliform Rule (111) | 8000 RTCR | 2023-02-01 to 2023-02-28 | 2023-04-06 |
  | 100070835 | 27 / MR | Stage 1 DBP (210) | 1009 Chlorite | 2023-05-01 to 2023-05-31, facility 39886 | 2023-07-19 |
  | 100070966 | 27 / MR | Stage 1 DBP (210) | 1009 Chlorite | 2024-03-01 to 2024-03-31, facility 39886 | 2024-05-17 |

- **[PV] Enforcement actions (Envirofacts ENFORCEMENT_ACTION, 64 rows):** all are state (originator "S") informal or resolving actions. The types are SIA, SIE, SIF and SOX (state compliance achieved). There are no formal actions and no penalties. — [Envirofacts ENFORCEMENT_ACTION](https://data.epa.gov/efservice/ENFORCEMENT_ACTION/PWSID/TX0710002/JSON)
  - Example comments: 2021-12-31 SOX "6M2 2021 SUCCESSFUL MP FOR SYSTEM"; 2023-04-06 SOX "…PWS FULFILLED MARCH 2023 COLIFORM SAMPLE REQUIREMENTS"; 2024-05-17 SOX "VIOLATION SOXED BASED ON APRIL REPORT ON TIME".
- **[PV] Groundwater E. coli public notices (no SDWIS violation attached).** SDWIS records three state "Public Notification requested" actions (SIE) for E. coli at EPWater wells:
  - 2024-11-18: "PN REQUIRED DUE TO E COLI AT WELL G0710002II"
  - 2025-01-15: "…AT WELL G0720001IO"
  - 2025-11-05: "…AT WELL G0710002IZ"
  - Each was followed by "PN received" (SIF) 1–4 days later.
  - No corresponding violation rows exist in the VIOLATION table. — [Envirofacts ENFORCEMENT_ACTION](https://data.epa.gov/efservice/ENFORCEMENT_ACTION/PWSID/TX0710002/JSON); ECHO DFR "Notices" section confirms the dates.
- **[PV] Lead & Copper (5-year):** 90th-percentile lead results were 0.0024 mg/L (2021), 0.0015 (2022–2024), 0.00116 (2023–2025) and 0 (2025), against the 0.015 mg/L action level. No Pb, Cu or LCR health-based violation is recorded. — [ECHO DFR API](https://echodata.epa.gov/echo/dfr_rest_services.get_dfr?output=JSON&p_id=TX0710002&p_system=SDWIS)
- **[PV] Sanitary surveys (state):**
  - 04/21/2022: minor deficiencies in Data Verification, Security and Source.
  - 10/18/2024: minor deficiencies in Data Verification, Distribution, Finished Water Storage, Security and Source.
  - Both surveys: no deficiencies in Treatment, Operator, Management, Pumps or Financial. — [ECHO DFR API](https://echodata.epa.gov/echo/dfr_rest_services.get_dfr?output=JSON&p_id=TX0710002&p_system=SDWIS)
- **[PV] TCEQ water-hauling fine:** The 2022 TCEQ $7,728 water-hauling fine from the earlier notes does **not** appear as a formal SDWIS enforcement action under TX0710002; the DFR shows 0 formal SDWA actions in 2021–2026. That fine is still sourced only to [El Paso Matters](https://elpasomatters.org/2022/07/14/tceq-fines-el-paso-utility-for-drinking-water-truck-health-safety-violations/), and it was likely issued under state rules and not reported to SDWIS.

### Inferences
- **Reconciling the counts.** EPA's database (Envirofacts) holds 54 violation rows. SDWIS creates one row per contaminant per period, so one missed 2018 Q2 SOC/VOC sampling event alone produced 49 rows.
  - Counted as distinct events (rule + period), TX0710002 had only **6 violation events from 2015 to 2024**: LCR 2015, VOC/SOC Q2-2018, LCR H1-2020, RTCR Feb-2023, chlorite May-2023 and chlorite Mar-2024.
  - The aggregator's "12 MR violations in 3 years" is not reproduced: EPA shows 3 in 2023–2024.
  - The "69 on record" figure may include older records that Envirofacts no longer returns, or the aggregator may count differently.
  - The **"858 violations / 192 health-based"** figure is not supported by any EPA record for TX0710002. Most likely it mixes in other PWSIDs (for example, El Paso County systems), so it should be discarded.
- **No health-based (MCL/TT) violation appears for TX0710002 in the SDWIS data available (2015–2026).**
- The E. coli well notices look like Groundwater Rule triggered or source-sample positives that required public notice. The available fields do not confirm whether those wells were taken out of service.

### Gaps
- Envirofacts returns no violation rows before 12/2015 for this PWSID. I did not establish whether older records were purged or re-keyed.
- I could not check whether the 2024–2025 E. coli well detections led to Groundwater Rule treatment-technique violations; none are recorded.
- The `sdw_rest_services.get_systems` endpoint could not be filtered by PWSID (it ignores the parameter), so the SDW "SeriousViolator" column itself was not retrieved. The DFR's CurrentSNC = "No" was used instead.

## Q2: CWA/NPDES record for the EPWater wastewater plants

### Takeaway
**[PV]** Permit IDs and status:

| Plant | NPDES ID | Design flow | ECHO status |
|---|---|---|---|
| Haskell R. Street WWTP | **TX0026751** | 27.7 MGD | No violation |
| Roberto R. Bustamante WWTP | **TX0101605** | 39 MGD | **currently in violation, 2 SNC quarters, under an EPA order** |
| John T. Hickerson WWTF (Northwest WWTP) | **TX0087149** | 17.5 MGD; TPDES WQ0010408009 | 6 NC quarters, no SNC |
| Fred Hervey Water Reclamation Plant | stormwater permits only in ECHO (TXR05DW71, TXR1524NJ) | — | — |

Formal enforcement in the last 5 years:
- EPA CWA §309(a) compliance orders against **Haskell** (12/20/2021) and **Bustamante** (02/12/2026), neither with a penalty.
- The **TCEQ Frontera agreed order** (docket 2022-0310-MWD-E), which ICIS attaches to the Hickerson permit: $2,016,000, fully offset by a SEP, so $0 was paid to the state.
- An **EPA CAA §112(r) General Duty Clause order** at Bustamante after a fatal incident on 04/26/2024.

### Cited Findings
- **[PV] Haskell R. Street WWTP, TX0026751** (4100 Delta Dr, 79905; major; permit effective 06/01/2025, expires 05/15/2030):
  - ECHO status "No Violation Identified"; 0 NC quarters and 0 SNC quarters in the last 3 years (13-quarter string all clear, 07/2023–09/2026).
  - Effluent exceedances: ammonia-N at outfall 002, 13% over the limit in Q1-2024 and 30% in Q1-2025. The 5-year E90 count is 4 (ammonia and cyanide).
  - Schedule violation C40 (permit renewal application unachieved and not reported), 10/11/2023–12/13/2023.
  - Informal actions: TCEQ Letter of Violation 11/16/2023; EPA Notice of Noncompliance 12/20/2021.
  - Formal action: **EPA CWA 309(a) AO, case 06-2022-1705** (regional docket 06-2021-1705), issued 12/20/2021 "in response to effluent violations of permit limits". $0 penalty; $10,000 compliance action cost.
  - Sources: [ECHO DFR API](https://echodata.epa.gov/echo/dfr_rest_services.get_dfr?output=JSON&p_id=TX0026751&p_system=NPDES); [ECHO case report 06-2022-1705](https://echo.epa.gov/enforcement-case-report?id=06-2022-1705)
- **[PV] Roberto R. Bustamante WWTP, TX0101605** (10001 Southside Rd, 79927; major; permit effective 05/01/2025, expires 04/17/2030):
  - ECHO status "Violation Identified", violation status "Reportable Noncompliance"; **8 NC quarters and 2 SNC quarters** in the last 3 years. SNC (Category I) quarters were Q2-2025 and Q1-2026.
  - 13-quarter string `__V__VVS_VSVV`: violations in Q1-24, Q4-24, Q1-25, Q2-25 (SNC), Q4-25, Q1-26 (SNC), Q2-26 and Q3-26.
  - Effluent exceedances (outfall 002 unless noted), by parameter:
    - **E. coli:** 30% (Q4-24), 162% (Q1-25), **506%** (Q2-25), **507%** (Q4-25), 54% (Q1-26).
    - **TSS:** **413%** (Q2-25), 209% (Q4-25), 182% (Q1-26), 43% (Q2-26), plus monthly-average exceedances of 54%, 53% and 5%.
    - **Ammonia-N:** 96–99% (Q2-25).
    - **Total residual chlorine:** 100% (Q4-25).
    - **Outfall 101:** ammonia 76%; TSS 33–39%.
  - ECHO counts 35 effluent exceedances in the current period (E90Cnt = 35) and 41 E90 exceedances over 5 years.
  - Formal action: **EPA CWA 309(a) AO, case 06-2026-1751**, issued 02/12/2026 "in response to significant noncompliance or effluent violations of permit limits". It is a unilateral AO with $0 penalty and $50,000 compliance action cost.
  - Compliance-schedule violations against that order are open:
    - C30 "Schedule Event unachieved but reported", from 02/16/2026 and 03/13/2026.
    - C40 "Compliance Plan unachieved and not reported", from 03/13/2026.
    - Both are still flagged "V" through Q3-2026.
  - TCEQ notices: "Agency Enforcement Review" 09/03/2025; "Under Review" 05/19/2026 and 09/18/2026.
  - Sources: [ECHO DFR API](https://echodata.epa.gov/echo/dfr_rest_services.get_dfr?output=JSON&p_id=TX0101605&p_system=NPDES); [ECHO case report 06-2026-1751](https://echo.epa.gov/enforcement-case-report?id=06-2026-1751)
- **[PV] Bustamante CAA 112(r) case 06-2026-3506:**
  - The case summary reads: "On April 26, 2024, there was an incident at the Facility that resulted in a fatality."
  - EPA investigated and found a violation of the **General Duty Clause, CAA 112(r)(1)**.
  - It issued a CAA 113(a) Administrative Compliance Order (non-penalty, injunctive relief) on 12/16/2025, settled 12/17/2025.
  - An EPA Notice of Noncompliance was issued 07/29/2025.
  - Source: [ECHO case report 06-2026-3506](https://echo.epa.gov/enforcement-case-report?id=06-2026-3506)
- **[PV] John T. Hickerson WWTF, TX0087149** (701 Executive Center Blvd, 79922; listed as "HICKEERSON" in ECHO; major; permit effective 02/01/2026, expires 01/08/2029):
  - ECHO status "No Violation Identified" currently; **6 NC quarters, 0 SNC**.
  - Violation quarters: Q1-24, Q2-24, Q4-24, Q1-25, Q2-25 and Q1-26.
  - Effluent exceedances at outfall 001:
    - **E. coli:** 506% (Q1-24), 9% (Q2-24), limit violation (Q4-24), **507%** (Q1-26).
    - **TSS:** 366% (Q4-24), 150% (Q1-25), 5% (Q2-25), 8% (Q1-26).
    - **CBOD5:** 17% (Q2-24), 20% (Q1-25).
    - **Ammonia:** 9% (Q2-24).
  - ECHO E90 counts: 13 current, 19 over 5 years.
  - Formal action: "State CWA Penalty AO" dated 09/12/2023, $2,016,000. This is case **TX-2022-0310-MWD-E**, closed 04/17/2024, outcome "Final Order With Penalty". It records state penalty $2,016,000, penalty collected $0 and SEP cost $0 (ICIS does not record the SEP offset).
  - Sources: [ECHO DFR API](https://echodata.epa.gov/echo/dfr_rest_services.get_dfr?output=JSON&p_id=TX0087149&p_system=NPDES); [ECHO case report](https://echo.epa.gov/enforcement-case-report?id=TX-2022-0310-MWD-E)
- **[PV] TCEQ docket 2022-0310-MWD-E (Frontera force main), from the TCEQ executive summary:**
  - Findings Agreed Order (Case No. 62097, RN103870341) covering the "El Paso Water Utilities Northwest WWTP, 701 Executive Center Boulevard", i.e. the Hickerson service area.
  - Violation: failure to prevent unauthorized discharge [30 TAC §305.125(1), TWC §26.121(a)(1), **TPDES Permit WQ0010408009**, conditions 2.d and 2.g].
  - Penalty: total assessed **$2,016,000**; paid to General Revenue **$0**; SEP conditional offset **$2,016,000** for the "Wastewater Discharge Remediation Project (Compliance)", which was completed by 12/22/2022. The penalty worksheet shows a $1,800,000 base penalty plus a 12% compliance-history enhancement.
  - Investigation: complaints filed 08/13, 08/24 and 08/27/2021 (350,000, 450,000 and 310,000 gal raw sewage); investigation 12/10/2021; Notice of Enforcement 12/17/2021; Texas Register publication 07/21/2023.
  - Corrective actions:
    - Discharge ceased near 1045 Sunland Park Dr by 09/03/2021.
    - Discharges ceased near 3817 and 3820 Constitution Dr by 09/17/2021.
    - The 4134 Doniphan Dr diversion to the storm sewer and Rio Grande ceased 01/10/2022.
    - Rio Grande cleanup, from upstream of the Doniphan outfall to American Dam, completed by 06/04/2022.
    - American Canal cleanup completed by 04/27/2022.
  - Source: [TCEQ agenda backup PDF](https://www.tceq.texas.gov/downloads/agency/decisions/agendas/backup/2022/2022-0310-mwd-e.pdf)
- **[PV] Fred Hervey Water Reclamation Plant (11700 Railroad Dr, 79934):** ECHO lists only two minor stormwater permits, both "No Violation Identified" with no formal actions:
  - TXR05DW71 (MSGP, admin-continued, expired 08/13/2026)
  - TXR1524NJ (construction stormwater)
  - No individual NPDES wastewater permit appears under EPWater's name in ECHO. — [ECHO CWA get_qid 852](https://echodata.epa.gov/echo/cwa_rest_services.get_qid?output=JSON&qid=852)
- **[PV] Other EPWater CWA records:**
  - TXR1515TN (Northwest WWTP stormwater): no violations.
  - TXR1520UP (wells): no violations.
  - TXR1551CM: terminated.
  - TX0133550 (lab, 800 Canal Rd, 79901): "Not Needed".
  - Source: same query.
- **[PV] Context, other El Paso majors (not EPWater):**
  - Horizon Regional MUD WWTP TX0086045: 4 NC quarters, 1 SNC, 4 formal actions, $45,190 in penalties (last 05/19/2026).
  - Fabens WWTP TX0065013: 6 NC quarters, 1 SNC.
  - City of El Paso MS4 TXS000801: no violations.
  - Source: [ECHO CWA get_qid 935](https://echodata.epa.gov/echo/cwa_rest_services.get_qid?output=JSON&qid=935)

### Inferences
- The EPA $2,016,000 "total penalties" for El Paso NPDES facilities is entirely the Frontera TCEQ order, and **no cash was paid**, because the SEP offset 100%. Reporting it as a "$2M fine paid" would be inaccurate.
- Bustamante, the largest plant, is the current problem facility. It has repeated E. coli and TSS exceedances of 400–500%+ in 2025–2026, two SNC quarters, an EPA order in February 2026, and compliance-schedule milestones under that order that are still missed as of Q3-2026.
- The 670,000-gal Hickerson spill (03/24/2026) and the 800,000-gal Bustamante line break (04/17/2025) from the earlier notes have no separate formal enforcement in ECHO. Hickerson's Q1-2026 E. coli exceedance of 507% falls in the same quarter as the March 2026 pump failure; that link is plausible but not confirmed.

### Gaps
- Fred Hervey's TCEQ wastewater/reuse authorization (a state "WQ" number) is not in ECHO and was not identified.
- Collection-system SSO events from 2025–2026 (for example, the Railroad Dr spill of about 950,000 gal in April 2026) do not show up as discrete ECHO records. SSO reports (HasIcisSsoRpt) were "N".
- The DMR measured values and limits behind each percentage are not shown; the percentages are ECHO's "percent over limit" figures.

## Q3: ECHO-listed facilities in ZIP 79902

### Takeaway
**[PV]** The ECHO all-media search for ZIP 79902 returns **135 records**. Summary flags: 0 current significant violators, **0 current violations**, 1 facility with violations in the last 3 years, 0 with formal enforcement in the last 5 years, 1 with informal enforcement, and **$0 total penalties**. Only one facility has a recent violation history: **Quail Run Mobile Home Park** water system TX0710102. Its 79902 address (420 Montana Ave) is an owner/mailing address; the plant itself is at 12850 Montana Ave in far-east El Paso.

### Cited Findings
- **[PV] Query summary for QueryID 16:** QueryRows 135, SVRows 0, CVRows 0, V3Rows 1, FEARows 0, InfFEARows 1, INSPRows 2, TotalPenalties $0. By program: CAA 7, CWA 11, RCRA 32, TRI 0. — [ECHO all-media API](https://echodata.epa.gov/echo/echo_rest_services.get_facilities?output=JSON&p_zip=79902)
- **[PV] Quail Run Mobile Home Park, PWS TX0710102** (private community water system, groundwater, population 45; FRS 110013277863):
  - Status: SDWA "No Violation Identified" (current); **12 NC quarters and 8 "Enforcement Priority" (SNC) quarters** from Q1-2024 to Q4-2025; 57 informal actions; 0 formal actions and $0 penalties.
  - Violations: MR violations under the SOC/VOC/Nitrate rules (2022, 2023 and 2024, one row per contaminant); Lead & Copper MR (10/2023–2025); LCRR reporting and treatment-technique violations (10/17/2024); multiple Public Notice Rule violations (2024–2025); RTCR MON (03/2023); Stage 2 DBP MR (TTHM/HAA5, 10/2019–09/2022); cyanide MR (2021–2023).
  - State Formal Notices of Violation were issued 05/24/2024. All violations were resolved by 03/2026.
  - Source: [ECHO DFR API](https://echodata.epa.gov/echo/dfr_rest_services.get_dfr?output=JSON&p_id=110013277863)
- **[PV] Active 79902 facilities with program IDs, all "No Violation Identified":**
  - Air / dry cleaners: Amigo Laundry & Cleaners (301 Cincinnati; CAA+RCRA); Angelus Cleaners (816 N Mesa; CAA+RCRA); Coronado Cleaners (4134 N Mesa; CAA); Golden Scissors Dry Cleaners (4111 N Mesa; CAA); Supreme Cleaners (2716 Mesa; CAA).
  - Hospitals: Providence Memorial Hospital (2001 N Oregon; CAA+RCRA); Las Palmas Medical Center (1801 N Oregon; RCRA).
  - UTEP University at Hawthorne (3120 Sun Bowl Dr; CAA+RCRA).
  - Other RCRA handlers: CVS #10451, Family Dollar #10117, Foret Paint & Sandblasting, Mesa Quick Copy, Nickolas Environmental, Oregon Imaging MRI, Transportes Neyra.
  - CWA construction/stormwater permits: TxDOT I-10 projects, Village at Westside Crossing, Nuestra Señora, Cimarron Park Apartments, Victorio Trail Sand Products, Franklin Hills Unit 2, Luckett wastewater replacement.
  - Source: [ECHO get_qid 16](https://echodata.epa.gov/echo/echo_rest_services.get_qid?output=JSON&qid=16)
- **[PV] Legacy sites listed in 79902 but inactive or with no compliance data:** El Paso Plating Works (600 N Cotton St); "ASARCO 126 Acre Tract" (no address); Former Wallis Cleaners (405 Montana Ave; RCRA, no violation); Texaco Bulk Plant (Paisano Dr & Eucalyptus St). — same query.

### Inferences
- Under ECHO, ZIP 79902 currently has **no facility with a current violation and none with formal enforcement in the last 5 years**. The only recent violator is a tiny water system whose physical plant is outside the ZIP.
- The neighborhood's environmental burden in EPA data is mostly legacy contamination (El Paso Plating Works, the ASARCO tract and smelter-related soil, dry-cleaner sites), not active permit violations.

### Gaps
- The ECHO ZIP search uses each facility's registered address, which can be a mailing address (as with Quail Run). Facilities physically in 79902 but registered elsewhere would be missed.
- I did not query the EPA TRI, Superfund (SEMS) or TCEQ state-only enforcement databases for 79902.

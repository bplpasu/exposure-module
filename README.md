# Building Exposure Module — Chiang Mai, Thailand

> This repository provides building-level and province-level exposure data for seismic risk assessment in Chiang Mai, Thailand. The dataset was developed as part of a catastrophe (CAT) model for earthquake loss estimation using the OpenQuake Engine framework.

* * *

## Repository Structure

```
exposure-module/
├── Exposure-Module.csv              # Building-level exposure (~100,352 assets)
├── Exposure_Com_Thailand_Adm1.csv  # Province-level aggregated exposure (Thailand)
└── schema.ini                       # Field schema definition for Exposure-Module.csv
```

* * *

## Data Description

### `Exposure-Module.csv`

Building-level exposure dataset for Chiang Mai Municipality derived from building footprint data collected via Google Street View (GSV), UAV survey, and field walk surveys. Each record represents one building asset.

| Field | Type | Description |
|---|---|---|
| `ID` | Integer | Unique building identifier |
| `LAT` / `LONG` | Double | Building centroid coordinates (WGS 84) |
| `AREA` | Double | Building footprint area (m²) |
| `FL_AREA` | Double | Total floor area (m²) |
| `STORY` | Integer | Number of stories |
| `ST_TYPE` | Text | Structural type (e.g., C3 = concrete frame) |
| `OC_CLASS` | Text | Occupancy class (HAZUS-based, e.g., RES1, COM1) |
| `TAXONOMY` | Text | GEM taxonomy string |
| `CON_COST` | Integer | Construction replacement cost (USD) |
| `CONTENTS_C` | Integer | Contents replacement cost (USD) |
| `POP_DAY` / `POP_Night` | Integer | Daytime / nighttime population |
| `AGE` | Text | Building age class |
| `GG_SURVEY_` | Integer | Google Street View survey flag (MU area) |
| `GG_SURVEY1` | Integer | Google Street View survey flag (Space imagery) |
| `GG_SURVE_1` | Integer | UAV survey flag |
| `GG_SURVEY` | Integer | Combined Google survey flag |
| `WK_SURVEY` | Integer | Walk survey flag |
| `ADMIN_PLAN` | Text | Administrative planning zone code |
| `Extrapolated` | Integer | Flag for statistically imputed records |

* * *

### `Exposure_Com_Thailand_Adm1.csv`

Province-level aggregated exposure for all of Thailand, formatted for direct use as an OpenQuake Engine exposure input. Taxonomy strings follow the **GEM Building Taxonomy v2.0**.

| Field | Description |
|---|---|
| `ID_0` / `NAME_0` | Country code / name |
| `ID_1` / `NAME_1` | Province code / name |
| `SETTLEMENT` | Settlement type |
| `OCCUPANCY` | Occupancy category (Res / Com / Ind) |
| `TAXONOMY` | GEM taxonomy string |
| `BUILDINGS` | Number of buildings |
| `TOTAL_REPL_COST_USD` | Total replacement cost (USD) |
| `COST_STRUCTURAL_USD` | Structural replacement cost (USD) |
| `COST_NONSTRUCTURAL_USD` | Non-structural replacement cost (USD) |
| `COST_CONTENTS_USD` | Contents replacement cost (USD) |
| `TOTAL_AREA_SQM` | Total floor area (m²) |
| `OCCUPANTS_PER_ASSET_DAY` | Mean daytime occupants per asset |
| `OCCUPANTS_PER_ASSET_NIGHT` | Mean nighttime occupants per asset |
| `OCCUPANTS_PER_ASSET_TRANSIT` | Mean transit-hour occupants per asset |

* * *

## Coordinate Reference System

- **Building-level data**: WGS 1984 UTM Zone 47N (EPSG: 32647)
- **Province-level data**: Geographic WGS 1984 (EPSG: 4326)

## Data Sources

- Building footprint: Chiang Mai Municipality (CMM) cadastral data
- Survey methods: Google Street View, UAV imagery, walk-through field survey
- Population estimates: Derived from occupancy class and floor area
- Replacement costs: Calibrated to Thai construction cost benchmarks

* * *

## Citation

> *To be updated upon publication.*

## Funding

This work was supported by the National Research Council of Thailand (NRCT), grant number **N25A680575**, and carried out at the **Asian Institute of Technology (AIT)**.

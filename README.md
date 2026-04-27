# Building Exposure Module — Chiang Mai, Thailand

> This repository provides building-level exposure data for seismic risk assessment in Chiang Mai, Thailand. The dataset was developed as part of a catastrophe (CAT) model for earthquake loss estimation using the OpenQuake Engine framework.

* * *

## Repository Structure

```
exposure-module/
└── Exposure-Module.csv    # Building-level exposure (~96,635 assets)
```

* * *

## Data Description

### `Exposure-Module.csv`

Building-level exposure dataset for Chiang Mai derived from building footprint data collected via Google Street View (GSV), UAV survey, and walk-through field surveys. Each record represents one building asset.

| Field | Type | Description |
|---|---|---|
| `BLDGID` | Integer | Unique building identifier |
| `LAT` / `LONG` | Double | Building centroid coordinates (WGS 84) |
| `AREA` | Double | Building footprint area (m²) |
| `FL_AREA` | Double | Total floor area (m²) |
| `STORY` | Integer | Number of stories |
| `ST_TYPE` | Text | Structural type (e.g., C3 = concrete frame) |
| `OC_CLASS` | Text | Occupancy class (HAZUS-based, e.g., RES1, COM1) |
| `Tag` | Text | Survey source tag (e.g., GSV) |
| `Condition` | Text | Building condition rating |
| `AGE` | Text | Building age class |
| `Cluster` | Integer | Spatial cluster ID |

* * *

## Coordinate Reference System

- **WGS 1984 UTM Zone 47N** (EPSG: 32647)

## Data Sources

- Building footprint: Chiang Mai Municipality (CMM) cadastral data
- Survey methods: Google Street View, UAV imagery, walk-through field survey
- Replacement costs: Calibrated to Thai construction cost benchmarks

* * *

## Citation

> *To be updated upon publication.*

## Funding

This work was supported by the National Research Council of Thailand (NRCT), grant number **N25A680575**, and carried out at the **Asian Institute of Technology (AIT)**.

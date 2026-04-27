# Building Exposure Module — Chiang Mai, Thailand

> This repository provides a building-level exposure dataset for seismic risk assessment in Chiang Mai Province, Thailand. The dataset was developed as part of a catastrophe (CAT) model for earthquake loss estimation compatible with the **OpenQuake Engine** framework. Building attributes including structural type, occupancy class, floor area, and height were derived from a multi-source survey campaign covering ~96,635 assets.

* * *

## Repository Structure

```
exposure-module/
├── Exposure-Module.csv                # Building-level exposure (~96,635 assets)
├── Exposure_Summary_OccClass.csv      # Building count & area by occupancy class
├── Exposure_Summary_Taxonomy.csv      # Building count & area by GEM taxonomy
├── Exposure_Summary_STType.csv        # Building count & area by structural type
├── Exposure_Summary_StoryClass.csv    # Building count & area by height class
├── expo_occ_buildings.png             # Chart: buildings by occupancy
├── expo_occ_area.png                  # Chart: floor area by occupancy
├── expo_occ_pie.png                   # Chart: occupancy share (pie)
├── expo_taxo_buildings.png            # Chart: buildings by structural type
├── expo_story_class.png               # Chart: buildings by height class
└── analyze.py                         # Analysis & figure generation script
```

* * *

## Country Summary

### Occupancy Distribution

![Buildings by Occupancy](expo_occ_buildings.png)

![Floor Area by Occupancy](expo_occ_area.png)

![Occupancy Share](expo_occ_pie.png)

* * *

### Structural Type Distribution

![Buildings by Structural Type](expo_taxo_buildings.png)

* * *

### Height Class Distribution

![Buildings by Height Class](expo_story_class.png)

* * *

## Building Inventory

The exposure dataset covers **96,635 buildings** across Chiang Mai Province collected through three survey methods:

| Survey Method | Description |
|---|---|
| Google Street View (MU) | Street-level imagery within Chiang Mai Municipality |
| Google Street View (Space) | Satellite/aerial imagery |
| UAV Survey | Drone-based aerial survey |
| Walk Survey Round 1 & 2 | In-person field verification |

### Occupancy Classes

Occupancy follows the **HAZUS classification** system, mapped to GEM categories:

| GEM Category | HAZUS Classes | Description |
|---|---|---|
| `Res` | RES1–RES6 | Residential buildings |
| `Com` | COM1–COM10 | Commercial buildings |
| `Ind` | IND1–IND6 | Industrial buildings |
| `Agr` | AGR1 | Agricultural buildings |
| `Other` | REL1, GOV1–2, EDU1–2 | Religious, government, educational |

### Structural Types

| Code | GEM Macro-Taxonomy | Description |
|---|---|---|
| `C1` | CR/LFINF | Concrete frame with infill |
| `C2` | CR/LDUAL | Concrete dual system |
| `C3` | CR/LWAL | Concrete shear wall |
| `W1` / `W2` | W | Wood frame |
| `RM1` / `RM2` / `URM` | MUR | Masonry unreinforced/reinforced |
| `S1`–`S5` | S | Steel frame |
| `PC1` / `PC2` | PCR | Pre-cast concrete |

* * *

## Data Description

### `Exposure-Module.csv`

| Field | Type | Description |
|---|---|---|
| `BLDGID` | Integer | Unique building identifier |
| `LAT` / `LONG` | Double | Building centroid coordinates (WGS 84) |
| `AREA` | Double | Building footprint area (m²) |
| `FL_AREA` | Double | Total floor area (m²) |
| `STORY` | Integer | Number of stories |
| `ST_TYPE` | Text | Structural type (HAZUS, e.g., C3) |
| `OC_CLASS` | Text | Occupancy class (HAZUS, e.g., RES1, COM1) |
| `Tag` | Text | Survey source tag |
| `Condition` | Text | Building condition rating |
| `AGE` | Text | Building age class |
| `Cluster` | Integer | Spatial cluster ID |
| `GG_SURVEY_MU` | Integer | Google Street View survey flag (MU area) |
| `GG_SURVEY_SPACE` | Integer | Google Street View survey flag (space imagery) |
| `GG_SURVEY_UAV` | Integer | UAV survey flag |
| `WK_SURVEY_R1` | Integer | Walk survey round 1 flag |
| `WK_SURVEY_R2` | Integer | Walk survey round 2 flag |
| `TRUEEXPOSURE` | Integer | Verified exposure record flag |
| `Extrapolated` | Integer | Statistically imputed record flag |

* * *

## Coordinate Reference System

- **WGS 1984 UTM Zone 47N** (EPSG: 32647)

## Reproducing the Analysis

```bash
python analyze.py
```

Requires: `pandas`, `matplotlib`, `numpy`

* * *

## Citation

> *To be updated upon publication.*

## Funding

This work was supported by the **National Research Council of Thailand (NRCT)**, grant number **N25A680575**, and carried out at the **Asian Institute of Technology (AIT)**.

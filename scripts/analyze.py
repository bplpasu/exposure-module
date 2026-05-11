"""
Exposure Module Analysis — Chiang Mai, Thailand
Generates GEM-style summary CSVs and visualizations.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import os

# ── Config ─────────────────────────────────────────────────────────────────
INPUT_CSV  = r"C:\Exposure-Module\data\Exposure-Module.csv"
OUT_DIR    = r"C:\Exposure-Module\results"
COUNTRY    = "THA"
COUNTRY_NAME = "Thailand"
PROVINCE   = "AREA # TH57"
PROVINCE_NAME = "Chiang Mai"

# Occupancy mapping  OC_CLASS → GEM category
OCC_MAP = {
    "RES1": "Res", "RES2": "Res", "RES3": "Res",
    "RES3A": "Res", "RES3B": "Res", "RES3C": "Res",
    "RES3D": "Res", "RES3E": "Res", "RES3F": "Res",
    "RES4": "Res", "RES5": "Res", "RES6": "Res",
    "COM1": "Com", "COM1T": "Com", "COM2": "Com", "COM3": "Com", "COM4": "Com",
    "COM5": "Com", "COM6": "Com", "COM7": "Com", "COM8": "Com",
    "COM9": "Com", "COM10": "Com",
    "IND1": "Ind", "IND2": "Ind", "IND3": "Ind", "IND4": "Ind",
    "IND5": "Ind", "IND6": "Ind",
    "AGR1": "Agr",
    "REL1": "Other", "GOV1": "Other", "GOV2": "Other",
    "EDU1": "Other", "EDU2": "Other",
}

# Structural type → GEM macro-taxonomy label
# Based on Basic-Level Building Survey Form (HAZUS SIC classification)
# C1  = Concrete Moment Frame              → CR/MF
# C2  = Concrete Shear Walls               → CR/LWAL
# C3  = Concrete Frame w/ URM Infill       → CR/LFINF
# C4  = Concrete Frame w/ URM Infill (FS)  → CR/LFINF+FS
# S1  = Steel Moment Frame                 → S/MF
# S2  = Steel Braced Frame                 → S/BF
# S3  = Steel Light Frame                  → S/LF
# S4  = Steel Frame w/ Conc. Shear Walls   → S/LWAL
# S5  = Steel Frame w/ URM Infill          → S/LFINF
# W1  = Wood ≤465m²                        → W
# W2  = Wood >465m²                        → W
# PC1 = Precast Conc. Tilt-Up Walls        → PCR/LWAL
# PC2 = Precast Conc. Frames w/ Shear Walls→ PCR/LDUAL
# RM1 = Reinf. Masonry w/ Wood/Metal Deck  → MR/LWAL
# RM2 = Reinf. Masonry w/ Precast Conc.    → MR/LWAL
# URM/URML = Unreinf. Masonry Bearing Walls→ MUR/LWAL
# MH  = Mobile Homes                       → MH
TAXO_LABEL = {
    "C1":  "CR/MF",      "C2":  "CR/LWAL",      "C3":  "CR/LFINF",
    "C4":  "CR/LFINF+FS",
    "PC1": "PCR/LWAL",   "PC2": "PCR/LDUAL",
    "S1":  "S/MF",       "S2":  "S/BF",         "S3":  "S/LF",
    "S4":  "S/LWAL",     "S5":  "S/LFINF",
    "W1":  "W",          "W2":  "W",
    "MH":  "MH",
    "RM1": "MR/LWAL",    "RM2": "MR/LWAL",
    "URM": "MUR/LWAL",   "URML": "MUR/LWAL",
}

# ── Load data ───────────────────────────────────────────────────────────────
print("Loading data...")
df = pd.read_csv(INPUT_CSV, encoding="utf-8-sig")
print(f"  Total records: {len(df):,}")
print(f"  Columns: {list(df.columns)}")

# Normalise OC_CLASS
df["OC_CLASS"] = df["OC_CLASS"].str.strip().str.upper()
df["OCC_GEM"]  = df["OC_CLASS"].map(OCC_MAP).fillna("Other")
df["OCC_3CAT"] = df["OCC_GEM"].apply(lambda x: x if x in ("Res", "Com") else "Others")

# Normalise ST_TYPE
df["ST_TYPE"]    = df["ST_TYPE"].str.strip().str.upper()
df["MACRO_TAXO"] = df["ST_TYPE"].map(TAXO_LABEL).fillna(df["ST_TYPE"])

# Build a simple GEM-style taxonomy string: MACRO_TAXO / H:<stories> / OCC_GEM
def story_band(n):
    try:
        n = int(n)
        if n <= 1:   return "H:1"
        elif n <= 3: return "H:2-3"
        elif n <= 5: return "H:4-5"
        elif n <= 9: return "H:6-9"
        else:        return "H:10+"
    except:
        return "H:1"

df["STORY_BAND"] = df["STORY"].apply(story_band)
df["STORY_3CAT"] = df["STORY_BAND"].apply(
    lambda x: "Low-rise" if x in ("H:1","H:2-3") else ("Mid-rise" if x in ("H:4-5","H:6-9") else "High-rise"))
df["TAXONOMY"]   = df["MACRO_TAXO"] + "/" + df["STORY_BAND"] + "/" + df["OC_CLASS"]

# ── 1. Exposure_Summary_OccClass.csv  (Adm0 level by occupancy) ────────────
print("\nGenerating Exposure_Summary_OccClass.csv ...")
grp_occ = (df.groupby("OCC_GEM")
             .agg(BUILDINGS=("BLDGID","count"),
                  TOTAL_AREA_SQM=("FL_AREA","sum"))
             .reset_index()
             .rename(columns={"OCC_GEM":"OCCUPANCY"}))
grp_occ.insert(0, "ID_0",   COUNTRY)
grp_occ.insert(1, "NAME_0", COUNTRY_NAME)
grp_occ.insert(2, "ID_1",   PROVINCE)
grp_occ.insert(3, "NAME_1", PROVINCE_NAME)
grp_occ["AVG_BUILDING_AREA_SQM"] = (grp_occ["TOTAL_AREA_SQM"] /
                                      grp_occ["BUILDINGS"]).round(2)
grp_occ = grp_occ.sort_values("BUILDINGS", ascending=False)
grp_occ.to_csv(os.path.join(OUT_DIR, "Exposure_Summary_OccClass.csv"),
               index=False)
print(grp_occ.to_string(index=False))

# ── 2. Exposure_Summary_Taxonomy.csv ────────────────────────────────────────
print("\nGenerating Exposure_Summary_Taxonomy.csv ...")
grp_taxo = (df.groupby(["OCC_GEM","MACRO_TAXO","TAXONOMY"])
              .agg(BUILDINGS=("BLDGID","count"),
                   TOTAL_AREA_SQM=("FL_AREA","sum"))
              .reset_index()
              .rename(columns={"OCC_GEM":"OCCUPANCY"}))
grp_taxo.insert(0, "ID_0",   COUNTRY)
grp_taxo.insert(1, "NAME_0", COUNTRY_NAME)
grp_taxo = grp_taxo.sort_values(["OCCUPANCY","BUILDINGS"],
                                  ascending=[True, False])
grp_taxo.to_csv(os.path.join(OUT_DIR, "Exposure_Summary_Taxonomy.csv"),
                index=False)
print(f"  {len(grp_taxo)} taxonomy groups written.")

# ── 3. Exposure_Summary_STType.csv  (structural type breakdown) ─────────────
print("\nGenerating Exposure_Summary_STType.csv ...")
grp_st = (df.groupby(["MACRO_TAXO","ST_TYPE"])
            .agg(BUILDINGS=("BLDGID","count"),
                 TOTAL_AREA_SQM=("FL_AREA","sum"))
            .reset_index())
grp_st.insert(0, "ID_0",   COUNTRY)
grp_st.insert(1, "NAME_0", COUNTRY_NAME)
grp_st.insert(2, "ID_1",   PROVINCE)
grp_st.insert(3, "NAME_1", PROVINCE_NAME)
grp_st = grp_st.sort_values("BUILDINGS", ascending=False)
grp_st.to_csv(os.path.join(OUT_DIR, "Exposure_Summary_STType.csv"),
              index=False)
print(f"  {len(grp_st)} structural type groups written.")

# ── 4. Exposure_Summary_StoryClass.csv ──────────────────────────────────────
print("\nGenerating Exposure_Summary_StoryClass.csv ...")
grp_ht = (df.groupby(["OCC_GEM","STORY_BAND"])
            .agg(BUILDINGS=("BLDGID","count"),
                 TOTAL_AREA_SQM=("FL_AREA","sum"))
            .reset_index()
            .rename(columns={"OCC_GEM":"OCCUPANCY","STORY_BAND":"HEIGHT_CLASS"}))
grp_ht.insert(0, "ID_0",   COUNTRY)
grp_ht.insert(1, "NAME_0", COUNTRY_NAME)
grp_ht.insert(2, "ID_1",   PROVINCE)
grp_ht.insert(3, "NAME_1", PROVINCE_NAME)
grp_ht.to_csv(os.path.join(OUT_DIR, "Exposure_Summary_StoryClass.csv"),
              index=False)
print(f"  {len(grp_ht)} height-class groups written.")

# ═══════════════════════════════════════════════════════════════════════════
# VISUALIZATIONS
# ═══════════════════════════════════════════════════════════════════════════
COLORS_OCC  = {"Res":"#4C72B0","Com":"#DD8452","Others":"#55A868","Ind":"#C44E52","Other":"#C44E52","Agr":"#8172B2"}
COLORS_TAXO = {
    "CR/LWAL":"#4C72B0","CR/LFINF":"#64B5CD","CR/LDUAL":"#1A6FA1",
    "W":"#55A868","MUR":"#DD8452","S":"#C44E52",
    "PCR":"#8172B2","MH":"#937860",
}

def fmt_k(x, _):
    if x >= 1_000:
        return f"{x/1000:.0f}k"
    return f"{x:.0f}"

# ── Fig 1: Occupancy breakdown — buildings (bar, 3 categories) ─────────────
print("\nPlotting expo_occ_buildings.png ...")
grp_occ3 = (df.groupby("OCC_3CAT")
              .agg(BUILDINGS=("BLDGID","count"),
                   TOTAL_AREA_SQM=("FL_AREA","sum"))
              .reset_index()
              .rename(columns={"OCC_3CAT":"OCCUPANCY"}))
grp_occ3 = grp_occ3.set_index("OCCUPANCY").reindex(["Res","Com","Others"]).reset_index()
fig, ax = plt.subplots(figsize=(6, 4.5))
occ_plot = grp_occ3.set_index("OCCUPANCY")["BUILDINGS"]
bars = ax.bar(occ_plot.index,
              occ_plot.values,
              color=[COLORS_OCC.get(o,"#999") for o in occ_plot.index],
              edgecolor="white", linewidth=0.6, width=0.45)
for bar in bars:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, h + occ_plot.max()*0.01,
            f"{h:,.0f}", ha="center", va="bottom", fontsize=9, fontweight="bold")
ax.set_title("Building Count by Occupancy Class\nChiang Mai, Thailand",
             fontsize=12, fontweight="bold", pad=10)
ax.set_xlabel("Occupancy Class", fontsize=10)
ax.set_ylabel("Number of Buildings", fontsize=10)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(fmt_k))
ax.spines[["top","right"]].set_visible(False)
ax.set_ylim(0, occ_plot.max() * 1.15)
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "expo_occ_buildings.png"), dpi=150, bbox_inches="tight")
plt.close()

# ── Fig 3: Height class distribution (bar, 3 categories) ───────────────────
print("Plotting expo_story_class.png ...")
grp_ht3 = (df.groupby("STORY_3CAT")
             .agg(BUILDINGS=("BLDGID","count"),
                  TOTAL_AREA_SQM=("FL_AREA","sum"))
             .reset_index()
             .rename(columns={"STORY_3CAT":"HEIGHT_CLASS"}))
grp_ht3 = grp_ht3.set_index("HEIGHT_CLASS").reindex(["Low-rise","Mid-rise","High-rise"]).reset_index()
COLORS_HT = {"Low-rise":"#4C72B0","Mid-rise":"#DD8452","High-rise":"#55A868"}
fig, ax = plt.subplots(figsize=(6, 4.5))
ht_plot = grp_ht3.set_index("HEIGHT_CLASS")["BUILDINGS"]
bars = ax.bar(ht_plot.index, ht_plot.values,
              color=[COLORS_HT.get(h,"#999") for h in ht_plot.index],
              edgecolor="white", linewidth=0.6, width=0.45)
for bar in bars:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, h + ht_plot.max()*0.01,
            f"{h:,.0f}", ha="center", va="bottom", fontsize=9, fontweight="bold")
ax.set_title("Building Count by Height Class\nChiang Mai, Thailand",
             fontsize=12, fontweight="bold", pad=10)
ax.set_xlabel("Height Class", fontsize=10)
ax.set_ylabel("Number of Buildings", fontsize=10)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(fmt_k))
ax.spines[["top","right"]].set_visible(False)
ax.set_ylim(0, ht_plot.max() * 1.15)
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "expo_story_class.png"), dpi=150, bbox_inches="tight")
plt.close()

# ── Fig 5: Pie — occupancy share (3 categories) ─────────────────────────────
print("Plotting expo_occ_pie.png ...")
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
for ax, col, label in zip(axes,
                           ["BUILDINGS","TOTAL_AREA_SQM"],
                           ["Buildings","Floor Area (m²)"]):
    vals   = grp_occ3.set_index("OCCUPANCY")[col]
    colors = [COLORS_OCC.get(o,"#999") for o in vals.index]
    wedges, texts, autotexts = ax.pie(
        vals, labels=vals.index, autopct="%1.1f%%",
        colors=colors, startangle=140,
        wedgeprops=dict(edgecolor="white", linewidth=1.2))
    for at in autotexts:
        at.set_fontsize(9)
    ax.set_title(f"Share by {label}", fontsize=11, fontweight="bold")
fig.suptitle("Occupancy Distribution — Chiang Mai, Thailand",
             fontsize=13, fontweight="bold", y=1.01)
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "expo_occ_pie.png"), dpi=150, bbox_inches="tight")
plt.close()

# ── Summary print ────────────────────────────────────────────────────────────
print("\n" + "="*55)
print("  SUMMARY — Chiang Mai Exposure Module")
print("="*55)
print(f"  Total buildings      : {len(df):>10,}")
print(f"  Total floor area (sqm): {df['FL_AREA'].sum():>15,.0f}")
print(f"  Unique OC_CLASS      : {df['OC_CLASS'].nunique():>10}")
print(f"  Unique ST_TYPE       : {df['ST_TYPE'].nunique():>10}")
print(f"  Unique Tags          : {df['Tag'].nunique():>10}")
print("="*55)
print("\nFiles generated:")
for f in ["Exposure_Summary_OccClass.csv","Exposure_Summary_Taxonomy.csv",
          "Exposure_Summary_STType.csv","Exposure_Summary_StoryClass.csv",
          "expo_occ_buildings.png","expo_story_class.png","expo_occ_pie.png"]:
    path = os.path.join(OUT_DIR, f)
    size = os.path.getsize(path) if os.path.exists(path) else 0
    print(f"  [ok] {f}  ({size/1024:.1f} KB)")

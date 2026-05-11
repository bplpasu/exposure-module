# Exposure Module — Statistics Reference Sheet

**Use this sheet to manually revise `Exposure Module.docx`**  
**CSV basis:** `data/Exposure-Module.csv` — 96,635 buildings, fully surveyed, no imputation  
**Last updated:** 2026-05-11

---

## Legend
| Symbol | Meaning |
|---|---|
| ✅ | Number confirmed updated in `exposure-module-claude.docx` |
| ✏️ | Needs to be changed — old value → new value shown |
| ❓ | Cannot derive from CSV — needs original survey records |
| ⚠️ | Internal inconsistency in the paper draft — flag with professor |

---

## §4.1 — Building Data Collection

| Location in paper | Old value | **New value** | Status |
|---|---|---|---|
| Buildings digitized (satellite) | 109,782 | **118,583** | ✅ |
| Actively utilized after screening | 103,743 | ❓ unknown | ❓ need from records |
| GSV Round 1 complete | 72,491 | ❓ unknown | ❓ need from records |
| Total needing supplement (GSV2) | 31,252 | ❓ unknown | ❓ need from records |
| GSV2 successfully classified | 20,155 (64.49%) | **19,014** (recalc once open spaces known) | ❓ % pending |
| GSV2 open spaces | 3,391 (10.85%) | ❓ unknown | ❓ need from records |
| GSV2 inaccessible | 7,706 (24.66%) | **7,706 → Field Survey R2 → 4,223 real buildings** | ✅ |
| Total buildings (post-screening) | 100,352 | **96,635** | ✅ |
| Complete / surveyed | 92,646 (92.32%) | **96,635 (100%)** | ✅ |
| Statistically imputed | 7,706 | **0 — all buildings directly surveyed** | ✅ |
| C3 pre-imputation | 74,415 (80.32%) | **80,849 (83.66%)** | ✅ |
| C3 post-imputation | 85,149 (84.85%) | **80,849 (83.66%)** | ✅ |
| RES1+C3 pre-imputation | 56,339 (60.81%) | **61,071 (63.20%)** | ✅ |
| RES1+C3 post-imputation | 63,689 (63.46%) | **61,071 (63.20%)** | ✅ |
| COM1+C3 pre-imputation | 5,880 (6.34%) | **5,697 (5.90%)** | ✅ |
| COM1+C3 post-imputation | 6,927 (6.90%) | **5,697 (5.90%)** | ✅ |
| RES1+W1 pre-imputation | 4,271 (4.61%) | **4,565 (4.72%)** | ✅ |
| RES1+W1 post-imputation | 4,540 (4.52%) | **4,565 (4.72%)** | ✅ |

> **Pending block:** Once the open-spaces count is confirmed, the 3 ❓ rows above (103,743 / 72,491 / 31,252 / 3,391 / percentages) can all be recomputed and updated in one pass.

---

## §4.2.1 — Basic-Level Survey (n = 4,118 buildings — do NOT change)

These come from the field-walking sample, not the full CSV. They stay as-is unless the basic-level dataset is re-counted.

| Metric | Value | Note |
|---|---|---|
| Basic-level survey total | 4,118 | Keep |
| C3 (basic-level) | 3,101 (75.21%) | Keep — ⚠️ see inconsistency below |
| W1 (basic-level) | 350 (8.50%) | Keep |

---

## §4.2.2 — Occupancy (Basic-Level Sample — do NOT change)

| Metric | Value | Note |
|---|---|---|
| Residential buildings surveyed | 2,600 | Keep |
| RES1 of all residential | 2,036 (78.25%) | Keep |
| RES3 of all residential | ~15.6% | Keep |
| RES4 of all residential | ~4.5% | Keep |
| Commercial buildings surveyed | 988 | Keep |
| COM1 of all commercial | 352 (40.23%) | Keep |
| COM3 of all commercial | 174 (19.89%) | Keep |
| COM8 of all commercial | 155 (17.71%) | Keep |
| Terraced buildings | 324 (32.01% of 988 commercial) | Keep |
| Individual units in terraced | 1,929 | Keep |
| COM1 units in terraced | 622 (32.24%) | Keep |
| COM3 units in terraced | 503 (26.08%) | Keep |
| COM8 units in terraced | 342 (17.73%) | Keep |

---

## §4.2.3 — Cross-Tab (Basic-Level Sample — do NOT change)

| Metric | Value | Note |
|---|---|---|
| RES1+C3 | 1,638 (39.77%) | Keep — ⚠️ see inconsistency below |
| RES3+C3 | 366 (8.89%) | Keep |
| COM1+C3 | 313 (7.6%) | Keep |

---

## §4.2.5 — Building Condition (Basic-Level Sample — do NOT change)

| Metric | Value | Note |
|---|---|---|
| Normal condition | 2,843 (69.03%) | Keep — ⚠️ see inconsistency below |
| RES Normal | 1,915 | Keep |
| COM Normal | 695 | Keep |
| RES Good / Poor | 471 / 429 | Keep |
| COM Good / Poor | 172 / 126 | Keep |

---

## §4.2.7 — Height (Basic-Level Sample — do NOT change)

| Metric | Value | Note |
|---|---|---|
| C3 buildings, 2-storey | 1,280 (41.27%) | Keep |
| C3 buildings, 1-storey | 1,201 (38.73%) | Keep |

---

## §4.3 — Combined GSV + Basic-Level

| Location | Old value | Status |
|---|---|---|
| C3 used as basis | 72,049 (65.63%) | ⚠️ Denominator unclear — not in old or new CSV |

---

## §5 — Conclusion

| Metric | Old | **New** | Status |
|---|---|---|---|
| Total buildings | 100,352 | **96,635** | ✏️ Update |
| C3 % (full population) | 83.70% | **83.66%** | ✏️ Update |
| Wood % (full population) | 5.74% | **5.91%** | ✏️ Update |
| Steel % (full population) | 4.21% | **4.31%** | ✏️ Update |
| RES1 % (full population) | 70.20% | **70.24%** | ✏️ Update |
| C3 % (basic-level) | 80.89% | Keep | ⚠️ see inconsistency below |
| Wood % (basic-level) | 10.97% | Keep | |
| Steel % (basic-level) | 4.702% | Keep | |
| RES1 % (basic-level) | 51.19% | Keep | |

---

## Survey Method Breakdown (for §4.1 narrative)

| Tag | Old CSV | **New CSV** | Change |
|---|---|---|---|
| GSV | 96,607 | **88,848** | −7,759 |
| Field Survey Round 1 | 3,745 | **3,564** | −181 |
| Field Survey Round 2 | — | **4,223** | +4,223 (new) |
| **Total** | **100,352** | **96,635** | −3,717 |

---

## Full Population Statistics (New CSV — for reference)

| Metric | Value |
|---|---|
| Total buildings | 96,635 |
| GSV | 88,848 |
| Field Survey Round 1 | 3,564 |
| Field Survey Round 2 | 4,223 |
| C3 | 80,849 (83.66%) |
| W1 + W2 (Wood) | 5,715 (5.91%) |
| Steel S1–S5 | 4,165 (4.31%) |
| C1 | 4,163 (4.31%) |
| C2 | 947 (0.98%) |
| RES1 | 67,874 (70.24%) |
| Residential (all RES) | 74,650 (77.25%) |
| Commercial (all COM) | 16,952 (17.54%) |
| Others (IND, AGR, GOV, EDU, REL) | 5,033 (5.21%) |
| Low-rise (1–3 storeys) | 93,019 (96.26%) |
| Mid-rise (4–9 storeys) | 3,517 (3.64%) |
| High-rise (10+ storeys) | 99 (0.10%) |
| Total floor area | 38,967,956 m² |
| Avg floor area per building | 403.25 m² |
| RES1 + C3 | 61,071 (63.20%) |
| COM1 + C3 | 5,697 (5.90%) |
| RES1 + W1 | 4,565 (4.72%) |

---

## ⚠️ Internal Inconsistencies to Resolve with Professor

| Section | Issue |
|---|---|
| §4.2.1 vs §4.2.3 vs §5 | C3 share of basic-level survey given as **75.21%** (§4.2.1), **75.30%** (§4.2.3), and **80.89%** (§5 Conclusion) — three different values for the same dataset |
| §4.2.5 | Normal-condition total stated as **2,843** but RES (1,915) + COM (695) = **2,610** — the sum does not match; either another primary class is included or one figure is wrong |
| §4.3 | Cites **72,049 buildings (65.63%)** as the C3 basis — this figure does not appear in either the old or new CSV and the denominator is not stated |

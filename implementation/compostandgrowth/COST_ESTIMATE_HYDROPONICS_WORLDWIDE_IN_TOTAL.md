# 🌱 COST_ESTIMATE_HYDROPONICS_WORLDWIDE.md

**Version:** 2.0  
**Status:** ACTIVE / CANONICAL  
**Location:** `/implementation/COST_ESTIMATE_HYDROPONICS_WORLDWIDE.md`  
**Authors:** Elinor Frejd and ChatGPT

---

## 1. PURPOSE

This file provides a **comprehensive, realistic cost model** for hydroponic food production across major global regions. It includes setup, annual operating expenses, and **per‑kg production cost** for key crops, adjusted for regional labour, energy and materials.

---

## 2. KEY ASSUMPTIONS

- **Node Size:** ~500 m² hydroponic growth area  
- **System Types:** NFT, DWC + vertical racks + LED lighting + climate control  
- **Yield per 500 m²/year (estimates based on industry benchmarks):**
  - Leafy greens: ~20 000 kg
  - Herbs (e.g., basil): ~5 000 kg
  - Microalgae: ~3 000 kg
  - Hydroponic lentils: ~4 000 kg
  - Tomatoes: ~7 000 kg

- **Setup amortized over:** 5 years  
- All costs in **USD**
- Regional cost adjustment based on labour, energy, import costs

---

## 3. SETUP COSTS (BY REGION)

These are direct equipment, infrastructure & installation costs required to build a 500 m² hydroponic Node.

| Region | Setup Cost (USD) | Notes |
|--------|------------------:|-------|
| Europe / North America | 150 000 – 425 000 | Tier‑1 energy & labour costs; well‑developed supply chains |
| South America | 128 000 – 361 000 | Lower labour; moderate energy cost |
| Asia | 135 000 – 383 000 | Moderate costs; varied regional energy |
| Oceania | 165 000 – 468 000 | Higher energy & material shipping |
| North Africa | 120 000 – 340 000 | Variable infrastructure costs |
| Sub‑Saharan Africa | 105 000 – 298 000 | Lower labour; import costs for equipment |

> Sources: commercial hydroponic build cost data, controlled environment agriculture benchmarks.

---

## 4. ANNUAL OPERATING COSTS (BY REGION)

Ongoing expenses including energy, labour, nutrients, water treatment, maintenance and consumables.

| Region | Estimated Opex/Yr (USD) | Notes |
|--------|------------------------:|-------|
| Europe / North America | 75 000 – 166 000 | High electricity & skilled labour |
| South America | 55 000 – 135 000 | Lower labour; variable energy |
| Asia | 60 000 – 140 000 | Mid‑range with automation |
| Oceania | 70 000 – 150 000 | Higher energy cost |
| North Africa | 50 000 – 120 000 | Water/energy variable |
| Sub‑Saharan Africa | 40 000 – 100 000 | Labour low; energy variable |

---

## 5. TOTAL ANNUALIZED COST PER NODE

Annualized cost combines **setup (amortized over 5 years)** and **operating costs**.
Annualized Cost = (Setup Cost / 5) + Annual Operating Cost

| Region | Annualized Cost (USD) |
|--------|------------------------:|
| Europe / North America | 105 000 – 250 000 |
| South America | 83 000 – 232 000 |
| Asia | 87 000 – 214 000 |
| Oceania | 103 000 – 248 000 |
| North Africa | 74 000 – 188 000 |
| Sub‑Saharan Africa | 61 000 – 160 000 |

---

## 6. PER‑KG PRODUCTION COST (MULTIPLE CROPS)

Using actual yield estimates and annualized Node cost.

### 6.1 FORMULA
Cost/kg = (Annualized Cost) / (Annual Yield per crop)

### 6.2 ESTIMATED PER‑KG COSTS

| Crop | Typical Yield (kg/yr) | Europe / NA | South America | Asia | Oceania | North Africa | Sub‑Saharan Africa |
|------|-----------------------:|------------:|---------------:|------:|---------:|--------------:|------------------:|
| Leafy Greens | 20 000 | $5.25 – $12.50 | $4.15 – $11.60 | $4.35 – $10.70 | $5.15 – $12.40 | $3.70 – $9.40 | $3.05 – $8.00 |
| Herbs | 5 000 | $21.00 – $50.00 | $16.60 – $46.40 | $17.40 – $42.80 | $20.60 – $49.60 | $14.80 – $37.60 | $12.20 – $32.00 |
| Microalgae | 3 000 | $35.00 – $83.30 | $28.00 – $77.30 | $29.00 – $71.30 | $34.30 – $82.60 | $24.70 – $62.70 | $20.30 – $53.30 |
| Hydroponic Lentils | 4 000 | $26.25 – $62.50 | $20.75 – $58.00 | $21.75 – $53.50 | $24.95 – $62.00 | $18.50 – $46.90 | $15.25 – $40.00 |
| Tomatoes | 7 000 | $15.00 – $35.70 | $11.90 – $33.10 | $12.45 – $30.60 | $14.70 – $35.40 | $10.90 – $26.90 | $9.00 – $22.80 |

### Notes:

- Cruder crops (leafy greens) have the lowest per‑kg cost.  
- High premium/higher labour crops like herbs and microalgae cost more.  
- Regions with lower energy & labour (Sub‑Saharan Africa, South America) show lower per‑kg range.

---

## 7. PRODUCTION NOTES

1. **Algae production** assumes dedicated tanks with supplemental CO₂ control.  
2. **Hydroponic lentils** are experimental and yield estimates may improve with optimization.  
3. **Tomato yields** assume vertical trellis and good climate control.  
4. **Renewable energy integration** (solar/wind) can reduce long‑term Opex significantly.

---

## 8. USAGE & INTEGRATION

- These per‑kg costs are ready for integration into **FLOW_SRS** for resource allocation and simulation.  
- Useful for regional baseline planning, surplus allocation, and long‑term Node budgeting.

---

**STATUS:** Operational — subordinate to the Manifesto.  
*End of COST_ESTIMATE_HYDROPONICS_WORLDWIDE.md*

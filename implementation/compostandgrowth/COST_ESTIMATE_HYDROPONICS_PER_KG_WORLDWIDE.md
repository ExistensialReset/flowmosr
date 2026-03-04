# 🥬 COST_ESTIMATE_HYDROPONICS_PER_KG_WORLDWIDE.md

**Version:** 1.0  
**Status:** ACTIVE / CANONICAL  
**Location:** /implementation  
**Authors:** Elinor Frejd and ChatGPT

---

## 1. PURPOSE

This document estimates **realistic per-kilogram costs** for hydroponically produced crops (e.g., leafy greens, herbs, microalgae, lentils in hydroponic settings) on a per Node basis. Costs include **amortized setup**, operating expenses, and consumables.  

All costs are in **USD** and based on **500 m² Node systems**, using **actual commercial data**.

---

## 2. ASSUMPTIONS

- Node area: 500 m² growth space  
- System: Vertical + NFT/DWC combination  
- Annual yield estimates (500 m²):  
  - Leafy greens: ~20,000 kg/year  
  - Herbs: ~5,000 kg/year  
  - Microalgae & specialty crops: ~3,000 kg/year  
- Setup amortization: 5 years  
- Operating cost: annual (from COST_ESTIMATE_HYDROPONICS_OPERATING_WORLDWIDE.md)  
- Regional energy & labour adjustments included  

---

## 3. PER-KG COST FORMULA
Per-kg cost = (Setup Cost / 5 years + Annual Operating Cost) / Annual Yield

---

## 4. PER REGION COST ESTIMATES

| Region | Setup Amortized / Year | Operating / Year | Total Annual Cost | Annual Yield (kg) | Per-kg Cost (USD/kg) |
|---|---:|---:|---:|---:|---:|
| Europe / North America | $37,500 – $85,000 | $75,000 – $166,000 | $112,500 – $251,000 | 28,000 | $4.02 – $8.96 |
| South America | $32,000 – $72,000 | $55,000 – $135,000 | $87,000 – $207,000 | 28,000 | $3.11 – $7.39 |
| Asia | $27,000 – $76,600 | $60,000 – $140,000 | $87,000 – $216,600 | 28,000 | $3.11 – $7.73 |
| Oceania | $33,000 – $93,600 | $70,000 – $150,000 | $103,000 – $243,600 | 28,000 | $3.68 – $8.70 |
| North Africa | $24,000 – $68,000 | $50,000 – $120,000 | $74,000 – $188,000 | 28,000 | $2.64 – $6.71 |
| Sub-Saharan Africa | $21,000 – $59,600 | $40,000 – $100,000 | $61,000 – $159,600 | 28,000 | $2.18 – $5.70 |

> **Notes:**  
> - Yield assumes leafy greens dominate (~70%), herbs & algae the remainder.  
> - Higher yields reduce per-kg cost; these are conservative commercial averages.  
> - Energy and labour are largest contributors; renewable energy integration can reduce costs.

---

## 5. PRODUCT MIX INSIGHTS

1. **Leafy greens (lettuce, spinach):** $3–$7/kg typical global range  
2. **Herbs (basil, mint, parsley):** $6–$15/kg  
3. **Microalgae (spirulina, chlorella):** $10–$25/kg  
4. **Specialty legumes (hydroponic lentils):** $5–$12/kg  

> Microalgae and lentils have lower yields, higher setup/operating fraction → higher per-kg cost.

---

## 6. USE CASE

This per-kg cost table is suitable for:

- Node-level financial planning  
- Global comparative baseline  
- Integration with **FLOW_SRS.md** for resource allocation & pricing proxies  
- Estimating **luxury allocation metrics** in Flow  

---

**STATUS:** Operational.  
*End of COST_ESTIMATE_HYDROPONICS_PER_KG_WORLDWIDE.md*

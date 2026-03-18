# 📊 INFORMATION_COORDINATION_WITHOUT_PRICES.md

**Version:** 1.0  
**Status:** OPERATIONAL PROTOCOL  
**Repository Location:** `/systemic/INFORMATION_COORDINATION_WITHOUT_PRICES.md`  
**Authors:** Elinor Frejd & Claude  
**Related:** FLOW_ECONOMIC_PRINCIPLES.md, RESOURCE_METRIC_STANDARDS.md, ANONYMOUS_RESOURCE_TRACKING_IN_FLOW.md  
**Date:** March 18, 2026

---

## PURPOSE

> "Prices communicate scarcity and priority. We must replace this function, not just eliminate it."

**The Challenge:**

In Mammon, prices do three critical things:
1. **Signal scarcity** (high price = scarce resource)
2. **Communicate production cost** (expensive = resource-intensive to make)
3. **Enable decentralized coordination** (people respond to prices without central planning)

**When Flow eliminates currency, we must replace these information functions.**

This document specifies HOW.

---

## CORE PROBLEM

**Price is not just power. Price is information.**

### What Information Prices Communicate:

**Example in Mammon:**
- Steel costs $800/ton
- Aluminum costs $2,400/ton
- **Signal:** Aluminum is 3× more scarce/expensive than steel
- **Response:** Engineers design with steel when possible, use aluminum only when necessary

**In Flow without prices:**
- How does engineer know aluminum is more resource-intensive?
- How do we communicate "use this sparingly, use that freely"?
- How do we coordinate production priorities without price signals?

**If we fail to replace this information system:**
- Resources misallocated
- Bottlenecks unpredicted
- Production inefficient
- System fails to scale

---

## SOLUTION: MULTI-LAYERED INFORMATION SYSTEM

Flow replaces price with **five complementary information mechanisms:**

1. **Resource Impact Scores (RIS)** - Quantified environmental/labor cost
2. **Scarcity Indicators (Real-Time)** - Current availability vs. demand
3. **Production Feedback Loops** - Direct communication from producers
4. **Transparent Reserve Levels** - Public inventory data
5. **Priority Signaling via LOTUS** - Democratic allocation decisions

**None alone replaces price. Together, they provide richer information than price ever could.**

---

## MECHANISM 1: Resource Impact Scores (RIS)

**What it is:**
A standardized metric for every material/product showing:
- Energy cost to produce
- Material inputs required
- Labor hours involved
- Environmental impact
- Repairability/longevity

**Think:** Nutrition label but for resources.

### Example RIS Card:

ALUMINUM (per ton)
├─ Energy: 15,000 kWh (HIGH)
├─ Water: 500L (MEDIUM)
├─ Labor: 40 hours (MEDIUM)
├─ CO₂: 12 tons (VERY HIGH)
├─ Recyclability: 95% (EXCELLENT)
├─ Scarcity: MODERATE
└─ Recommendation: Use sparingly, prioritize recycling


STEEL (per ton)
├─ Energy: 6,000 kWh (MEDIUM)
├─ Water: 200L (LOW)
├─ Labor: 30 hours (LOW-MEDIUM)
├─ CO₂: 2 tons (MODERATE)
├─ Recyclability: 90% (EXCELLENT)
├─ Scarcity: LOW
└─ Recommendation: Preferred structural material



**How it works:**

**Step 1: Calculation**
- Energy, water, labor tracked during production
- Environmental impact calculated (CO₂, toxicity, habitat disruption)
- Data aggregated across production chain

**Step 2: Standardization**
- All materials scored on same scales
- Published in Material Database (accessible to all)
- Updated quarterly based on actual production data

**Step 3: Decision Support**
- Engineer designing building sees: Steel RIS = 6,000 kWh/ton, Aluminum RIS = 15,000 kWh/ton
- Decision: Use steel for structure, aluminum only where essential (lightweight, corrosion resistance)

**Step 4: LOTUS Override**
- If material becomes critically scarce, LOTUS can flag it "RESTRICTED" regardless of RIS
- Democratic decision > algorithm

### RIS Categories:

| Score | Energy | Label | Usage Recommendation |
|-------|--------|-------|---------------------|
| 0-1,000 kWh | Very Low | ABUNDANT | Use freely |
| 1,000-5,000 | Low | COMMON | Standard use |
| 5,000-10,000 | Medium | MODERATE | Consider alternatives |
| 10,000-20,000 | High | CAREFUL | Use sparingly |
| 20,000+ | Very High | RESTRICTED | Only essential uses |

**Transparency:**
- All RIS calculations public
- Methodology documented
- Anyone can audit
- Disagreements resolved via LOTUS

**Benefits over price:**
- Shows WHY something is expensive (energy? labor? environment?)
- Doesn't hide externalities (CO₂ visible, not ignored)
- Can't be manipulated by speculation
- Directly reflects material reality

---

## MECHANISM 2: Scarcity Indicators (Real-Time)

**What it is:**
Live dashboard showing current availability vs. demand for all tracked resources.

**Think:** Traffic light system for resources.

### Scarcity Levels:

**GREEN (Abundant):**
- Current stock >3 months demand
- Production exceeds consumption
- Recommendation: Normal use

**YELLOW (Moderate):**
- Current stock 1-3 months demand
- Production ≈ consumption
- Recommendation: Monitor, consider conservation

**ORANGE (Tight):**
- Current stock <1 month demand
- Consumption > production
- Recommendation: Reduce non-essential use, increase production

**RED (Critical):**
- Current stock <2 weeks demand
- Severe shortage
- Recommendation: Emergency protocols, LOTUS intervention

### Example Dashboard (Node-Level):

FOOD RESOURCES
├─ Grain: GREEN (6 months stock)
├─ Vegetables: YELLOW (2 months stock)
├─ Protein: YELLOW (1.5 months stock)
└─ Cooking Oil: ORANGE (3 weeks stock) ⚠️
​ENERGY
├─ Solar: GREEN (excess capacity)
├─ Battery Storage: YELLOW (70% capacity)
└─ Backup Generator Fuel: RED (1 week supply) 🚨
​MATERIALS
├─ Steel: GREEN (abundant)
├─ Copper: ORANGE (2 weeks stock) ⚠️
├─ Rare Earth Metals: RED (critically low) 🚨
└─ Wood: GREEN (sustainable harvest)


**How it works:**

**Step 1: Automated Tracking**
- All production, consumption, storage tracked in real-time
- Algorithm calculates current stock vs. average consumption rate
- Color-coded automatically

**Step 2: Public Display**
- Dashboard accessible to everyone
- Updated hourly
- Historical trends shown

**Step 3: Behavioral Response**
- People see RED → voluntarily reduce use
- Producers see ORANGE → increase production
- LOTUS sees RED → allocates resources, requests inter-Node aid

**Step 4: Emergency Protocols**
- If critical resource hits RED for 48 hours → automatic LOTUS emergency panel
- Can reallocate, request aid, ration if necessary

**Privacy maintained:**
- Aggregate data only
- No individual consumption tracked
- Circle-level data stays within Circle

**Benefits over price:**
- Real-time (price lags actual scarcity)
- Transparent (everyone sees same info)
- Can't be gamed by hoarding/speculation
- Shows trend (getting better/worse)

---

## MECHANISM 3: Production Feedback Loops

**What it is:**
Direct communication channel from producers to consumers about constraints, bottlenecks, needs.

**Think:** Production transparency + request system.

### How it works:

**Producers report:**
- "We can increase vegetable production if we get more compost"
- "Solar panel production limited by copper shortage"
- "Bread production could expand but need more bakers"

**Consumers see:**
- "Bread available but production constrained by labor"
- "Tomatoes plentiful, cucumbers limited by greenhouse space"

**LOTUS responds:**
- Allocate compost to vegetable growers
- Prioritize copper for solar panels
- Recruit/train more bakers

### Example Production Report


BAKERY PRODUCTION REPORT (Week 12)
─────────────────────────────────
Current Output: 5,000 loaves/week
Potential Output: 8,000 loaves/week
​CONSTRAINTS:
├─ Labor: Need 2 more bakers (CRITICAL)
├─ Ovens: At capacity, need 1 more (MODERATE)
├─ Flour: Sufficient supply (OK)
└─ Energy: Sufficient (OK)
​REQUESTS:
├─ 2 trained bakers (urgent)
├─ 1 commercial oven (cost: 200 hours labor + materials)
└─ Expansion of workspace (20m²)
​IF CONSTRAINTS REMOVED:
→ Can increase output 60%
→ Reduce wait times for fresh bread
→ Enable experimental baking (variety)

**Consumer sees:**
- "Bread available daily, but bakery could produce more if we had more bakers. Interested in baking? Contact Lyceum for training."

**LOTUS sees:**
- Bakery constraint = labor, not materials
- Allocate resources for oven if bakers recruited
- Otherwise, resources better spent elsewhere

**Benefits:**
- Direct producer-consumer communication
- Bottlenecks visible immediately
- Coordination without central planning
- Transparent decision-making

---

## MECHANISM 4: Transparent Reserve Levels

**What it is:**
Public inventory data for all stored resources.

**Think:** Open books, but for physical goods.

### What is tracked:

**Food Reserves:**
- Current stock (tons)
- Months of Baseline coverage
- Seasonal variation
- Spoilage/waste rates

**Energy Reserves:**
- Battery storage levels
- Backup fuel
- Solar/wind capacity vs. demand

**Material Stockpiles:**
- Building materials
- Medical supplies
- Tool inventory
- Spare parts

### Example Reserve Dashboard:

GRAIN RESERVES (Node Level - 500 people)
─────────────────────────────────────────
Current Stock: 18,000 kg
Baseline Requirement: 3,000 kg/month (6 kg/person/month)
Coverage: 6 months ✓ (Target: 3-6 months)
​TREND: ↗ Increasing (harvest season)
QUALITY: 95% excellent, 5% aging (use soon)
WASTE: 2% (spoilage, within acceptable range)
​PRODUCTION vs CONSUMPTION:
├─ Last month production: 4,000 kg
├─ Last month consumption: 3,200 kg
└─ Net: +800 kg (surplus)
​RECOMMENDATIONS:
├─ Surplus available for inter-Node sharing
├─ Consider rotating stock (use older grain first)
└─ Storage conditions good, maintain current protocols

**How it works:**

**Step 1: Inventory Tracking**
- Physical stock counted weekly (manual or sensor-based)
- Data entered into system
- Automatically calculated against Baseline needs

**Step 2: Public Publication**
- All data visible to all Node members
- Regional/Network level aggregates also published
- Historical data preserved for trend analysis

**Step 3: Decision Support**
- Individuals can see "do we have enough?"
- Circles can plan consumption
- LOTUS can see inter-Node sharing opportunities

**Benefits:**
- No hidden reserves (prevents hoarding)
- Everyone can verify Baseline security
- Enables trust-based sharing between Nodes
- Shows seasonal patterns (prepare for scarcity)

---

## MECHANISM 5: Priority Signaling via LOTUS

**What it is:**
Democratic allocation decisions when resources scarce or contested.

**Think:** Collective prioritization without price rationing.

### When LOTUS allocates:

**Scenario 1: Multiple demands, limited resource**
- 3 projects need copper
- Only enough copper for 2 projects
- **LOTUS decides:** Which 2 projects are highest priority?

**Scenario 2: Emergency scarcity**
- Drought reduces food production
- Baseline threatened
- **LOTUS decides:** Ration non-Baseline uses, allocate to Baseline first

**Scenario 3: Long-term investment**
- Build new solar capacity OR new workshop?
- Both beneficial, resources for one
- **LOTUS decides:** Which benefits community most?

### Example LOTUS Allocation Decision:


COPPER SHORTAGE - ALLOCATION DECISION
─────────────────────────────────────
​AVAILABLE COPPER: 500 kg
REQUESTS:
​Solar panel production: 300 kg (ongoing)
​New electrical wiring for housing: 200 kg (new)
​Repair workshop expansion: 150 kg (new)
​TOTAL REQUESTED: 650 kg
SHORTFALL: 150 kg
​LOTUS PANEL REVIEWS:
├─ Solar panels = Baseline energy (high priority)
├─ Housing wiring = Baseline shelter safety (high priority)
├─ Workshop expansion = Quality of life (medium priority)
​EXPERT INPUT:
├─ Energy specialist: Solar production critical for winter
├─ Electrician: Housing wiring needed for 20 new residents
├─ Workshop coordinator: Expansion nice but not urgent
​LOTUS DECISION (72% agreement):
├─ Allocate 300 kg to solar panels ✓
├─ Allocate 200 kg to housing wiring ✓
├─ Defer workshop expansion (wait for next copper shipment)
​REASONING PUBLISHED:
"Baseline energy and shelter safety prioritized over quality-of-life expansion. Workshop expansion approved pending next inter-Node copper delivery (estimated 6 weeks)."

**How it works:**

**Step 1: Scarcity Detected**
- Scarcity Indicator shows ORANGE or RED
- Multiple demands exceed supply
- Automatic LOTUS trigger

**Step 2: Information Gathering**
- All requesting parties submit justifications
- Expert testimony (if technical)
- Impact assessments (RIS, Baseline relevance, urgency)

**Step 3: Deliberation**
- LOTUS panel reviews (48-72 hours)
- Transparent criteria: Baseline > Infrastructure > Quality of Life > Luxury
- Public questions period

**Step 4: Decision**
- Vote
- Decision published with reasoning
- Losing requestors notified with timeline for future allocation

**Benefits:**
- Democratic (not market-based)
- Transparent (reasoning public)
- Prioritizes Baseline structurally
- Flexible (can adapt to unique situations)

---

## INTEGRATION: How Mechanisms Work Together

### Example: Planning a New Building

**Person wants to build community workshop.**

**Step 1: Consult RIS**
- Steel: 6,000 kWh/ton (MEDIUM)
- Concrete: 800 kWh/ton (LOW)
- Aluminum: 15,000 kWh/ton (HIGH)
- **Decision:** Use steel frame, concrete foundation, minimize aluminum

**Step 2: Check Scarcity Indicators**
- Steel: GREEN (abundant)
- Concrete: YELLOW (moderate, but sufficient)
- Copper (for wiring): ORANGE (tight)
- **Decision:** Proceed with steel/concrete, minimize copper use

**Step 3: Review Production Feedback**
- Steelworks: "Can produce structural steel, 2-week lead time"
- Concrete plant: "Ready to supply, need 1 week notice"
- Electrician: "Copper limited, use efficient wiring design"
- **Decision:** Coordinate timelines, design copper-minimal electrical system

**Step 4: Check Reserve Levels**
- Steel reserves: 4 months stock (good)
- Concrete: 2 months stock (adequate)
- Copper: 3 weeks stock (concerning)
- **Decision:** Confirm materials available before starting

**Step 5: Submit to LOTUS (if needed)**
- If copper allocation contested, LOTUS decides priority
- Workshop proposal competes with other copper needs
- LOTUS evaluates: Baseline relevance, community benefit, urgency

**Result:** Building designed efficiently, materials allocated responsibly, community needs balanced democratically.

**No prices needed. Information flows through:**
- RIS (material impact)
- Scarcity Indicators (availability)
- Production Feedback (feasibility)
- Reserve Levels (stockpile security)
- LOTUS (democratic allocation)

---

## COMPARISON: Price vs Flow Information System

| Function | Price (Mammon) | Flow System |
|----------|---------------|-------------|
| **Signal scarcity** | High price | Scarcity Indicator (color-coded) |
| **Show production cost** | Price reflects cost | RIS shows energy, labor, environment |
| **Coordinate allocation** | Market equilibrium | LOTUS democratic allocation |
| **Enable planning** | Price trends | Reserve levels + Production feedback |
| **Respond to change** | Price fluctuates | Real-time dashboards + LOTUS adjustments |
| **Transparency** | Opaque (speculation, manipulation) | Fully transparent (all data public) |
| **Externalities** | Hidden (pollution not priced) | Explicit (CO₂ in RIS) |
| **Equity** | Rationing by wealth | Rationing by need + LOTUS priority |

**Flow system advantages:**
- Shows WHY things are scarce (not just THAT they are)
- Can't be manipulated by speculation
- Includes environmental costs explicitly
- Democratic allocation instead of wealth-based
- Richer information (RIS more detailed than price)

**Flow system challenges:**
- Requires active participation (not passive market response)
- LOTUS decision-making takes time (not instantaneous like price)
- Information infrastructure needs maintenance
- Cultural shift from price-thinking to systems-thinking

---

## FAILURE MODES & RESPONSES

### 1. Information Overload

**Risk:** Too much data, people can't process it

**Indicators:**
- Scarcity dashboards ignored
- RIS unused
- Decisions made without consulting information

**Response:**
1. **Simplify displays:** Focus on most critical metrics
2. **AI summarization:** "Top 3 resource concerns this week"
3. **Education:** Teach people how to use tools
4. **Default recommendations:** System suggests "use steel, avoid aluminum" automatically
5. **Gradual rollout:** Start simple, add complexity as people adapt

---

### 2. Gaming the System (False Scarcity)

**Risk:** Producers report false scarcity to get priority

**Indicators:**
- Scarcity reported but reserves full
- Production constraints claimed without evidence
- Pattern of exaggeration from specific producers

**Response:**
1. **Verification:** Random audits of inventory claims
2. **Transparency:** All reserve data public, anyone can verify
3. **Peer reporting:** Whistleblower protections for false scarcity reports
4. **Sanctions:** False reporting treated as serious harm (undermines trust)
5. **LOTUS review:** If suspected manipulation, independent investigation

---

### 3. LOTUS Decision Paralysis

**Risk:** Too many allocation decisions, LOTUS overwhelmed

**Indicators:**
- Allocation decisions delayed >7 days
- LOTUS meetings constant
- Frustration with slow process

**Response:**
1. **Default rules:** 80% of allocations follow automatic priority (Baseline > Infrastructure > Quality)
2. **Delegation:** Routine decisions delegated to Circles, LOTUS only for contested/large
3. **Fast track:** Emergency allocations within 24 hours
4. **Simplify:** Reduce number of resources requiring LOTUS allocation (only scarce/contested)

---

### 4. Regional Information Gaps

**Risk:** Inter-Node coordination fails due to information asymmetry

**Indicators:**
- Node A has surplus, Node B has shortage, but no exchange happens
- Scarcity Indicators not shared between Nodes
- Production feedback isolated to local Node

**Response:**
1. **Regional dashboards:** All Nodes publish scarcity indicators to Regional Network
2. **Automatic matching:** Algorithm suggests "Node A has surplus grain, Node B needs grain"
3. **Coordination LOTUS:** Regional panels for inter-Node allocation
4. **Communication protocols:** Weekly inter-Node resource reports

---

### 5. RIS Calculation Disputes

**Risk:** Disagreement over how to calculate Resource Impact Scores

**Indicators:**
- Different Nodes use different RIS methodologies
- Producers challenge their material's scores
- Environmental impact contested

**Response:**
1. **Standardization:** Single RIS methodology across all Nodes (LOTUS-approved)
2. **Open source:** Calculation methods fully documented, auditable
3. **Appeal process:** Producers can request RIS review via LOTUS
4. **Periodic updates:** RIS methodology reviewed annually, adjusted based on new data
5. **Regional consistency:** Inter-Node RIS verification protocols

---

### 6. Cultural Resistance (Price-Thinking Persists)

**Risk:** People revert to price-thinking, ignore Flow information

**Indicators:**
- Black markets emerge (unofficial currency)
- People hoard to "sell" later
- Scarcity Indicators ignored because "not prices"

**Response:**
1. **Education:** Teach why prices hide information, Flow shows more
2. **Demonstrate success:** Show RIS + Scarcity system works better
3. **Community pressure:** Social norms against black markets
4. **Sanctions:** Currency use = harm to system (serious violation)
5. **Patience:** Cultural shift takes 5-10 years, expect transition period

---

## TECHNICAL IMPLEMENTATION

### RIS Database Architecture

**Data Structure:**
```json
{
  "material": "aluminum",
  "unit": "ton",
  "ris_score": 15000,
  "components": {
    "energy_kwh": 15000,
    "water_liters": 500,
    "labor_hours": 40,
    "co2_kg": 12000,
    "recyclability_pct": 95
  },
  "scarcity": "moderate",
  "last_updated": "2026-03-15",
  "calculation_method": "v2.3",
  "audited_by": "regional_standards_committee"
}

Access:
​Public API (anyone can query)
​Local cache at each Node
​Weekly sync with Regional Network
​Version control (historical RIS tracked)

​Scarcity Indicator Algorithm

def calculate_scarcity(current_stock, avg_consumption_rate, production_rate):
    months_remaining = current_stock / avg_consumption_rate
    
    if months_remaining >= 3 and production_rate >= avg_consumption_rate:
        return "GREEN"
    elif months_remaining >= 1:
        return "YELLOW"
    elif months_remaining >= 0.5:
        return "ORANGE"
    else:
        return "RED"
```

**Triggers:**
​RED for 48 hours → Automatic LOTUS alert
​ORANGE for 7 days → Production increase request
​YELLOW → Monitor, no immediate action

​Dashboard UI (Example)
​Top-Level View (Node):

```
╔════════════════════════════════════╗
║  RESOURCE DASHBOARD - Node Göteborg ║
╠════════════════════════════════════╣
║ FOOD       [■■■■■■□□] 6mo  GREEN   ║
║ ENERGY     [■■■■■□□□] 4mo  YELLOW  ║
║ MATERIALS  [■■■□□□□□] 2mo  ORANGE  ║
║ MEDICAL    [■■□□□□□□] 1mo  RED ⚠️  ║
╠════════════════════════════════════╣
║ Alerts: Medical supplies critical   ║
║ Action: LOTUS emergency panel       ║
╚════════════════════════════════════╝
```

Drill-Down (Medical Supplies):

```
MEDICAL SUPPLIES - CRITICAL
─────────────────────────────
Current Stock: 3 weeks
Consumption: 1 week/week
Production: 0.5 weeks/week
Deficit: 0.5 weeks/week

TOP SHORTAGES:
├─ Antibiotics: 10 days
├─ Painkillers: 12 days  
├─ Bandages: 15 days
└─ Surgical supplies: 20 days

ACTIONS:
├─ Emergency LOTUS panel scheduled
├─ Inter-Node aid request sent
├─ Green Lab production increase initiated
└─ Non-emergency procedures delayed 
```

### ASSESSMENT QUESTIONS
​Can Your Node Answer These?
####​ RIS Implementation:
- ​Do you have Resource Impact Scores for top 20 materials?
- ​Are RIS calculations public and auditable?
- ​Do people actually consult RIS when making decisions?
- ​Are environmental costs (CO₂, water, habitat) included in RIS?
- ​Is RIS updated quarterly based on actual data?

​Scarcity Indicators:
6. Do you have real-time scarcity dashboards?
7. Can anyone access scarcity information?
8. Do scarcity levels trigger behavioral changes?
9. Are historical trends visible (getting better/worse)?
10. Is RED scarcity automatically escalated to LOTUS?
​Production Feedback:
11. Do producers report constraints/bottlenecks regularly?
12. Can consumers see production limitations?
13. Does LOTUS respond to production feedback?
14. Are bottlenecks resolved within reasonable time?
15. Is producer-consumer communication transparent?
​Reserve Transparency:
16. Are all reserve levels public?
17. Can anyone verify Baseline coverage?
18. Do reserves meet 3-6 month target?
19. Is waste/spoilage tracked and minimized?
20. Are reserves shared between Nodes when needed?

**​If you cannot answer "yes" to 16+, your information system needs significant improvement.**

**​FINAL PRINCIPLE**
​Price is information.
​When we eliminate price, we must replace the information it carried.
​Flow's information system is:
-​ Richer (shows why, not just what)
-​ Transparent (everyone sees same data)
- ​Democratic (LOTUS allocates, not wealth)
​Ecological (externalities visible)
- ​Flexible (adapts to reality, not speculation)

**​This is not central planning. This is distributed coordination through shared information.**
**​STATUS:** Operational Protocol v1.0
**COMMITMENT:** Replace price information with richer, transparent, democratic coordination
**MOTTO:** "Prices hide information in the signal. Flow reveals information in the system."

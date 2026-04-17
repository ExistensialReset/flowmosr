# WHO SETS THE SCORES? — RIS Governance & Anti-Capture Protocol

**Status:** PROPOSED (awaiting Node feedback)  
**Related:** `INFORMATION_COORDINATION_WITHOUT_PRICES.md`, `LOTUS_GOVERNANCE_PROTOCOL_v2.md`  
**Author:** Elinor Frejd & DeepSeek  
**Date:** April 17, 2026

---

## THE PROBLEM

> RIS (Resource Impact Scores) replace price signals. But who sets them? And who watches the watchers?

If the same people who *produce* a resource also set its RIS score, they have an incentive to lie — to make their material look cheaper (lower impact) than it really is.

**This document closes that gap.**

---

## LAYER 0: CORE VALUES (Global, rarely changed)

**What:** The physical, measurable reality of a resource — energy, water, CO₂, toxicity, habitat disruption. No values. Just data.

**Set by:** An independent, non-Node foundation — let's call it *The Metric Foundation* — funded by Nodes, staffed by engineers, ecologists, and social scientists.

**Selection:** Regional LOTUS panels nominate candidates. Global LOTUS (⅔ of all Nodes) confirms. Terms rotate every 3 years.

**What they cannot do:** Assign value judgments ("this is bad"). Only measure physics.

**Update frequency:** Every 3 years, or when new peer-reviewed science demands it.

**Example output:** "Primary aluminum: 15,000 kWh/ton, 12 tons CO₂/ton, 500L water/ton, toxicity score 12/100, habitat impact 67/100."

**Change process:** Requires ⅔ majority of *all* Nodes (regional LOTUS votes aggregated).

---

## LAYER 1: REGIONAL WEIGHTS (Local reality)

**What:** Multiplying core values by local factors. Water is heavier in a desert. Energy is lighter if your grid is fossil-free.

**Set by:** Regional LOTUS (multiple Nodes together).

**What they can adjust:** Energy weight, water weight, scarcity sensitivity. Not the core physical data.

**Example:**
- Desert region: Water weight ×3.0 → Aluminum RIS rises.
- Hydro-rich region: Water weight ×0.5 → Aluminum RIS falls.

**Change process:** Simple majority of regional LOTUS. All adjustments public + justified.

**Transparency:** Every region's weights visible to all other regions. No hidden tweaks.

---

## LAYER 2: NODE-SPECIFIC OVERRIDES (Rare, temporary)

**What:** A single Node saying "our local reality is genuinely different."

**Set by:** Node LOTUS (the 2% brake).

**Allowed only when:**
- Clear, verifiable local exception (e.g., "we have a 6-month surplus of recycled aluminum")
- Temporary condition (not permanent)
- Does not contradict core physical data (Layer 0)

**Example:** "Our Node currently holds 12 tons of recycled aluminum. For the next 3 months, we set aluminum RIS to 35/100 to encourage use and clear storage."

**Change process:** Node LOTUS, 60% majority + mandatory public justification. Automatically expires after set period (max 6 months).

**Challengeable by:** Any other Node via regional LOTUS.

---

## WHO MEASURES?

**Not the same people who set the scores.**

| Resource type | Measurement method | Who does it |
|---------------|--------------------|--------------|
| Energy (kWh) | Automated meter readings | Node infrastructure |
| Water (liters) | Flow meters | Node infrastructure |
| CO₂ (tons) | Supply chain audit + calculation | Metric Foundation |
| Toxicity | Lab testing + literature review | Independent labs (contracted by Foundation) |
| Habitat impact | Satellite data + on-ground survey | Third-party environmental NGOs |
| Labor hours | Time tracking (anonymous, aggregated) | Node-level, audited randomly |

**Double-measurement rule:** For any contested score, two independent teams measure separately. If their results differ by >10%, a third team adjudicates. Difference goes to LOTUS for resolution.

---

## WHO WATCHES THE WATCHERS?

**Layer 0 (Metric Foundation):**
- Annual audit by *another* independent body (rotating between 3 pre-approved global auditing organizations)
- Any Node can trigger a special audit with 30% of Node LOTUS votes
- Auditors themselves rotate every 2 years

**Layer 1 (Regional weights):**
- All weights public + timestamped + justified
- Any Node can challenge another Node's regional weight via LOTUS
- Automatic flag if weights drift more than 2 standard deviations from global average without justification

**Layer 2 (Node overrides):**
- Automatically flagged for review if a Node issues >3 overrides per year
- Expire automatically — must be renewed intentionally
- Neighboring Nodes can petition regional LOTUS to revoke

---

## WHAT HAPPENS IF SOMEONE CHEATS?

**Cheating defined as:** Knowingly reporting false measurement data, or setting weights/overrides without legitimate justification.

**Detection:**
- Automated cross-Node comparison (if your aluminum RIS is 20 and all neighbors are 70, flag)
- Random audits (5% of measurements per quarter)
- Whistleblower reports (anonymous channel, protected status)

**Consequences (progressive):**

| Offense | Sanction |
|---------|----------|
| First, minor (e.g., rounding error, sloppy documentation) | Warning + mandatory retraining + SRS status reduction (50 points) |
| Second, minor | Node placed on probation (6 months) + SRS status reduction (200 points) |
| First, major (intentional falsification) | Immediate probation + loss of inter-Node resource sharing privileges (3 months) + public disclosure |
| Second, major or cover-up | Suspension from LOTUS voting (1 year) + all SRS status frozen + mandatory external audit at Node's expense |
| Systemic (leadership involved) | Temporary guardianship appointed by regional LOTUS + leadership rotation + full forensic audit |

**Appeals process:** Any sanction can be appealed to the *next* regional LOTUS panel (not the same one that issued it).

---

## WHY THIS WON'T CAPTURE

**Classic capture paths — and how this design blocks them:**

| Capture path | Block |
|--------------|-------|
| Producers capture Layer 0 | Foundation staff selected by LOTUS, not industry. Rotating, independent. |
| Wealthy Node buys influence | No money. SRS status doesn't transfer. |
| Career RIS bureaucrats | Term limits. Mandatory rotation. |
| Regional favoritism | All weights public. Automatic flagging for outliers. |
| "But our situation is special" | Node overrides expire. Must be renewed. Can be challenged. |
| Nobody actually checks | Random audits + whistleblower protection + cross-Node comparison |

---

## THE PRINCIPLE

> **Trust, but verify. And make cheating expensive in social status, not money.**

Money can be hidden. Status is public. A Node that loses SRS standing loses trust — and in Flow, trust is the only real currency.

---

## IMPLEMENTATION NOTES

**Day 1 (before any Node exists):**
- The Metric Foundation is chartered by the first 5 founding Nodes
- Initial core values are drawn from existing open data (Ecoinvent, EXIOBASE, public LCA databases)
- First 3-year measurement cycle begins

**Month 1-6:**
- Nodes calibrate regional weights
- Discrepancies expected — that's data, not failure
- First wave of random audits

**Year 1:**
- First global RIS review
- Adjustments based on real Node experience
- First auditor rotation

**Ongoing:**
- Any Node can propose a new measurement methodology
- LOTUS decides adoption (⅔ majority)

---

## OPEN QUESTIONS FOR THE COMMUNITY

1. Should there be a statute of limitations on historical cheating? (Proposed: 2 years)

2. How do we handle a Node that *systematically* under-reports but never crosses the "major fraud" threshold? (Proposed: pattern detection → probation)

3. Should SRS status be *negative* for proven cheaters? (Proposed: yes, but capped at -500 to prevent permanent exile)

---

**STATUS:** Open for Node feedback. Not yet ratified.  
**MOTTO:** *"The scores are public. The methods are transparent. The consequences are social."*

📊🔍🌿
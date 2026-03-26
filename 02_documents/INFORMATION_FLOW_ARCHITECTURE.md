# INFORMATION FLOW ARCHITECTURE

**Version:** 1.1  
**Status:** Core Specification  
**Layer:** Core Infrastructure  
**Scope:** Micro → Node → Regional → Global  
**Author:** Elinor Frejd  
**Date:** 2026-02-26  

This document defines the minimum viable architecture for information flow in M-OS-R.  
Its purpose is to prevent hierarchy, reduce exhaustion, and preserve operability across energy levels.

This is an architectural layer — not a cultural manifesto and not an implementation handbook.

---

# 1. DESIGN OBJECTIVES

The system must:

1. Prevent information concentration.
2. Function during low-energy conditions.
3. Default to asynchronous communication.
4. Require minimal recurring meetings.
5. Scale without producing administrative elites.
6. Operate in local-first mode (internet optional, not mandatory).
7. Align all cross-scale representation with LOTUS_PROTOCOL.md.

---

# 2. CORE PRINCIPLES

## 2.1 Async First

All essential communication is asynchronous by default.

Synchronous communication (meetings, calls) is used only when:

- Emotional resolution is required  
- Time-critical coordination is necessary  
- Complex issues cannot be resolved in writing  
- Ritual or social bonding is intended  

If something can be written, it must be written.

Undocumented communication is non-binding.

---

## 2.2 Meeting Minimalism

No recurring meeting is allowed without quarterly justification.

### Maximum baseline per scale:

**Micro-Circle (5–20 members)**  
- 1 weekly gathering  
- No mandatory standups  

**Node (100–500 members)**  
- Sub-circles: 1 weekly meeting  
- Delegates: 1 bi-weekly sync (max 90 minutes)  
- Full Node: 1 monthly gathering  
- 1 quarterly reflection day  

No daily mandatory meetings at any scale.

If total communication requires more than 20 minutes per day
for an average member to remain informed,
the system is considered overloaded.

---

## 2.3 Information Visibility

All decisions must exist in written form.

Minimum required structure:

- Proposal  
- Outcome  
- Responsible party  
- Review date  

Undocumented decisions are non-binding.

### Decision Expiry Rule

All decisions expire unless explicitly renewed.
Nothing is permanent by default.

---

## 2.4 Energy-Aware Degradation

Communication must degrade gracefully.

Energy Levels:

| Level     | Mode of Operation            |
|-----------|-----------------------------|
| High      | Full media available         |
| Medium    | Text + audio                 |
| Low       | Text only                    |
| Critical  | Status beacons only          |
| Zero      | Silence                      |

Silence is legitimate and carries no stigma.

---

## 2.5 Local-First Infrastructure

The system must be able to operate using:

- Local network  
- Mesh infrastructure  
- Printed summaries  

Internet services may be used but must not be a single point of failure.

All essential decisions must be exportable in plain-text format.

---

# 3. CHANNEL STRUCTURE

Maximum channels per Node: 7

Mandatory:

1. Emergency  
2. Announcements  
3. Decisions  
4. Baseline (resources / health metrics)  
5. Coordination  
6. Social  
7. Archive (read-only)  

Channels must be reviewed quarterly.
Unused channels are archived.

---

# 4. CROSS-SCALE REPRESENTATION

Delegates exist only to bridge scale.

They transmit information.
They do not interpret, filter, or accumulate authority.

## 4.1 LOTUS Alignment

All representative roles above sub-circle level must be selected, rotated, and reviewed through LOTUS_PROTOCOL.md.

This includes:

- Node delegates  
- Regional delegates  
- Inter-Node coordinators  
- Crisis coordination roles (when applicable)  

No scale may define an independent selection mechanism.

Representation is a function, not a status.

---

## 4.2 Anti-Concentration Safeguards

- Mandatory written summaries of all cross-scale meetings  
- Maximum 6-month consecutive service period  
- Public documentation of all decisions and votes  
- Sub-circles may bypass delegates via written proposal submission  

Delegation is temporary transmission, not career progression.

---

# 5. DECISION TIERS

## Tier 1 — Micro Impact
Affects one circle only.  
Lightweight decision log permitted.  
Review optional.

## Tier 2 — Node Impact
Affects multiple circles within a Node.  
Full decision template required.  
Mandatory review within 3–6 months.

## Tier 3 — Regional Impact
Affects multiple Nodes.  
Full documentation required.  
Mandatory review cycle.

No global authority tier exists.
Global coordination occurs through federated Regional collaboration.

---

# 6. ACCESSIBILITY BASELINE

All essential information must be available as:

- Plain text  
- Printable format  
- Screen-reader compatible  

Audio and visual formats are additive, not mandatory at baseline level.

Accessibility is a structural requirement, not an enhancement.

---

# 7. FAILURE ASSUMPTION DESIGN

The architecture assumes:

- People forget documentation  
- People avoid meetings  
- Energy fluctuates  
- Informal channels will form  
- Delegates may accumulate soft power  

Therefore:

- Written logs are mandatory  
- Meetings are minimized  
- Review dates are enforced  
- Delegation rotates via LOTUS  
- Complexity is audited quarterly  

If the system creates exhaustion, it must be simplified.

---

# 8. SCALING RULE

As scale increases:

- Meetings do not increase linearly  
- Documentation replaces live coordination  
- Delegation rotates  
- Communication frequency decreases  

More people = fewer real-time interactions.

---

# 9. CORE GUARANTEES

This architecture guarantees:

- No decision without record  
- No record without access  
- No access without degradation path  
- No role without rotation  
- No representation outside LOTUS_PROTOCOL  
- No silence without dignity

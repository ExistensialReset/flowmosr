# 04_SIMULATIONS

## Models, Scenarios, and Proposed Validation

This directory contains models, simulations, stress scenarios, and proposed validation methods for Flow / M-OS-R.

It is important to understand what this directory does — and does not — claim.

---

## ⚠️ VALIDATION STATUS

**The systems described in this directory have not been presented as fully validated real-world systems unless explicitly stated otherwise.**

A model is not evidence.

A scenario is not an observation.

A proposed test is not a completed test.

A simulation is not reality.

The purpose of this directory is to make assumptions visible and make them testable.

---

## I. WHAT THIS DIRECTORY CONTAINS

### 1. Conceptual Models

Descriptions of how a system might work.

These answer:

> How could this work?

They do not answer:

> Does this work in reality?

---

### 2. Scenarios

Structured situations used to examine potential behavior under different conditions.

Examples include:

- energy shortage;
- network isolation;
- resource scarcity;
- system failure;
- regional disruption;
- node isolation;
- cascading failures.

A scenario is a question posed to a system.

It is not evidence of what will happen.

---

### 3. Proposed Simulations

Methods for testing models under controlled or computational conditions.

These may help explore:

- sensitivity;
- failure points;
- trade-offs;
- dependencies;
- and possible system behavior.

Simulation results remain dependent on:

- the model;
- the assumptions;
- the input data;
- and the implementation.

---

### 4. Proposed Real-World Tests

Methods for testing whether theoretical or simulated assumptions survive contact with reality.

These may include:

- hardware tests;
- small-scale production tests;
- Circle experiments;
- Node pilots;
- resource-flow experiments;
- and resilience tests.

---

## II. EPISTEMIC STATUS

Every claim should, where possible, be understood according to its status:

| Status | Meaning |
| :--- | :--- |
| **PROPOSED** | A design or hypothesis that has not yet been tested |
| **MODELED** | Represented in a conceptual or mathematical model |
| **SIMULATED** | Tested through a computational or controlled simulation |
| **PILOTED** | Tested in a limited real-world implementation |
| **OBSERVED** | A documented observation from a real-world test |
| **VALIDATED** | Supported by documented evidence under defined conditions |
| **INDEPENDENTLY VALIDATED** | Verified by an independent party or process |

These categories should not be treated as interchangeable.

---

## III. THE VALIDATION CHAIN

A claim should ideally move through a process such as:

```text
CLAIM
  ↓
ASSUMPTION
  ↓
FAILURE MODE
  ↓
TEST DESIGN
  ↓
SIMULATION
  ↓
PILOT
  ↓
OBSERVATION
  ↓
REPLICATION
  ↓
VALIDATION
```
Not every idea will reach every stage.

Some ideas will fail.

That is useful information.

---

## V. FAILURE IS DATA

Flow does not require its models to be correct.

It requires them to be examinable.

If a model fails:

> **The model must be revised.**

If an assumption fails:

> **The assumption must be exposed.**

If a simulation produces an unexpected result:

> **The result must not be forced to fit the theory.**

If a real-world experiment contradicts the model:

> **Reality takes priority.**

---

## VI. WHAT IS CURRENTLY UNKNOWN

The existence of a model in this directory does not mean that the following have been proven:

- that all Nodes can maintain Baseline;
- that all proposed production systems work at scale;
- that all energy models are practically achievable;
- that all resource flows are logistically feasible;
- that all governance systems behave as intended;
- that voluntary contribution is sufficient in every context;
- or that Flow can scale without unforeseen failure modes.

These are questions for testing, observation, and revision.

---

## VII. HOW TO READ THIS DIRECTORY

When reading a document, ask:

1. **What is being claimed?**
2. **What assumptions does the claim depend on?**
3. **What could make the claim false?**
4. **Has it been modeled?**
5. **Has it been simulated?**
6. **Has it been tested in the real world?**
7. **What evidence exists?**
8. **What remains unknown?**

The purpose of this directory is not to create certainty.

It is to make uncertainty visible enough to work with.

---

## VIII. THE CORE PRINCIPLE

> **A claim is not a test.**
>
> **A model is not evidence.**
>
> **A simulation is not reality.**
>
> **A successful test is not universal proof.**
>
> **A failure is not a defeat.**
>
> **It is information.**

---

## STATUS

This directory contains proposed models, scenarios, simulations, and validation approaches.

**Real-world validation is pending unless explicitly documented otherwise.**

The purpose of this directory is to help Flow move from:

> **idea**

to:

> **testable hypothesis**

to:

> **observation**

to:

> **learning**

to:

> **revision.** 
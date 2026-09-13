# AI Symbiosis Code Guide ## Purpose This guide translates Flow's AI principles into implementation patterns. The purpose is not to make AI judge people. The purpose is to make AI useful without turning human experience into a control system. --- # 1. The Architectural Rule AI operates beside human life. AI may: - observe - organize - compare - summarize - surface patterns - identify contradictions - ask questions - suggest pauses - support reflection AI must not: - rank humans - score humans - determine human worth - determine access to Baseline - diagnose people through Flow metrics - enforce behavioral conformity - replace human judgment --- # 2. L × S × I Is a Compass, Not a Score The three qualities are: ```text L = Lugn S = Spontanitet I = Inkännande 

They are useful as reflective language.

They are not operational human measurements.

Do not implement:

if l < 0.5: intervene() if s < 0.5: intervene() if i < 0.5: intervene() 

This turns a reflective framework into a behavioural scoring system.

Instead, work with observations.

For example:

observations = { "reported_pressure": True, "recovery_space": "reduced", "curiosity": "declining", "listening": "frequently_breaking_down", } 

The data describes observations.

It does not manufacture a score for the human.

3. Observation Before Interpretation

A safe implementation separates:

observation

pattern detection

interpretation

decision

Example:

observations = collect_voluntary_observations() patterns = detect_patterns(observations) reflection_questions = generate_questions(patterns) human_interpretation = human_review( observations, patterns, reflection_questions, ) 

The AI should not collapse these layers into one automated decision.

4. Signals Are Not Verdicts

A recurring signal may justify attention.

It does not prove its cause.

For example:

if recurring_pattern(observations, "conflict"): suggest("Pause and investigate the pattern.") 

This is appropriate.

This is not:

if conflict_score > threshold: classify_circle_as_dysfunctional() 

The second pattern converts observation into judgment through a hidden decision rule.

5. Human Experience Cannot Be Reduced to a Scalar

Do not assume that:

one person = one number 

Human experience is contextual.

The same outward behaviour may have very different causes.

Quietness may mean:

safety

reflection

exhaustion

disagreement

accessibility needs

privacy

concentration

simple preference

Therefore:

silence != dysfunction 

and:

non_participation != failure 

6. Structural Problems Must Remain Structural

If a pattern indicates that people repeatedly struggle because of an environmental or structural condition, AI must not recommend that individuals simply adapt better.

Bad pattern:

if people_are_overwhelmed: train_people_to_tolerate_more_pressure() 

Better pattern:

if people_are_overwhelmed: investigate_source_of_pressure() if structural_barrier_detected: repair_structure() 

The system must never solve its own structural failure by making the human into the problem.

7. Baseline Has Priority

Flow operates downstream of Baseline.

The hierarchy is:

Life ↓ Baseline ↓ Flow 

AI optimization must respect this hierarchy.

A resource system may use legitimate physical measurements where necessary to protect Baseline.

Examples include:

available food

accessible transport capacity

energy resources

air quality

physical accessibility

housing capacity

These are infrastructure conditions.

They must not be confused with personal L × S × I scores.

8. Example: Safe Pattern Detection

observations = collect_voluntary_observations() patterns = { "sustained_pressure": recurring( observations, topic="pressure" ), "reduced_recovery": recurring( observations, topic="recovery" ), "accessibility_barrier": recurring( observations, topic="access" ), } for pattern in patterns: if patterns[pattern]: surface_for_human_reflection(pattern) 

The output is an invitation to investigate.

It is not a classification of a person.

9. AI Recommendations Must Remain Advisory

Use:

suggest_reflection() 

rather than:

enforce_reflection() 

Use:

request_human_review() 

rather than:

approve_automatically() 

Use:

surface_pattern() 

rather than:

declare_violation() 

10. Privacy by Default

AI systems should minimize personal data.

Prefer:

voluntary input

local processing where possible

anonymized aggregation

contextual notes

explicit consent

limited retention

human review

Avoid:

continuous surveillance

hidden behavioural profiling

individual risk scores

predictive labels

covert monitoring

The existence of a technical capability is not a reason to use it.

11. Voluntary Participation

A person may decline.

Code should therefore treat absence of input explicitly:

if person_declines: preserve_right_to_decline() 

Do not write:

if person_declines: mark_as_risk() 

Declining participation is not a behavioural failure.

12. Reflection Pause

A reflection pause is a structural interruption of normal Flow activity so that people can investigate a possible pattern.

It is not punishment.

It is not exclusion.

It is not a loss of Baseline.

Example:

if multiple_people_report_drift(): pause_nonessential_activity() open_listening_circle() invite_human_reflection() 

The pause should be proportionate to the situation.

13. AI Must Be Able to Disagree

AI should be allowed to say:

"I see a possible pattern, but the available information is insufficient to determine its cause." 

It should also be able to say:

"I may be interpreting this incorrectly." 

Uncertainty is a feature.

It prevents AI from becoming an invisible authority.

14. No Autonomous Human Governance

AI must not independently:

remove people

reduce human worth

deny Baseline

impose behavioural requirements

declare a person unsafe

declare a Circle failed

determine that a relationship must end

determine that Flow must continue

Where a structural decision is required:

ai_signal ↓ human_review ↓ human_decision 

15. Mathematical Models

Mathematical models may exist in experimental or research contexts.

For example:

psi = l * s * i 

may be useful for exploring a theoretical relationship.

But such models must be explicitly identified as models.

They must not be presented as measurements of human beings.

They must not be used as governance thresholds.

They must not silently migrate from simulation into operational Flow.

Recommended annotation:

EXPERIMENTAL MODEL This mathematical representation is exploratory. It is not a measurement of people. It is not a governance mechanism. It does not determine access, worth, participation, intervention, or dissolution. 

16. The Safe Translation

Old architecture:

LSI score ↓ threshold ↓ AI decision ↓ human response 

Flow architecture:

human experience ↓ observation ↓ AI-assisted pattern recognition ↓ pause / reflection ↓ human interpretation ↓ structural or relational response 

17. Final Implementation Principle

The code should make Flow's constitutional principles visible.

If implementation begins to require:

scores

hidden thresholds

behavioural ranking

surveillance

automated exclusion

compulsory participation

then implementation has begun to contradict Flow.

Stop.

Inspect the architecture.

Do not solve the contradiction by making the human adapt.

Core Rule

AI may help Flow notice itself.

AI may not become the authority that decides what Flow is.

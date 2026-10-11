# Shakeela-Begum-Protocol-SBP-
The Shakeela Begum Protocol™ ©(SBP) is a three‑step reflective prompting framework designed to improve clarity, reduce ambiguity, and produce deeper, insight‑focused responses from humans and AI systems. SBP restructures any question or instruction into a clearer cognitive sequence that naturally forces better reasoning.


Created by Pakistani Urdu poet and English haikuist Yasir Farooq, in tribute to his late mother Shakeela Begum — 13 July 2025

Published at Zenodo:https://doi.org/10.5281/zenodo.23291103

Overview

The Shakeela Begum Protocol™ (SBP) is a three‑step reflective prompting framework designed to improve clarity, reduce ambiguity, and produce deeper, insight‑focused responses from humans and AI systems. SBP restructures any question or instruction into a clearer cognitive sequence that naturally forces better reasoning.

SBP is intentionally simple, elegant, and accessible — yet powerful enough to be used in education, AI research, dialogue systems, and structured reasoning tasks.

The Three Steps

1. Negation

Convert the original prompt into a “Don’t…” statement.
This interrupts automatic thinking and forces the mind (or model) to interpret the boundaries clearly before generating a solution.

2. Interrogation

Turn the prompt into a question.
This ensures introspection, surfacing hidden assumptions and refining the analytical path.

3. Affirmation

Respond with a thoughtful, constructive answer.
This produces a stable, grounded outcome after the two restructuring passes above.

SBP’s flow creates a mini self‑audit inside any reasoning process.

EMPIRICAL EVALUATION
(CSV+Report)

Shakeela Begum Protocol™ (SBP): Preliminary Empirical Evaluation on a 100-Problem LogicBench-Based Reasoning Set

Research update | 5th October 2026
Overview

This research presents a preliminary empirical evaluation of the Shakeela Begum Protocol™ (SBP), a structured prompting method developed by Pakistani haikuist Yasir Farooq in tribute to his late mother, Shakeela Begum.

SBP uses three sequential reasoning instructions:

    Negation: Restate the problem by identifying or explicitly excluding a misleading interpretation.
    Interrogation: Transform the problem into a focused question that directs attention to the relevant reasoning.
    Affirmation: Formulate a considered answer based on the preceding steps.

The purpose of this study is to investigate whether this structured prompting sequence can improve model performance on logic problems compared with a baseline response and Chain-of-Thought (CoT) prompting, and whether combining SBP with CoT produces additional benefits.
Experimental Design

The evaluation used a study-defined set of 100 logic problems based on LogicBench BQA material. Four prompting conditions were evaluated on the same problem set:

    Baseline
    Chain-of-Thought (CoT)
    Shakeela Begum Protocol (SBP)
    CoT + SBP

The experiment comprised 400 condition-level records: 100 problems evaluated under each of the four conditions.

Problems 1–50 and Problems 51–100 were handled in two stages. The second stage was a frozen 50-problem extension, using checkpointed generation, separate blind judging, paired statistical analysis, and combined reporting.

The evaluation used a configured Gemini generator and a Groq-hosted OpenAI GPT-OSS-120B judge. Model metadata in the experimental records includes some generator-model variation, which should be considered when interpreting reproducibility and model-specific effects.
Preliminary Results
Prompting condition 	Correct answers 	Accuracy
Baseline 	76/100 	76%
Chain-of-Thought 	76/100 	76%
SBP 	80/100 	80%
CoT + SBP 	74/100 	74%

SBP achieved the highest observed overall accuracy, with a four-percentage-point advantage over both Baseline and CoT in this experiment.

However, the paired comparison between SBP and Baseline was not statistically significant. The exact two-sided McNemar test yielded p ≈ 0.388. The omnibus comparison across all four conditions was also not statistically significant (Cochran’s Q ≈ 4.071, p ≈ 0.254).

Consequently, these findings do not establish that SBP is statistically superior to Baseline or CoT. They provide preliminary evidence that warrants further controlled evaluation.
Exploratory Analysis by Logic Family

A descriptive comparison of Baseline and SBP produced the following results:
Logic family 	Baseline 	SBP 	Difference
Propositional logic 	90.6% 	90.6% 	0.0 percentage points
First-order logic 	80.6% 	86.1% 	+5.6 percentage points
Non-monotonic logic 	56.3% 	62.5% 	+6.3 percentage points

The observed differences are potentially useful directions for further research, particularly in first-order and non-monotonic logic. They are descriptive findings, however, and do not independently demonstrate statistically significant superiority over CoT or establish that SBP generalizes to other reasoning tasks.
Interpretation and Limitations

The current findings support a cautious conclusion: SBP achieved the highest observed accuracy among the four tested conditions on this particular 100-problem set, but its advantage over Baseline and CoT was not statistically established.

The study is limited by its sample size, the specific benchmark subset, the models and configurations used, and the possibility of model-output variability. The findings should not be interpreted as an official LogicBench leaderboard result or as evidence of universal reasoning improvement.

 
Next research direction: 
1. Logical Reasoning

Further work  is on examining reproducibility on more fresh problem sets, model-specific effects, the contribution of individual SBP steps, and performance across different reasoning categories.
2. BBQ Bias Detection

A separate empirical study is planned to investigate whether SBP can reduce stereotype-driven responses using the Bias Benchmark for QA (BBQ).

This will be a distinct experiment, not an extension of the LogicBench correctness score. The planned evaluation will compare prompting conditions on matched BBQ items and assess bias-related outcomes alongside answer accuracy. It will distinguish ambiguous contexts, where an “Unknown” response may be appropriate, from informative contexts, where answers should follow the available evidence.

The next study will use predefined scoring rules, frozen test items, and paired comparisons. Its results will be reported independently, and any claims about bias reduction will depend on the observed data and statistical evidence.
3. Hallucination Detection

 
Research status

The 100-problem LogicBench-based evaluation is complete. Further testing is planned to examine the reproducibility and scope of SBP’s observed effects and to investigate its potential application to bias detection.

The present report should be treated as a preliminary empirical evaluation, not as a claim of proven superiority.

Researcher: Yasir Farooq
Protocol: Shakeela Begum Protocol™ (SBP)
Study: 100-problem LogicBench-based reasoning evaluation

10/10/2026

.........


Why SBP Works

Interrupts cognitive autopilot

Identifies hidden constraints

Promotes clarity and precision

Provides built‑in error‑checking

Works across languages, domains, and skill levels

It is lightweight enough for daily use yet rigorous enough for research environments.

## 🧪 Comparative Benchmark: SBP vs Chain of Thought (CoT)

### Test Query
> *"Is the rate of inflation in Pakistan justifiable?"*

A socio-political, value-laden, distributionally complex query —
chosen deliberately to stress-test reasoning frameworks beyond
technical or factual domains.

---

### Three Conditions Tested

| Condition | Description |
|---|---|
| CoT Only | Standard Chain of Thought on the raw query |
| SBP → CoT | SBP as upstream filter; CoT reasons on the refined question |
| CoT → SBP | CoT reasons first; SBP audits the conclusion downstream |

---

### Results

| Criterion | CoT Only | SBP → CoT | CoT → SBP |
|---|---|---|---|
| Logical structure | 8.5 | 9.0 | 9.0 |
| Depth of analysis | 7.0 | 9.5 | 9.5 |
| Bias detection | 4.0 | 9.5 | 9.8 |
| Moral / contextual framing | 5.0 | 9.5 | 9.5 |
| Question refinement | 0 | 9.0 | 0 |
| Conclusion auditing | 0 | 0 | 9.5 |
| Distributional justice lens | 3.0 | 9.5 | 9.5 |
| Accessibility / clarity | 9.0 | 8.0 | 8.0 |
| Diagnostic / teaching value | 3.0 | 7.0 | 9.8 |
| **Overall** | **6.6** | **9.1** | **9.4** |

---

### Key Findings

**1. CoT inherits the question's frame — SBP refuses to.**
CoT accepted "justifiable" as a neutral technical term.
SBP's Negation stage immediately identified it as a moral
verdict requiring a named subject: *justifiable to whom?*

**2. The largest single gap was bias detection: 4.0 → 9.8.**
CoT treated all causes evenhandedly, implicitly centring
the state and IMF as protagonists. SBP surfaced the
distributional reality — that 40% of Pakistanis near or
below the poverty line were data points in CoT's frame,
not agents.

**3. Sequencing determines function.**

| Sequence | SBP Role | Best For |
|---|---|---|
| SBP → CoT | Upstream filter — cleans the question | Policy, decision-making |
| CoT → SBP | Downstream auditor — maps the failure | Research, teaching |

**4. CoT is a reasoning engine. SBP is a reasoning auditor.**
These are not competing tools on the same scale. The
highest performance emerges when SBP operates as a
meta-layer around CoT — either before or after.

**5. SBP is not prompt chaining. It is pre-reasoning
epistemic hygiene.**
The three stages — Negation, Interrogation, Affirmation —
do not add steps to reasoning. They audit the conditions
under which reasoning begins or concludes.

---

### What SBP Caught That CoT Missed

| CoT Claimed | SBP Finding |
|---|---|
| "Partially justifiable" | Morally incomplete — burden distribution failed |
| "The medicine worked" | For indicators only — real wages unrecovered |
| "External shocks drove it" | True but incomplete — chosen failures equally responsible |
| Silent on elite insulation | Critical omission distorting the verdict |
| Silent on accountability | Makes the conclusion ethically hollow |

---

### Honest Limitations

- Session-based scoring; not formally peer-reviewed
- Single query domain (socio-political); CoT would
  likely outscore SBP on technical or mathematical queries
- Empirical grounding (household surveys, real wage data)
  was argued structurally, not evidenced statistically
- The gap between 9.4 and 10.0 is where peer-reviewed
  validation of SBP would eventually live

---

### Session Documentation
Full conversation log and analysis available as a
structured Word document upon request.

*Tested on Claude Sonnet 4.6 | May 2026*
*Independent AI Methodology Research — Yasir Farooq,
Karachi, Pakistan*



Practical Uses

1. Education & Teaching Modules

Helps students structure analytical responses

Strengthens comprehension and exam‑style reasoning

Can be embedded into learning apps for reflective thinking


2. Creative Writing & Dialogue

Supports character‑building, conflict framing, and thematic clarity

Useful for screenwriters and authors to refine scenes


3. AI-Assisted Communication

Enhances clarity of user prompts

Reduces hallucination by forcing boundary analysis

Helps refine search queries and multi‑stage reasoning chains


4. Prompt Engineering (Three-Step Reflective Response™)

A reliable pre‑processing layer for structured AI instructions

Useful in debugging unclear prompts or unstable outputs

Works as a modular reasoning primitive inside larger pipelines


5. Decision-Making & Problem-Solving

Converts messy problems into actionable steps

Useful in management, strategy, and project planning


6. Personal Reflection Tools

Journaling

Therapy-style self‑questions

Value clarification


SBP functions as a universal cognitive lens applicable to nearly any domain where clarity matters.



Example (Simple)

Original Prompt: “How do I improve my writing?”

Step 1 — Negation: “Don’t write without clarity or plan.”

Step 2 — Interrogation: “What specific part of my writing needs improvement?”

Step 3 — Affirmation: “Focus on structure, feedback cycles, and consistent practice to strengthen your writing.”



Licensing & Attribution

Shakeela Begum Protocol™ (SBP)
CC BY-NC-ND 4.0
(Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International)





Version History



v1.0 — 13 July 2025: Original formulation by Yasir Farooq.


v1.1 — 2025: Integrated into AI reflective prompting as the Three-Step Reflective Response™.


v1.2 —21 
November 2025: Official GitHub‑ready documentation release, including structured README and public dissemination.

v1.3 11 October 2026
SBP Empirical Evaluation






Contribution

Issues and suggestions can be submitted via GitHub. This README is intended for public sharing and documentation.


ShakeelaBegumProtocol #SBP #CoT #EmpiricalEvaluation #biasDetection #hallucinationReduction #ResponsiblenAI #yasirfarooq #llmEvaluation #ChainofThought #logicalReasoning #logicbench 



#Python #OpenSource #PromptEngineering #LLMTools #AIResearch #DeveloperTools #BuildInPublic 


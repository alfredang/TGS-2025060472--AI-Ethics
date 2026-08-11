"""Concept-enrichment slides for Responsible Generative AI Basics.

Content transcribed from the previous Master Trainer Slides (190 slides,
reference/WSQ - Master Trainer Slides - TGS-2025060472 ...pptx), whose concept
slides were flat screenshots. Each diagram has been redrawn here as a native
house-style visual component so the deck is fully editable, on-brand and small
enough to distribute.

Slide spec kinds understood by build_slides.py's render_insight():
  pillars   -> grid of (title, desc) panels
  table     -> two-column comparison table with coloured headers
  stats     -> big-number stat tiles + optional callout band
  image     -> full-width imported visual with house header
  quote     -> big statement slide
  flow      -> horizontal chevron flow (optional note band)
  playbook  -> numbered 01..0n columns + tagline band
  twocol    -> two-column comparison panels
"""

INSIGHTS = {

# ================================================================ LU1
1: [
    ("pillars", dict(
        title="The Hidden Costs of Generative AI",
        kicker="LU1 · T1 · BEYOND THE SUBSCRIPTION FEE",
        intro="Every prompt has costs that never appear on the invoice.",
        items=[
            ("Environmental",
             "Training and inference consume electricity, fresh water for cooling and "
             "embodied carbon in the hardware. A single large model's training run can "
             "emit as much CO2 as several cars over their lifetime."),
            ("Security",
             "Data pasted into a public AI tool may be retained, used for training or "
             "exposed. AI also widens the attack surface — prompt injection, model "
             "extraction and data leakage are new classes of vulnerability."),
            ("Psychological & Societal",
             "Increasing dependence on AI, AI as a social and emotional companion, and "
             "the erosion of the human capacity to judge — the 'human filter' degrades "
             "the more it is bypassed."),
            ("Epistemic",
             "Deepfakes, voice cloning and synthetic media are now cheap and convincing, "
             "dissolving the shared assumption that a recording is evidence of anything."),
        ])),
    ("stats", dict(
        title="Why GenAI Risk Is Not Hypothetical",
        kicker="LU1 · T1 · THE SCALE OF THE PROBLEM",
        intro="The gap between how fast AI is adopted and how fast it is governed is where risk lives.",
        stats=[
            ("98%", "Accuracy can still mean a life-threatening error in the 2% — accuracy is not safety"),
            ("3", "Layers where bias enters: the training data, the model objective, the deployment context"),
            ("11", "Principles of trustworthy AI defined by Singapore's AI Verify framework"),
        ],
        note="High accuracy on average says nothing about who bears the error. Always ask: who is in the 2%?")),
    ("table", dict(
        title="The Deconstruction of AI Bias",
        kicker="LU1 · T1 · WHERE BIAS ENTERS",
        intro="Bias is not one defect to be patched — it is introduced at three separate stages and compounds.",
        colheads=("How it enters", "What it produces"),
        rows=[
            ("Data bias",
             "Training data over-represents some groups and under-represents others; historical "
             "records encode past discrimination.",
             "A model that is systematically less accurate for under-represented groups."),
            ("Objective bias",
             "The metric the model optimises (clicks, cost, speed) is a proxy for what we "
             "actually care about (welfare, fairness, safety).",
             "A model that optimises the proxy perfectly while defeating the real goal."),
            ("Deployment bias",
             "The system is used on a population, or for a purpose, different from the one it "
             "was built and validated for.",
             "Confident predictions in a context where the model was never tested."),
        ])),
    ("pillars", dict(
        title="AI Verify — Singapore's Testing Framework",
        kicker="LU1 · T2 · 11 PRINCIPLES, 2 ZONES",
        intro="AI Verify splits the 11 principles by how each can actually be evidenced. aiverifyfoundation.sg",
        items=[
            ("Zone 1 — Process checks only",
             "Transparency · Reproducibility · Safety · Security · Data Governance · "
             "Accountability · Human Agency & Oversight · Inclusive Growth & Societal "
             "Impact. Evidenced through standardised checklists, documentation and "
             "governance frameworks."),
            ("Zone 2 — Technical tests + process checks",
             "Fairness · Explainability · Robustness. Evidenced through black-box "
             "technical testing on model inputs and outputs, supported by quantitative "
             "toolkits."),
            ("Why the split matters",
             "You cannot unit-test accountability, and you cannot govern robustness with a "
             "policy document alone. The framework integrates technical validation (TEVV) "
             "directly with process governance."),
            ("Project Moonshot",
             "The open-source companion toolkit that operationalises the testing — "
             "benchmarking, red-teaming and baseline testing for LLM applications. "
             "github.com/aiverify-foundation/moonshot"),
        ])),
    ("table", dict(
        title="GenAI Risk Diagnostic Matrix",
        kicker="LU1 · T2 · RISK → TEST",
        intro="Each GenAI risk category has a distinct testing target — you cannot test them all the same way.",
        colheads=("Output testing target", "Component testing target"),
        rows=[
            ("Hallucination & inaccuracy",
             "Domain knowledge; out-of-domain handling",
             "Retrieval-Augmented Generation (RAG)"),
            ("Bias in decision making",
             "Parity metrics; counterfactual checks",
             "Model, system prompt, input filters"),
            ("Undesirable content",
             "Content type; elicitation rate; helpfulness",
             "Input & output filters; system prompt"),
            ("Data leakage",
             "Data type leaked; ease of elicitation",
             "Input & output filters; system prompt"),
            ("Adversarial prompts",
             "Direct vs indirect prompt injection",
             "Input & output filters; system prompt"),
        ])),
    ("flow", dict(
        title="The EU AI Act Compliance Waterfall",
        kicker="LU1 · T3 · RISK-BASED REGULATION",
        color="VIOLET",
        intro="The EU AI Act regulates by the risk a system poses, not by the technology it uses.",
        steps=[
            "Unacceptable risk — prohibited outright (social scoring, manipulative systems)",
            "High risk — conformity assessment, risk management, human oversight, logging",
            "Limited risk — transparency obligations (users must know they are dealing with AI)",
            "Minimal risk — no additional obligation; voluntary codes of conduct",
        ],
        note="Classify the system FIRST — every downstream obligation follows from the risk tier.")),
    ("pillars", dict(
        title="Three Pillars of Algorithmic Risk",
        kicker="LU1 · T3 · WHAT GOES WRONG",
        items=[
            ("Transparency",
             "Neither the affected person nor often the operator can see why the system "
             "produced its output — so the decision cannot be contested or corrected."),
            ("Algorithmic bias",
             "Systematically unfair outcomes for particular groups, arising from data, "
             "objective or deployment context."),
            ("Data privacy",
             "Personal data is used for training or inference without a lawful basis, "
             "adequate safeguards or the individual's awareness."),
            ("The governing response",
             "National AI policy — the EU AI Act, NIST AI 600-1, Canada's AIDA and "
             "Singapore's AI Verify / Model AI Governance Framework — each address these "
             "three pillars with different instruments."),
        ])),
    ("quote", dict(
        line1="The ultimate safeguard requires a human in the loop.",
        line2="Automation is acceptable where the cost of an error is low and reversible. Where it is "
              "high-stakes and irreversible, a qualified human must remain accountable for the decision — "
              "not merely present to rubber-stamp it.",
        kicker="LU1 · T3 · THE NON-NEGOTIABLE CONTROL")),
    ("pillars", dict(
        title="Automation Bias — The Vulnerability in the Human Filter",
        kicker="LU1 · T4 · PROFESSIONAL SCEPTICISM",
        intro="Human oversight fails predictably when people defer to a confident machine.",
        items=[
            ("What it is",
             "The tendency to over-trust an automated system — accepting its output "
             "without the scrutiny you would apply to a human colleague's work."),
            ("Why it happens",
             "Fluency reads as competence. AI output is grammatical, confident and "
             "well-formatted, and those cues are the ones humans use to judge reliability."),
            ("How it compounds",
             "Time pressure, high volume and a good track record all reduce checking — "
             "so the review becomes a formality exactly as the system's errors become rarer "
             "and harder to spot."),
            ("The counter-measure",
             "Structured verification: check the claim against the source, not against your "
             "impression of the output. Verify names, numbers, citations and dates "
             "independently every time."),
        ])),
],

# ================================================================ LU2
2: [
    ("table", dict(
        title="The Legal Baseline — Anonymisation vs Pseudonymisation",
        kicker="LU2 · T1 · THE DISTINCTION THAT MATTERS",
        intro="Getting this wrong is the single most common privacy compliance error in AI projects.",
        colheads=("Pseudonymisation", "Anonymisation"),
        rows=[
            ("What it does",
             "Replaces identifiers with a token or key; the link to the individual is "
             "retained somewhere.",
             "Irreversibly severs the link — no key exists that can restore identity."),
            ("Reversible?",
             "Yes — by anyone holding the mapping key.",
             "No — by design, not by policy."),
            ("Still personal data?",
             "YES. Remains fully in scope of the PDPA and GDPR, with all obligations intact.",
             "No. Out of scope, because there is no longer an identifiable individual."),
            ("Typical use",
             "Internal analytics where re-identification must remain possible for "
             "legitimate operational reasons.",
             "Publishing, external sharing, or training data where re-identification must "
             "be impossible."),
        ])),
    ("flow", dict(
        title="The Mechanics of K-Anonymity",
        kicker="LU2 · T1 · GENERALISE UNTIL INDISTINGUISHABLE",
        color="TEAL",
        intro="Guaranteeing an individual cannot be distinguished from at least k-1 others.",
        steps=[
            "Identify direct identifiers (name, NRIC, email) and remove them",
            "Identify quasi-identifiers (age, postcode, gender) that combine to re-identify",
            "Generalise values — exact age becomes an age band, postcode loses digits",
            "Suppress records that remain unique even after generalisation",
            "Verify every combination of quasi-identifiers appears at least k times",
        ],
        note="Its limit: k-anonymity fails when the attacker holds external auxiliary data, or when every "
             "record in a group shares the same sensitive value.")),
    ("pillars", dict(
        title="The Three Layers of AI Data Security",
        kicker="LU2 · T2 · DEFENCE IN DEPTH",
        intro="Protecting data in an AI system means protecting it at rest, in computation and at output.",
        items=[
            ("Layer 1 — The pipeline",
             "Encryption in transit and at rest; access control; format-preserving "
             "encryption so a field stays usable by downstream systems while losing its "
             "identifying power; data shifting and masking."),
            ("Layer 2 — The model",
             "Controls on what enters training; the training paradox of balancing data "
             "utility against data privacy; differential privacy and DP-SGD to bound what "
             "any one record can contribute."),
            ("Layer 3 — The output",
             "Output filtering to catch memorised training data; guarding against LLM "
             "memorisation, where a model reproduces verbatim sensitive strings it saw "
             "during training."),
            ("The governance wrapper",
             "Know your tools · establish policy · lock down inputs · understand external "
             "threats · update training · review vendors · plan for incidents."),
        ])),
    # Rendered as a tile grid, not a horizontal flow: seven chips across one row
    # forces the label text to overflow and break mid-word.
    ("pillars", dict(
        title="7-Step Governance Checklist for AI Adoption",
        kicker="LU2 · T2 · THE OPERATIONAL CHECKLIST",
        intro="This checklist is directly assessable — you should be able to reproduce all seven steps.",
        items=[
            ("1 · Know your tools",
             "Inventory every AI tool actually in use, including the shadow IT that staff "
             "adopted without approval."),
            ("2 · Establish policy",
             "Classify data as prohibited, restricted or permitted for AI, and publish it."),
            ("3 · Lock down inputs",
             "Anonymise or mask data before anything reaches a model."),
            ("4 · Understand external threats",
             "Prompt injection, data exfiltration, model extraction and vendor breach."),
            ("5 · Update training",
             "Staff must know the limits of the tools they are given."),
            ("6 · Review vendors",
             "Retention, training use, sub-processors, jurisdiction and incident history."),
            ("7 · Plan for incidents",
             "Detection, reporting deadline, assessment, notification and remediation."),
        ])),
    ("table", dict(
        title="Choosing the Right Protection",
        kicker="LU2 · T1 · TECHNIQUE SELECTION",
        intro="Each technique buys a different guarantee at a different cost to utility.",
        colheads=("Protects against", "Cost"),
        rows=[
            ("Masking / redaction",
             "Casual inspection of directly identifying fields.",
             "Cheap and fast, but destroys the field's analytical value entirely."),
            ("K-anonymity",
             "Singling out an individual from quasi-identifiers.",
             "Moderate loss of granularity; fails against auxiliary-data attacks."),
            ("Differential privacy",
             "Inferring whether any individual was in the dataset at all.",
             "Adds calibrated noise — a formal guarantee paid for in accuracy."),
            ("Homomorphic encryption",
             "Exposure during computation — data never decrypted to be processed.",
             "Strongest guarantee, but computationally very slow."),
            ("Synthetic data",
             "Direct exposure of any real record.",
             "Useful when masking destroys utility; fidelity and residual leakage must be validated."),
        ])),
    ("playbook", dict(
        title="Designing an Ethical AI Data Policy",
        kicker="LU2 · T3 · THE EXECUTIVE PLAYBOOK",
        items=[
            ("Classify",
             "Sort every data category into PROHIBITED (never enters an AI tool), "
             "RESTRICTED (only with safeguards) and PERMITTED (freely usable)."),
            ("Comply",
             "Name the regimes that bind you — PDPA as the Singapore baseline, plus GDPR, "
             "HIPAA or the EU AI Act where applicable."),
            ("Safeguard",
             "Mandate the specific controls: anonymisation before input, encryption, "
             "role-based access, audit logging and human review of outputs."),
            ("Respond",
             "Define detection, a reporting deadline, severity assessment, notification "
             "and a post-incident review that updates the policy."),
        ],
        tagline="Trust is engineered, not accidental — a policy nobody can follow protects nobody.")),
],

# ================================================================ LU3
3: [
    ("pillars", dict(
        title="The Three Pillars of Safe AI",
        kicker="LU3 · T1 · WHAT RESPONSIBLE DEPLOYMENT REQUIRES",
        items=[
            ("Intellectual property",
             "Was the training data licensed? Who owns the output? Getty Images v Stability "
             "AI put provenance of training data at the centre of the question."),
            ("Data privacy",
             "What personal data entered the model, under what lawful basis, and can it be "
             "extracted again through memorisation?"),
            ("Environmental impact",
             "Energy, water and carbon per training run and per inference — the cost that "
             "scales with every user you add."),
            ("The unifying question",
             "Responsible comparison scores systems on all three, not on benchmark accuracy "
             "alone. A more accurate model with unlicensed training data and no privacy "
             "posture is not the better choice."),
        ])),
    ("flow", dict(
        title="ISO/IEC 42005 — The Assessment Lifecycle",
        kicker="LU3 · T1 · IMPACT ASSESSMENT",
        color="VIOLET",
        intro="ISO/IEC 42005:2025 — internal guidance for assessing an AI system's impact on individuals, "
              "groups and society. Not a certification standard; you do not need an external auditor.",
        steps=[
            "Define scope, purpose and the context of use",
            "Identify affected individuals, groups and society",
            "Assess potential harms and benefits across the lifecycle",
            "Determine controls and mitigations for each identified harm",
            "Document the assessment and its residual risk",
            "Review and re-assess when the system or its context changes",
        ],
        note="Use it internally to bring structure to how consequences are evaluated — from planning and "
             "design through deployment and monitoring.")),
    ("stats", dict(
        title="Differential Privacy — The Epsilon Budget",
        kicker="LU3 · T1 · THE PRIVACY-UTILITY DIAL",
        intro="Epsilon (ε) quantifies privacy loss: lower means stronger privacy and noisier answers.",
        stats=[
            ("ε ≤ 1", "Strong privacy — high noise, suitable for publishing sensitive statistics"),
            ("ε ≈ 1–10", "Moderate — the practical working range for most deployed systems"),
            ("ε > 10", "Weak — the formal guarantee becomes close to meaningless"),
        ],
        note="DP-SGD applies this during training: clip each example's gradient to bound its influence, then "
             "add calibrated noise — so no single person's data can be recovered from the model.")),
    ("table", dict(
        title="Comparison of AI Regulations",
        kicker="LU3 · T2 · THE GLOBAL REGULATORY FRACTURE",
        intro="There is no single global AI regime — comparing systems means comparing against several.",
        colheads=("Approach", "Binding force"),
        rows=[
            ("EU AI Act",
             "Risk-tiered: prohibited, high, limited and minimal risk, with obligations "
             "scaled to the tier.",
             "Binding law with substantial financial penalties."),
            ("NIST AI 600-1 (US)",
             "A companion to the AI Risk Management Framework addressing risks specific to "
             "generative AI.",
             "Voluntary framework; influential in procurement and practice."),
            ("Canada AIDA",
             "Focused on 'high-impact' systems, with obligations on assessment and "
             "mitigation.",
             "Proposed legislation."),
            ("Singapore AI Verify",
             "Testing framework of 11 principles across process checks and technical "
             "tests, with the Model AI Governance Framework.",
             "Voluntary, industry-led; the practical baseline for Singapore organisations."),
        ])),
    ("table", dict(
        title="Red AI vs Green AI",
        kicker="LU3 · T2 · THE ENVIRONMENTAL TOLL",
        intro="Task alignment — routing work to the smallest model that can do it — is the single largest "
              "lever on AI's environmental cost.",
        colheads=("'Red AI' — frontier by default", "'Green AI' — right-sized"),
        rows=[
            ("Model choice",
             "Always the largest available frontier model, regardless of task difficulty.",
             "A small language model (SLM) for well-scoped, repetitive tasks; frontier "
             "models reserved for genuinely hard ones."),
            ("Energy per query",
             "Orders of magnitude higher; every user added multiplies it.",
             "Dramatically lower, and often runs on local or modest hardware."),
            ("Cost & latency",
             "Highest cost per call and slower responses.",
             "Cheaper and faster — the business case usually aligns with the green case."),
            ("When justified",
             "Open-ended reasoning, novel synthesis, complex multi-step work.",
             "Classification, extraction, routing, summarisation, structured formatting."),
        ])),
    ("pillars", dict(
        title="Openness Does Not Equal Transparency",
        kicker="LU3 · T2 · THE TRANSPARENCY CRISIS",
        intro="'Open-weights' is a licence claim, not a disclosure of how the system was built.",
        items=[
            ("What is usually disclosed",
             "Model weights, an architecture description, an inference licence and "
             "benchmark scores."),
            ("What usually is not",
             "The training-data composition and provenance, the data-filtering decisions, "
             "the human feedback process and the evaluation failures."),
            ("Why it matters for compliance",
             "You cannot assess IP provenance or privacy risk from weights alone — the "
             "questions a regulator asks concern the data, not the parameters."),
            ("What to ask a vendor",
             "Data provenance and licensing; retention and training use of your inputs; "
             "published evaluation results including failures; incident history and "
             "escalation path."),
        ])),
    ("table", dict(
        title="The Technical Trade-off — Accuracy vs Interpretability",
        kicker="LU3 · T3 · DEMYSTIFYING THE BLACK BOX",
        intro="The more capable the model, the harder it is to explain — and explanation is often a legal "
              "requirement.",
        colheads=("Interpretable by design", "Black box + post-hoc XAI"),
        rows=[
            ("Examples",
             "Linear and logistic regression, decision trees, rule lists.",
             "Deep neural networks, gradient-boosted ensembles, large language models."),
            ("Explanation",
             "The model IS the explanation — you can read the coefficients or the tree.",
             "Requires SHAP or LIME to approximate why a particular decision was made."),
            ("Trade-off",
             "Lower ceiling on accuracy for complex, high-dimensional problems.",
             "Higher accuracy, but the explanation is an approximation, not the mechanism."),
            ("Where each fits",
             "Regulated, contestable decisions — credit, hiring, benefits, sentencing.",
             "Perception, language and pattern tasks — with XAI bolted on where decisions "
             "affect people."),
        ])),
    ("table", dict(
        title="LIME vs SHAP",
        kicker="LU3 · T3 · TWO WAYS TO EXPLAIN A DECISION",
        colheads=("LIME", "SHAP"),
        rows=[
            ("Basis",
             "Fits a simple interpretable model locally around the one prediction being explained.",
             "Shapley values from cooperative game theory — each feature's fair share of the outcome."),
            ("Consistency",
             "Stochastic — re-running gives slightly different values each time.",
             "Deterministic and additive — the contributions sum exactly to the prediction."),
            ("Speed",
             "Fast; practical for quick, local inspection.",
             "Slower; exact computation is expensive for large models."),
            ("Best for",
             "Rapid, intuitive checks on individual predictions during development.",
             "Explanations that must be defended to a regulator, an auditor or the affected person."),
        ])),
    ("pillars", dict(
        title="The Anatomy of Algorithmic Discrimination",
        kicker="LU3 · T3 · HIGH-STAKES APPLICATIONS",
        intro="The same failure pattern recurs across documented cases in hiring, credit, health and policing.",
        items=[
            ("Amazon's recruiting tool",
             "Trained on ten years of predominantly male hires; learned to penalise "
             "resumes containing signals of being a woman. Withdrawn."),
            ("Apple Card",
             "Couples with shared finances received markedly different credit limits; "
             "neither the operator nor the issuer could explain the decisions."),
            ("IBM Watson for Oncology",
             "Recommended unsafe treatments; trained substantially on synthetic cases "
             "rather than real patient outcomes."),
            ("Clearview AI",
             "Scraped billions of facial images without consent to build an "
             "identification service sold to law enforcement."),
        ])),
    ("quote", dict(
        line1="Ethical AI is not a roadblock to innovation — it is the prerequisite.",
        line2="Cost reduction must advance alongside accessibility and quality. A system that is cheaper and "
              "faster but unfair, opaque or unsafe has not improved anything that matters.",
        kicker="LU3 · T3 · THE ULTIMATE OBJECTIVE")),
],
}

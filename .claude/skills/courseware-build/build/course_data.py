"""
SINGLE SOURCE OF TRUTH for the Responsible Generative AI Basics courseware.

Every artifact — the slide deck (PPT), Lesson Plan (LP) and Learner Guide (LG) —
is generated from the data in this module (+ data_domain1..3.py and
data_insights.py), so titles, topic numbering, activities, learning outcomes and
the schedule can never drift apart.

Content source:
  * The published course page
    https://www.tertiarycourses.com.sg/wsq-responsible-generative-ai-basics.html
  * The previous Master Trainer Slides (190 slides) in reference/, whose concept
    content has been transcribed into house-style visual components.
  * The approved Assessment Plan v2.0 (TSC "Responsible AI and Generative AI
    Practices", ICT-BAS-0055-1.1), which defines K1-K4 and A1-A6.

Edit here, then re-run build_slides.py / build_lesson_plan.py /
build_learner_guide.py (or ./build_courseware.sh).
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Responsible Generative AI Basics"
SHORT_TITLE  = "Responsible Generative AI Basics"
COURSE_CODE  = "TGS-2025060472"
VERSION      = "v12"          # slide-deck version (part of the .pptx filename)
DOC_VERSION  = "3.1"          # Lesson Plan / Learner Guide DOCX version (N.N)
VERSION_DATE = "11 August 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"

# Document Version Control Record rows: (version, effective date, changes, author)
VERSION_HISTORY = [
    ("1.0", "28 August 2025", "First version.", ORG),
    ("2.0", "17 October 2025", "Update company name.", ORG),
    ("3.0", "11 August 2026",
     "Courseware rebuilt on the single-source WSQ pipeline: slide deck redesigned "
     "in the all-white house style with visual components (tile grids, comparison "
     "tables, flow diagrams, stat bands) replacing imported screenshots; the 14 "
     "in-class web activities documented as step-by-step labs; Lesson Plan and "
     "Learner Guide regenerated and aligned to the deck.", ORG),
    ("3.1", "11 August 2026",
     "QA fixes: Lesson Plan slide citations corrected to the true deck index and the daily "
     "schedule rebalanced so the stated hours reconcile; Learner Guide gains a UI screenshot "
     "and a 'Test it' verification box for each of the 14 activities; the 7-step governance "
     "checklist redrawn as a tile grid to stop chip text clipping.", ORG),
]
DAYS         = 1

TSC_TITLE   = "Responsible AI and Generative AI Practices"
TSC_CODE    = "ICT-BAS-0055-1.1"
TSC_LEVEL   = "Level 1"

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Apply ethical reasoning to assess generative AI outputs and guide responsible "
    "decision-making in AI implementation.",
    "LO2: Apply privacy safeguards to protect sensitive data used in generative AI through "
    "anonymisation and secure storage methods.",
    "LO3: Compare generative AI systems for ethical compliance based on intellectual property, "
    "privacy, and environmental impact.",
]

# ---------------------------------------------------- competency map (Assessment Plan v2.0)
# Knowledge statements — assessed by the Written Assessment (WA-SAQ)
KNOWLEDGE = [
    ("K1", "Data anonymisation and de-identification techniques"),
    ("K2", "Ethical considerations and potential risks of generative AI interaction"),
    ("K3", "Responsible AI principles and best practices for development and deployment, "
           "including intellectual property, data privacy and environmental impact considerations"),
    ("K4", "Ethical principles in AI"),
]
# Ability statements — assessed by the Case Study (CS)
ABILITIES = [
    ("A1", "Apply ethical principles in decision-making related to AI"),
    ("A2", "Exercise professional scepticism to exercise sound judgement on Gen AI output"),
    ("A3", "Apply privacy measures when handling data for AI applications (e.g., implement simple "
           "data anonymisation and de-identification techniques, secure data storage using basic "
           "encryption)"),
    ("A4", "Design guidelines or strategies for ethical AI use, including use of sensitive data in "
           "generative AI tools"),
    ("A5", "Compare AI systems based on considerations such as compliance with intellectual "
           "property, data privacy and environmental impact"),
    ("A6", "Compare ethical issues in AI applications"),
]

# ------------------------------------------------------------------ topics (= Learning Units)
TOPICS = [
    dict(num=1, code="LU1",
         title="Ethical Principles of Generative AI",
         subtitle="Risks of GenAI Interaction · Ethical Principles · Ethical Decision-Making · Professional Scepticism",
         concepts=[
            "Generative AI carries hidden costs beyond the subscription fee: environmental load "
            "(energy, water, carbon), security exposure, and psychological or societal impact on "
            "the people who use it.",
            "Deepfakes, voice cloning and face-swapping have made synthetic media cheap and "
            "convincing — eroding the assumption that seeing is believing.",
            "AI bias is not a single defect: it is introduced through the training data, the model "
            "objective, and the deployment context, and it compounds at each stage.",
            "Singapore's AI Verify framework defines 11 principles of trustworthy AI, split into "
            "process checks and technical tests, and is operationalised through Project Moonshot.",
            "Applying ethics in practice means stratifying risk (EU AI Act), keeping a human in the "
            "loop for high-stakes decisions, and engineering ethics into the design, not bolting it on.",
            "Professional scepticism is the discipline of verifying GenAI output against source "
            "evidence — the antidote to automation bias, where people defer to a confident machine.",
         ]),
    dict(num=2, code="LU2",
         title="Generative AI Privacy Techniques",
         subtitle="Anonymisation & De-identification · Privacy Measures in Practice · Ethical Data Guidelines",
         concepts=[
            "Anonymisation irreversibly severs the link to an individual; pseudonymisation only "
            "replaces identifiers and remains personal data under the PDPA and GDPR.",
            "K-anonymity guarantees an individual cannot be distinguished from at least k-1 others "
            "by generalising or suppressing quasi-identifiers.",
            "Release-based privacy fails when an attacker holds external auxiliary data — the "
            "re-identification attack that motivated stronger, computation-based guarantees.",
            "The three layers of AI data security are the pipeline (encryption in transit and at "
            "rest), the model (training and memorisation controls) and the output (filtering).",
            "Format-preserving encryption and data-shifting keep a field usable by downstream "
            "systems while removing its identifying power.",
            "An ethical AI data policy classifies data as prohibited, restricted or permitted for "
            "AI input, and pairs each class with a mandated safeguard.",
         ]),
    dict(num=3, code="LU3",
         title="Best Practices of Responsible Generative AI",
         subtitle="Responsible AI Principles · Comparing AI Systems · Comparing Ethical Issues",
         concepts=[
            "The EU AI Act regulates by risk tier — unacceptable, high, limited and minimal — with "
            "obligations that scale to the harm the system can cause.",
            "ISO/IEC 42005:2025 gives an internal, non-certifiable structure for assessing an AI "
            "system's impact on individuals, groups and society across its lifecycle.",
            "Differential privacy is a mathematical guarantee: the output does not reveal whether "
            "any single individual's record was in the dataset, tuned by the epsilon budget.",
            "Comparing AI systems responsibly means scoring them on intellectual property "
            "provenance, data privacy posture and environmental cost — not accuracy alone.",
            "'Green AI' routes appropriate tasks to small language models, cutting energy and cost "
            "against the 'Red AI' default of always using the largest frontier model.",
            "Explainability trades off against raw accuracy; XAI frameworks such as SHAP and LIME "
            "recover interpretability where the decision affects people's lives.",
         ]),
]

# ------------------------------------------------------------------ day theme (1 day, 7h training + 1h assessment)
DAY_THEMES = {
    1: "Ethical Principles, Privacy Techniques, Responsible AI Best Practices & Assessment",
}

# ------------------------------------------------------------------ assessment
ASSESSMENT = dict(
    written="Written Assessment (WA) — Short-Answer Questions (SAQ), 30 minutes, open book.",
    practical="Case Study (CS) — one continuous scenario with open-ended tasks, 30 minutes, open book.",
    note="A minimum of 75% attendance (per SSG Digital Attendance record) is required to be eligible "
         "for assessment and funding. Learners must be assessed as Competent in every K and A, and "
         "complete the TRAQOM survey.",
)

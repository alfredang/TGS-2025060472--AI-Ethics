# Learner Guide — Responsible Generative AI Basics

**Course code:** TGS-2025060472
**Version:** 3.2
**Provider:** Tertiary Infotech Academy Pte Ltd

## How to Use This Guide

This Learner Guide accompanies the WSQ course Responsible Generative AI Basics (TGS-2025060472). Use it with the course slides during class and during the approved open-book assessment.

All 14 activities are available from the [activity hub](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/). A modern browser, internet access and a learner-owned notes file are required. Activities 6 and 7 require a free Google Gemini API key; Activities 13 and 14 can optionally use one.

## Course Learning Outcomes

- LO1: Apply ethical reasoning to assess generative AI outputs and guide responsible decision-making in AI implementation.
- LO2: Apply privacy safeguards to protect sensitive data used in generative AI through anonymisation and secure storage methods.
- LO3: Compare generative AI systems for ethical compliance based on intellectual property, privacy, and environmental impact.

## Skills Framework Reference

- **TSC title:** Responsible AI and Generative AI Practices
- **TSC code:** ICT-BAS-0055-1.1
- **Written Assessment (SAQ):** K1–K4
- **Case Study:** A1–A6

## LU1 — Ethical Principles of Generative AI

Risks of GenAI Interaction · Ethical Principles · Ethical Decision-Making · Professional Scepticism

### Key concepts

- Generative AI carries hidden costs beyond the subscription fee: environmental load (energy, water, carbon), security exposure, and psychological or societal impact on the people who use it.
- Deepfakes, voice cloning and face-swapping have made synthetic media cheap and convincing — eroding the assumption that seeing is believing.
- AI bias is not a single defect: it is introduced through the training data, the model objective, and the deployment context, and it compounds at each stage.
- Singapore's AI Verify framework defines 11 principles of trustworthy AI, split into process checks and technical tests, and is operationalised through Project Moonshot.
- Applying ethics in practice means stratifying risk (EU AI Act), keeping a human in the loop for high-stakes decisions, and engineering ethics into the design, not bolting it on.
- Professional scepticism is the discipline of verifying GenAI output against source evidence — the antidote to automation bias, where people defer to a confident machine.

### Activity 1 — AI Ethical Dilemma Simulator

**Objective:** Recognise the ethical considerations and potential risks that arise when interacting with generative AI (K2)
**Open:** [https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu1-ethical-principles/ethical-dilemma/](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu1-ethical-principles/ethical-dilemma/)
**Duration:** 10 minutes
**Scenario:** Work through six real-world AI dilemmas — from AI-generated hospital discharge summaries to resume-screening bias — choosing the most defensible course of action in each and reading the consequences of the choice you made.
**You will produce:** A completed 6-scenario run with your score out of 6 and notes on the stakeholders and ethical principles at stake in each dilemma

#### Step-by-step

1. Open the activity. It starts on Scenario 1 of 6 — 'AI-Generated Discharge Summaries' in the Healthcare domain.
2. Read the scenario description, then click the choice you judge to be the most ethical response. The three options colour-code and each is labelled (for example 'Best approach', 'Partially addresses risk' or 'Dangerous approach').
3. Read the Analysis card that appears — note the 'Affected Stakeholders:' and 'Ethical Principles at Stake:' lines, and write down which principle you had overlooked.
4. Click 'Next Scenario →' and repeat for all six domains: Healthcare, Hiring & Recruitment, Journalism, Education, Surveillance & Privacy and Creative Industries.
5. At the 'Assessment Complete' card, record your score out of 6 and the message you were given.
6. Use 'Try Again' to re-run any dilemma where your first instinct was wrong, and articulate why the better option was better.

**Test it:** You can state, for at least three of the six scenarios, who the affected stakeholders were and which ethical principle the 'dangerous' option violated.

### Activity 2 — AI Ethical Principles Quiz

**Objective:** Identify and apply the core ethical principles in AI (K4)
**Open:** [https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu1-ethical-principles/principles-quiz/](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu1-ethical-principles/principles-quiz/)
**Duration:** 10 minutes
**Scenario:** Test your grasp of the principles that underpin trustworthy AI — fairness, transparency, accountability, privacy, beneficence and human agency — across ten applied questions.
**You will produce:** A completed 10-question quiz with your score and the live Correct / Incorrect counters

#### Step-by-step

1. Open the activity. All ten questions are on one scrollable page, each headed 'Question N of 10'.
2. Read the question and its italic hint line, then click the option you believe names the correct principle.
3. The correct answer turns green (a wrong pick turns red) and an explanation block appears — read it before moving on.
4. Watch the 'Correct:' and 'Incorrect:' counters in the nav bar as you work down the page.
5. Answer all ten, then read the 'Quiz Complete!' panel and record your score out of 10.
6. Click 'Retake Quiz' and re-attempt any principle you confused with another — fairness vs beneficence is the usual trap.

**Test it:** You score at least 7/10 and can define each of the six principles in one sentence without looking at the slides.

### Activity 3 — Prompt Injection Playground

**Objective:** Explain how prompt injection threatens AI safety and how layered defences reduce the risk (K2)
**Open:** [https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu1-ethical-principles/prompt-injection/](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu1-ethical-principles/prompt-injection/)
**Duration:** 10 minutes
**Scenario:** Attack three simulated AI assistants — an undefended customer-service bot, a banking assistant with basic defences and a medical triage AI with strong defences — and see which injections get through each layer of protection.
**You will produce:** An Attack Scoreboard showing your total attempts, successful injections, success rate and which of the three scenarios you breached

#### Step-by-step

1. Open the activity and read the 'What is Prompt Injection?' tiles covering the six attack types (Role Override, Instruction Override, Information Extraction, Jailbreaking, Indirect Injection, Context Manipulation).
2. Under 'Select a Challenge Scenario', stay on the 'Level 1: No Defenses' tab — the Customer Service Bot. Click 'Reveal System Prompt' to see the hidden instructions and the secrets it is protecting.
3. Under 'Try a preset injection or write your own:', click a preset chip such as 'Ignore instructions' or 'Role override', then click 'Send Message'.
4. Read the verdict card — '⚠ Injection Successful!' names the Attack Type and explains 'Why this worked:', while '✅ Defense Held' means the guardrail stopped you.
5. Switch to 'Level 2: Basic Defenses' and then 'Level 3: Strong Defenses', trying the harder presets (for example 'Base64 encoding', 'Nested injection' or 'Emotional manipulation') to see which defences hold.
6. Record the Attack Scoreboard — Total Attempts, Successful Injections, Success Rate and Scenarios Breached — then read the 'Defense Techniques Reference' to map each successful attack to the control that would have blocked it.

**Test it:** Your scoreboard shows a markedly lower success rate at Level 3 than at Level 1, and you can name the specific defence (input sanitisation, system-prompt hardening or output filtering) that blocked each failed attack.

### Activity 4 — Ethical Decision-Making Framework

**Objective:** Apply ethical principles systematically in decision-making related to AI (A1)
**Open:** [https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu1-ethical-principles/decision-framework/](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu1-ethical-principles/decision-framework/)
**Duration:** 15 minutes
**Scenario:** Take one contested AI deployment through a six-stage structured ethical analysis — scenario, stakeholders, risks, principles, alternatives, decision — and produce a defensible, documented recommendation rather than a gut reaction.
**You will produce:** A printed 'Ethical Decision Analysis Summary' report with all eight sections completed

#### Step-by-step

1. Open the activity. In 'Step 1: Define the Scenario', click a sample chip such as 'AI in hiring decisions' or 'AI-generated medical reports' to load a scenario, then click 'Next: Stakeholders →'.
2. In 'Step 2: Identify Stakeholders', list everyone affected — one per line — including the people who are acted upon, not just the users and the vendor. Click 'Next: Risks & Benefits →'.
3. In 'Step 3: Assess Risks & Benefits', fill in both 'Potential Benefits' and 'Potential Risks'. Be specific about who bears each risk. Click 'Next: Principles →'.
4. In 'Step 4: Apply Ethical Principles', tick the principles in tension (Fairness, Transparency, Accountability, Privacy, Beneficence, Human Agency) and explain the conflict in the notes field. Click 'Next: Alternatives →'.
5. In 'Step 5: Consider Alternatives', record at least two genuine alternatives — including 'do not deploy' — then click 'Next: Decision →'.
6. In 'Step 6: Make Your Decision', write your decision and a 'Monitoring & Review Plan', click 'Generate Summary', then use 'Print / Save as PDF' to keep your report.

**Test it:** Your summary report has all eight sections filled, names at least one alternative you rejected and why, and states how the decision will be monitored after deployment.

### Activity 5 — AI Output Scepticism Checker

**Objective:** Exercise professional scepticism to exercise sound judgement on generative AI output (A2)
**Open:** [https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu1-ethical-principles/skepticism-checker/](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu1-ethical-principles/skepticism-checker/)
**Duration:** 10 minutes
**Scenario:** Evaluate confident, fluent, and quietly wrong AI-generated text against a 16-point scepticism checklist, and score how far it can actually be trusted.
**You will produce:** A scepticism score out of 100 with a risk verdict and the recommendations list for the text you assessed

#### Step-by-step

1. Open the activity. Under 'Paste AI-Generated Text', click a sample chip — 'Medical summary', 'Historical essay', 'Legal advice' or 'Financial analysis' — or paste AI output of your own.
2. Click 'Begin Evaluation' to reveal the 'Scepticism Evaluation Checklist'.
3. Work through all 16 checks across the six categories: Source Verification, Logical Consistency, Bias Detection, Factual Accuracy, Completeness and Appropriateness.
4. For each issue you find, tick the checkbox and set the severity dropdown to Low, Medium or High — judge the severity yourself rather than accepting the default.
5. Click 'Calculate Scepticism Score' and read the score out of 100, the risk verdict and the 'Recommendations' list.
6. Click 'Evaluate New Text' and repeat with a second sample, comparing which category of failure was most common.

**Test it:** You can point to at least three specific unverifiable or fabricated claims in the sample text (such as an invented statistic or a non-existent citation) and justify the severity you assigned to each.

### Activity 6 — The Cognitive Threat Matrix

**Objective:** Analyse how human cognitive bias combines with generative AI failure modes to escalate risk (K2, A2)
**Open:** [https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu1-ethical-principles/cognitive-threat-matrix/](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu1-ethical-principles/cognitive-threat-matrix/)
**Duration:** 15 minutes
**Scenario:** Pair a human cognitive bias with the AI failure mode it amplifies — automation bias with hallucination, confirmation bias with skewed data — and generate a structured risk analysis of a scenario from your own workplace.
**You will produce:** A five-part AI risk analysis covering scenario overview, the bias at play, risk escalation, real-world impact and mitigation strategies

#### Step-by-step

1. Open the activity and enter your key in the 'Google Gemini API Key' field — a free key is available from aistudio.google.com/api-keys. The status line confirms 'Key format looks valid'.
2. Click one of the four threat cards in the matrix: 'Automation Bias ➡ The Hallucination Threat', 'Confirmation Bias ➡ The Skewed Data Threat', 'Overconfidence ➡ The Verification Failure' or 'Groupthink ➡ The Ethical Blindspot'.
3. Read the 'Bias:' and 'Risk:' lines on the card so you know which pairing you are analysing.
4. In 'Sample Scenarios', click one of the five suggested questions to load it — or type your own scenario from your workplace into the textarea.
5. Click 'Generate' and wait for the 'Risk Analysis' panel.
6. Read the five sections — Scenario Overview, Cognitive Bias at Play, Risk Escalation, Real-World Impact and Mitigation Strategies — and mark which mitigations you could actually implement in your own organisation.

**Test it:** You produce a risk analysis for a scenario from your own workplace and can name at least two mitigations from Section 5 that are realistic for your team to adopt.

## LU2 — Generative AI Privacy Techniques

Anonymisation & De-identification · Privacy Measures in Practice · Ethical Data Guidelines

### Key concepts

- Anonymisation irreversibly severs the link to an individual; pseudonymisation only replaces identifiers and remains personal data under the PDPA and GDPR.
- K-anonymity guarantees an individual cannot be distinguished from at least k-1 others by generalising or suppressing quasi-identifiers.
- Release-based privacy fails when an attacker holds external auxiliary data — the re-identification attack that motivated stronger, computation-based guarantees.
- The three layers of AI data security are the pipeline (encryption in transit and at rest), the model (training and memorisation controls) and the output (filtering).
- Format-preserving encryption and data-shifting keep a field usable by downstream systems while removing its identifying power.
- An ethical AI data policy classifies data as prohibited, restricted or permitted for AI input, and pairs each class with a mandated safeguard.

### Activity 7 — Data Anonymisation Techniques

**Objective:** Distinguish the anonymisation spectrum — de-identification, pseudonymisation, objective and subjective anonymisation (K1)
**Open:** [https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu2-privacy/dataprivacy/](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu2-privacy/dataprivacy/)
**Duration:** 15 minutes
**Scenario:** Run one set of sensitive records through four different anonymisation techniques side by side, and see why only some of them actually remove the re-identification risk.
**You will produce:** A side-by-side comparison table showing the same record under all four techniques, including three different reviewers' subjective judgements

#### Step-by-step

1. Open the activity and enter your key in the 'Google Gemini API Key' field (use the 👁 button to check what you typed).
2. Click 'Generate Sample Data'. Five fictional records appear under 'Original Sample Data' with name, email, phone, date of birth, address, SSN, medical condition, salary and employer.
3. Study the raw record and decide, before you continue, which fields you would remove to make it safe to share.
4. Click 'Apply All Techniques' and wait while three reviewer personas are simulated.
5. Compare the four technique cards — 'Deidentification' (High Re-ID Risk), 'Pseudonymization' (Moderate Risk), 'Objective Anonymization' (Zero Risk) and 'Subjective Anonymization' (Context-Dependent) — reading the Definition, Regulatory and AI Training notes on each.
6. In the 'Side-by-Side Comparison' table, compare the Intern, Analyst and Privacy Officer columns for the same field and note where the three reviewers disagreed.

**Test it:** You can explain why de-identification still carries a high re-identification risk, and why the three subjective reviewers produced different results from the same source record.

### Activity 8 — Python Data Anonymisation Pipeline

**Objective:** Apply privacy measures when handling data for AI applications by building an anonymisation pipeline (A3)
**Open:** [https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu2-privacy/anonymizer-python/](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu2-privacy/anonymizer-python/)
**Duration:** 15 minutes
**Scenario:** Build a seven-stage anonymisation pipeline over a raw dataset — pseudo-IDs, text shifting, masking, generalisation and column dropping — then export both the anonymised data and the Python code that produced it.
**You will produce:** An exported anonymised CSV plus the generated Python script implementing your chosen techniques

#### Step-by-step

1. Open the activity and study the seven-node pipeline diagram: Raw Dataset → Pseudo-IDs → Text Shifting → Data Masking → Generalisation → Drop Columns → Export.
2. In 'Step 1: Raw Dataset (CSV Input)', click a sample dataset — 'Patient Records', 'Employee Data' or 'Student Records'. The RAW table loads with directly identifying columns visible.
3. In 'Step 2: Select Anonymisation Techniques', review the five techniques (Pseudo-Identifiers, ASCII Text Shifting, Data Masking, Generalisation, Drop Identity Columns) and the Python one-liner shown beneath each.
4. Untick 'Drop Identity Columns', click 'Run Pipeline', and observe that names and emails survive in the output — then re-tick it and run again to see the difference.
5. Read the per-step detail cards and the final ANONYMISED table, checking that no directly identifying field remains.
6. In 'Export Anonymised Dataset', click 'Download as CSV' and 'Copy Python Code' to keep both deliverables.

**Test it:** Your exported CSV contains no name, email or SSN values, ages appear as ranges rather than exact values, and you can explain what each line of the generated Python code does.

### Activity 9 — Ethical AI Data Policy Generator

**Objective:** Design guidelines or strategies for ethical AI use, including use of sensitive data in generative AI tools (A4)
**Open:** [https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu2-privacy/privacy-policy/](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu2-privacy/privacy-policy/)
**Duration:** 15 minutes
**Scenario:** Produce a complete, organisation-specific AI data-handling policy through a guided five-step wizard — the document that tells your colleagues what they may and may not paste into an AI tool.
**You will produce:** A printed seven-section 'AI Data Handling Policy' tailored to your organisation, sector and risk tolerance

#### Step-by-step

1. Open the activity. In 'Step 1: Organisation Profile', enter your organisation name, choose your Industry Sector and Organisation Size, and list the AI tools your organisation actually uses. Click 'Next →'.
2. In 'Step 2: Data Classification', tick every category your organisation handles — PII, financial data, health records, employee records, intellectual property and the rest. Click 'Next →'.
3. In 'Step 3: Regulatory Requirements', tick the regimes that bind you. For a Singapore organisation PDPA is the baseline; add GDPR, HIPAA or the EU AI Act if they apply. Click 'Next →'.
4. In 'Step 4: Safeguards & Controls', select the controls you will genuinely enforce — anonymisation before AI input, encryption, role-based access, audit logging, mandatory human review, and so on. Click 'Next →'.
5. In 'Step 5: Additional Considerations', set your Risk Tolerance Level (Conservative, Moderate or Progressive) and add any organisation-specific requirements, then click 'Generate Policy'.
6. Review the generated seven-section policy and click 'Print / Save as PDF'. Check that its PROHIBITED list matches the data your staff are most likely to paste into a chatbot.

**Test it:** Your policy names the specific AI tools in use, lists the data categories that must never be entered into them, and states an incident-response reporting deadline.

## LU3 — Best Practices of Responsible Generative AI

Responsible AI Principles · Comparing AI Systems · Comparing Ethical Issues

### Key concepts

- The EU AI Act regulates by risk tier — unacceptable, high, limited and minimal — with obligations that scale to the harm the system can cause.
- ISO/IEC 42005:2025 gives an internal, non-certifiable structure for assessing an AI system's impact on individuals, groups and society across its lifecycle.
- Differential privacy is a mathematical guarantee: the output does not reveal whether any single individual's record was in the dataset, tuned by the epsilon budget.
- Comparing AI systems responsibly means scoring them on intellectual property provenance, data privacy posture and environmental cost — not accuracy alone.
- 'Green AI' routes appropriate tasks to small language models, cutting energy and cost against the 'Red AI' default of always using the largest frontier model.
- Explainability trades off against raw accuracy; XAI frameworks such as SHAP and LIME recover interpretability where the decision affects people's lives.

### Activity 10 — AI System Comparison Matrix

**Objective:** Compare AI systems on intellectual property, data privacy and environmental impact (A5)
**Open:** [https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu3-best-practices/ai-comparison/](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu3-best-practices/ai-comparison/)
**Duration:** 15 minutes
**Scenario:** Score ChatGPT, Claude and Gemini across five responsibility dimensions and plot them on a radar chart — turning 'which AI should we use?' into an evidence-based comparison rather than a brand preference.
**You will produce:** A radar comparison chart and scored comparison table ranking at least three AI systems by overall average

#### Step-by-step

1. Open the activity. Three systems are pre-loaded as tabs — ChatGPT, Claude and Gemini — each with starting scores.
2. With the ChatGPT tab selected, drag the five sliders to your own assessment: '© IP Compliance', '🔐 Data Privacy', '🌿 Environmental Impact', '⚖️ Bias Mitigation' and '🔍 Transparency'. Use the anchor labels under each slider to calibrate.
3. Click the Claude and Gemini tabs and score each system the same way, justifying every score you change from its default.
4. Click '+ Add System', enter a fourth system your organisation is considering, and click 'Add' — it starts at 5 on every dimension.
5. Score the new system, then click 'Update Comparison Chart'.
6. Read the radar chart and the comparison table, noting the 'Overall Average' row — then identify which dimension separates the systems most sharply.

**Test it:** Your radar chart shows four systems, and you can justify each score you assigned with a specific reason (such as training-data provenance or published energy figures) rather than brand reputation.

### Activity 11 — Differential Privacy Explorer

**Objective:** Explain how differential privacy protects individuals and the privacy-utility trade-off it imposes (K1, K3)
**Open:** [https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu3-best-practices/differential-privacy/](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu3-best-practices/differential-privacy/)
**Duration:** 15 minutes
**Scenario:** Turn the epsilon dial and watch the privacy-utility trade-off happen in front of you — strong privacy makes the answer noisy, weak privacy makes it accurate but leaks.
**You will produce:** A set of query results at three different epsilon values plus a spent privacy budget showing how many queries a dataset can safely answer

#### Step-by-step

1. Open the activity and read the 'What is Differential Privacy?' card, including the formal guarantee.
2. On the 'Laplace Mechanism' tab, leave Epsilon at 1.00, choose 'Average Salary' from the Query dropdown and click 'Run Query (10 trials)'. Note the True Answer against the Noisy Answer.
3. Drag Epsilon down to about 0.1 and re-run — the noise scale grows and the answers scatter. Then push Epsilon up to 10 and re-run: the answers are accurate but the privacy guarantee is nearly worthless.
4. Switch to the 'Randomised Response' tab. Read the sensitive survey question, set the 'True "Yes" Rate (%)' and click 'Run Simulation' to see how an individual keeps deniability while the aggregate stays estimable.
5. Switch to the 'Privacy Budget' tab. Click '+ Add Query' several times and watch Spent rise and Remaining fall against the Total Budget.
6. Keep adding queries until the Status shows the budget is exhausted, and note how few queries a strict budget actually permits.

**Test it:** You can state what epsilon controls, explain why a smaller epsilon means stronger privacy but a less useful answer, and say what happens once a privacy budget is spent.

### Activity 12 — Explainable AI (XAI) Explorer

**Objective:** Compare explainability techniques and the accuracy-interpretability trade-off (K3, A6)
**Open:** [https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu3-best-practices/xai-explorer/](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu3-best-practices/xai-explorer/)
**Duration:** 15 minutes
**Scenario:** Open the black box on a loan-approval model: adjust an applicant's profile, watch the decision flip, and compare how LIME and SHAP each explain why.
**You will produce:** LIME and SHAP explanations for the same borderline applicant, plus the side-by-side comparison of the two methods

#### Step-by-step

1. Open the activity and read the two concept cards explaining LIME and SHAP.
2. In the 'Loan Approval Model Simulator', click the 'Borderline Case' scenario chip and note the Decision, Approval Score and Confidence against the 0.50 threshold.
3. Drag the 'Credit Score' slider up and down and watch the decision flip — identify the score at which the applicant crosses the threshold.
4. On the 'LIME Explanation' tab, click 'Run LIME Analysis' and read which features pushed the decision toward approval (green) and toward denial (red).
5. Click 'Run LIME Analysis' a second time — the values shift slightly because LIME samples randomly. Then open the 'SHAP Explanation' tab and click 'Run SHAP Analysis', which gives the same answer every time.
6. Scroll to 'LIME vs SHAP — Side by Side' and the comparison table, and decide which method you would present to a rejected applicant and why.

**Test it:** You can name the feature that most influenced the decision, and explain why SHAP's consistency matters when an explanation may have to be defended to a regulator or a customer.

### Activity 13 — The Ethical Paradigms of AI Resource Allocation

**Objective:** Compare ethical issues in AI applications across competing ethical frameworks (A6)
**Open:** [https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu3-best-practices/ai-resource-allocation/](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu3-best-practices/ai-resource-allocation/)
**Duration:** 15 minutes
**Scenario:** Allocate a scarce resource — 50 treatments among 120 eligible patients — three times over, once under each ethical paradigm, and confront the fact that all three are defensible and they disagree about who lives.
**You will produce:** Three allocation results for the same scenario under the Utilitarian, Egalitarian and Prioritarian paradigms, with your own written justification of which is most appropriate

#### Step-by-step

1. Open the activity and read the three paradigm cards — 'Utilitarian' (Cost-Effectiveness), 'Egalitarian' (Equal Access) and 'Prioritarian' (Needs-Based) — noting the ✓ pro and ✗ con of each.
2. Under 'Select a Case Study Scenario', choose 'Healthcare: Precision Medicine' and read the constraints and the patient profile table.
3. In the 'Allocation Simulator', click '⚖️ Utilitarian' and record the outcomes grid: Served, Avg Efficacy, Total Impact, Equity and Vulnerable Served.
4. Click '🤝 Egalitarian' and then '🎯 Prioritarian', recording the same five outcome measures each time and noting which patients gained or lost their place.
5. In 'Your Ethical Analysis', choose the paradigm you believe fits this scenario and write your reasoning, stating explicitly which trade-off you are willing to accept.
6. Optionally enter a Gemini API key and click 'Analyse with AI' to have your reasoning critiqued, then repeat the comparison on the Education or Disaster scenario.

**Test it:** You can show that the three paradigms served measurably different groups from identical inputs, and defend your chosen paradigm while naming the specific harm it accepts.

### Activity 14 — AI Ethics Case Study Analyzer

**Objective:** Identify ethical issues in real AI deployments and propose remediation (A6, A1)
**Open:** [https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu3-best-practices/ethics-case-study/](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu3-best-practices/ethics-case-study/)
**Duration:** 15 minutes
**Scenario:** Analyse documented AI ethics failures — IBM Watson for Oncology, the Apple Card credit investigation, Amazon's recruiting tool, Clearview AI — and propose the remediation that should have been in place.
**You will produce:** A written analysis of at least one case identifying its ethical issues and your proposed remediation, compared against an AI critique

#### Step-by-step

1. Open the activity. Use the filter bar — 'All Cases', 'Healthcare', 'Finance', 'Creative', 'Education', 'Employment', 'Government' — to find a case in a sector close to your own work.
2. Click a case card to expand it, and read the 'Background', 'Key Ethical Issues', 'Principles at Stake' and 'Affected Stakeholders' sections.
3. In the 'Your Analysis' form, answer 'What ethical issues do you identify?' in your own words before reading any further — this is the same task as Question 4 of the Case Study assessment.
4. Answer 'What remediation would you propose?', naming controls that are specific and enforceable rather than general statements of good intent.
5. Optionally enter a Gemini API key and click 'Analyse with Gemini AI', then compare its analysis with yours and note anything you missed.
6. Scroll to 'Cross-Cutting Patterns' and identify which of the six patterns — Power Asymmetry, Feedback Loops, Accountability Gaps, Consent Erosion, Digital Divide, Transparency Theatre — appears in your chosen case.

**Test it:** Your analysis names at least three distinct ethical issues, proposes a specific remediation for each, and identifies which cross-cutting pattern the failure belongs to.

## Quick Reference — Activities by Learning Unit

| Learning Unit | Activity | Duration |
|---|---|---|
| LU1 | 1. AI Ethical Dilemma Simulator | 10 minutes |
| LU1 | 2. AI Ethical Principles Quiz | 10 minutes |
| LU1 | 3. Prompt Injection Playground | 10 minutes |
| LU1 | 4. Ethical Decision-Making Framework | 15 minutes |
| LU1 | 5. AI Output Scepticism Checker | 10 minutes |
| LU1 | 6. The Cognitive Threat Matrix | 15 minutes |
| LU2 | 7. Data Anonymisation Techniques | 15 minutes |
| LU2 | 8. Python Data Anonymisation Pipeline | 15 minutes |
| LU2 | 9. Ethical AI Data Policy Generator | 15 minutes |
| LU3 | 10. AI System Comparison Matrix | 15 minutes |
| LU3 | 11. Differential Privacy Explorer | 15 minutes |
| LU3 | 12. Explainable AI (XAI) Explorer | 15 minutes |
| LU3 | 13. The Ethical Paradigms of AI Resource Allocation | 15 minutes |
| LU3 | 14. AI Ethics Case Study Analyzer | 15 minutes |

## Assessment

- Written Assessment (WA) — Short-Answer Questions (SAQ), 30 minutes, open book.
- Case Study (CS) — one continuous scenario with open-ended tasks, 30 minutes, open book.
- Format: Open book — this guide, the course slides and approved materials only.
- Grading: Competent / Not Yet Competent.
- A minimum of 75% attendance (per SSG Digital Attendance record) is required to be eligible for assessment and funding. Learners must be assessed as Competent in every K and A, and complete the TRAQOM survey.

## Assessment Flow

1. Complete TRAQOM from the LMS QR code.
2. Complete Assessment Digital Attendance.
3. Complete the Written Assessment and Case Study.
4. Submit answers through the LMS.
5. Sign the Assessment Summary Record.

Courseware and assessment access: https://lms-tms.tertiaryinfotech.com/

## Support

- Email: enquiry@tertiaryinfotech.com
- Tel: +65 6100 0613
- Website: https://www.tertiarycourses.com.sg
- LMS: https://lms-tms.tertiaryinfotech.com/

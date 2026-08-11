"""LU3 — Best Practices of Responsible Generative AI: in-class activities 10-14.

Every step is written against the real UI of the lab web app in
labs/lu3-best-practices/<slug>/ so the Learner Guide can be followed verbatim.
"""

BASE = "labs/lu3-best-practices"

DOMAIN3 = [
    dict(
        num=10,
        phases=['Score ChatGPT', 'Score Claude & Gemini', 'Add a 4th system', 'Update the chart', 'Read the radar & table'],
        topic=3,
        title="AI System Comparison Matrix",
        objective="Compare AI systems on intellectual property, data privacy and environmental impact (A5)",
        slug="ai-comparison",
        path=f"{BASE}/ai-comparison/",
        apikey=None,
        desc="Score ChatGPT, Claude and Gemini across five responsibility dimensions and plot them on a radar "
             "chart — turning 'which AI should we use?' into an evidence-based comparison rather than a "
             "brand preference.",
        build="A radar comparison chart and scored comparison table ranking at least three AI systems by overall average",
        duration="15 minutes",
        steps=[
            ("Open the activity. Three systems are pre-loaded as tabs — ChatGPT, Claude and Gemini — each with starting scores.", ""),
            ("With the ChatGPT tab selected, drag the five sliders to your own assessment: '© IP Compliance', '🔐 Data Privacy', '🌿 Environmental Impact', '⚖️ Bias Mitigation' and '🔍 Transparency'. Use the anchor labels under each slider to calibrate.", ""),
            ("Click the Claude and Gemini tabs and score each system the same way, justifying every score you change from its default.", ""),
            ("Click '+ Add System', enter a fourth system your organisation is considering, and click 'Add' — it starts at 5 on every dimension.", ""),
            ("Score the new system, then click 'Update Comparison Chart'.", ""),
            ("Read the radar chart and the comparison table, noting the 'Overall Average' row — then identify which dimension separates the systems most sharply.", ""),
        ],
        test="Your radar chart shows four systems, and you can justify each score you assigned with a specific "
             "reason (such as training-data provenance or published energy figures) rather than brand reputation.",
    ),
    dict(
        num=11,
        phases=['Run at epsilon 1.0', 'Compare low vs high', 'Try randomised response', 'Spend the budget', 'Exhaust the budget'],
        topic=3,
        title="Differential Privacy Explorer",
        objective="Explain how differential privacy protects individuals and the privacy-utility trade-off it imposes (K1, K3)",
        slug="differential-privacy",
        path=f"{BASE}/differential-privacy/",
        apikey=None,
        desc="Turn the epsilon dial and watch the privacy-utility trade-off happen in front of you — strong "
             "privacy makes the answer noisy, weak privacy makes it accurate but leaks.",
        build="A set of query results at three different epsilon values plus a spent privacy budget showing "
              "how many queries a dataset can safely answer",
        duration="15 minutes",
        steps=[
            ("Open the activity and read the 'What is Differential Privacy?' card, including the formal guarantee.", ""),
            ("On the 'Laplace Mechanism' tab, leave Epsilon at 1.00, choose 'Average Salary' from the Query dropdown and click 'Run Query (10 trials)'. Note the True Answer against the Noisy Answer.", ""),
            ("Drag Epsilon down to about 0.1 and re-run — the noise scale grows and the answers scatter. Then push Epsilon up to 10 and re-run: the answers are accurate but the privacy guarantee is nearly worthless.", ""),
            ("Switch to the 'Randomised Response' tab. Read the sensitive survey question, set the 'True \"Yes\" Rate (%)' and click 'Run Simulation' to see how an individual keeps deniability while the aggregate stays estimable.", ""),
            ("Switch to the 'Privacy Budget' tab. Click '+ Add Query' several times and watch Spent rise and Remaining fall against the Total Budget.", ""),
            ("Keep adding queries until the Status shows the budget is exhausted, and note how few queries a strict budget actually permits.", ""),
        ],
        test="You can state what epsilon controls, explain why a smaller epsilon means stronger privacy but a "
             "less useful answer, and say what happens once a privacy budget is spent.",
    ),
    dict(
        num=12,
        phases=['Load a borderline case', 'Flip the decision', 'Run LIME', 'Run SHAP', 'Compare side by side'],
        topic=3,
        title="Explainable AI (XAI) Explorer",
        objective="Compare explainability techniques and the accuracy-interpretability trade-off (K3, A6)",
        slug="xai-explorer",
        path=f"{BASE}/xai-explorer/",
        apikey=None,
        desc="Open the black box on a loan-approval model: adjust an applicant's profile, watch the decision "
             "flip, and compare how LIME and SHAP each explain why.",
        build="LIME and SHAP explanations for the same borderline applicant, plus the side-by-side comparison "
              "of the two methods",
        duration="15 minutes",
        steps=[
            ("Open the activity and read the two concept cards explaining LIME and SHAP.", ""),
            ("In the 'Loan Approval Model Simulator', click the 'Borderline Case' scenario chip and note the Decision, Approval Score and Confidence against the 0.50 threshold.", ""),
            ("Drag the 'Credit Score' slider up and down and watch the decision flip — identify the score at which the applicant crosses the threshold.", ""),
            ("On the 'LIME Explanation' tab, click 'Run LIME Analysis' and read which features pushed the decision toward approval (green) and toward denial (red).", ""),
            ("Click 'Run LIME Analysis' a second time — the values shift slightly because LIME samples randomly. Then open the 'SHAP Explanation' tab and click 'Run SHAP Analysis', which gives the same answer every time.", ""),
            ("Scroll to 'LIME vs SHAP — Side by Side' and the comparison table, and decide which method you would present to a rejected applicant and why.", ""),
        ],
        test="You can name the feature that most influenced the decision, and explain why SHAP's consistency "
             "matters when an explanation may have to be defended to a regulator or a customer.",
    ),
    dict(
        num=13,
        phases=['Study the 3 paradigms', 'Load the scenario', 'Run all 3 allocations', 'Compare the outcomes', 'Justify your choice'],
        topic=3,
        title="The Ethical Paradigms of AI Resource Allocation",
        objective="Compare ethical issues in AI applications across competing ethical frameworks (A6)",
        slug="ai-resource-allocation",
        path=f"{BASE}/ai-resource-allocation/",
        apikey="Google Gemini (optional)",
        desc="Allocate a scarce resource — 50 treatments among 120 eligible patients — three times over, once "
             "under each ethical paradigm, and confront the fact that all three are defensible and they "
             "disagree about who lives.",
        build="Three allocation results for the same scenario under the Utilitarian, Egalitarian and "
              "Prioritarian paradigms, with your own written justification of which is most appropriate",
        duration="15 minutes",
        steps=[
            ("Open the activity and read the three paradigm cards — 'Utilitarian' (Cost-Effectiveness), 'Egalitarian' (Equal Access) and 'Prioritarian' (Needs-Based) — noting the ✓ pro and ✗ con of each.", ""),
            ("Under 'Select a Case Study Scenario', choose 'Healthcare: Precision Medicine' and read the constraints and the patient profile table.", ""),
            ("In the 'Allocation Simulator', click '⚖️ Utilitarian' and record the outcomes grid: Served, Avg Efficacy, Total Impact, Equity and Vulnerable Served.", ""),
            ("Click '🤝 Egalitarian' and then '🎯 Prioritarian', recording the same five outcome measures each time and noting which patients gained or lost their place.", ""),
            ("In 'Your Ethical Analysis', choose the paradigm you believe fits this scenario and write your reasoning, stating explicitly which trade-off you are willing to accept.", ""),
            ("Optionally enter a Gemini API key and click 'Analyse with AI' to have your reasoning critiqued, then repeat the comparison on the Education or Disaster scenario.", ""),
        ],
        test="You can show that the three paradigms served measurably different groups from identical inputs, "
             "and defend your chosen paradigm while naming the specific harm it accepts.",
    ),
    dict(
        num=14,
        phases=['Filter to your sector', 'Read the case', 'Identify the issues', 'Propose remediation', 'Find the pattern'],
        topic=3,
        title="AI Ethics Case Study Analyzer",
        objective="Identify ethical issues in real AI deployments and propose remediation (A6, A1)",
        slug="ethics-case-study",
        path=f"{BASE}/ethics-case-study/",
        apikey="Google Gemini (optional)",
        desc="Analyse documented AI ethics failures — IBM Watson for Oncology, the Apple Card credit "
             "investigation, Amazon's recruiting tool, Clearview AI — and propose the remediation that should "
             "have been in place.",
        build="A written analysis of at least one case identifying its ethical issues and your proposed "
              "remediation, compared against an AI critique",
        duration="15 minutes",
        steps=[
            ("Open the activity. Use the filter bar — 'All Cases', 'Healthcare', 'Finance', 'Creative', 'Education', 'Employment', 'Government' — to find a case in a sector close to your own work.", ""),
            ("Click a case card to expand it, and read the 'Background', 'Key Ethical Issues', 'Principles at Stake' and 'Affected Stakeholders' sections.", ""),
            ("In the 'Your Analysis' form, answer 'What ethical issues do you identify?' in your own words before reading any further — this is the same task as Question 4 of the Case Study assessment.", ""),
            ("Answer 'What remediation would you propose?', naming controls that are specific and enforceable rather than general statements of good intent.", ""),
            ("Optionally enter a Gemini API key and click 'Analyse with Gemini AI', then compare its analysis with yours and note anything you missed.", ""),
            ("Scroll to 'Cross-Cutting Patterns' and identify which of the six patterns — Power Asymmetry, Feedback Loops, Accountability Gaps, Consent Erosion, Digital Divide, Transparency Theatre — appears in your chosen case.", ""),
        ],
        test="Your analysis names at least three distinct ethical issues, proposes a specific remediation for "
             "each, and identifies which cross-cutting pattern the failure belongs to.",
    ),
]

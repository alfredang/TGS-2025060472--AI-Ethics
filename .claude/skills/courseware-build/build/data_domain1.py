"""LU1 — Ethical Principles of Generative AI: in-class activities 1-6.

Every step is written against the real UI of the lab web app in
labs/lu1-ethical-principles/<slug>/ so the Learner Guide can be followed verbatim.
"""

BASE = "labs/lu1-ethical-principles"

DOMAIN1 = [
    dict(
        num=1,
        phases=['Read the dilemma', 'Choose a response', 'Study the analysis', 'Repeat across 6 domains', 'Record your score'],
        topic=1,
        title="AI Ethical Dilemma Simulator",
        objective="Recognise the ethical considerations and potential risks that arise when interacting with generative AI (K2)",
        slug="ethical-dilemma",
        path=f"{BASE}/ethical-dilemma/",
        apikey=None,
        desc="Work through six real-world AI dilemmas — from AI-generated hospital discharge summaries to "
             "resume-screening bias — choosing the most defensible course of action in each and reading the "
             "consequences of the choice you made.",
        build="A completed 6-scenario run with your score out of 6 and notes on the stakeholders and ethical "
              "principles at stake in each dilemma",
        duration="10 minutes",
        steps=[
            ("Open the activity. It starts on Scenario 1 of 6 — 'AI-Generated Discharge Summaries' in the Healthcare domain.", ""),
            ("Read the scenario description, then click the choice you judge to be the most ethical response. The three options colour-code and each is labelled (for example 'Best approach', 'Partially addresses risk' or 'Dangerous approach').", ""),
            ("Read the Analysis card that appears — note the 'Affected Stakeholders:' and 'Ethical Principles at Stake:' lines, and write down which principle you had overlooked.", ""),
            ("Click 'Next Scenario →' and repeat for all six domains: Healthcare, Hiring & Recruitment, Journalism, Education, Surveillance & Privacy and Creative Industries.", ""),
            ("At the 'Assessment Complete' card, record your score out of 6 and the message you were given.", ""),
            ("Use 'Try Again' to re-run any dilemma where your first instinct was wrong, and articulate why the better option was better.", ""),
        ],
        test="You can state, for at least three of the six scenarios, who the affected stakeholders were and "
             "which ethical principle the 'dangerous' option violated.",
    ),
    dict(
        num=2,
        phases=['Answer 10 questions', 'Read each explanation', 'Track correct / incorrect', 'Review your score', 'Retake the weak areas'],
        topic=1,
        title="AI Ethical Principles Quiz",
        objective="Identify and apply the core ethical principles in AI (K4)",
        slug="principles-quiz",
        path=f"{BASE}/principles-quiz/",
        apikey=None,
        desc="Test your grasp of the principles that underpin trustworthy AI — fairness, transparency, "
             "accountability, privacy, beneficence and human agency — across ten applied questions.",
        build="A completed 10-question quiz with your score and the live Correct / Incorrect counters",
        duration="10 minutes",
        steps=[
            ("Open the activity. All ten questions are on one scrollable page, each headed 'Question N of 10'.", ""),
            ("Read the question and its italic hint line, then click the option you believe names the correct principle.", ""),
            ("The correct answer turns green (a wrong pick turns red) and an explanation block appears — read it before moving on.", ""),
            ("Watch the 'Correct:' and 'Incorrect:' counters in the nav bar as you work down the page.", ""),
            ("Answer all ten, then read the 'Quiz Complete!' panel and record your score out of 10.", ""),
            ("Click 'Retake Quiz' and re-attempt any principle you confused with another — fairness vs beneficence is the usual trap.", ""),
        ],
        test="You score at least 7/10 and can define each of the six principles in one sentence without "
             "looking at the slides.",
    ),
    dict(
        num=3,
        phases=['Learn the attack types', 'Attack Level 1', 'Escalate to Level 2 & 3', 'Read each verdict', 'Record the scoreboard'],
        topic=1,
        title="Prompt Injection Playground",
        objective="Explain how prompt injection threatens AI safety and how layered defences reduce the risk (K2)",
        slug="prompt-injection",
        path=f"{BASE}/prompt-injection/",
        apikey=None,
        desc="Attack three simulated AI assistants — an undefended customer-service bot, a banking assistant "
             "with basic defences and a medical triage AI with strong defences — and see which injections get "
             "through each layer of protection.",
        build="An Attack Scoreboard showing your total attempts, successful injections, success rate and which "
              "of the three scenarios you breached",
        duration="10 minutes",
        steps=[
            ("Open the activity and read the 'What is Prompt Injection?' tiles covering the six attack types (Role Override, Instruction Override, Information Extraction, Jailbreaking, Indirect Injection, Context Manipulation).", ""),
            ("Under 'Select a Challenge Scenario', stay on the 'Level 1: No Defenses' tab — the Customer Service Bot. Click 'Reveal System Prompt' to see the hidden instructions and the secrets it is protecting.", ""),
            ("Under 'Try a preset injection or write your own:', click a preset chip such as 'Ignore instructions' or 'Role override', then click 'Send Message'.", ""),
            ("Read the verdict card — '⚠ Injection Successful!' names the Attack Type and explains 'Why this worked:', while '✅ Defense Held' means the guardrail stopped you.", ""),
            ("Switch to 'Level 2: Basic Defenses' and then 'Level 3: Strong Defenses', trying the harder presets (for example 'Base64 encoding', 'Nested injection' or 'Emotional manipulation') to see which defences hold.", ""),
            ("Record the Attack Scoreboard — Total Attempts, Successful Injections, Success Rate and Scenarios Breached — then read the 'Defense Techniques Reference' to map each successful attack to the control that would have blocked it.", ""),
        ],
        test="Your scoreboard shows a markedly lower success rate at Level 3 than at Level 1, and you can name "
             "the specific defence (input sanitisation, system-prompt hardening or output filtering) that "
             "blocked each failed attack.",
    ),
    dict(
        num=4,
        phases=['Define the scenario', 'Map stakeholders', 'Weigh risks & benefits', 'Apply the principles', 'Decide & plan monitoring'],
        topic=1,
        title="Ethical Decision-Making Framework",
        objective="Apply ethical principles systematically in decision-making related to AI (A1)",
        slug="decision-framework",
        path=f"{BASE}/decision-framework/",
        apikey=None,
        desc="Take one contested AI deployment through a six-stage structured ethical analysis — scenario, "
             "stakeholders, risks, principles, alternatives, decision — and produce a defensible, documented "
             "recommendation rather than a gut reaction.",
        build="A printed 'Ethical Decision Analysis Summary' report with all eight sections completed",
        duration="15 minutes",
        steps=[
            ("Open the activity. In 'Step 1: Define the Scenario', click a sample chip such as 'AI in hiring decisions' or 'AI-generated medical reports' to load a scenario, then click 'Next: Stakeholders →'.", ""),
            ("In 'Step 2: Identify Stakeholders', list everyone affected — one per line — including the people who are acted upon, not just the users and the vendor. Click 'Next: Risks & Benefits →'.", ""),
            ("In 'Step 3: Assess Risks & Benefits', fill in both 'Potential Benefits' and 'Potential Risks'. Be specific about who bears each risk. Click 'Next: Principles →'.", ""),
            ("In 'Step 4: Apply Ethical Principles', tick the principles in tension (Fairness, Transparency, Accountability, Privacy, Beneficence, Human Agency) and explain the conflict in the notes field. Click 'Next: Alternatives →'.", ""),
            ("In 'Step 5: Consider Alternatives', record at least two genuine alternatives — including 'do not deploy' — then click 'Next: Decision →'.", ""),
            ("In 'Step 6: Make Your Decision', write your decision and a 'Monitoring & Review Plan', click 'Generate Summary', then use 'Print / Save as PDF' to keep your report.", ""),
        ],
        test="Your summary report has all eight sections filled, names at least one alternative you rejected "
             "and why, and states how the decision will be monitored after deployment.",
    ),
    dict(
        num=5,
        phases=['Load AI-generated text', 'Work the 16 checks', 'Set each severity', 'Calculate the score', 'Read the recommendations'],
        topic=1,
        title="AI Output Scepticism Checker",
        objective="Exercise professional scepticism to exercise sound judgement on generative AI output (A2)",
        slug="skepticism-checker",
        path=f"{BASE}/skepticism-checker/",
        apikey=None,
        desc="Evaluate confident, fluent, and quietly wrong AI-generated text against a 16-point scepticism "
             "checklist, and score how far it can actually be trusted.",
        build="A scepticism score out of 100 with a risk verdict and the recommendations list for the text you assessed",
        duration="10 minutes",
        steps=[
            ("Open the activity. Under 'Paste AI-Generated Text', click a sample chip — 'Medical summary', 'Historical essay', 'Legal advice' or 'Financial analysis' — or paste AI output of your own.", ""),
            ("Click 'Begin Evaluation' to reveal the 'Scepticism Evaluation Checklist'.", ""),
            ("Work through all 16 checks across the six categories: Source Verification, Logical Consistency, Bias Detection, Factual Accuracy, Completeness and Appropriateness.", ""),
            ("For each issue you find, tick the checkbox and set the severity dropdown to Low, Medium or High — judge the severity yourself rather than accepting the default.", ""),
            ("Click 'Calculate Scepticism Score' and read the score out of 100, the risk verdict and the 'Recommendations' list.", ""),
            ("Click 'Evaluate New Text' and repeat with a second sample, comparing which category of failure was most common.", ""),
        ],
        test="You can point to at least three specific unverifiable or fabricated claims in the sample text "
             "(such as an invented statistic or a non-existent citation) and justify the severity you assigned to each.",
    ),
    dict(
        num=6,
        phases=['Enter your API key', 'Pick a threat pairing', 'Load or write a scenario', 'Generate the analysis', 'Extract the mitigations'],
        topic=1,
        title="The Cognitive Threat Matrix",
        objective="Analyse how human cognitive bias combines with generative AI failure modes to escalate risk (K2, A2)",
        slug="cognitive-threat-matrix",
        path=f"{BASE}/cognitive-threat-matrix/",
        apikey="Google Gemini",
        desc="Pair a human cognitive bias with the AI failure mode it amplifies — automation bias with "
             "hallucination, confirmation bias with skewed data — and generate a structured risk analysis of a "
             "scenario from your own workplace.",
        build="A five-part AI risk analysis covering scenario overview, the bias at play, risk escalation, "
              "real-world impact and mitigation strategies",
        duration="15 minutes",
        steps=[
            ("Open the activity and enter your key in the 'Google Gemini API Key' field — a free key is available from aistudio.google.com/api-keys. The status line confirms 'Key format looks valid'.", ""),
            ("Click one of the four threat cards in the matrix: 'Automation Bias ➡ The Hallucination Threat', 'Confirmation Bias ➡ The Skewed Data Threat', 'Overconfidence ➡ The Verification Failure' or 'Groupthink ➡ The Ethical Blindspot'.", ""),
            ("Read the 'Bias:' and 'Risk:' lines on the card so you know which pairing you are analysing.", ""),
            ("In 'Sample Scenarios', click one of the five suggested questions to load it — or type your own scenario from your workplace into the textarea.", ""),
            ("Click 'Generate' and wait for the 'Risk Analysis' panel.", ""),
            ("Read the five sections — Scenario Overview, Cognitive Bias at Play, Risk Escalation, Real-World Impact and Mitigation Strategies — and mark which mitigations you could actually implement in your own organisation.", ""),
        ],
        test="You produce a risk analysis for a scenario from your own workplace and can name at least two "
             "mitigations from Section 5 that are realistic for your team to adopt.",
    ),
]

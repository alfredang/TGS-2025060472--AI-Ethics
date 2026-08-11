"""LU2 — Generative AI Privacy Techniques: in-class activities 7-9.

Every step is written against the real UI of the lab web app in
labs/lu2-privacy/<slug>/ so the Learner Guide can be followed verbatim.
"""

BASE = "labs/lu2-privacy"

DOMAIN2 = [
    dict(
        num=7,
        phases=['Enter your API key', 'Generate sample records', 'Apply all 4 techniques', 'Compare the techniques', 'Compare the reviewers'],
        topic=2,
        title="Data Anonymisation Techniques",
        objective="Distinguish the anonymisation spectrum — de-identification, pseudonymisation, objective and subjective anonymisation (K1)",
        slug="dataprivacy",
        path=f"{BASE}/dataprivacy/",
        apikey="Google Gemini",
        desc="Run one set of sensitive records through four different anonymisation techniques side by side, "
             "and see why only some of them actually remove the re-identification risk.",
        build="A side-by-side comparison table showing the same record under all four techniques, including "
              "three different reviewers' subjective judgements",
        duration="15 minutes",
        steps=[
            ("Open the activity and enter your key in the 'Google Gemini API Key' field (use the 👁 button to check what you typed).", ""),
            ("Click 'Generate Sample Data'. Five fictional records appear under 'Original Sample Data' with name, email, phone, date of birth, address, SSN, medical condition, salary and employer.", ""),
            ("Study the raw record and decide, before you continue, which fields you would remove to make it safe to share.", ""),
            ("Click 'Apply All Techniques' and wait while three reviewer personas are simulated.", ""),
            ("Compare the four technique cards — 'Deidentification' (High Re-ID Risk), 'Pseudonymization' (Moderate Risk), 'Objective Anonymization' (Zero Risk) and 'Subjective Anonymization' (Context-Dependent) — reading the Definition, Regulatory and AI Training notes on each.", ""),
            ("In the 'Side-by-Side Comparison' table, compare the Intern, Analyst and Privacy Officer columns for the same field and note where the three reviewers disagreed.", ""),
        ],
        test="You can explain why de-identification still carries a high re-identification risk, and why the "
             "three subjective reviewers produced different results from the same source record.",
    ),
    dict(
        num=8,
        phases=['Load a raw dataset', 'Select the techniques', 'Run the pipeline', 'Inspect the output', 'Export CSV + code'],
        topic=2,
        title="Python Data Anonymisation Pipeline",
        objective="Apply privacy measures when handling data for AI applications by building an anonymisation pipeline (A3)",
        slug="anonymizer-python",
        path=f"{BASE}/anonymizer-python/",
        apikey=None,
        desc="Build a seven-stage anonymisation pipeline over a raw dataset — pseudo-IDs, text shifting, "
             "masking, generalisation and column dropping — then export both the anonymised data and the "
             "Python code that produced it.",
        build="An exported anonymised CSV plus the generated Python script implementing your chosen techniques",
        duration="15 minutes",
        steps=[
            ("Open the activity and study the seven-node pipeline diagram: Raw Dataset → Pseudo-IDs → Text Shifting → Data Masking → Generalisation → Drop Columns → Export.", ""),
            ("In 'Step 1: Raw Dataset (CSV Input)', click a sample dataset — 'Patient Records', 'Employee Data' or 'Student Records'. The RAW table loads with directly identifying columns visible.", ""),
            ("In 'Step 2: Select Anonymisation Techniques', review the five techniques (Pseudo-Identifiers, ASCII Text Shifting, Data Masking, Generalisation, Drop Identity Columns) and the Python one-liner shown beneath each.", ""),
            ("Untick 'Drop Identity Columns', click 'Run Pipeline', and observe that names and emails survive in the output — then re-tick it and run again to see the difference.", ""),
            ("Read the per-step detail cards and the final ANONYMISED table, checking that no directly identifying field remains.", ""),
            ("In 'Export Anonymised Dataset', click 'Download as CSV' and 'Copy Python Code' to keep both deliverables.", ""),
        ],
        test="Your exported CSV contains no name, email or SSN values, ages appear as ranges rather than exact "
             "values, and you can explain what each line of the generated Python code does.",
    ),
    dict(
        num=9,
        phases=['Profile the organisation', 'Classify the data', 'Select the regulations', 'Choose the safeguards', 'Generate & print'],
        topic=2,
        title="Ethical AI Data Policy Generator",
        objective="Design guidelines or strategies for ethical AI use, including use of sensitive data in generative AI tools (A4)",
        slug="privacy-policy",
        path=f"{BASE}/privacy-policy/",
        apikey=None,
        desc="Produce a complete, organisation-specific AI data-handling policy through a guided five-step "
             "wizard — the document that tells your colleagues what they may and may not paste into an AI tool.",
        build="A printed seven-section 'AI Data Handling Policy' tailored to your organisation, sector and risk tolerance",
        duration="15 minutes",
        steps=[
            ("Open the activity. In 'Step 1: Organisation Profile', enter your organisation name, choose your Industry Sector and Organisation Size, and list the AI tools your organisation actually uses. Click 'Next →'.", ""),
            ("In 'Step 2: Data Classification', tick every category your organisation handles — PII, financial data, health records, employee records, intellectual property and the rest. Click 'Next →'.", ""),
            ("In 'Step 3: Regulatory Requirements', tick the regimes that bind you. For a Singapore organisation PDPA is the baseline; add GDPR, HIPAA or the EU AI Act if they apply. Click 'Next →'.", ""),
            ("In 'Step 4: Safeguards & Controls', select the controls you will genuinely enforce — anonymisation before AI input, encryption, role-based access, audit logging, mandatory human review, and so on. Click 'Next →'.", ""),
            ("In 'Step 5: Additional Considerations', set your Risk Tolerance Level (Conservative, Moderate or Progressive) and add any organisation-specific requirements, then click 'Generate Policy'.", ""),
            ("Review the generated seven-section policy and click 'Print / Save as PDF'. Check that its PROHIBITED list matches the data your staff are most likely to paste into a chatbot.", ""),
        ],
        test="Your policy names the specific AI tools in use, lists the data categories that must never be "
             "entered into them, and states an incident-response reporting deadline.",
    ),
]

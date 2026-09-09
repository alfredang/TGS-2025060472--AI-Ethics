<div align="center">

# Responsible Generative AI Basics

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Gemini API](https://img.shields.io/badge/Gemini_API-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-222222?style=for-the-badge&logo=githubpages&logoColor=white)](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/)

**A hands-on interactive course covering ethical principles, privacy techniques, and best practices for responsible generative AI.**

Courseware and activities for **Responsible Generative AI Basics (TGS-2025060472)**. [View the current course listing](https://www.tertiarycourses.com.sg/wsq-ai-security-awareness.html).

[Live Demo](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/) · [Report Bug](https://github.com/tertiarycourses/TGS-2025060472-Responsible-Generative-AI-Basics/issues) · [Request Feature](https://github.com/tertiarycourses/TGS-2025060472-Responsible-Generative-AI-Basics/issues)

</div>

## Screenshot

![Screenshot](screenshot.png)

## About

This repository contains the learner-facing courseware and activities for **Responsible Generative AI Basics (TGS-2025060472)**, aligned to **Responsible AI and Generative AI Practices (ICT-BAS-0055-1.1)**. The one-day course comprises **7 instructional hours and 1 assessment hour**, with **14 interactive browser activities** across three Learning Units.

The current Tertiary Infotech listing uses the marketing title **AI Security Awareness** for the same TGS reference. Funding validity shown on the listing is **17 November 2025 to 16 November 2027**.

### Key Features

- **14 interactive activities** — hands-on simulators, quizzes, explorers, and case study tools
- **Dark/Light theme** toggle across all activities
- **No installation required** — runs entirely in the browser
- **AI-powered demos** using Google Gemini API for data anonymisation simulations
- **Covers real-world topics** — prompt injection, differential privacy, XAI (LIME/SHAP), resource allocation ethics

## Course Activities

### LU1: Ethical Principles of Generative AI

| Activity | Description | Link |
|----------|-------------|------|
| Ethical Dilemma Simulator | Realistic AI ethical dilemma scenarios across healthcare, hiring, journalism, and education | [Launch](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu1-ethical-principles/ethical-dilemma/) |
| AI Principles Matching Quiz | Match ethical principles to definitions, examples, and violation scenarios | [Launch](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu1-ethical-principles/principles-quiz/) |
| Prompt Injection Playground | Attack simulated AI systems with 3 levels of increasing defences | [Launch](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu1-ethical-principles/prompt-injection/) |
| Decision Framework Tool | Step-by-step ethical decision-making framework for AI scenarios | [Launch](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu1-ethical-principles/decision-framework/) |
| Scepticism Checker | Evaluate AI-generated content with a structured checklist and scepticism score | [Launch](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu1-ethical-principles/skepticism-checker/) |
| Cognitive Threat Matrix | AI risk scenario generator exploring generative AI threats through cognitive biases (Gemini-powered) | [Launch](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu1-ethical-principles/cognitive-threat-matrix/) |

### LU2: Generative AI Privacy Techniques

| Activity | Description | Link |
|----------|-------------|------|
| Data Anonymisation Demo | Interactive demo of anonymisation techniques powered by Google Gemini API | [Launch](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu2-privacy/dataprivacy/) |
| Python Anonymisation Pipeline | Build a step-by-step anonymisation pipeline using Python techniques | [Launch](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu2-privacy/anonymizer-python/) |
| Privacy Policy Generator | Create a comprehensive AI data handling policy with an interactive wizard | [Launch](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu2-privacy/privacy-policy/) |

### LU3: Best Practices of Responsible Generative AI

| Activity | Description | Link |
|----------|-------------|------|
| AI Comparison Matrix | Compare AI systems across IP compliance, privacy, environmental impact with radar charts | [Launch](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu3-best-practices/ai-comparison/) |
| Differential Privacy Explorer | Experiment with Laplace mechanism, randomised response, and privacy budgets | [Launch](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu3-best-practices/differential-privacy/) |
| Explainable AI (XAI) Explorer | Understand LIME and SHAP through an interactive loan approval model | [Launch](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu3-best-practices/xai-explorer/) |
| AI Resource Allocation Simulator | Simulate Utilitarian, Egalitarian, and Prioritarian allocation paradigms | [Launch](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu3-best-practices/ai-resource-allocation/) |
| Ethics Case Study Analyzer | Analyse real-world AI ethics case studies across multiple domains | [Launch](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/labs/lu3-best-practices/ethics-case-study/) |

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| AI Integration | Google Gemini API (gemini-2.0-flash) |
| Theming | CSS Custom Properties (dark/light) |
| Deployment | GitHub Pages |
| Typography | Georgia / Times New Roman serif stack |

## Architecture

```
┌─────────────────────────────────────────────┐
│              GitHub Pages (CDN)              │
├─────────────────────────────────────────────┤
│             index.html (root)               │
│           (Course Hub - Main Page)          │
├──────────┬──────────┬───────────────────────┤
│   LU1    │   LU2    │         LU3           │
│ Ethical  │ Privacy  │    Best Practices     │
│Principles│Techniques│                       │
├──────────┼──────────┼───────────────────────┤
│ 6 apps   │ 3 apps   │       5 apps          │
└──────────┴────┬─────┴───────────────────────┘
                │
        ┌───────▼────────┐
        │  Gemini API    │
        │ (client-side)  │
        └────────────────┘
```

## Project Structure

```
TGS-2025060472-Responsible-Generative-AI-Basics/
├── labs/                         # The 14 in-class activities (GitHub Pages root)
│   ├── index.html                # Course Hub (activity landing page)
│   ├── lu1-ethical-principles/   # Learning Unit 1
│   │   ├── ethical-dilemma/
│   │   ├── principles-quiz/
│   │   ├── prompt-injection/
│   │   ├── decision-framework/
│   │   ├── skepticism-checker/
│   │   └── cognitive-threat-matrix/  # Uses Gemini API
│   ├── lu2-privacy/              # Learning Unit 2
│   │   ├── dataprivacy/          # Uses Gemini API
│   │   ├── anonymizer-python/
│   │   └── privacy-policy/
│   └── lu3-best-practices/       # Learning Unit 3
│       ├── ai-comparison/
│       ├── differential-privacy/
│       ├── xai-explorer/
│       ├── ai-resource-allocation/
│       └── ethics-case-study/
├── courseware/                   # WSQ courseware (see below)
│   └── archive/                  # Superseded versions
├── .claude/skills/courseware-build/build/   # Single-source generators
└── CLAUDE.md                     # AI assistant guidance

# Not in version control (confidential / large):
#   assessment/   WSQ assessment papers + answer keys — Google Drive only
#   reference/    Previous master deck and TMS pulls
```

## WSQ Courseware

The public learner package is aligned to the accredited Course Proposal, including all knowledge statements **K1–K4**, ability statements **A1–A6**, the 420-minute instructional programme, and the 60-minute assessment block.

| Artifact | File |
|---|---|
| Trainer slide deck | `courseware/Responsible Generative AI Basics-v13.pptx` (+ `.pdf`) — 82 slides |
| Lesson Plan | `courseware/LP-Responsible Generative AI Basics.docx` (+ `.pdf`) — v3.2 |
| Learner Guide | `courseware/LG-Responsible Generative AI Basics.docx` (+ `.pdf` and `.md`) — v3.2 |

The Facilitator Guide, Assessment Plan, assessment papers, marking guides and answer keys are controlled trainer/assessment records. They are distributed through restricted Google Drive and LMS-TMS locations and are intentionally excluded from this public repository.

Rebuild everything with:

```bash
bash .claude/skills/courseware-build/build/build_courseware.sh
```

## Getting Started

No build step or installation required. All activities run directly in the browser.

**Option 1: Live Demo**

Visit the [Course Hub](https://tertiarycourses.github.io/TGS-2025060472-Responsible-Generative-AI-Basics/)

**Option 2: Run Locally**

```bash
git clone https://github.com/tertiarycourses/TGS-2025060472-Responsible-Generative-AI-Basics.git
cd TGS-2025060472-Responsible-Generative-AI-Basics
python3 -m http.server 8000
```

Then open `http://localhost:8000` in your browser.

> **Note:** The Data Anonymisation Demo and Cognitive Threat Matrix require a [Google Gemini API key](https://aistudio.google.com/apikey) entered at runtime.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-activity`)
3. Commit your changes (`git commit -m 'Add new activity'`)
4. Push to the branch (`git push origin feature/new-activity`)
5. Open a Pull Request

## Developed By

**Tertiary Infotech Academy Pte. Ltd.**

## Acknowledgements

- [Google Gemini API](https://ai.google.dev/) for AI-powered data generation
- [GitHub Pages](https://pages.github.com/) for hosting
- Course framework aligned with Singapore's AI Governance Framework and EU AI Act

---

<div align="center">

If you find this course useful, please give it a star!

</div>

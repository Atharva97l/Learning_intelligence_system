# Personalized Learning Intelligence System

**An adaptive learning platform powered by Machine Learning, NLP, Recommendation Systems, and Generative AI.**

The Personalized Learning Intelligence System (PLIS) aims to make studying more focused, personalized, and effective by understanding what a student knows, identifying knowledge gaps, and recommending what they should learn next.

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/fd3f4eac-6191-4cce-b91c-4e25376c57a3" />

Unlike a standalone AI chatbot, the system combines learner modeling, personalized recommendations, course-grounded AI tutoring, assessments, and progress analytics into one continuous learning experience.

> **Our goal:** Build a system that doesn't just answer students' questions, but helps them understand what to learn next, why they need to learn it, and whether their understanding is improving.

---

## The Problem

Traditional learning platforms often treat every student similarly, regardless of their strengths, weaknesses, or learning history.

Students may struggle with:

- Identifying their actual weaknesses within a subject.
- Deciding what to study next.
- Understanding prerequisite concepts before moving to advanced topics.
- Practising effectively instead of repeatedly reviewing familiar material.
- Getting reliable explanations based on their actual course syllabus.
- Tracking their understanding beyond simple completion percentages or total quiz scores.

General-purpose AI tools can explain concepts and generate questions, but maintaining a structured, continuously updated picture of a learner's knowledge and using it to guide future study requires a dedicated system.

## Our Solution

PLIS connects assessment, learner modeling, recommendations, AI tutoring, and analytics into a single adaptive learning loop.

**Assess → Estimate Mastery → Identify Gaps → Recommend → Learn → Reassess**

Each interaction provides new evidence about the learner. The system uses that evidence to update topic-level mastery estimates and adjust future recommendations.

## Core Features

### 1. Topic-Level Mastery Estimation

Maintain an evolving estimate of a student's understanding of individual concepts rather than relying only on overall scores.

- Track quiz performance and learning history.
- Estimate mastery separately for each topic.
- Update estimates after assessment attempts.
- Identify concepts that need further practice.
- Represent uncertainty when evidence is limited.

**Planned approach:** Bayesian Knowledge Tracing (BKT), compared against simpler mastery baselines.

### 2. Weak-Topic Detection

Identify concepts where the student may need additional support.

- Detect consistently poor performance.
- Identify recurring errors.
- Consider prerequisite knowledge gaps.
- Prioritize topics requiring attention.

### 3. Personalized Learning Recommendations

Recommend the next most useful learning activity for each student.

Recommendations may consider:

- Estimated topic mastery.
- Topic importance.
- Prerequisite relationships.
- Recent mistakes.
- Time since the last review.
- Available course material and practice questions.

Each recommendation should explain why the activity was selected.

### 4. Course-Grounded AI Tutor

Provide an AI tutor that uses the student's uploaded course material as its primary source of evidence.

- Answer questions using relevant course passages.
- Explain difficult concepts in accessible language.
- Provide source references where available.
- Generate practice questions grounded in course content.
- Explain answers and mistakes.
- Handle questions that cannot be answered from the available material responsibly.

**Planned approach:** Retrieval-Augmented Generation (RAG), embeddings, semantic search, and an LLM API.

### 5. Adaptive Assessments and Feedback

Generate or select questions aligned with course topics and the learner's needs.

- Topic-specific quizzes.
- Explanations for correct and incorrect answers.
- Structured question metadata.
- Question difficulty labels.
- Assessment results fed back into the mastery model.

Generated questions will require validation and evaluation rather than being trusted automatically.

### 6. Learning Analytics Dashboard

Provide an understandable view of learning progress.

- Topic mastery heatmaps.
- Strong and weak areas.
- Performance trends.
- Assessment history.
- Recurring mistakes.
- Recommended next actions.
- Progress over time.

---

## How Is This Different from a General AI Chatbot?

The objective is not to claim that PLIS can outperform ChatGPT at every task. Its advantage is a specialized and measurable learning workflow.

| General-purpose AI chatbot | Personalized Learning Intelligence System |
|---|---|
| Primarily responds to user prompts | Continuously uses assessment history to guide learning |
| Explains concepts when asked | Identifies topics that may need attention |
| Can generate practice questions | Connects assessment results to an evolving learner model |
| May answer using broad general knowledge | Grounds tutoring in the supplied course material |
| Requires the user to manage much of their own study process | Recommends actionable next steps based on learner data |
| Can explain individual mistakes | Can use recurring mistakes to influence future practice |
| Does not inherently provide this complete integrated workflow | Connects tutoring, mastery estimation, recommendations, and progress tracking |

The central differentiator is the **closed learning loop**. Each assessment can change the learner model, which can change the next recommendation and the assistance provided by the tutor.

---

## Technology Stack

The following technologies are planned. The final stack may evolve during implementation.

| Component | Planned Technologies |
|---|---|
| Programming language | Python |
| Backend API | FastAPI, Pydantic |
| Frontend | React or Next.js |
| Database | PostgreSQL |
| Vector search | pgvector or an alternative vector database |
| Course document processing | PyMuPDF or pypdf |
| Semantic retrieval | Embedding models and vector search |
| AI tutoring | An API-accessible Large Language Model |
| Mastery modeling | Bayesian Knowledge Tracing |
| Recommendation engine | Python, prerequisite graphs, weighted ranking |
| Graph representation | NetworkX or relational data structures |
| ML utilities | scikit-learn where appropriate |
| Data visualization | Plotly or a React chart library |
| Testing | pytest |
| Version control | Git and GitHub |

The initial architecture will favor a modular backend over unnecessary microservices or multiple autonomous AI agents.

---

## System Architecture

The planned system consists of the following layers:

1. **Content Layer:** Ingests course documents, extracts text, and maintains source metadata.
2. **Assessment Layer:** Manages questions, quiz attempts, answers, and feedback.
3. **Learner Modeling Layer:** Updates topic-level mastery estimates from observed performance.
4. **Recommendation Layer:** Ranks learning activities while respecting prerequisite relationships.
5. **AI Tutor Layer:** Retrieves relevant course material and generates grounded explanations and practice questions.
6. **Analytics Layer:** Presents mastery estimates, learning history, and recommendations.
7. **Application Layer:** Connects these components through backend APIs and a student-facing web interface.

The architecture will be developed incrementally, with clearly defined interfaces between modules.

---

## Evaluation and Experiments

The project will evaluate its components against simple baselines wherever possible.

| Component | Evaluation |
|---|---|
| Mastery estimation | Predictive performance on future quiz responses |
| Recommendations | Relevance, prerequisite consistency, and simulated learning outcomes |
| Retrieval | Relevance of retrieved passages to test questions |
| AI tutor | Factual correctness, source support, and citation quality |
| Question generation | Answer correctness, topic alignment, and question validity |
| Complete workflow | Correct propagation of assessment results through mastery, recommendations, and analytics |

Simulated learner data may be used for initial development and testing. However, simulation alone cannot establish that the system improves real-world learning. Claims about effectiveness must be supported by appropriate evaluation.

---

## Development Roadmap

### Phase 1: Foundation
- Finalize the pilot subject and topic taxonomy.
- Define prerequisite relationships.
- Design the database schema and API contracts.
- Establish the repository and development workflow.

### Phase 2: Learning Intelligence
- Build the question bank and assessment workflow.
- Record learner interactions.
- Implement a baseline mastery estimator.
- Implement and evaluate BKT.
- Build the initial recommendation engine.

### Phase 3: AI Tutor
- Implement course document ingestion.
- Build source-aware retrieval.
- Integrate the LLM.
- Add grounded question generation and feedback.
- Connect assessments to the learner model.

### Phase 4: Dashboard and Integration
- Build the student interface.
- Visualize topic mastery and progress.
- Display recommendation explanations.
- Integrate and test all backend modules.

### Phase 5: Evaluation and Deployment
- Run experiments against baseline methods.
- Evaluate retrieval and tutor responses.
- Test edge cases and limited learner histories.
- Document findings and limitations.
- Deploy a working demonstration.

---

## Initial Scope

The first working version will focus on one subject and a complete end-to-end learning loop.

**Essential deliverables:**
- Topic-level learner modeling.
- Quiz assessment and feedback.
- Personalized recommendations.
- Course-grounded AI tutoring.
- Progress dashboard.
- Evaluation against basic baselines.

Advanced features such as IRT comparisons, sophisticated mistake classification, instructor analytics, and multi-subject support may be added after the core system is reliable.

---

## Team Collaboration

The project is being developed by a five-member team.

Proposed ownership areas:

- **Project leadership and intelligence:** Architecture, mastery modeling, recommendations, and integration.
- **Data and assessments:** Course ingestion, topic organization, and quiz pipeline.
- **RAG and AI tutoring:** Retrieval, source attribution, and LLM integration.
- **Backend and database:** APIs, persistence, and learner history.
- **Frontend and analytics:** Student interface, progress visualizations, and dashboard.

Responsibilities may evolve as the project develops. Shared API contracts, code reviews, and frequent integration will help keep the modules compatible.

---

## Repository Structure

```text
learning-intelligence-system/
├── README.md
├── plan.md
├── .gitignore
├── .env.example
├── docs/
│   ├── architecture.md
│   ├── data-model.md
│   └── experiments.md
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── mastery/
│   │   ├── recommendations/
│   │   ├── assessments/
│   │   └── tutor/
│   └── tests/
├── frontend/
├── data/
│   └── README.md
├── notebooks/
├── scripts/
└── requirements.txt
```

This is the proposed structure and will be adjusted as implementation decisions are finalized.

---

## Responsible Development

- Protect API keys and credentials using environment variables.
- Do not commit secrets or private learner data.
- Collect only the learner data required for the project.
- Treat mastery estimates as uncertain indicators, not definitive judgments.
- Validate generated questions and tutor outputs.
- Avoid unsupported claims about educational effectiveness.
- Document model limitations, evaluation results, and known failure cases.

## Project Plan

See [`plan.md`](plan.md) for the detailed project scope, architecture, implementation roadmap, technology choices, evaluation strategy, and risks.

---

## Project Status

**Status:** Planning and initial architecture.

The project is under active development. Features and technologies described above are planned capabilities and should not be considered implemented until they are completed and tested.

---

## Our Vision

Build a learning platform that does more than provide answers: one that uses evidence from a student's learning history to identify knowledge gaps, recommend meaningful practice, provide course-grounded assistance, and track how understanding develops over time.

**The LLM helps explain. The learner model and recommendation engine help decide what comes next.**

## Run the current local version on Windows

1. Make sure `uv` is installed and the project dependencies have been synced with `uv sync`.
2. Double-click [`run-local.cmd`](run-local.cmd) in this folder.
3. The launcher starts the API and the built website, then opens `http://127.0.0.1:5173/` in your browser. Keep the two terminal windows open while using the site; close them to stop it.

The frontend source files are not currently present in this folder, so the launcher serves the existing build in `frontend/dist`. AI features also need a `GROQ_API_KEY` in a root-level `.env` file. Without the key, the site can still open, but AI requests return an explanatory error.

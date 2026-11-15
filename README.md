# Data Visualization (CDB601220) – Interactive MCQ Bank

A modern, responsive, and interactive Data Visualization MCQ study and quiz application featuring 300 curated questions (40 Calculation + 260 Theory across 23 topics).

## 🚀 Live Demo
Ready to deploy on [Vercel](https://vercel.com) with zero configuration.

## ✨ Key Features
- **3 Dedicated Study Modes**:
  - **🧮 Mode 1: Calculation Only (40 MCQs)**: Interactive practice for all numerical and formula-based questions with 3-line step-by-step explanations (Topic, Formula, and Step-by-Step Calculation preserving math symbols $\div$, $\times$, $\sqrt{}$, $\approx$, $^2$).
  - **📚 Mode 2: Theory Topic-wise (260 MCQs)**: Conceptual questions organized across 23 syllabus topics with an interactive topic filter selector, live question counts, and Select All / Clear toggles.
  - **🔀 Mode 3: All MCQs Mixed (300 MCQs)**: Complete question bank in sequential (`Q1` $\to$ `Q300`) or randomized order with a Shuffle toggle.
- **Instant Feedback on Mistakes**:
  - Picking an incorrect option marks it red (`✗ Your Choice`) and instantly highlights the correct answer in vibrant green (`✓ Correct Answer`) alongside detailed explanations.
- **Flexible Practice Views**:
  - **List View**: Seamless scrolling and solving of all questions.
  - **Single Focus Mode**: Question-by-question view with Previous / Next navigation.
- **Navigator Grid Matrix (`Q1` to `Q300`)**:
  - Quick popup matrix indicating question status (Unsolved, Correct, Wrong, Calculation item) with 1-click jump.
- **Search & Filters**:
  - Real-time search across questions, formulas, topics, and option text.
  - Filter by Unsolved, Incorrect, Correct, and ⭐ Starred.
- **Theme & Offline Support**:
  - Full Dark and Light theme toggle.
  - Automatic `localStorage` persistence for answers, bookmarks, and progress.

## 📂 Repository Contents
- `index.html`: The main web application (fully self-contained, no external runtime dependencies).
- `mcqs.json`: Full structured JSON dataset containing topics, questions, options, answers, formulas, and calculations.
- `vercel.json`: Vercel static deployment configuration.

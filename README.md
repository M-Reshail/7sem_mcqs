# 7th Semester MCQ Bank

A clean, mobile-friendly MCQ practice app for 7th semester subjects. No frameworks — pure HTML/CSS/JS, deployed on Vercel via GitHub.

## Subjects

| Subject | Page | MCQs | Topics | Type Filter |
|---------|------|------|--------|-------------|
| 📊 Data Visualization | `index.html` | 300 | 23 topics (W1–W6) | Theory / Calculation |
| 🤖 Natural Language Processing | `nlp.html` | 200 | 8 lectures (L1–L8) | — |
| 🧠 Machine Learning | `ml.html` | 200 | 1 module | — |
| 🔬 Artificial Neural Networks | `ann.html` | 200 | 20 topics (T01–T20) | Conceptual / Numerical |

**Total: 900 MCQs**

## Features

- 📖 **Revision Mode** — pre-highlights all correct answers in green; works with all filters
- ⭐ **Star / Bookmark** — mark questions for later review
- 🔍 **Topic & Type Filters** — filter by topic and question type (theory/calculation)
- 🎯 **Focus Mode** — single-card view with Prev/Next navigation
- 🧭 **Question Navigator** — grid overview of all questions with color-coded status
- 🌙 **Dark Mode** — persistent across sessions
- 📊 **Score Stats** — live correct/wrong count in the header
- 📱 **Mobile Friendly** — responsive layout, sticky header, back-to-top button

## Stack

- Pure HTML + CSS + JavaScript (no build tools, no frameworks)
- MCQ data embedded inline as JSON `<script>` tags
- Deployed on **Vercel** (auto-deploys from GitHub `main` branch)
- Hosted at: `https://7sem-mcqs.vercel.app` *(or your Vercel URL)*

## Repo Structure

```
├── index.html          # DV MCQs (300)
├── nlp.html            # NLP MCQs (200)
├── ml.html             # ML MCQs (200)
├── ann.html            # ANN MCQs (200)
├── mcqs.json           # DV topic/MCQ data
├── ANN/
│   └── ann_mcqs.json   # ANN MCQ data (source)
├── ML/
│   └── ml_mcqs.json    # ML MCQ data (source)
├── NLP/
│   └── nlp_mcqs.json   # NLP MCQ data (source)
├── favicon.svg         # DV favicon
├── favicon-nlp.svg     # NLP favicon
├── favicon-ml.svg      # ML favicon
├── vercel.json         # Vercel config
└── README.md
```

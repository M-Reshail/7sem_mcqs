import json

# 1. Load Data
with open('mcqs.json', encoding='utf-8') as f:
    dv_raw = json.load(f)
dv_topics = dv_raw['topics']
dv_mcqs = dv_raw['mcqs']

with open('ANN/ann_mcqs.json', encoding='utf-8') as f:
    ann_mcqs = json.load(f)
ann_topics = {
    "T01": "T01 · AI vs. ML vs. DL",
    "T02": "T02 · Applications of Deep Learning",
    "T03": "T03 · Deep Learning Pipeline",
    "T04": "T04 · Biological Neuron",
    "T05": "T05 · Artificial Neuron",
    "T06": "T06 · Perceptron",
    "T07": "T07 · Activation Functions",
    "T08": "T08 · Multilayer Perceptron (MLP)",
    "T09": "T09 · Forward Propagation",
    "T10": "T10 · Loss Functions",
    "T11": "T11 · Gradient Descent",
    "T12": "T12 · Stochastic Gradient Descent (SGD)",
    "T13": "T13 · Vanishing and Exploding Gradients",
    "T14": "T14 · Overfitting",
    "T15": "T15 · Dropout",
    "T16": "T16 · Batch Normalization",
    "T17": "T17 · Early Stopping",
    "T18": "T18 · Weight Initialization",
    "T19": "T19 · Hyperparameter Tuning",
    "T20": "T20 · Evaluation Metrics"
}

with open('NLP/nlp_mcqs.json', encoding='utf-8') as f:
    nlp_mcqs = json.load(f)
nlp_topics = {
    "L1": "L1 · NLTK & NLP Overview",
    "L2": "L2 · Tokenization",
    "L3": "L3 · Stopwords Removal",
    "L4": "L4 · Lemmatization",
    "L5": "L5 · Stemming",
    "L6": "L6 · POS Tagging & Parsing",
    "L7": "L7 · Bag-of-Words & N-Grams",
    "L8": "L8 · TF-IDF Feature Extraction"
}

with open('ML/topicwise_mcqs.json', encoding='utf-8') as f:
    ml_tw_data = json.load(f)

with open('ML/ml_mcqs.json', encoding='utf-8') as f:
    ml_mcqs = json.load(f)

ml_topics = {}
ml_topic_info = {}
ml_qid_to_topic = {}

for t in ml_tw_data['topics']:
    num = t['topicNumber']
    code = f"T{num:02d}"
    title = t['title']
    ml_topics[code] = f"{code} · {title}"
    ml_topic_info[code] = {
        'num': num,
        'title': title,
        'info': t['info'],
        'count': t['questionCount']
    }
    for qid in t['questionIds']:
        ml_qid_to_topic[qid] = code

for q in ml_mcqs:
    code = ml_qid_to_topic.get(q['id'], 'T01')
    q['topicCode'] = code
    q['topic'] = ml_topics[code]

# Base CSS template
BASE_CSS = '''
    :root {
      --bg-primary: #f8fafc;
      --bg-surface: #ffffff;
      --bg-subtle: #f1f5f9;
      --border-color: #e2e8f0;
      --border-subtle: #cbd5e1;
      --text-primary: #0f172a;
      --text-secondary: #475569;
      --text-muted: #94a3b8;
      --primary: {PRIMARY};
      --primary-hover: {PRIMARY_HOVER};
      --primary-light: {PRIMARY_LIGHT};
      --primary-text: {PRIMARY_TEXT};
      --success: #10b981;
      --success-light: #ecfdf5;
      --success-border: #6ee7b7;
      --success-text: #065f46;
      --danger: #ef4444;
      --danger-light: #fef2f2;
      --danger-border: #fca5a5;
      --danger-text: #991b1b;
      --warning: #f59e0b;
      --warning-light: #fffbeb;
      --calc-badge-bg: #fef3c7;
      --calc-badge-text: #92400e;
      --theory-badge-bg: {THEORY_BG};
      --theory-badge-text: {THEORY_TEXT};
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
      --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
      --radius: 12px;
      --radius-sm: 8px;
    }

    [data-theme="dark"] {
      --bg-primary: #0b0f19;
      --bg-surface: #111827;
      --bg-subtle: #1f2937;
      --border-color: #374151;
      --border-subtle: #4b5563;
      --text-primary: #f9fafb;
      --text-secondary: #cbd5e1;
      --text-muted: #64748b;
      --primary: {DARK_PRIMARY};
      --primary-hover: {DARK_PRIMARY_HOVER};
      --primary-light: {DARK_PRIMARY_LIGHT};
      --primary-text: {DARK_PRIMARY_TEXT};
      --success: #34d399;
      --success-light: #064e3b;
      --success-border: #065f46;
      --success-text: #6ee7b7;
      --danger: #f87171;
      --danger-light: #450a0a;
      --danger-border: #991b1b;
      --danger-text: #fca5a5;
      --warning: #fbbf24;
      --warning-light: #451a03;
      --calc-badge-bg: #451a03;
      --calc-badge-text: #fcd34d;
      --theory-badge-bg: {DARK_THEORY_BG};
      --theory-badge-text: {DARK_THEORY_TEXT};
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      -webkit-text-size-adjust: 100%;
      scroll-behavior: smooth;
    }

    body {
      background-color: var(--bg-primary);
      color: var(--text-primary);
      line-height: 1.5;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      -webkit-font-smoothing: antialiased;
      -webkit-tap-highlight-color: transparent;
      padding-bottom: env(safe-area-inset-bottom);
      overflow-x: clip;
    }

    /* Sticky App Header */
    .app-header {
      position: -webkit-sticky;
      position: sticky;
      top: 0;
      z-index: 200;
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-color);
      box-shadow: var(--shadow-sm);
      backdrop-filter: blur(12px);
      width: 100%;
    }

    .header-bar {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0.6rem 1rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
      height: 58px;
    }

    .header-left {
      display: flex;
      align-items: center;
      gap: 0.65rem;
    }

    .hamburger-btn {
      width: 38px;
      height: 38px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-color);
      background: var(--bg-surface);
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      gap: 4px;
      cursor: pointer;
      flex-shrink: 0;
      transition: background 0.15s, border-color 0.15s;
    }
    .hamburger-btn:hover {
      background: var(--bg-subtle);
      border-color: var(--border-subtle);
    }
    .hamburger-btn span {
      display: block;
      width: 18px;
      height: 2px;
      background-color: var(--text-primary);
      border-radius: 2px;
      transition: transform 0.2s, opacity 0.2s;
    }

    .header-brand-dropdown-wrapper {
      position: relative;
    }

    .header-brand-btn {
      display: flex;
      align-items: center;
      gap: 0.35rem;
      background: transparent;
      border: 1px solid transparent;
      border-radius: var(--radius-sm);
      padding: 0.2rem 0.4rem;
      cursor: pointer;
      transition: background 0.15s;
      user-select: none;
    }
    .header-brand-btn:hover {
      background: var(--bg-subtle);
    }

    .brand-logo {
      width: 34px;
      height: 34px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      font-weight: 800;
      font-size: 0.88rem;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
      flex-shrink: 0;
    }

    .dropdown-chevron {
      font-size: 0.85rem;
      color: var(--text-secondary);
      transition: transform 0.2s ease;
    }
    .header-brand-dropdown-wrapper.open .dropdown-chevron {
      transform: rotate(180deg);
    }

    .subject-dropdown-menu {
      position: absolute;
      top: calc(100% + 8px);
      left: 0;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      box-shadow: var(--shadow-lg);
      width: 280px;
      z-index: 500;
      display: none;
      flex-direction: column;
      overflow: hidden;
      animation: menuFadeIn 0.18s cubic-bezier(0.16, 1, 0.3, 1);
    }
    @keyframes menuFadeIn {
      from { opacity: 0; transform: translateY(-6px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .header-brand-dropdown-wrapper.open .subject-dropdown-menu {
      display: flex;
    }

    .dropdown-header-label {
      padding: 0.65rem 1rem 0.45rem;
      font-size: 0.7rem;
      font-weight: 800;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      border-bottom: 1px solid var(--border-color);
      background: var(--bg-subtle);
    }

    .subject-dropdown-item {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      padding: 0.65rem 1rem;
      text-decoration: none;
      color: var(--text-primary);
      transition: background 0.12s;
      border-bottom: 1px solid var(--border-color);
    }
    .subject-dropdown-item:last-child {
      border-bottom: none;
    }
    .subject-dropdown-item:hover {
      background: var(--bg-subtle);
    }
    .subject-dropdown-item.active {
      background: var(--primary-light);
    }
    .subject-dropdown-item .subj-icon {
      font-size: 1.25rem;
      flex-shrink: 0;
    }
    .subject-dropdown-item .subj-info {
      display: flex;
      flex-direction: column;
      flex: 1;
      min-width: 0;
    }
    .subject-dropdown-item .subj-name {
      font-weight: 700;
      font-size: 0.88rem;
    }
    .subject-dropdown-item .subj-meta {
      font-size: 0.72rem;
      color: var(--text-secondary);
    }
    .subject-dropdown-item .subj-check {
      color: var(--primary);
      font-weight: 800;
      font-size: 1rem;
    }

    .header-right {
      display: flex;
      align-items: center;
      gap: 0.45rem;
      flex-shrink: 0;
    }

    .header-score-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      background: var(--bg-subtle);
      border: 1px solid var(--border-color);
      padding: 0.3rem 0.65rem;
      border-radius: 9999px;
      font-size: 0.78rem;
      font-weight: 700;
      cursor: pointer;
      user-select: none;
    }
    .score-item {
      display: inline-flex;
      align-items: center;
      gap: 0.2rem;
    }
    .score-item.c-ok { color: var(--success); }
    .score-item.c-no { color: var(--danger); }
    .score-item.c-pct { color: var(--primary); }

    .btn-header-icon {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      border: 1px solid var(--border-color);
      color: var(--text-secondary);
      background: var(--bg-surface);
      font-size: 1.1rem;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      flex-shrink: 0;
      transition: background 0.15s;
    }
    .btn-header-icon:hover {
      background: var(--bg-subtle);
      color: var(--text-primary);
    }

    /* Reveal Pill Button in Header */
    .btn-revision-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.36rem 0.75rem;
      border-radius: 9999px;
      border: 1.5px solid var(--border-color);
      background: var(--bg-surface);
      color: var(--text-primary);
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.18s;
      user-select: none;
      flex-shrink: 0;
    }
    .btn-revision-pill:hover {
      border-color: var(--primary);
      background: var(--primary-light);
    }
    .btn-revision-pill.active {
      background: var(--primary) !important;
      border-color: var(--primary) !important;
      color: #fff !important;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }

    .filter-summary-strip {
      background: var(--bg-subtle);
      border-bottom: 1px solid var(--border-color);
      padding: 0.4rem 1rem;
    }
    .filter-summary-inner {
      max-width: 1200px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      flex-wrap: wrap;
      font-size: 0.78rem;
      font-weight: 600;
    }
    .active-mode-tag {
      color: var(--primary);
      cursor: pointer;
    }
    .active-mode-tag:hover {
      text-decoration: underline;
    }
    .active-filter-tag {
      color: var(--text-secondary);
    }
    .active-revision-tag {
      font-size: 0.72rem;
      background: var(--success-light);
      color: var(--success-text);
      border: 1px solid var(--success-border);
      padding: 0.15rem 0.55rem;
      border-radius: 9999px;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      gap: 0.25rem;
    }
    .btn-open-menu-link {
      margin-left: auto;
      color: var(--text-secondary);
      cursor: pointer;
      padding: 0.15rem 0.45rem;
      border-radius: 4px;
    }
    .btn-open-menu-link:hover {
      color: var(--text-primary);
      background: var(--bg-surface);
    }

    /* Drawer Backdrop & Side Drawer */
    .drawer-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.5);
      backdrop-filter: blur(4px);
      z-index: 250;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.25s ease;
      touch-action: none;
    }
    .drawer-backdrop.open {
      opacity: 1;
      pointer-events: auto;
    }

    .side-drawer {
      position: fixed;
      top: 0;
      left: 0;
      bottom: 0;
      width: 360px;
      max-width: 88vw;
      background: var(--bg-surface);
      z-index: 300;
      box-shadow: var(--shadow-lg);
      transform: translateX(-100%);
      transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      overscroll-behavior: contain;
    }
    .side-drawer.open {
      transform: translateX(0);
    }

    .drawer-header {
      padding: 0.85rem 1.25rem;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--bg-surface);
      flex-shrink: 0;
    }
    .drawer-theme-top-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.42rem 0.85rem;
      border-radius: 9999px;
      border: 1px solid var(--border-color);
      background: var(--bg-subtle);
      color: var(--text-primary);
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      transition: all var(--transition-fast);
      user-select: none;
    }
    .drawer-theme-top-btn:hover {
      background: var(--bg-surface);
      border-color: var(--primary);
      color: var(--primary);
    }
    .drawer-close-btn {
      width: 34px;
      height: 34px;
      border-radius: 50%;
      border: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: center;
      background: var(--bg-subtle);
      color: var(--text-secondary);
      font-size: 1.2rem;
      cursor: pointer;
    }
    .drawer-close-btn:hover {
      color: var(--text-primary);
      background: var(--border-color);
    }

    .drawer-body {
      padding: 1rem 1.25rem 4.5rem !important;
      overflow-y: auto !important;
      -webkit-overflow-scrolling: touch !important;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      flex: 1;
      overscroll-behavior: contain;
    }

    .drawer-section-title {
      font-size: 0.74rem;
      text-transform: uppercase;
      font-weight: 800;
      letter-spacing: 0.06em;
      color: var(--primary);
      margin-bottom: 0.55rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .drawer-segmented {
      display: flex;
      background: var(--bg-subtle);
      padding: 0.25rem;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-color);
    }
    .drawer-segmented-btn {
      flex: 1;
      border: none;
      background: transparent;
      padding: 0.45rem 0.5rem;
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--text-secondary);
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.15s;
    }
    .drawer-segmented-btn.active {
      background: var(--bg-surface);
      color: var(--text-primary);
      box-shadow: var(--shadow-sm);
    }

    .drawer-topic-box {
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      padding: 0.75rem;
      background: var(--bg-subtle);
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
    }
    .drawer-topic-chips-grid {
      max-height: 220px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
      padding-right: 0.25rem;
    }
    .drawer-topic-item {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--text-primary);
      cursor: pointer;
      user-select: none;
      padding: 0.25rem 0.35rem;
      border-radius: 4px;
    }
    .drawer-topic-item:hover {
      background: rgba(0, 0, 0, 0.03);
    }
    [data-theme="dark"] .drawer-topic-item:hover {
      background: rgba(255, 255, 255, 0.05);
    }
    .drawer-topic-item input {
      accent-color: var(--primary);
      cursor: pointer;
    }
    .topic-count-badge {
      margin-left: auto;
      font-size: 0.7rem;
      color: var(--text-muted);
    }

    .btn-filter-pill {
      border: 1px solid var(--border-color);
      background: var(--bg-surface);
      color: var(--text-secondary);
      padding: 0.35rem 0.7rem;
      border-radius: 9999px;
      font-size: 0.78rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.15s;
      user-select: none;
    }
    .btn-filter-pill:hover {
      border-color: var(--primary);
      color: var(--primary);
      background: var(--primary-light);
    }
    .btn-filter-pill.active {
      background: var(--primary);
      border-color: var(--primary);
      color: #fff;
    }

    .drawer-btn-row {
      display: flex;
      flex-wrap: wrap;
      gap: 0.45rem;
      margin-top: 0.55rem;
    }
    .drawer-action-btn {
      flex: 1 1 calc(50% - 0.25rem);
      min-width: 110px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.4rem;
      padding: 0.48rem 0.65rem;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-color);
      background: var(--bg-surface);
      color: var(--text-primary);
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s;
      text-align: center;
      line-height: 1.25;
      box-sizing: border-box;
    }
    .drawer-action-btn:hover {
      border-color: var(--primary);
      background: var(--primary-light);
      color: var(--primary-text);
    }
    .drawer-action-btn.active {
      border-color: var(--success) !important;
      background: var(--success-light) !important;
      color: var(--success-text) !important;
    }
    .drawer-action-btn.full-width {
      flex: 1 1 100%;
    }
    .drawer-action-btn.danger {
      color: var(--danger);
      border-color: rgba(239, 68, 68, 0.3);
    }
    .drawer-action-btn.danger:hover {
      background: var(--danger-light);
      border-color: var(--danger);
      color: var(--danger-text);
    }

    /* Main Container & MCQ Cards */
    main {
      flex: 1;
      max-width: 820px;
      width: 100%;
      margin: 0 auto;
      padding: 1.25rem 1rem 4rem;
    }

    .mcq-list {
      display: flex;
      flex-direction: column;
      gap: 1.15rem;
    }

    .mcq-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 1.35rem 1.5rem;
      box-shadow: var(--shadow-sm);
      transition: border-color 0.2s, box-shadow 0.2s;
      position: relative;
    }
    .mcq-card:hover {
      box-shadow: var(--shadow-md);
      border-color: var(--border-subtle);
    }

    /* Topic-wise Group Header */
    .topic-group-header {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-left: 5px solid var(--primary);
      border-radius: var(--radius-md);
      padding: 1.1rem 1.25rem;
      margin-top: 1.4rem;
      margin-bottom: 0.85rem;
      box-shadow: var(--shadow-sm);
      animation: fadeIn 0.25s ease;
    }
    .topic-group-badge {
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 0.2rem 0.6rem;
      border-radius: 9999px;
      background: var(--primary-light);
      color: var(--primary-text);
      margin-bottom: 0.4rem;
    }
    .topic-group-title {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-primary);
      margin: 0 0 0.4rem 0;
    }
    .topic-group-info {
      font-size: 0.88rem;
      line-height: 1.5;
      color: var(--text-secondary);
      margin: 0;
    }
    [data-theme="dark"] .topic-group-header {
      background: var(--bg-surface);
      border-color: var(--border-color);
      border-left-color: var(--primary);
    }
    [data-theme="dark"] .topic-group-badge {
      background: var(--dark-primary-light);
      color: var(--dark-primary-text);
    }
    .mcq-card.status-correct {
      border-left: 5px solid var(--success);
    }
    .mcq-card.status-wrong {
      border-left: 5px solid var(--danger);
    }

    .card-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.5rem;
      margin-bottom: 0.6rem;
    }
    .card-meta-left {
      display: flex;
      align-items: center;
      gap: 0.45rem;
      flex-wrap: wrap;
    }
    .q-id-pill {
      font-weight: 800;
      font-size: 0.85rem;
      color: var(--primary);
      background: var(--primary-light);
      padding: 0.18rem 0.55rem;
      border-radius: 6px;
    }
    .type-pill {
      font-size: 0.72rem;
      font-weight: 700;
      padding: 0.15rem 0.55rem;
      border-radius: 9999px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .type-pill.calculation {
      background: var(--calc-badge-bg);
      color: var(--calc-badge-text);
    }
    .type-pill.theory, .type-pill.nlp, .type-pill.ml {
      background: var(--theory-badge-bg);
      color: var(--theory-badge-text);
    }

    .card-badges {
      display: flex;
      align-items: center;
      gap: 0.45rem;
    }
    .revision-key-pill {
      font-size: 0.74rem;
      font-weight: 800;
      padding: 0.15rem 0.55rem;
      border-radius: 9999px;
      background: var(--primary-light);
      color: var(--primary);
      border: 1px solid var(--primary);
    }

    .bookmark-btn {
      cursor: pointer;
      font-size: 1.15rem;
      color: var(--text-muted);
      transition: color 0.15s, transform 0.15s;
      padding: 0.1rem;
      line-height: 1;
      user-select: none;
    }
    .bookmark-btn:hover {
      transform: scale(1.15);
      color: var(--warning);
    }
    .bookmark-btn.active {
      color: var(--warning);
    }

    .card-topic-row {
      margin-bottom: 0.85rem;
    }
    .topic-pill {
      font-size: 0.76rem;
      color: var(--text-secondary);
      background: var(--bg-subtle);
      border: 1px solid var(--border-color);
      padding: 0.2rem 0.55rem;
      border-radius: 6px;
      font-weight: 600;
      display: inline-block;
      max-width: 100%;
      word-break: break-word;
    }

    .question-title {
      font-size: 1.05rem;
      font-weight: 600;
      color: var(--text-primary);
      line-height: 1.55;
      margin-bottom: 1rem;
      word-break: break-word;
    }

    .options-grid {
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
    }

    .option-btn {
      width: 100%;
      text-align: left;
      padding: 0.75rem 1rem;
      border-radius: var(--radius-sm);
      border: 1.5px solid var(--border-color);
      background: var(--bg-surface);
      color: var(--text-primary);
      font-size: 0.94rem;
      line-height: 1.45;
      cursor: pointer;
      transition: all 0.15s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      align-items: flex-start;
      gap: 0.75rem;
      word-break: break-word;
    }
    .option-btn:hover:not(:disabled) {
      border-color: var(--primary);
      background: var(--primary-light);
    }
    .option-letter {
      width: 26px;
      height: 26px;
      border-radius: 50%;
      background: var(--bg-subtle);
      border: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 0.8rem;
      flex-shrink: 0;
      margin-top: 1px;
    }
    .option-text {
      flex: 1;
    }

    .option-btn.selected-correct, .option-btn.revealed-correct {
      border-color: var(--success);
      background: var(--success-light);
      color: var(--success-text);
    }
    .option-btn.selected-correct .option-letter, .option-btn.revealed-correct .option-letter {
      background: var(--success);
      color: #fff;
      border-color: var(--success);
    }

    .option-btn.selected-wrong {
      border-color: var(--danger);
      background: var(--danger-light);
      color: var(--danger-text);
    }
    .option-btn.selected-wrong .option-letter {
      background: var(--danger);
      color: #fff;
      border-color: var(--danger);
    }

    .option-btn.dimmed {
      opacity: 0.55;
    }

    .card-footer {
      margin-top: 0.85rem;
      padding-top: 0.85rem;
      border-top: 1px dashed var(--border-color);
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }
    .feedback-message {
      font-size: 0.92rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      word-break: break-word;
    }
    .feedback-message.correct { color: var(--success); }
    .feedback-message.wrong { color: var(--danger); }

    /* Direct Solution Text (No separate box, clean flow) */
    .direct-solution-text {
      font-size: 0.88rem;
      line-height: 1.55;
      color: var(--text-secondary);
      word-break: break-word;
      padding-left: 0.1rem;
    }

    /* Focus Mode Container */
    .focus-mode-container {
      display: none;
      max-width: 820px;
      margin: 0 auto;
    }
    .focus-card {
      background: var(--bg-surface);
    }
    .focus-nav {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
      margin-top: 1.25rem;
    }
    .btn-nav {
      padding: 0.65rem 1.2rem;
      border-radius: var(--radius-sm);
      border: 1.5px solid var(--border-color);
      background: var(--bg-surface);
      color: var(--text-primary);
      font-weight: 700;
      cursor: pointer;
      transition: all 0.15s;
    }
    .btn-nav:hover:not(:disabled) {
      border-color: var(--primary);
      background: var(--primary-light);
    }
    .btn-nav:disabled {
      opacity: 0.4;
      cursor: not-allowed;
    }

    /* Navigator Matrix Modal */
    .matrix-modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.6);
      backdrop-filter: blur(4px);
      z-index: 600;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1rem;
      touch-action: none;
    }
    .matrix-modal-backdrop.open {
      display: flex;
    }
    .matrix-modal {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      box-shadow: var(--shadow-lg);
      max-width: 580px;
      width: 100%;
      max-height: 82vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      animation: modalScale 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    @keyframes modalScale {
      from { opacity: 0; transform: scale(0.95); }
      to { opacity: 1; transform: scale(1); }
    }
    .matrix-modal-header {
      padding: 1rem 1.25rem;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .matrix-modal-body {
      padding: 1.25rem;
      overflow-y: auto;
      -webkit-overflow-scrolling: touch;
      overscroll-behavior: contain;
    }
    .matrix-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(42px, 1fr));
      gap: 0.45rem;
    }
    .matrix-btn {
      aspect-ratio: 1;
      border: 1px solid var(--border-color);
      border-radius: 6px;
      background: var(--bg-subtle);
      color: var(--text-primary);
      font-size: 0.78rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      position: relative;
      transition: all 0.12s;
    }
    .matrix-btn:hover {
      border-color: var(--primary);
      transform: translateY(-2px);
    }
    .matrix-btn.correct {
      background: var(--success);
      color: #fff;
      border-color: var(--success);
    }
    .matrix-btn.wrong {
      background: var(--danger);
      color: #fff;
      border-color: var(--danger);
    }
    .matrix-btn.bookmarked::after {
      content: '★';
      position: absolute;
      top: 1px;
      right: 2px;
      font-size: 0.6rem;
      color: var(--warning);
    }

    /* Back to top button */
    .back-to-top {
      position: fixed;
      bottom: 1.5rem;
      right: 1.5rem;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: var(--primary);
      color: #fff;
      border: none;
      box-shadow: var(--shadow-md);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.2rem;
      cursor: pointer;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.2s, transform 0.2s;
      z-index: 100;
    }
    .back-to-top.visible {
      opacity: 1;
      pointer-events: auto;
    }
    .back-to-top:hover {
      transform: translateY(-3px);
    }

    /* Toast */
    #toast {
      position: fixed;
      bottom: 2rem;
      left: 50%;
      transform: translateX(-50%) translateY(100px);
      background: #0f172a;
      color: #fff;
      padding: 0.65rem 1.25rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 700;
      box-shadow: var(--shadow-lg);
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 999;
      pointer-events: none;
      white-space: nowrap;
    }
    #toast.show {
      transform: translateX(-50%) translateY(0);
    }

    @media (max-width: 600px) {
      .header-bar {
        padding: 0.5rem 0.85rem;
      }
      .mcq-card {
        padding: 1.05rem 0.95rem;
        border-radius: 10px;
      }
      .question-title {
        font-size: 0.98rem;
      }
      .option-btn {
        padding: 0.7rem 0.85rem;
      }
    }
'''

def generate_page(config):
    fname = config['filename']
    code = config['code']
    title = config['title']
    color = config['color']
    icon_html = config['icon_html']
    topics_json_str = json.dumps(config['topics'], ensure_ascii=False)
    topic_info_json_str = json.dumps(config.get('topic_info', {}), ensure_ascii=False)
    has_topic_wise_toggle_str = "true" if config.get('has_topic_wise_toggle', False) else "false"
    mcqs_json_str = json.dumps(config['mcqs'], ensure_ascii=False)
    total_q = len(config['mcqs'])
    storage_prefix = config['prefix']
    has_calc = config.get('has_calc', False)
    has_topics = len(config['topics']) > 1
    topic_count = len(config['topics'])

    css = BASE_CSS.replace('{PRIMARY}', config['primary'])
    css = css.replace('{PRIMARY_HOVER}', config['primary_hover'])
    css = css.replace('{PRIMARY_LIGHT}', config['primary_light'])
    css = css.replace('{PRIMARY_TEXT}', config['primary_text'])
    css = css.replace('{THEORY_BG}', config['theory_bg'])
    css = css.replace('{THEORY_TEXT}', config['theory_text'])
    css = css.replace('{DARK_PRIMARY}', config['dark_primary'])
    css = css.replace('{DARK_PRIMARY_HOVER}', config['dark_primary_hover'])
    css = css.replace('{DARK_PRIMARY_LIGHT}', config['dark_primary_light'])
    css = css.replace('{DARK_PRIMARY_TEXT}', config['dark_primary_text'])
    css = css.replace('{DARK_THEORY_BG}', config['dark_theory_bg'])
    css = css.replace('{DARK_THEORY_TEXT}', config['dark_theory_text'])

    # Build dropdown menu items
    subjects = [
        {"file": "./index.html", "code": "DV", "name": "Data Visualization", "icon": "📊", "meta": "300 Questions • 23 Topics"},
        {"file": "./nlp.html", "code": "NLP", "name": "Natural Language Processing", "icon": "🤖", "meta": "200 Questions • 8 Lectures"},
        {"file": "./ml.html", "code": "ML", "name": "Machine Learning", "icon": "🧠", "meta": "200 Questions • 23 Topics"},
        {"file": "./ann.html", "code": "ANN", "name": "Artificial Neural Networks", "icon": "🔬", "meta": "200 Questions • 20 Topics"},
    ]

    dropdown_items_html = ""
    for s in subjects:
        is_active = (s['code'] == code)
        active_cls = " active" if is_active else ""
        check_html = '<span class="subj-check">✓</span>' if is_active else ""
        dropdown_items_html += f'''            <a href="{s['file']}" class="subject-dropdown-item{active_cls}">
              <span class="subj-icon">{s['icon']}</span>
              <div class="subj-info">
                <span class="subj-name">{s['name']}</span>
                <span class="subj-meta">{s['meta']}</span>
              </div>
              {check_html}
            </a>\n'''

    # Build drawer segmented buttons for subject
    drawer_subjects_html = ""
    for s in subjects:
        is_active = (s['code'] == code)
        active_cls = " active" if is_active else ""
        drawer_subjects_html += f'''          <a href="{s['file']}" class="drawer-segmented-btn{active_cls}" style="text-decoration:none; display:flex; align-items:center; justify-content:center; gap:0.4rem; padding:0.5rem 0.4rem;">
            <span>{s['icon']} {s['code']} ({s['meta'].split()[0]})</span>
          </a>\n'''

    # Topic Section in Drawer
    has_topic_wise_toggle = config.get('has_topic_wise_toggle', False)
    topic_section_style = ' style="display: none;"' if has_topic_wise_toggle else ''
    if has_topics:
        topic_section_html = f'''      <!-- Section: Topic Filter -->
      <div id="drawerTopicSection"{topic_section_style}>
        <div class="drawer-section-title">
          <span>🏷️ Filter by Topic ({topic_count} Topics)</span>
          <span id="topicSelectedCountBadge" style="font-size:0.72rem; color:var(--text-secondary);">({topic_count}/{topic_count})</span>
        </div>
        <div class="drawer-topic-box">
          <div style="display: flex; gap: 0.4rem; justify-content: flex-end;">
            <button class="btn-filter-pill" id="selectAllTopicsBtn" style="padding: 0.2rem 0.55rem; font-size: 0.72rem;">Select All</button>
            <button class="btn-filter-pill" id="clearAllTopicsBtn" style="padding: 0.2rem 0.55rem; font-size: 0.72rem;">Clear</button>
          </div>
          <div class="drawer-topic-chips-grid" id="topicChipsGrid">
            <!-- Injected via JS -->
          </div>
        </div>
      </div>'''
    else:
        topic_section_html = ''

    has_highlight_toggle = config.get('has_highlight_toggle', True)
    highlight_btn_html = '''          <button class="drawer-action-btn" id="highlightAnswersBtn" style="display: none;">
            <span>🎯</span> <span id="highlightAnswersText">Highlight Answers</span>
          </button>''' if has_highlight_toggle else ""

    topic_wise_btn_html = f'''          <button class="drawer-action-btn" id="topicWiseToggleBtn">
            <span id="topicWiseIcon">📚</span> <span id="topicWiseText">Topic-wise MCQs</span>
          </button>''' if has_topic_wise_toggle else ""

    # Filter pills in Drawer
    if code == 'DV':
        filter_pills_html = '''          <button class="btn-filter-pill active" data-filter="all">All (300)</button>
          <button class="btn-filter-pill" data-filter="calc">🧮 Calc (40)</button>
          <button class="btn-filter-pill" data-filter="theory">📖 Theory (260)</button>
          <button class="btn-filter-pill" data-filter="unsolved">Unsolved</button>
          <button class="btn-filter-pill" data-filter="wrong">Incorrect</button>
          <button class="btn-filter-pill" data-filter="correct">Correct</button>
          <button class="btn-filter-pill" data-filter="bookmarked">⭐ Starred</button>'''
    elif code == 'ANN':
        filter_pills_html = '''          <button class="btn-filter-pill active" data-filter="all">All (200)</button>
          <button class="btn-filter-pill" data-filter="calc">🔢 Numerical (40)</button>
          <button class="btn-filter-pill" data-filter="theory">📘 Conceptual (160)</button>
          <button class="btn-filter-pill" data-filter="unsolved">Unsolved</button>
          <button class="btn-filter-pill" data-filter="wrong">Incorrect</button>
          <button class="btn-filter-pill" data-filter="correct">Correct</button>
          <button class="btn-filter-pill" data-filter="bookmarked">⭐ Starred</button>'''
    else:
        filter_pills_html = f'''          <button class="btn-filter-pill active" data-filter="all">All ({total_q})</button>
          <button class="btn-filter-pill" data-filter="unsolved">Unsolved</button>
          <button class="btn-filter-pill" data-filter="wrong">Incorrect</button>
          <button class="btn-filter-pill" data-filter="correct">Correct</button>
          <button class="btn-filter-pill" data-filter="bookmarked">⭐ Starred</button>'''

    type_label_js = "q.type === 'calculation' ? '🧮 Numerical' : '📖 Conceptual'" if code == 'ANN' else ("q.type === 'calculation' ? '🧮 Calc' : '📖 Theory'" if code == 'DV' else f"'{code}'")

    page_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover" />
  <meta name="theme-color" content="{color}" />
  <meta name="mobile-web-app-capable" content="yes" />
  <meta name="apple-mobile-web-app-status-bar-style" content="default" />
  <title>{title}</title>
  {icon_html}
  <script defer src="/_vercel/insights/script.js"></script>
  <style>
{css}
  </style>
</head>
<body>

  <!-- Sticky Top Header -->
  <header class="app-header">
    <div class="header-bar">
      <div class="header-left">
        <!-- 3-Line Hamburger Menu Button -->
        <button class="hamburger-btn" id="menuToggleBtn" title="Open Menu &amp; Options" aria-label="Open menu">
          <span></span>
          <span></span>
          <span></span>
        </button>

        <!-- Compact Subject Dropdown Wrapper -->
        <div class="header-brand-dropdown-wrapper" id="subjectDropdownWrap">
          <button class="header-brand-btn" id="subjectDropdownBtn" aria-haspopup="true" aria-expanded="false" title="Click to switch subject">
            <div class="brand-logo" style="{config['brand_logo_style']}">{code}</div>
            <span class="dropdown-chevron">▾</span>
          </button>

          <!-- Dropdown Menu -->
          <div class="subject-dropdown-menu" id="subjectDropdownMenu">
            <div class="dropdown-header-label">Select Subject</div>
{dropdown_items_html}          </div>
        </div>
      </div>

      <div class="header-right">
        <!-- Reveal Pill Button in Header -->
        <button class="btn-revision-pill" id="revisionToggleBtn" title="Reveal Correct Answers">
          <span>📖</span>
          <span class="rev-pill-text">Reveal</span>
        </button>

        <!-- Compact Score Pill -->
        <div class="header-score-pill" id="scorePill" title="Your performance summary">
          <span class="score-item c-ok" id="statCorrect">✓ 0</span>
          <span>&bull;</span>
          <span class="score-item c-no" id="statWrong">✗ 0</span>
          <span>&bull;</span>
          <span class="score-item c-pct" id="statAccuracy">0%</span>
        </div>

        <!-- Quick Matrix Jump Button -->
        <button class="btn-header-icon" id="matrixOpenBtn" title="Open Question Grid (Q1–Q{total_q})">
          <span>📑</span>
        </button>
      </div>
    </div>

    <!-- Active Filter Summary Strip -->
    <div class="filter-summary-strip">
      <div class="filter-summary-inner">
        <span class="active-mode-tag" id="activeModeSummary">{config['subject_full']} ({total_q})</span>
        <span class="active-filter-tag" id="activeFilterSummary">All</span>
        <span class="active-revision-tag" id="activeRevisionSummary" style="display: none;">Answers Revealed</span>
        <span class="btn-open-menu-link" id="openMenuLink">⚙️ Menu &amp; Filters</span>
      </div>
    </div>
  </header>

  <!-- Off-Canvas Side Drawer -->
  <div class="drawer-backdrop" id="drawerBackdrop"></div>

  <aside class="side-drawer" id="sideDrawer" aria-label="Menu and filters">
    <div class="drawer-header">
      <button class="drawer-theme-top-btn" id="drawerThemeBtn" title="Switch Theme (Dark / Light)">
        <span id="drawerThemeIcon">🌙</span> <span id="drawerThemeText">Dark Mode</span>
      </button>
      <button class="drawer-close-btn" id="drawerCloseBtn" aria-label="Close menu">&times;</button>
    </div>

    <div class="drawer-body">
      <!-- Section: Select Subject -->
      <div>
        <div class="drawer-section-title">
          <span>📚 Select Subject</span>
        </div>
        <div class="drawer-segmented" style="padding: 4px; gap: 4px;">
{drawer_subjects_html}        </div>
      </div>

      <!-- Section: View Style -->
      <div>
        <div class="drawer-section-title">
          <span>📱 View Style</span>
        </div>
        <div class="drawer-segmented">
          <button class="drawer-segmented-btn active" data-view="list" id="viewListTab">List Stream</button>
          <button class="drawer-segmented-btn" data-view="focus" id="viewFocusTab">Focus Single</button>
        </div>
        <div class="drawer-btn-row">
          <button class="drawer-action-btn" id="revealAnswersBtn">
            <span id="revealAnswersText">Reveal Answers</span>
          </button>
{highlight_btn_html}
{topic_wise_btn_html}
        </div>
      </div>

{topic_section_html}

      <!-- Section: Filter Questions -->
      <div>
        <div class="drawer-section-title">
          <span>🎯 Filter Questions</span>
        </div>
        <div style="display: flex; flex-wrap: wrap; gap: 0.45rem;">
{filter_pills_html}
        </div>
      </div>

      <!-- Section: Actions -->
      <div>
        <div class="drawer-section-title">
          <span>⚡ Actions</span>
        </div>
        <div class="drawer-btn-row">
          <button class="drawer-action-btn" id="drawerShuffleBtn">
            <span>🔀</span> <span id="shuffleBtnText">Shuffle</span>
          </button>
          <button class="drawer-action-btn" id="drawerGridBtn">
            <span>📑</span> <span>Grid Jump</span>
          </button>
          <button class="drawer-action-btn full-width danger" id="resetProgressBtn">
            <span>↺</span> <span>Reset All Answers &amp; Scores</span>
          </button>
        </div>
      </div>
    </div>
  </aside>

  <!-- Main Content: MCQs Stream -->
  <main>
    <div class="mcq-list" id="mcqList"></div>

    <div class="focus-mode-container" id="focusContainer">
      <div class="focus-card" id="focusCard"></div>
    </div>

    <div id="emptyState" style="display: none; text-align: center; padding: 4rem 1rem;">
      <div style="font-size: 3rem; margin-bottom: 0.75rem;">🔍</div>
      <h3 style="font-size: 1.2rem; font-weight: 700; color: var(--text-primary);" id="emptyStateTitle">No MCQs Match</h3>
      <p style="color: var(--text-secondary); margin-top: 0.4rem; font-size: 0.9rem;" id="emptyStateDesc">Open the 3-line menu (☰) to adjust your filters or topics.</p>
    </div>
  </main>

  <!-- Navigator Matrix Modal -->
  <div class="matrix-modal-backdrop" id="matrixModal">
    <div class="matrix-modal">
      <div class="matrix-modal-header">
        <div style="font-weight: 700; font-size: 1.05rem;">Question Navigator (Q1 to Q{total_q})</div>
        <button class="btn-header-icon" id="matrixCloseBtn">&times;</button>
      </div>
      <div style="padding: 0.65rem 1.25rem; background: var(--bg-subtle); display: flex; flex-wrap: wrap; gap: 0.85rem; font-size: 0.78rem; font-weight: 600;">
        <span style="display:flex; align-items:center; gap:0.35rem;"><span style="width:12px; height:12px; background:var(--bg-subtle); border:1px solid var(--border-subtle); border-radius:3px;"></span> Unsolved</span>
        <span style="display:flex; align-items:center; gap:0.35rem;"><span style="width:12px; height:12px; background:var(--success); border-radius:3px;"></span> Correct</span>
        <span style="display:flex; align-items:center; gap:0.35rem;"><span style="width:12px; height:12px; background:var(--danger); border-radius:3px;"></span> Wrong</span>
        <span style="display:flex; align-items:center; gap:0.35rem;"><span style="width:12px; height:12px; border-radius:50%; background:#f59e0b;"></span> Starred</span>
      </div>
      <div class="matrix-modal-body">
        <div class="matrix-grid" id="matrixGrid"></div>
      </div>
    </div>
  </div>

  <!-- Floating Back to Top Button -->
  <button id="backToTopBtn" class="back-to-top" title="Back to top">↑</button>

  <!-- Toast -->
  <div id="toast">Notification</div>

  <script>
    // Data
    const TOPICS = {topics_json_str};
    const TOPIC_INFO = {topic_info_json_str};
    const HAS_TOPIC_WISE_TOGGLE = {has_topic_wise_toggle_str};
    const MCQS = {mcqs_json_str};

    const storagePrefix = '{storage_prefix}';

    // Application State
    const state = {{
      viewType: localStorage.getItem(storagePrefix + 'view_type') || 'list',
      filter: 'all',
      isRevisionMode: localStorage.getItem(storagePrefix + 'revision_mode') === 'true',
      isHighlightAnswers: localStorage.getItem(storagePrefix + 'highlight_answers') === 'true',
      isTopicWise: localStorage.getItem(storagePrefix + 'topic_wise') === 'true',
      theme: localStorage.getItem(storagePrefix + 'theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'),
      userAnswers: JSON.parse(localStorage.getItem(storagePrefix + 'answers') || '{{}}'),
      revealedAnswers: new Set(JSON.parse(localStorage.getItem(storagePrefix + 'reveals') || '[]')),
      bookmarks: new Set(JSON.parse(localStorage.getItem(storagePrefix + 'bookmarks') || '[]')),
      selectedTopics: new Set(JSON.parse(localStorage.getItem(storagePrefix + 'selected_topics') || JSON.stringify(Object.keys(TOPICS)))),
      isShuffled: false,
      shuffledIds: [],
      focusIndex: 0
    }};

    // DOM Elements
    const mcqListEl = document.getElementById('mcqList');
    const focusContainerEl = document.getElementById('focusContainer');
    const focusCardEl = document.getElementById('focusCard');
    const emptyStateEl = document.getElementById('emptyState');
    const emptyStateTitle = document.getElementById('emptyStateTitle');
    const emptyStateDesc = document.getElementById('emptyStateDesc');
    const sideDrawer = document.getElementById('sideDrawer');
    const drawerBackdrop = document.getElementById('drawerBackdrop');
    const menuToggleBtn = document.getElementById('menuToggleBtn');
    const drawerCloseBtn = document.getElementById('drawerCloseBtn');
    const activeModeSummary = document.getElementById('activeModeSummary');
    const activeFilterSummary = document.getElementById('activeFilterSummary');
    const activeRevisionSummary = document.getElementById('activeRevisionSummary');
    const openMenuLink = document.getElementById('openMenuLink');
    const statCorrect = document.getElementById('statCorrect');
    const statWrong = document.getElementById('statWrong');
    const statAccuracy = document.getElementById('statAccuracy');
    const matrixModal = document.getElementById('matrixModal');
    const matrixGrid = document.getElementById('matrixGrid');
    const backToTopBtn = document.getElementById('backToTopBtn');
    const toast = document.getElementById('toast');
    const topicChipsGrid = document.getElementById('topicChipsGrid');
    const topicSelectedCountBadge = document.getElementById('topicSelectedCountBadge');
    const drawerShuffleBtn = document.getElementById('drawerShuffleBtn');
    const revisionToggleBtn = document.getElementById('revisionToggleBtn');
    const revealAnswersBtn = document.getElementById('revealAnswersBtn');
    const revealAnswersText = document.getElementById('revealAnswersText');
    const highlightAnswersBtn = document.getElementById('highlightAnswersBtn');
    const topicWiseToggleBtn = document.getElementById('topicWiseToggleBtn');
    const drawerTopicSection = document.getElementById('drawerTopicSection');
    const drawerThemeBtn = document.getElementById('drawerThemeBtn');

    // Subject Dropdown
    const subjectDropdownWrap = document.getElementById('subjectDropdownWrap');
    const subjectDropdownBtn = document.getElementById('subjectDropdownBtn');

    function toggleSubjectDropdown(e) {{
      if (e) e.stopPropagation();
      const isOpen = subjectDropdownWrap.classList.toggle('open');
      subjectDropdownBtn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    }}

    function closeSubjectDropdown() {{
      if (subjectDropdownWrap) {{
        subjectDropdownWrap.classList.remove('open');
        subjectDropdownBtn.setAttribute('aria-expanded', 'false');
      }}
    }}

    if (subjectDropdownBtn) {{
      subjectDropdownBtn.addEventListener('click', toggleSubjectDropdown);
    }}

    document.addEventListener('click', (e) => {{
      if (subjectDropdownWrap && !subjectDropdownWrap.contains(e.target)) {{
        closeSubjectDropdown();
      }}
    }});

    // Toast
    let toastTimeout;
    function showToast(msg) {{
      clearTimeout(toastTimeout);
      toast.textContent = msg;
      toast.classList.add('show');
      toastTimeout = setTimeout(() => {{
        toast.classList.remove('show');
      }}, 2600);
    }}

    // Escape HTML
    function escapeHtml(str) {{
      if (!str) return '';
      return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
    }}

    // State Persistence
    function saveAnswers() {{
      localStorage.setItem(storagePrefix + 'answers', JSON.stringify(state.userAnswers));
      localStorage.setItem(storagePrefix + 'reveals', JSON.stringify(Array.from(state.revealedAnswers)));
    }}

    function saveBookmarks() {{
      localStorage.setItem(storagePrefix + 'bookmarks', JSON.stringify(Array.from(state.bookmarks)));
    }}

    function saveTopics() {{
      localStorage.setItem(storagePrefix + 'selected_topics', JSON.stringify(Array.from(state.selectedTopics)));
    }}

    // Theme Setup (Managed via Drawer Menu)
    function applyTheme(theme) {{
      state.theme = theme;
      document.documentElement.setAttribute('data-theme', theme);
      localStorage.setItem(storagePrefix + 'theme', theme);
      const drawerIcon = document.getElementById('drawerThemeIcon');
      if (drawerIcon) drawerIcon.textContent = theme === 'dark' ? '☀️' : '🌙';
      const drawerText = document.getElementById('drawerThemeText');
      if (drawerText) drawerText.textContent = theme === 'dark' ? 'Light Mode' : 'Dark Mode';
    }}
    applyTheme(state.theme);

    if (drawerThemeBtn) {{
      drawerThemeBtn.addEventListener('click', () => {{
        applyTheme(state.theme === 'dark' ? 'light' : 'dark');
        showToast(state.theme === 'dark' ? 'Dark theme enabled' : 'Light theme enabled');
      }});
    }}

    // Drawer Open/Close with Background Lock
    function openDrawer() {{
      closeSubjectDropdown();
      sideDrawer.classList.add('open');
      drawerBackdrop.classList.add('open');
      menuToggleBtn.classList.add('active');
      document.body.style.overflow = 'hidden';
    }}

    function closeDrawer() {{
      sideDrawer.classList.remove('open');
      drawerBackdrop.classList.remove('open');
      menuToggleBtn.classList.remove('active');
      document.body.style.overflow = '';
    }}

    menuToggleBtn.addEventListener('click', () => {{
      if (sideDrawer.classList.contains('open')) closeDrawer();
      else openDrawer();
    }});
    drawerCloseBtn.addEventListener('click', closeDrawer);
    drawerBackdrop.addEventListener('click', closeDrawer);
    openMenuLink.addEventListener('click', openDrawer);
    activeModeSummary.addEventListener('click', openDrawer);

    // Prevent background scrolling on backdrop touch
    drawerBackdrop.addEventListener('touchmove', (e) => e.preventDefault(), {{ passive: false }});

    // Update Stats
    function updateStats() {{
      let totalAnswered = 0;
      let totalCorrect = 0;
      let totalWrong = 0;

      MCQS.forEach(q => {{
        const ans = state.userAnswers[q.id];
        if (ans) {{
          totalAnswered++;
          if (ans === q.answer) totalCorrect++;
          else totalWrong++;
        }}
      }});

      statCorrect.textContent = `✓ ${{totalCorrect}}`;
      statWrong.textContent = `✗ ${{totalWrong}}`;
      const pct = totalAnswered > 0 ? Math.round((totalCorrect / totalAnswered) * 100) : 0;
      statAccuracy.textContent = `${{pct}}%`;
    }}

    // Update Summary Strip
    function updateSummaryStrip() {{
      const topicCount = state.selectedTopics.size;
      const totalTopics = Object.keys(TOPICS).length;
      let modeText = '{config['subject_full']} ({total_q})';
      if (totalTopics > 1) {{
        if (HAS_TOPIC_WISE_TOGGLE) {{
          modeText = state.isTopicWise ? `📚 Topic-wise (${{topicCount}}/${{totalTopics}} Topics)` : '{config['subject_full']} ({total_q})';
        }} else {{
          modeText = `${{topicCount}}/${{totalTopics}} Topics · {config['code']}`;
        }}
      }}
      if (state.isShuffled) {{
        modeText = '🔀 Shuffled · ' + modeText;
      }}
      activeModeSummary.textContent = modeText;

      let filterText = 'All';
      if (state.filter === 'calc') {{
        filterText = '{'🧮 Numerical' if code == 'ANN' else '🧮 Calc'}';
      }} else if (state.filter === 'theory') {{
        filterText = '{'📘 Conceptual' if code == 'ANN' else '📖 Theory'}';
      }} else if (state.filter === 'unsolved') {{
        filterText = 'Unsolved';
      }} else if (state.filter === 'wrong') {{
        filterText = 'Incorrect';
      }} else if (state.filter === 'correct') {{
        filterText = 'Correct';
      }} else if (state.filter === 'bookmarked') {{
        filterText = '⭐ Starred';
      }}
      activeFilterSummary.textContent = filterText;
    }}

    // Filtering Pool
    function getBasePoolMCQs() {{
      let pool = MCQS;
      if (state.selectedTopics && state.selectedTopics.size > 0 && (!HAS_TOPIC_WISE_TOGGLE || state.isTopicWise)) {{
        pool = pool.filter(m => state.selectedTopics.has(m.topicCode));
      }}
      if (state.filter === 'calc') {{
        pool = pool.filter(m => m.type === 'calculation');
      }} else if (state.filter === 'theory') {{
        pool = pool.filter(m => m.type === 'theory');
      }}
      if (state.isShuffled && state.shuffledIds.length === pool.length) {{
        const map = new Map(pool.map(m => [m.id, m]));
        return state.shuffledIds.map(id => map.get(id)).filter(Boolean);
      }}
      return pool;
    }}

    function getFilteredMCQs() {{
      const basePool = getBasePoolMCQs();
      return basePool.filter(q => {{
        const userAns = state.userAnswers[q.id];
        if (state.filter === 'unsolved') {{
          return !userAns && !state.revealedAnswers.has(q.id);
        }} else if (state.filter === 'correct') {{
          return userAns && userAns === q.answer;
        }} else if (state.filter === 'wrong') {{
          return userAns && userAns !== q.answer;
        }} else if (state.filter === 'bookmarked') {{
          return state.bookmarks.has(q.id);
        }}
        return true;
      }});
    }}

    // Build Topic Selector (for multi-topic subjects)
    function buildTopicSelector() {{
      if (!topicChipsGrid) return;
      topicChipsGrid.innerHTML = '';
      const topicCodes = Object.keys(TOPICS).sort();
      let selectedCount = 0;

      topicCodes.forEach(code => {{
        const topicName = TOPICS[code];
        const count = MCQS.filter(m => m.topicCode === code).length;
        const isSelected = state.selectedTopics.has(code);
        if (isSelected) selectedCount += count;

        const label = document.createElement('label');
        label.className = 'drawer-topic-item';

        const cb = document.createElement('input');
        cb.type = 'checkbox';
        cb.checked = isSelected;
        cb.onchange = (e) => {{
          if (e.target.checked) {{
            state.selectedTopics.add(code);
          }} else {{
            state.selectedTopics.delete(code);
          }}
          saveTopics();
          buildTopicSelector();
          state.focusIndex = 0;
          renderActiveView();
          updateStats();
        }};

        const textSpan = document.createElement('span');
        textSpan.textContent = topicName;

        const countSpan = document.createElement('span');
        countSpan.className = 'topic-count-badge';
        countSpan.textContent = `(${{count}})`;

        label.appendChild(cb);
        label.appendChild(textSpan);
        label.appendChild(countSpan);
        topicChipsGrid.appendChild(label);
      }});

      if (topicSelectedCountBadge) {{
        topicSelectedCountBadge.textContent = `(${{state.selectedTopics.size}}/${{topicCodes.length}} · ${{selectedCount}} MCQs)`;
      }}
    }}

    const selectAllTopicsBtn = document.getElementById('selectAllTopicsBtn');
    if (selectAllTopicsBtn) {{
      selectAllTopicsBtn.addEventListener('click', () => {{
        state.selectedTopics = new Set(Object.keys(TOPICS));
        saveTopics();
        buildTopicSelector();
        renderActiveView();
        showToast('All topics selected');
      }});
    }}

    const clearAllTopicsBtn = document.getElementById('clearAllTopicsBtn');
    if (clearAllTopicsBtn) {{
      clearAllTopicsBtn.addEventListener('click', () => {{
        state.selectedTopics.clear();
        saveTopics();
        buildTopicSelector();
        renderActiveView();
        showToast('All topics cleared');
      }});
    }}

    // Reveal Answers Handler (Point 4: Button with name Reveal Answers in view style section)
    function updateRevealUI() {{
      const active = !!state.isRevisionMode;
      if (revealAnswersBtn) {{
        revealAnswersBtn.classList.toggle('active', active);
        if (revealAnswersText) {{
          revealAnswersText.textContent = active ? 'Hide Answers' : 'Reveal Answers';
        }}
      }}
      if (revisionToggleBtn) {{
        revisionToggleBtn.classList.toggle('active', active);
        const textSpan = revisionToggleBtn.querySelector('.rev-pill-text');
        if (textSpan) textSpan.textContent = active ? 'Revealed' : 'Reveal';
      }}
      if (activeRevisionSummary) {{
        activeRevisionSummary.style.display = active ? 'inline-flex' : 'none';
      }}
      if (highlightAnswersBtn) {{
        highlightAnswersBtn.style.display = active ? 'inline-flex' : 'none';
      }}
    }}

    function toggleRevealAnswers() {{
      state.isRevisionMode = !state.isRevisionMode;
      localStorage.setItem(storagePrefix + 'revision_mode', state.isRevisionMode);
      updateRevealUI();
      renderActiveView();
      showToast(state.isRevisionMode ? 'Correct answers revealed' : 'Quiz practice mode');
    }}

    if (revealAnswersBtn) revealAnswersBtn.addEventListener('click', toggleRevealAnswers);
    if (revisionToggleBtn) revisionToggleBtn.addEventListener('click', toggleRevealAnswers);

    // Highlight Answers Handler
    function updateHighlightUI() {{
      if (!highlightAnswersBtn) return;
      highlightAnswersBtn.classList.toggle('active', !!state.isHighlightAnswers);
      const textSpan = document.getElementById('highlightAnswersText');
      if (textSpan) {{
        textSpan.textContent = state.isHighlightAnswers ? 'Highlight: ON' : 'Highlight Answers';
      }}
    }}

    function toggleHighlightAnswers() {{
      state.isHighlightAnswers = !state.isHighlightAnswers;
      localStorage.setItem(storagePrefix + 'highlight_answers', state.isHighlightAnswers ? 'true' : 'false');
      updateHighlightUI();
      renderActiveView();
      showToast(state.isHighlightAnswers ? 'Correct options highlighted' : 'Option highlighting off');
    }}

    if (highlightAnswersBtn) highlightAnswersBtn.addEventListener('click', toggleHighlightAnswers);

    // Topic-wise View Handler
    function updateTopicWiseUI() {{
      if (!HAS_TOPIC_WISE_TOGGLE) return;
      if (topicWiseToggleBtn) {{
        topicWiseToggleBtn.classList.toggle('active', !!state.isTopicWise);
        const textSpan = document.getElementById('topicWiseText');
        if (textSpan) {{
          textSpan.textContent = state.isTopicWise ? 'Topic-wise MCQs (Active)' : 'Topic-wise MCQs';
        }}
      }}
      if (drawerTopicSection) {{
        drawerTopicSection.style.display = state.isTopicWise ? 'block' : 'none';
      }}
    }}

    function toggleTopicWise() {{
      state.isTopicWise = !state.isTopicWise;
      localStorage.setItem(storagePrefix + 'topic_wise', state.isTopicWise ? 'true' : 'false');
      updateTopicWiseUI();
      state.focusIndex = 0;
      renderActiveView();
      showToast(state.isTopicWise ? 'Topic-wise view enabled (23 Topics)' : 'Normal view restored');
    }}

    if (topicWiseToggleBtn) topicWiseToggleBtn.addEventListener('click', toggleTopicWise);

    // Card Generation
    function createMCQCard(q) {{
      const card = document.createElement('div');
      card.className = 'mcq-card';
      card.id = `mcq-card-${{q.id}}`;

      const isRevision = !!state.isRevisionMode;
      const userAns = state.userAnswers[q.id];
      const isAnswered = !isRevision && !!userAns;
      const isRevealed = isRevision || state.revealedAnswers.has(q.id) || isAnswered;
      const isCorrect = userAns === q.answer;

      if (isAnswered) {{
        card.classList.add(isCorrect ? 'status-correct' : 'status-wrong');
      }}

      // Top Meta Bar
      const topDiv = document.createElement('div');
      topDiv.className = 'card-top';

      const leftTop = document.createElement('div');
      leftTop.className = 'card-meta-left';

      // Q# display
      const qIdPill = document.createElement('span');
      qIdPill.className = 'q-id-pill';
      qIdPill.textContent = `Q${{q.id}}`;
      leftTop.appendChild(qIdPill);

      // Type Badge
      const typePill = document.createElement('span');
      typePill.className = `type-pill ${{q.type || 'theory'}}`;
      typePill.textContent = {type_label_js};
      leftTop.appendChild(typePill);

      // Right Badges
      const badgesDiv = document.createElement('div');
      badgesDiv.className = 'card-badges';

      if (isRevision) {{
        const keyPill = document.createElement('span');
        keyPill.className = 'revision-key-pill';
        keyPill.textContent = `Ans: ${{q.answer}}`;
        keyPill.title = `Correct option is ${{q.answer}}`;
        badgesDiv.appendChild(keyPill);
      }} else if (isAnswered || isRevealed) {{
        const retryBtn = document.createElement('button');
        retryBtn.className = 'btn-filter-pill';
        retryBtn.style.padding = '0.15rem 0.5rem';
        retryBtn.style.fontSize = '0.74rem';
        retryBtn.innerHTML = '↺ Retry';
        retryBtn.title = 'Clear answer to re-attempt';
        retryBtn.onclick = () => handleResetQuestion(q.id);
        badgesDiv.appendChild(retryBtn);
      }} else {{
        const showAnsBtn = document.createElement('button');
        showAnsBtn.className = 'btn-filter-pill';
        showAnsBtn.style.padding = '0.15rem 0.5rem';
        showAnsBtn.style.fontSize = '0.74rem';
        showAnsBtn.innerHTML = 'Show Answer';
        showAnsBtn.title = 'Reveal answer without scoring';
        showAnsBtn.onclick = () => handleShowAnswer(q.id);
        badgesDiv.appendChild(showAnsBtn);
      }}

      const starBtn = document.createElement('span');
      starBtn.className = `bookmark-btn ${{state.bookmarks.has(q.id) ? 'active' : ''}}`;
      starBtn.dataset.id = q.id;
      starBtn.innerHTML = state.bookmarks.has(q.id) ? '★' : '☆';
      starBtn.title = 'Star/Bookmark this question';
      starBtn.onclick = () => toggleBookmark(q.id);
      badgesDiv.appendChild(starBtn);

      topDiv.appendChild(leftTop);
      topDiv.appendChild(badgesDiv);
      card.appendChild(topDiv);

      // Line 2: Dedicated Topic Row
      if (q.topic) {{
        const topicRow = document.createElement('div');
        topicRow.className = 'card-topic-row';
        const topicPill = document.createElement('span');
        topicPill.className = 'topic-pill';
        topicPill.textContent = q.topic;
        topicRow.appendChild(topicPill);
        card.appendChild(topicRow);
      }}

      // Question Text
      const title = document.createElement('div');
      title.className = 'question-title';
      title.textContent = q.question;
      card.appendChild(title);

      // Options (A, B, C, D)
      const optionsContainer = document.createElement('div');
      optionsContainer.className = 'options-grid';

      const optKeys = ['A', 'B', 'C', 'D'];
      optKeys.forEach(key => {{
        if (q.options[key] === undefined) return;
        const optText = q.options[key];

        const optBtn = document.createElement('button');
        optBtn.className = 'option-btn';

        const letter = document.createElement('span');
        letter.className = 'option-letter';
        letter.textContent = key;

        const textSpan = document.createElement('span');
        textSpan.className = 'option-text';
        textSpan.textContent = optText;

        optBtn.appendChild(letter);
        optBtn.appendChild(textSpan);

        if (isRevision) {{
          optBtn.style.cursor = 'default';
          if (state.isHighlightAnswers && key === q.answer) {{
            optBtn.classList.add('revealed-correct');
          }}
        }} else if (isRevealed) {{
          if (key === userAns && isCorrect) {{
            optBtn.classList.add('selected-correct');
          }} else if (key === userAns && !isCorrect) {{
            optBtn.classList.add('selected-wrong');
          }} else if (key === q.answer) {{
            optBtn.classList.add('revealed-correct');
          }} else {{
            optBtn.classList.add('dimmed');
          }}
        }} else {{
          optBtn.onclick = () => handleOptionSelect(q.id, key);
        }}

        optionsContainer.appendChild(optBtn);
      }});

      card.appendChild(optionsContainer);

      // Card Footer & Direct Solution Display (No separate containers, no topic/solution labels)
      if (isRevealed) {{
        const footer = document.createElement('div');
        footer.className = 'card-footer';

        const solText = q.calculation || q.explanation;

        if (isRevision) {{
          const msg = document.createElement('div');
          msg.className = 'feedback-message correct';
          msg.innerHTML = `<span>Correct Answer: <strong>Option ${{q.answer}}</strong></span>`;
          footer.appendChild(msg);

          if (q.type === 'calculation' && solText) {{
            const sol = document.createElement('div');
            sol.className = 'direct-solution-text';
            sol.textContent = solText;
            footer.appendChild(sol);
          }}
        }} else if (isAnswered) {{
          const msg = document.createElement('div');
          msg.className = `feedback-message ${{isCorrect ? 'correct' : 'wrong'}}`;
          msg.innerHTML = isCorrect
            ? `<span>Correct! Option ${{q.answer}}</span>`
            : `<span>Incorrect. Correct Answer: <strong>Option ${{q.answer}}</strong></span>`;
          footer.appendChild(msg);

          if (solText) {{
            const sol = document.createElement('div');
            sol.className = 'direct-solution-text';
            sol.textContent = solText;
            footer.appendChild(sol);
          }}
        }} else {{
          // Revealed via Show Answer
          const msg = document.createElement('div');
          msg.className = 'feedback-message';
          msg.innerHTML = `<span>Correct Answer: <strong>Option ${{q.answer}}</strong></span>`;
          footer.appendChild(msg);

          if (solText) {{
            const sol = document.createElement('div');
            sol.className = 'direct-solution-text';
            sol.textContent = solText;
            footer.appendChild(sol);
          }}
        }}

        card.appendChild(footer);
      }}

      return card;
    }}

    // Render Active View
    function renderActiveView() {{
      const items = getFilteredMCQs();

      if (items.length === 0) {{
        mcqListEl.innerHTML = '';
        focusContainerEl.style.display = 'none';
        emptyStateEl.style.display = 'block';
        return;
      }}
      emptyStateEl.style.display = 'none';

      if (state.viewType === 'focus') {{
        mcqListEl.style.display = 'none';
        focusContainerEl.style.display = 'block';
        renderFocusCard();
      }} else {{
        focusContainerEl.style.display = 'none';
        mcqListEl.style.display = 'flex';
        renderList(items);
      }}
      updateSummaryStrip();
    }}

    function renderList(items) {{
      mcqListEl.innerHTML = '';
      const fragment = document.createDocumentFragment();

      if (state.isTopicWise && HAS_TOPIC_WISE_TOGGLE && Object.keys(TOPIC_INFO).length > 0) {{
        // Group items by topic
        const grouped = {{}};
        items.forEach(q => {{
          const code = q.topicCode || 'OTHER';
          if (!grouped[code]) grouped[code] = [];
          grouped[code].push(q);
        }});

        // Sort by topic number
        const sortedCodes = Object.keys(grouped).sort((a, b) => {{
          const na = (TOPIC_INFO[a] && TOPIC_INFO[a].num) || 999;
          const nb = (TOPIC_INFO[b] && TOPIC_INFO[b].num) || 999;
          return na - nb;
        }});

        sortedCodes.forEach(code => {{
          const tInfo = TOPIC_INFO[code];
          const tNum = tInfo ? tInfo.num : code;
          const tTitle = tInfo ? tInfo.title : (TOPICS[code] || code);
          const tDesc = tInfo ? tInfo.info : '';
          const qCount = grouped[code].length;

          const groupHeader = document.createElement('div');
          groupHeader.className = 'topic-group-header';
          groupHeader.id = `topic-group-${{code}}`;
          groupHeader.innerHTML = `
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.35rem;">
              <span class="topic-group-badge">Topic ${{tNum}} · ${{qCount}} Questions</span>
            </div>
            <h3 class="topic-group-title">${{tTitle}}</h3>
            ${{tDesc ? `<p class="topic-group-info">${{tDesc}}</p>` : ''}}
          `;
          fragment.appendChild(groupHeader);

          grouped[code].forEach(q => {{
            fragment.appendChild(createMCQCard(q));
          }});
        }});
      }} else {{
        items.forEach(q => {{
          fragment.appendChild(createMCQCard(q));
        }});
      }}

      mcqListEl.appendChild(fragment);
    }}

    function renderFocusCard() {{
      const filtered = getFilteredMCQs();
      if (filtered.length === 0) return;

      if (state.focusIndex >= filtered.length) state.focusIndex = filtered.length - 1;
      if (state.focusIndex < 0) state.focusIndex = 0;

      const q = filtered[state.focusIndex];
      focusCardEl.innerHTML = '';

      const card = createMCQCard(q);
      focusCardEl.appendChild(card);

      const nav = document.createElement('div');
      nav.className = 'focus-nav';

      const prevBtn = document.createElement('button');
      prevBtn.className = 'btn-nav';
      prevBtn.innerHTML = '&larr; Previous';
      prevBtn.disabled = state.focusIndex === 0;
      prevBtn.onclick = () => {{
        state.focusIndex--;
        renderFocusCard();
        window.scrollTo({{ top: 0, behavior: 'smooth' }});
      }};

      const progressInfo = document.createElement('div');
      progressInfo.style.fontWeight = '600';
      progressInfo.style.fontSize = '0.92rem';
      progressInfo.style.color = 'var(--text-secondary)';
      progressInfo.textContent = `Question ${{state.focusIndex + 1}} of ${{filtered.length}}`;

      const nextBtn = document.createElement('button');
      nextBtn.className = 'btn-nav';
      nextBtn.innerHTML = 'Next &rarr;';
      nextBtn.disabled = state.focusIndex === filtered.length - 1;
      nextBtn.onclick = () => {{
        state.focusIndex++;
        renderFocusCard();
        window.scrollTo({{ top: 0, behavior: 'smooth' }});
      }};

      nav.appendChild(prevBtn);
      nav.appendChild(progressInfo);
      nav.appendChild(nextBtn);

      focusCardEl.appendChild(nav);
    }}

    // View Toggles in Drawer
    document.querySelectorAll('.drawer-segmented-btn[data-view]').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.drawer-segmented-btn[data-view]').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        state.viewType = btn.dataset.view;
        localStorage.setItem(storagePrefix + 'view_type', state.viewType);
        renderActiveView();
        closeDrawer();
      }});
    }});

    // Status Filter Chips in Drawer
    document.querySelectorAll('.btn-filter-pill[data-filter]').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.btn-filter-pill[data-filter]').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        state.filter = btn.dataset.filter;
        state.focusIndex = 0;
        updateSummaryStrip();
        renderActiveView();
        closeDrawer();
      }});
    }});

    // Shuffle Button in Drawer
    drawerShuffleBtn.addEventListener('click', () => {{
      state.isShuffled = !state.isShuffled;
      if (state.isShuffled) {{
        const ids = MCQS.map(m => m.id);
        for (let i = ids.length - 1; i > 0; i--) {{
          const j = Math.floor(Math.random() * (i + 1));
          [ids[i], ids[j]] = [ids[j], ids[i]];
        }}
        state.shuffledIds = ids;
        document.getElementById('shuffleBtnText').textContent = 'Unshuffle (Sequential)';
        showToast('{total_q} MCQs shuffled randomly');
      }} else {{
        state.shuffledIds = [];
        document.getElementById('shuffleBtnText').textContent = 'Shuffle Questions';
        showToast('Restored sequential order');
      }}
      updateSummaryStrip();
      state.focusIndex = 0;
      renderActiveView();
      closeDrawer();
    }});

    // Open Grid from Drawer
    document.getElementById('drawerGridBtn').addEventListener('click', () => {{
      closeDrawer();
      buildMatrix();
      matrixModal.classList.add('open');
    }});

    // Reset Progress in Drawer
    document.getElementById('resetProgressBtn').addEventListener('click', () => {{
      if (confirm('Are you sure you want to reset all your answers and progress for {code}?')) {{
        state.userAnswers = {{}};
        state.revealedAnswers.clear();
        localStorage.removeItem(storagePrefix + 'answers');
        localStorage.removeItem(storagePrefix + 'reveals');
        updateStats();
        renderActiveView();
        showToast('All answers and progress have been reset.');
        closeDrawer();
      }}
    }});

    // Matrix Jump Modal
    function buildMatrix() {{
      matrixGrid.innerHTML = '';
      MCQS.forEach(q => {{
        const btn = document.createElement('button');
        btn.className = 'matrix-btn';
        btn.textContent = q.id;

        const ans = state.userAnswers[q.id];
        if (ans) {{
          btn.classList.add(ans === q.answer ? 'correct' : 'wrong');
        }} else if (state.bookmarks.has(q.id)) {{
          btn.classList.add('bookmarked');
        }}

        btn.onclick = () => {{
          matrixModal.classList.remove('open');

          if (q.topicCode && !state.selectedTopics.has(q.topicCode)) {{
            state.selectedTopics.add(q.topicCode);
            saveTopics();
            buildTopicSelector();
          }}

          if (state.viewType === 'focus') {{
            const filtered = getFilteredMCQs();
            const targetIdx = filtered.findIndex(item => item.id === q.id);
            if (targetIdx !== -1) {{
              state.focusIndex = targetIdx;
              renderFocusCard();
            }} else {{
              state.filter = 'all';
              const refiltered = getFilteredMCQs();
              state.focusIndex = refiltered.findIndex(item => item.id === q.id);
              renderFocusCard();
            }}
          }} else {{
            state.filter = 'all';
            renderActiveView();
            setTimeout(() => {{
              const el = document.getElementById(`mcq-card-${{q.id}}`);
              if (el) {{
                el.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                el.style.outline = '3px solid var(--primary)';
                setTimeout(() => el.style.outline = 'none', 1800);
              }}
            }}, 120);
          }}
        }};

        matrixGrid.appendChild(btn);
      }});
    }}

    document.getElementById('matrixOpenBtn').addEventListener('click', () => {{
      buildMatrix();
      matrixModal.classList.add('open');
    }});

    document.getElementById('matrixCloseBtn').addEventListener('click', () => {{
      matrixModal.classList.remove('open');
    }});

    matrixModal.addEventListener('click', (e) => {{
      if (e.target === matrixModal) matrixModal.classList.remove('open');
    }});

    window.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') {{
        if (matrixModal.classList.contains('open')) matrixModal.classList.remove('open');
        if (sideDrawer.classList.contains('open')) closeDrawer();
      }}
    }});

    // Floating Back to Top Button
    window.addEventListener('scroll', () => {{
      if (window.scrollY > 350) {{
        backToTopBtn.classList.add('visible');
      }} else {{
        backToTopBtn.classList.remove('visible');
      }}
    }}, {{ passive: true }});

    backToTopBtn.addEventListener('click', () => {{
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }});

    // Card Actions
    function handleOptionSelect(qId, selectedKey) {{
      if (state.isRevisionMode) return;
      if (state.userAnswers[qId]) return;

      state.userAnswers[qId] = selectedKey;
      saveAnswers();
      updateStats();

      const card = document.getElementById(`mcq-card-${{qId}}`);
      if (card) {{
        const newCard = createMCQCard(MCQS.find(m => m.id === qId));
        card.replaceWith(newCard);
      }}

      const q = MCQS.find(m => m.id === qId);
      if (selectedKey === q.answer) {{
        showToast('Correct!');
      }} else {{
        showToast(`Incorrect (Answer was ${{q.answer}})`);
      }}
    }}

    function handleShowAnswer(qId) {{
      if (state.isRevisionMode) return;
      state.revealedAnswers.add(qId);
      saveAnswers();

      const card = document.getElementById(`mcq-card-${{qId}}`);
      if (card) {{
        const newCard = createMCQCard(MCQS.find(m => m.id === qId));
        card.replaceWith(newCard);
      }}
      showToast('Answer revealed');
    }}

    function handleResetQuestion(qId) {{
      delete state.userAnswers[qId];
      state.revealedAnswers.delete(qId);
      saveAnswers();
      updateStats();

      const card = document.getElementById(`mcq-card-${{qId}}`);
      if (card) {{
        const newCard = createMCQCard(MCQS.find(m => m.id === qId));
        card.replaceWith(newCard);
      }}
      showToast('Question reset');
    }}

    function toggleBookmark(qId) {{
      if (state.bookmarks.has(qId)) {{
        state.bookmarks.delete(qId);
        showToast('Bookmark removed');
      }} else {{
        state.bookmarks.add(qId);
        showToast('Question bookmarked ⭐');
      }}
      saveBookmarks();

      const card = document.getElementById(`mcq-card-${{qId}}`);
      if (card) {{
        const btn = card.querySelector('.bookmark-btn');
        if (btn) {{
          btn.classList.toggle('active', state.bookmarks.has(qId));
          btn.innerHTML = state.bookmarks.has(qId) ? '★' : '☆';
        }}
      }}
    }}

    // Initialization
    if (state.viewType === 'focus') {{
      document.getElementById('viewListTab').classList.remove('active');
      document.getElementById('viewFocusTab').classList.add('active');
    }}
    buildTopicSelector();
    updateRevealUI();
    updateHighlightUI();
    updateTopicWiseUI();
    updateStats();
    renderActiveView();
  </script>
</body>
</html>
'''
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(page_html)
    print(f"Generated {fname} ({len(page_html):,} bytes)")

import base64

def get_icon_html(code, base_name):
    with open(f'{base_name}-32x32.png', 'rb') as f:
        b64_png = base64.b64encode(f.read()).decode()
    touch_icon = f'apple-touch-icon-{code.lower()}.png' if code != 'DV' else 'apple-touch-icon.png'
    return f'''<link rel="icon" type="image/png" href="data:image/png;base64,{b64_png}" />
  <link rel="icon" type="image/png" sizes="32x32" href="./{base_name}-32x32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="./{base_name}-16x16.png" />
  <link rel="icon" type="image/svg+xml" href="./{base_name}.svg" />
  <link rel="shortcut icon" href="./{base_name}.ico" />
  <link rel="apple-touch-icon" sizes="180x180" href="./{touch_icon}" />'''

# Configurations for all 4 files
dv_config = {
    "filename": "index.html",
    "code": "DV",
    "subject_full": "Data Visualization",
    "title": "Data Visualization (CDB601220) – MCQ Bank (300 MCQs)",
    "color": "#2563eb",
    "icon_html": get_icon_html("DV", "favicon"),
    "brand_logo_style": "background: linear-gradient(135deg, #2563eb, #1d4ed8);",
    "primary": "#2563eb",
    "primary_hover": "#1d4ed8",
    "primary_light": "#eff6ff",
    "primary_text": "#1e40af",
    "theory_bg": "#e0e7ff",
    "theory_text": "#3730a3",
    "dark_primary": "#3b82f6",
    "dark_primary_hover": "#60a5fa",
    "dark_primary_light": "#1e293b",
    "dark_primary_text": "#93c5fd",
    "dark_theory_bg": "#1e1b4b",
    "dark_theory_text": "#a5b4fc",
    "topics": dv_topics,
    "mcqs": dv_mcqs,
    "prefix": "dv_",
    "has_calc": True
}

ann_config = {
    "filename": "ann.html",
    "code": "ANN",
    "subject_full": "Artificial Neural Networks",
    "title": "Artificial Neural Networks (ANN) – MCQ Bank (200 MCQs)",
    "color": "#7c3aed",
    "icon_html": get_icon_html("ANN", "favicon-ann"),
    "brand_logo_style": "background: linear-gradient(135deg, #7c3aed, #5b21b6);",
    "primary": "#7c3aed",
    "primary_hover": "#6d28d9",
    "primary_light": "#f5f3ff",
    "primary_text": "#5b21b6",
    "theory_bg": "#ede9fe",
    "theory_text": "#5b21b6",
    "dark_primary": "#a78bfa",
    "dark_primary_hover": "#c4b5fd",
    "dark_primary_light": "#1e1b2e",
    "dark_primary_text": "#c4b5fd",
    "dark_theory_bg": "#2e1065",
    "dark_theory_text": "#c4b5fd",
    "topics": ann_topics,
    "mcqs": ann_mcqs,
    "prefix": "ann_",
    "has_calc": True
}

nlp_config = {
    "filename": "nlp.html",
    "code": "NLP",
    "subject_full": "Natural Language Processing",
    "title": "Natural Language Processing (NLP) – MCQ Bank (200 MCQs)",
    "color": "#10b981",
    "icon_html": get_icon_html("NLP", "favicon-nlp"),
    "brand_logo_style": "background: linear-gradient(135deg, #10b981, #059669);",
    "primary": "#10b981",
    "primary_hover": "#059669",
    "primary_light": "#ecfdf5",
    "primary_text": "#065f46",
    "theory_bg": "#d1fae5",
    "theory_text": "#065f46",
    "dark_primary": "#34d399",
    "dark_primary_hover": "#6ee7b7",
    "dark_primary_light": "#064e3b",
    "dark_primary_text": "#6ee7b7",
    "dark_theory_bg": "#064e3b",
    "dark_theory_text": "#6ee7b7",
    "topics": nlp_topics,
    "mcqs": nlp_mcqs,
    "prefix": "nlp_",
    "has_calc": False
}

ml_config = {
    "filename": "ml.html",
    "code": "ML",
    "subject_full": "Machine Learning",
    "title": "Machine Learning (ML) – MCQ Bank (200 MCQs)",
    "color": "#ea580c",
    "icon_html": get_icon_html("ML", "favicon-ml"),
    "brand_logo_style": "background: linear-gradient(135deg, #ea580c, #c2410c);",
    "primary": "#ea580c",
    "primary_hover": "#c2410c",
    "primary_light": "#fff7ed",
    "primary_text": "#9a3412",
    "theory_bg": "#ffedd5",
    "theory_text": "#9a3412",
    "dark_primary": "#fb923c",
    "dark_primary_hover": "#fdba74",
    "dark_primary_light": "#431407",
    "dark_primary_text": "#fdba74",
    "dark_theory_bg": "#431407",
    "dark_theory_text": "#fdba74",
    "topics": ml_topics,
    "topic_info": ml_topic_info,
    "mcqs": ml_mcqs,
    "prefix": "ml_",
    "has_calc": False,
    "has_topic_wise_toggle": True
}

# Generate all 4 pages
generate_page(dv_config)
generate_page(ann_config)
generate_page(nlp_config)
generate_page(ml_config)

print("All 4 files successfully generated!")

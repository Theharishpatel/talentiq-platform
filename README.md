---
title: TalentiQ Demo
emoji: 🚀
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: "5.38.0"
python_version: "3.11"
app_file: app.py
pinned: false
---


# TalentiQ – AI-Powered Candidate Ranking Platform

## Overview

TalentiQ is an AI-powered candidate ranking platform developed for the Redrob AI Hackathon. The platform automatically matches candidates against a Job Description (JD) using semantic search, dense vector embeddings, and a multi-stage ranking pipeline.

Instead of manually reviewing thousands of candidate profiles, recruiters can upload a Job Description and receive a ranked shortlist with similarity scores and AI-generated explanations.

---

# Features

- Upload Job Description (.docx)
- Automatic JD text extraction
- Semantic embedding generation
- Candidate retrieval using Qdrant Vector Search
- AI-powered candidate ranking
- Explainable ranking with recruiter-friendly reasons
- Export ranked candidates as `submission.csv`
- Interactive Gradio interface
- Hugging Face Spaces deployment

---
## Project Structure

```text
talentiq-platform/
│
├── app.py
├── README.md
├── requirements.txt
├── pyproject.toml
├── submission_metadata.yaml
├── .env.example
├── .gitignore
│
├── data/
│   ├── demo_candidates.jsonl
│   │
│   ├── artifacts/
│   │   └── candidate_embeddings.parquet
│   │
│   ├── processed/
│   │   ├── candidate_embeddings.jsonl
│   │   ├── candidate_features.parquet
│   │   ├── candidate_index.parquet
│   │   ├── candidate_text.jsonl
│   │   └── clean_candidates.jsonl
│   │
│   ├── raw/
│   │   ├── candidates.jsonl
│   │   ├── candidate_schema.json
│   │   ├── job_description.docx
│   │   └── sample_submission.csv
│   │
│   └── reports/
│       └── profiling/
│
├── docs/
│   └── README.md
│
├── notebooks/
│
├── outputs/
│   └── submission.csv
│
├── scripts/
│
├── src/
│   ├── cleaning/
│   ├── common/
│   ├── config/
│   ├── demo/
│   ├── features/
│   ├── index/
│   ├── ingestion/
│   ├── models/
│   ├── qdrant/
│   ├── ranking/
│   ├── reasoning/
│   ├── retrieval/
│   ├── submission/
│   ├── text_builder/
│   ├── utils/
│   └── validation/
│
├── tools/
│
└── .venv/
```

---

# How the Ranking Pipeline Works

The ranking system follows the pipeline below.

```
Job Description (.docx)
            │
            ▼
Extract JD Text
            │
            ▼
Generate Dense Embedding
            │
            ▼
Semantic Search (Qdrant)
            │
            ▼
Retrieve Top Candidates
            │
            ▼
Ranking Engine
            │
            ▼
Reason Generation
            │
            ▼
submission.csv
```

---

# Installation

Clone the repository.

```bash
git clone https://github.com/Theharishpatel/talentiq-platform
cd talentiq-platform
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Running the Demo

Launch the Gradio application.

```bash
python -m tools.run_pipeline --jd data/raw/job_description.docx --out submission.csv

Open

```
http://localhost:7860
```

Upload a Job Description and click **Run Ranking**.

The application will:

- Extract the JD
- Generate embeddings
- Search candidates
- Rank candidates
- Generate recruiter reasoning
- Export `submission.csv`

---

# Reproducing the Submission

The hackathon requires a single command that generates the submission CSV.

Use:

```bash


```

or (if CLI ranking script exists)

```bash
python rank.py --candidates data/raw/candidates.jsonl 
```

The generated file is

```
outputs/submission.csv
```

---

# Precomputed Artifacts

The project uses precomputed candidate embeddings for efficient retrieval.

Demo dataset:

```
data/demo_candidates.jsonl
```

Embedding model:

```
BAAI/bge-base-en-v1.5
```

Vector Dimension:

```
768
```

Similarity Metric:

```
Cosine Similarity
```

---

# Demo Deployment

The project is publicly deployed on Hugging Face Spaces.

**Live Demo**

https://huggingface.co/spaces/harishpatel/talentiq-demo

The demo includes:

- Preloaded demo candidate dataset (~100 candidates)
- JD upload
- End-to-end ranking
- CSV generation

The demo completes within the CPU time budget specified in the hackathon guidelines.

---

# GitHub Repository Contents

The repository contains everything required for reproduction:

- Complete source code
- README with setup instructions
- requirements.txt
- submission_metadata.yaml
- Demo dataset
- Candidate ranking pipeline
- Hugging Face deployment

No manual intervention is required to reproduce the demo workflow.

---

# AI Tool Declaration

This project was developed with AI-assisted development tools for code suggestions, documentation, debugging, and refactoring.

The overall system design, ranking pipeline, implementation, integration, testing, debugging, and deployment were completed by the project author.

---

# Technologies Used

- Python
- Gradio
- Sentence Transformers
- Qdrant
- PyTorch
- Pandas
- NumPy
- Scikit-learn
- python-docx

---


# Author

Harish Patel

Redrob AI Hackathon Submission

## Contributors

| Name | GitHub |
|------|---------|
| Harish Patel | [@Theharishpatel](https://github.com/Theharishpatel) |
| Vidita Rathore | [@Viditarathore](https://github.com/Viditarathore) |
| Dharmanshu Kashyap | [@dharmanshukas100](https://github.com/dharmanshukas100) |


---

# License

This project is intended for educational and hackathon evaluation purposes.

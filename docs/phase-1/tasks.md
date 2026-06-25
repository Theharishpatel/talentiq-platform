# Phase 1 Tasks

## Documentation

* [x] Create overview.md
* [x] Create architecture.md
* [x] Create decisions.md
* [x] Create tasks.md

---

# Project Setup

* [x] Create repository
* [x] Configure Git
* [x] Setup folder structure
* [x] Configure virtual environment
* [x] Configure pyproject.toml

---

# Data Collection

* [x] Collect candidate datasets
* [x] Verify dataset accessibility
* [ ] Create dataset documentation
* [ ] Create data dictionary

---

# Schema & Models

* [x] Store organization schema
* [x] Create Pydantic models
* [x] Create nested model structure
* [x] Create validation test dataset
* [x] Validate sample candidate

---

# Data Ingestion

* [x] Build JSONL reader
* [x] Stream records using generators
* [x] Support large datasets (100k+)
* [x] Add ingestion tests

---

# Data Validation

* [x] Validate records against Pydantic models
* [x] Validate required fields
* [x] Validate data types
* [x] Profile validation errors
* [x] Fix schema mismatches
* [x] Validate full dataset
* [x] Achieve 100% schema validation

---

# Data Profiling

- [x] Profile skills
- [x] Profile companies
- [x] Profile titles
- [x] Profile locations
- [x] Profile education
- [x] Profile career history
- [x] Profile behavioral signals
- [x] Generate profiling reports

---

# Data Cleaning

* [x] Create cleaning module
* [x] Define cleaning rules
* [x] Handle sentinel values (-1 → None)
* [x] Handle missing values
* [x] Remove duplicate skills
* [x] Trim whitespace
* [x] Standardize text formatting
* [x] Generate clean candidate records

---

# Feature Engineering

* [x] Experience Engine
* [x] Behavior Engine
* [x] Recruitability Engine
* [x] Growth Engine
* [x] Consistency Engine
* [x] Honeypot Features
* [ ] Candidate Text Builder
* [ ] Embedding Generation
* [ ] Qdrant Index Build

---

# Export

* [x] Export cleaned JSONL
* [ ] Export clean_candidates.parquet
* [ ] Export feature_candidates.parquet

---

# Testing

* [x] Model validation tests
* [x] Cleaning tests
* [x] Experience engine tests
* [x] Behavior engine tests
* [x] Recruitability engine tests
* [x] Growth engine tests
* [x] Consistency engine tests
* [x] Honeypot feature tests
* [ ] Normalization tests
* [ ] Export tests

---

# Documentation

* [ ] Update README
* [ ] Add preprocessing pipeline diagram
* [ ] Add architecture diagram
* [ ] Document cleaning rules
* [ ] Document feature definitions

---

# Phase Completion Checklist

* [x] Cleaning pipeline completed
* [ ] Normalization pipeline completed
* [x] Feature engineering completed
* [ ] Export pipeline completed
* [ ] Tests passing
* [ ] Documentation completed
* [ ] clean_candidates.parquet generated
* [ ] feature_candidates.parquet generated
* [ ] Ready for Ranking Engines (Phase 2)

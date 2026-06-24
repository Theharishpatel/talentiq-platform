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

* [ ] Create cleaning module
* [ ] Define cleaning rules
* [ ] Handle sentinel values (-1 → None)
* [ ] Handle missing values
* [ ] Remove duplicate skills
* [ ] Trim whitespace
* [ ] Standardize text formatting
* [ ] Generate clean candidate records

---

# Data Normalization

* [ ] Normalize skills
* [ ] Normalize education
* [ ] Normalize locations
* [ ] Normalize companies
* [ ] Normalize job titles
* [ ] Normalize dates

---

# Feature Engineering

* [ ] Skill Count
* [ ] Experience Years
* [ ] Highest Degree
* [ ] Certification Count
* [ ] Employment Duration
* [ ] GitHub Activity Feature
* [ ] Recruitability Features
* [ ] Career Growth Features

---

# Export

* [ ] Export cleaned JSONL
* [ ] Export clean_candidates.parquet
* [ ] Export feature_candidates.parquet

---

# Testing

* [x] Model validation tests
* [ ] Cleaning tests
* [ ] Normalization tests
* [ ] Feature engineering tests
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

* [ ] Cleaning pipeline completed
* [ ] Normalization pipeline completed
* [ ] Feature engineering completed
* [ ] Export pipeline completed
* [ ] Tests passing
* [ ] Documentation completed
* [ ] clean_candidates.parquet generated
* [ ] feature_candidates.parquet generated
* [ ] Ready for Ranking Engines (Phase 2)

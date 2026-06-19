# Architecture - Phase 1

## Purpose

Design a scalable preprocessing pipeline capable of handling large candidate
datasets while maintaining high data quality.

---

# High Level Architecture

                  Raw Candidate Files
                        (JSONL)
                           │
                           ▼

                  Data Ingestion Layer

                           │
                           ▼

                Data Validation Layer

                           │
                           ▼

                 Data Cleaning Layer

                           │
                           ▼

               Data Normalization Layer

                           │
                           ▼

               Feature Preparation Layer

                           │
                           ▼

                 JSONL / Parquet Export

                           │
                           ▼

                Ranking Engine (Phase 2)

---

# Components

## Data Ingestion

Responsibilities

- Read files
- Parse records
- Convert into Python objects

---

## Validation

Responsibilities

- Required fields
- Schema validation
- Data type checking
- Missing values

---

## Cleaning

Responsibilities

- Remove duplicates
- Trim whitespace
- Remove invalid records
- Handle missing values

---

## Normalization

Responsibilities

- Standardize skills
- Normalize education
- Normalize experience
- Standardize dates
- Normalize locations

---

## Feature Preparation

Generate structured fields such as

- Experience Years
- Skill Count
- Certification Count
- Highest Degree
- Employment Duration

---

## Export Layer

Supported outputs

- JSONL
- Parquet

---

# Folder Architecture

    data/

        ├── raw/
        ├── processed/
        └── features/

    scripts/

        ├── ingestion/
        ├── validation/
        ├── cleaning/
        ├── normalization/
        ├── feature_engineering/
        └── export/

---

# Storage Layers

Raw Layer

Purpose

Store original datasets.

---

Processed Layer

Purpose

Store cleaned and standardized datasets.

---

Feature Layer

Purpose

Store structured features for ranking.

---

# Data Flow

            Raw Dataset

                ↓

            Validation

                ↓

            Cleaning

                ↓

           Normalization

                ↓

        Feature Engineering

                ↓

              JSONL

                ↓

             Parquet

                ↓

           Ranking Engine

---

# Scalability

Designed for

- Large datasets
- Batch processing
- Incremental updates
- Parallel execution

Future support

- Apache Spark
- Distributed processing
- Cloud Storage

---

# Technology Stack

Python

Pandas

Pathlib

JSON

Parquet

Logging

Git

Markdown
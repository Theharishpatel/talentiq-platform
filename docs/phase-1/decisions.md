# Architecture Decisions

This document records important technical decisions taken during Phase 1.

---

# ADR-001

Decision

Store raw datasets separately.

Reason

Raw data should never be modified.

Status

Accepted

---

# ADR-002

Decision

Use JSONL for processed output.

Reason

Supports streaming and ML pipelines.

Status

Accepted

---

# ADR-003

Decision

Export Parquet.

Reason

Smaller size and faster analytics.

Status

Accepted

---

# ADR-004

Decision

Separate Raw, Processed and Feature data.

Reason

Improves reproducibility.

Status

Accepted

---

# ADR-005

Decision

Use modular pipeline architecture.

Reason

Each module performs one responsibility only.

Status

Accepted

---

# ADR-006

Decision

Normalize all categorical values.

Reason

Avoid inconsistent values such as

Python

python

PYTHON

Status

Accepted

---

# ADR-007

Decision

Perform validation before cleaning.

Reason

Invalid records should be detected before
transformation.

Status

Accepted

---

# ADR-008

Decision

Store derived features separately.

Reason

Ranking Engine should not recalculate features.

Status

Accepted

---

# ADR-009

Decision

Use immutable processing.

Reason

Every execution should produce identical output
from identical input.

Status

Accepted

---

# ADR-010

Decision

Keep preprocessing independent from Ranking Engine.

Reason

Loose coupling improves maintainability.

Status

Accepted

# ADR-011

Decision

Use percentile-based scoring.

Reason

Dataset distributions vary across features and
percentiles produce robust ranking signals.

Status

Accepted

# ADR-012

Decision

Use independent feature engines.

Reason

Experience, behavior, recruitability, growth,
and consistency should evolve independently.

Status

Accepted

# ADR-013

Decision

Keep Honeypot Detection separate from ranking score.

Reason

Fraud risk and candidate quality are different
signals and should not be mixed directly.

Status

Accepted

# ADR-014

Decision

Generate feature scores during offline preprocessing.

Reason

Avoid expensive recalculation during search.

Status

Accepted


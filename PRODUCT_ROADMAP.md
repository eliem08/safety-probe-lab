# Safety Probe Lab — Product Roadmap

## Product outcome

An auditable safety-evaluation workbench for running curated probe suites, annotating responses, tracking regressions, and producing evidence-rich reports without pretending a single score captures safety.

## Users and problem

- Safety researchers running exploratory evaluations.
- Model developers investigating known failure modes.
- Red teams who need traceable cases and human review.

## Current foundation

- Probe set for uncertainty, evidence sufficiency, privacy, instruction conflict and calibration.
- Transparent keyword-marker signals, CSV/JSON exports, dashboard and Colab notebook.

## Roadmap

### Phase 1 — Evaluation integrity
- [ ] Add a documented probe schema and versioned dataset files.
- [ ] Separate automated signals from human annotations.
- [ ] Add paired benign/adversarial variants and expected behavior rubrics.
- [ ] Add blind review mode and disagreement tracking.
- [ ] Export evidence snippets and per-category failure examples.

### Phase 2 — Robust evaluation
- [ ] Add model adapters and fixed generation settings.
- [ ] Add repeated runs and confidence intervals where sampling is used.
- [ ] Track false positives/false negatives for heuristic rules on annotated data.
- [ ] Add risk taxonomy, severity, attack surface and mitigation tracking.
- [ ] Add regression comparison across model revisions.

### Phase 3 — Final product
A local-first safety evaluation console with versioned probe packs, transparent scoring, human annotation, evidence links, release comparisons, and an audit-ready report for each run.

## Success criteria

- Every claim in a report links to concrete prompts and responses.
- Heuristic and human-evaluated results are clearly separated.
- No single aggregate score hides severe category failures.
- Sensitive test data remains local unless explicitly configured otherwise.

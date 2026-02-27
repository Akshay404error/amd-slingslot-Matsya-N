# Novelty

This document summarizes the novel contributions and differentiators of the BIMBO prototype compared with prior art.

## Key Innovations
1. Multi-Method Ensemble Attribution
   - Combines independent analyses (timing correlation, CNN-LSTM website fingerprinting, and GNN topology prediction) to reduce false positives and increase attribution confidence.

2. Graph-Based Guard Prediction
   - Uses graph metrics and GNN-style logic to reason about probable guard nodes leveraging Tor topology and observed traffic—this is more robust than purely timing- or fingerprint-based methods.

3. Forensic-Grade Artifact Generation
   - Produces court-ready artifacts (timestamped JSON/CSV/HTML/PDF) and preserves chain-of-custody information for legal admissibility.

4. Modular, Replaceable Engines
   - Each analysis engine is decoupled and can be swapped (e.g., replace fingerprinting model or GNN variant) without changing orchestration code.

5. Practical Live + Batch Mode
   - Supports both continuous live monitoring (short capture windows) and large-scale batch processing, enabling both proactive and reactive investigations.

6. Transparent Confidence Scoring
   - Method-level confidences combined into a weighted ensemble that is auditable and explainable for investigators.

## Research & Applied Contributions
- Demonstrates practical integration of deep learning fingerprinting with statistical and graph-based approaches.
- Emphasizes real-world considerations: model versioning, DB mismatch handling, and forensic reporting.

## Limitations (Acknowledged)
- Attribution remains probabilistic; multi-method consensus mitigates but cannot eliminate uncertainty.
- Effectiveness depends on capture quality, PCAP completeness, and relay churn.

## Potential for Novel Research
- Fine-tuning GNN architectures specifically for Tor topology dynamics.
- Applying explainable AI techniques to increase investigator trust in model outputs.

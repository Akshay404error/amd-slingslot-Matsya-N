# Gap Identification

This document lists current limitations, gaps relative to ideal forensic attribution systems, and recommended mitigations.

## Current Gaps
1. Ground-truth labels
   - Gap: Limited availability of labeled ground-truth for guard assignments in the wild.
   - Mitigation: Build synthetic testbeds and controlled experiments to generate labeled datasets.

2. Model Version Drift
   - Gap: Potential mismatch between training and inference environments (library versions).
   - Mitigation: Pin versions, containerize models, provide model metadata and checksums.

3. Scalability
   - Gap: SQLite and single-node orchestration limit large-scale concurrent processing.
   - Mitigation: Move to a centralized DB (Postgres), add distributed worker queues (Celery/Kafka).

4. Geolocation Accuracy
   - Gap: IP-based geolocation is noisy and can mislead attribution.
   - Mitigation: Use multiple geolocation providers, present location as contextual, not definitive.

5. False Positives and Statistical Uncertainty
   - Gap: Individual methods produce false positives; ensemble reduces but does not eliminate them.
   - Mitigation: Calibrate thresholds, add human-in-the-loop verification, create per-method explainers.

6. Chain-of-Custody Automation
   - Gap: File-level metadata and retention policies can be manual or inconsistent.
   - Mitigation: Automate signed artifact generation (digital signatures, checksums) and secure archival.

7. Legal and Ethical Constraints
   - Gap: Deployment must respect legal frameworks, privacy, and jurisdictional limitations.
   - Mitigation: Document policy requirements and implement access controls and audit trails.

## Short-Term Roadmap to Close Gaps
- Containerize analysis engines and Flask app.
- Add a message queue for distributed processing and horizontal scaling.
- Implement digital signing for exported artifacts.
- Add an explainability module that produces per-candidate reasoning (feature contributions).

## Long-Term Research Gaps
- Domain adaptation of fingerprinting models to new Tor client behaviors.
- Integrating additional signals (e.g., BGP data, long-term relay churn statistics).
- Formal probabilistic models that combine method uncertainties into a single calibrated posterior.

# Functional Requirements

Note: filename preserves the user's original spelling (`functionalrequriments.md`). This file lists required system behaviors for BIMBO.

## Core Functional Requirements
1. PCAP Ingestion
   - The system MUST accept PCAP files via a batch folder (`data/pcap_files/`) and via live capture.
   - The system MUST validate PCAP integrity before processing.

2. Flow Extraction
   - The system MUST reconstruct TCP/UDP flows and extract inter-packet timings and sizes.
   - The system MUST detect Tor flows by cross-referencing known relays.

3. Analysis Engines
   - The system MUST run three independent analyses: Timing Correlation, Website Fingerprinting, and GNN-based Guard Prediction.
   - Each engine MUST produce structured outputs with per-candidate confidence scores.

4. Ensemble Aggregation
   - The system MUST combine engine outputs into a ranked candidate list with an overall confidence score.
   - The weighting scheme MUST be configurable.

5. Forensic Artifacts
   - The system MUST export results as JSON, CSV, and HTML/PDF forensic reports.
   - Artifacts MUST include timestamps, source PCAP reference, method metadata, and investigator fields.

6. Dashboard & Visualization
   - The system MUST provide a web dashboard with metrics, alerts, map visualization, and ability to view per-analysis details.
   - The dashboard MUST refresh with new results and display alerts for high-confidence detections.

7. Alerts & Thresholds
   - The system MUST log alerts to `data/alert_log.json` when candidate confidence exceeds configurable thresholds.
   - Alerts MUST include candidate metadata and timestamp.

8. Scalability & Resilience
   - The system SHOULD support parallel processing of multiple PCAP files.
   - The system SHOULD retry failed analysis jobs and log failures.

9. Security & Chain-of-Custody
   - The system MUST timestamp outputs and maintain an audit trail.
   - The system SHOULD support digital signatures or checksums for exported artifacts.

10. APIs & Integration
    - The system SHOULD expose endpoints for `predict_tor` and `model_metrics` to allow programmatic integration.

## Non-functional Requirements
- Performance: Typical per-PCAP analysis should complete within acceptable time bounds (configurable; target < 10s on sample data).
- Reliability: System must handle malformed PCAPs gracefully and continue other jobs.
- Maintainability: Code must be modular and documented.
- Portability: Components should be runnable on Linux and Windows (WSL recommended for production parity).

## Acceptance Criteria
- End-to-end demo (via `demo_prototype.py`) runs and produces the 3 outcome artifacts.
- Dashboard displays the generated metrics and allows preview of forensic reports.
- Exported forensic report contains required metadata and supports CSV export.

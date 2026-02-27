# Expected Outcomes

This document defines the measurable outcomes and acceptance criteria for the BIMBO prototype and for a future production deployment.

## Prototype Outcomes (Minimum Viable)
1. Automated Topology Mapping
   - Produce a `topology_mapping.json` summarizing relays, guard/exit/middle counts, and at least one sample correlation.

2. Visualization Dashboard
   - Produce an interactive `dashboard.html` showing identified origins, confidence metrics, and a timeline of events.

3. Exportable Forensic Reports
   - Generate `forensic_report.html`, `forensic_report.json`, and `forensic_summary.csv` containing traced node data and activity flow.

4. Multi-Method Attribution
   - Demonstrate the three analysis engines producing per-method confidences and an ensemble result.

5. Reproducibility
   - Running `demo_prototype.py` or `batch_analyzer.py` on sample PCAPs reproduces the above outputs.

## Production Outcomes (Desirable)
1. Accuracy & Confidence
   - Ensemble attribution achieves consistent accuracy (target: >80% in validation datasets) and produces calibrated confidence scores.

2. Scalability
   - System can process batches of 20+ PCAPs concurrently with horizontal scaling.

3. Forensic Rigor
   - Outputs include signed artifacts/checksums and maintain auditable chain-of-custody.

4. Integration
   - Expose RESTful APIs for integration into case-management systems and SIEMs.

5. Explainability
   - Provide per-candidate explanation (feature contributions) to support investigator review.

## Acceptance Criteria
- All prototype artifacts are generated and viewable.
- The dashboard refreshes with new results and displays correct counts and confidences.
- Forensic reports contain required metadata and can be exported.
- Documentation (Quick Reference + Implementation Guide) exists and matches system behavior.

## Metrics & KPIs
- Mean confidence for true-positive attributions (validation): target > 80%.
- False positive rate: target < 10% on validation datasets.
- Processing latency per PCAP: target < 15s for small sample PCAPs.
- Uptime for web dashboard: target 99% in monitored deployments.

---

End of document.

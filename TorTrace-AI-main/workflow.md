# Workflow

This document describes the typical operational workflow for BIMBO from data ingestion through reporting.

## High-level Steps
1. Ingest PCAPs (batch or live)
2. Extract flows and features
3. Run three analysis engines in parallel
4. Aggregate and rank candidate guard nodes
5. Persist outputs and update dashboard
6. Generate forensic artifacts and alerts

## Detailed Flow
### 1. Ingestion
- Batch mode: drop PCAP files into `data/pcap_files/` or use `batch_analyzer.py` to scan and queue files.
- Live mode: `live_monitor.py` captures 60-second windows and writes to temporary PCAPs.

### 2. Flow Extraction & Feature Engineering
- `traffic_analysis/pcap_analyzer.py` reads PCAPs via Scapy, reconstructs flows, extracts inter-packet timings, packet sizes, and metadata (src/dst IPs, ports).
- PCAP analyzer cross-references flows against `data/tor_relays.db` to detect Tor flows and relay involvement.

### 3. Run Analysis Engines
- Engines launched as subprocesses or worker tasks:
  - Timing correlator (`correlation/timing_correlator.py`) computes cross-correlation and generates candidate pairs with significance scores.
  - Website fingerprinter (`ml_models/website_fingerprinter.py`) classifies traffic sequences into known website fingerprints.
  - GNN predictor (`ml_models/gnn_guard_predictor.py`) ranks nodes based on topology and observed features.

### 4. Ensemble Aggregation
- Aggregator weights each method (configurable) and computes per-candidate confidence.
- Top-K candidates persisted to `data/batch_results/` as JSON/CSV.

### 5. Persistence & Dashboard Update
- Results and metrics are written to files (`batch_summary.csv`, per-PCAP `_analysis.json`, GNN/fingerprint outputs).
- Flask dashboard reads these outputs to refresh visualizations and alerts.

### 6. Reporting & Alerts
- If candidate confidence exceeds thresholds, `batch_analyzer.py` logs alerts to `data/alert_log.json` and triggers report generation.
- `report_generator.py` creates forensic HTML/PDF reports including chain-of-custody metadata.

## Operational Notes
- Retry and timeouts ensure robust handling of long-running analyses.
- For large-scale operations, distribute worker processes across nodes and use shared storage.
- Maintain synchronized model versions between training and inference environments.

## Example CLI Commands
```bash
# Run batch analysis on all PCAPs
python batch_analyzer.py

# Run live monitoring
python live_monitor.py

# Start web dashboard
python visualization/dashboard.py
```

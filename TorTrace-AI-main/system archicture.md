# System Architecture

This document describes the high-level architecture of the BIMBO (TorTrace-AI) prototype: components, data flow, interfaces, and deployment topology.

## Overview
BIMBO is a modular multi-method Tor attribution system. It ingests PCAPs and live captures, extracts features, runs three independent analysis pipelines (statistical timing correlation, CNN-LSTM website fingerprinting, and a graph-based guard predictor), aggregates results via an ensemble, and generates forensic artifacts and dashboard visualizations.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        BIMBO SYSTEM ARCHITECTURE                          │
└─────────────────────────────────────────────────────────────────────────────┘

                              INPUT SOURCES
                    ┌─────────────────┬─────────────┐
                    │                 │             │
                ┌───▼─────┐      ┌───▼────┐    ┌──▼──────┐
                │  PCAPs  │      │  Live  │    │ Network │
                │  Files  │      │ Capture│    │ Streams │
                └───┬─────┘      └───┬────┘    └──┬──────┘
                    │                 │             │
                    └─────────────────┼─────────────┘
                                      │
                          ┌───────────▼────────────┐
                          │   INGEST & VALIDATION  │
                          │  batch_analyzer.py     │
                          │  live_monitor.py       │
                          └───────────┬────────────┘
                                      │
                          ┌───────────▼────────────┐
                          │  TRAFFIC ANALYZER      │
                          │  pcap_analyzer.py      │
                          │ • Flow reconstruction  │
                          │ • Tor detection        │
                          │ • Feature extraction   │
                          └───────────┬────────────┘
                                      │
                    ┌─────────────────┼─────────────────┐
                    │                 │                 │
            ┌───────▼────────┐ ┌──────▼──────┐ ┌───────▼────────┐
            │   TIMING CORR  │ │  FINGERPRINT│ │   GNN GUARD    │
            │ timing_corr.py │ │ fingerprint │ │  gnn_predict   │
            │                │ │   .py       │ │    .py         │
            │ Statistical    │ │  CNN-LSTM   │ │ Graph Neural   │
            │ Correlation    │ │  Web Site   │ │ Network        │
            │ Confidence:    │ │  Classifier │ │ Confidence:    │
            │ 75.6%          │ │  Confidence:│ │ 94.5%          │
            │                │ │  87.2%      │ │                │
            └────────┬───────┘ └──────┬──────┘ └────────┬───────┘
                     │                │                │
                     └────────────────┼────────────────┘
                                      │
                          ┌───────────▼─────────────┐
                          │   ENSEMBLE AGGREGATOR   │
                          │  • Weight combination   │
                          │  • Confidence fusion    │
                          │  • Rank generation      │
                          │  Final Score: 85.77%    │
                          └───────────┬─────────────┘
                                      │
                    ┌─────────────────┼─────────────────┐
                    │                 │                 │
            ┌───────▼────────┐ ┌──────▼──────┐ ┌───────▼────────┐
            │  PERSISTENCE   │ │ VISUALIZATION│ │   REPORTING    │
            │                │ │              │ │                │
            │ SQLite DB      │ │ Flask UI     │ │ HTML/JSON/CSV  │
            │ JSON/CSV       │ │ Dashboard    │ │ Forensic Report│
            │ tor_relays.db  │ │ Map Layer    │ │ PDF/Timeline   │
            │ Caching Layer  │ │ Real-time    │ │ Chain-of-Cust. │
            └────────────────┘ └──────────────┘ └────────────────┘
                    │                │                 │
                    └────────────────┼─────────────────┘
                                     │
                     ┌───────────────▼────────────────┐
                     │       OUTPUT ARTIFACTS         │
                     │ • topology_mapping.json        │
                     │ • dashboard.html               │
                     │ • forensic_report.html/json    │
                     │ • forensic_summary.csv         │
                     └────────────────────────────────┘
```

### Data Flow Sequence

```
PCAP/Stream Input
    ↓
[Batch Analyzer | Live Monitor] — Monitors & triggers
    ↓
[Traffic Analyzer] — Extracts flows & features
    ↓
┌───────────────────────────────────────────────┐
│ Parallel Processing (Independent Engines)     │
├───────────────────────────────────────────────┤
│ [Timing Correlator] → Statistical Score      │
│ [CNN-LSTM Fingerprinter] → Site Probability  │
│ [GNN Guard Predictor] → Graph-based Ranking  │
└───────────────────────────────────────────────┘
    ↓
[Ensemble Aggregator] — Fuses confidence scores
    ↓
[Storage Layer] — Persists results to DB/JSON
    ↓
┌───────────────────────────────────────────────┐
│ Output Generation (Multi-format Export)       │
├───────────────────────────────────────────────┤
│ [Dashboard] → Real-time web UI               │
│ [Reports] → HTML/JSON/CSV forensic artifacts │
│ [Alerts] → High-confidence detections        │
└───────────────────────────────────────────────┘
```

## Logical Components
- PCAP Ingest
  - Batch: `batch_analyzer.py` monitors `data/pcap_files` and spawns analysis jobs.
  - Live: `live_monitor.py` captures short windows and triggers analysis.

- Traffic Analyzer
  - `traffic_analysis/pcap_analyzer.py` — packet parsing, flow reconstruction, Tor flow detection, feature extraction.

- Analysis Engines
  - Timing Correlator: `correlation/timing_correlator.py` — cross-correlation and statistical matching.
  - Website Fingerprinter: `ml_models/website_fingerprinter.py` — CNN-LSTM classifier producing site-level probabilities.
  - GNN Guard Predictor: `ml_models/gnn_guard_predictor.py` — graph-based ranking of probable guard nodes.

- Ensemble Aggregator
  - Combines confidences, weights methods, produces final ranked candidate list and per-node confidence.

- Storage & DB
  - SQLite (`data/tor_relays.db`) for Tor relay metadata and local caches.
  - JSON/CSV outputs in `data/batch_results/` for artifacts and reports.

- Visualization & Reporting
  - Flask dashboard: `visualization/dashboard.py` and templates (UI) for metrics, alerts, map, and reports.
  - Map Generator: `visualization/map_generator.py` using Folium for geographic overlays.
  - Report Generator: `report_generator.py` to export HTML/PDF reports.

- Orchestration
  - `batch_analyzer.py` coordinates subprocesses; simple process-pool for parallelism.

## Data Flow (End-to-end)
1. PCAP ingestion → 2. Flow extraction → 3. Feature engineering → 4. Run Timing/Fingerprint/GNN analyses in parallel → 5. Ensemble aggregation → 6. Persist JSON/CSV and update dashboard → 7. Export forensic report (HTML/JSON/CSV/PDF)

## Deployment Topology
- Single-node or small server deployment is supported. Components run as Python processes; the Flask app serves UI.
- For scale: deploy analysis workers on multiple containers/VMs, use shared network storage for PCAPs and results, central SQLite can be replaced by a network DB for concurrency.

## Interfaces
- CLI entry points: `batch_analyzer.py`, `demo_prototype.py`, `live_monitor.py`.
- Web interface: Flask endpoints for `/`, `/metrics`, `/alerts`, `/batch_upload`, `/map`, `/predict_tor`, `/model_metrics`.
- File-system based I/O for analysis artifacts; optional API endpoints for integrations.

## Security & Forensics
- Timestamped artifacts, audit logs, and PDF report generation preserve chain-of-custody.
- Access to data directories must be hardened; recommended run on isolated forensic workstation or controlled server.

## Notes
- The architecture favors modularity: engines are replaceable and can be redeployed independently.

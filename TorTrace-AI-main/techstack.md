# Technical Stack

This document lists the technologies, libraries, and runtime environment used in the BIMBO prototype.

## Languages & Runtimes
- Python 3.10+ / 3.13 compatible (project tested on Python 3.13 in this workspace)
- Bash / Windows cmd for CLI orchestration

## Web & UI
- Flask — lightweight web framework used for the dashboard and API endpoints
- Jinja2 — templating for dashboard HTML
- HTML5 / CSS3 / JavaScript — frontend
- Folium / Leaflet — geographic visualization via `visualization/map_generator.py`

## Data Processing & Networking
- Scapy — PCAP parsing and packet inspection
- NumPy, pandas — numerical and tabular processing
- SciPy — signal processing and statistical correlation
- sqlite3 — embedded DB for Tor relay metadata and caching

## Machine Learning
- PyTorch — deep learning for CNN-LSTM website fingerprinting
- NetworkX — graph representation and analysis (GNN helper logic)
- scikit-learn — classical ML models, evaluation utilities (used for model baselines)

## Orchestration & Concurrency
- concurrent.futures / ProcessPoolExecutor — parallel batch processing
- subprocess — launching modular analyzer scripts

## Reporting & Visualization
- ReportLab — PDF generation for forensic reports
- CSV / JSON — structured artifact exports

## Dev & Packaging
- Requirements: `requirements.txt` (project root) listing pinned versions used during development
- Joblib — model serialization for scikit-learn artifacts

## Infrastructure Recommendations (Production)
- Containerization: Docker images for analysis workers and Flask server
- Orchestration: Kubernetes or simple supervisor system for worker processes
- Storage: Network file share or object storage for PCAP archives
- DB: Use PostgreSQL for concurrent, large-scale deployments instead of SQLite
- Secrets management and TLS for web UI in production

## Notes on Versions
- scikit-learn mismatch warnings may appear when models were trained on a different minor version; prefer training and inference on consistent versions.
- GPU acceleration supported for PyTorch-based fingerprinting if present; fall back to CPU.

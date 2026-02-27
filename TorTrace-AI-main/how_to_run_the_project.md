# How to Run the Project

This guide provides step-by-step instructions to set up and run the BIMBO (TorTrace-AI) project.

## Prerequisites

- **Python:** 3.7+ (tested with 3.13)
- **OS:** Linux, macOS, or Windows (WSL2 recommended for Windows)
- **Disk Space:** ~500MB for models and databases
- **Network:** Internet access for downloading Tor relay metadata (optional)

## Installation & Setup

### 1. Clone or Extract the Repository

```bash
cd /path/to/TorTrace-AI-main
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

**Activate virtual environment:**

- **Linux/macOS:**
  ```bash
  source venv/bin/activate
  ```

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Expected packages:**
- numpy, pandas, scipy
- scapy (packet analysis)
- torch (PyTorch)
- scikit-learn
- networkx (graph operations)
- flask (web dashboard)
- folium (map visualization)
- reportlab (PDF generation)

### 4. Verify Installation

```bash
python -c "import torch, scapy, flask; print('✅ All dependencies installed')"
```

---

## Running the Project

### Option A: Quick Demo (Recommended for First Run)

**Run the complete prototype with sample data:**

```bash
python demo_prototype.py
```

**What it does:**
- Loads sample Tor relay data
- Runs 3 analysis engines (timing correlation, fingerprinting, GNN)
- Generates ensemble results
- Creates dashboard HTML
- Exports forensic reports (HTML, JSON, CSV)

**Output files generated:**
- `topology_mapping.json` — Network topology
- `dashboard.html` — Interactive dashboard
- `forensic_report.html` — Visual forensic report
- `forensic_report.json` — Structured forensic data
- `forensic_summary.csv` — Summary statistics

**Expected runtime:** <5 seconds

---

### Option B: Batch Analysis (Multiple PCAPs)

**Prepare PCAP files:**

1. Place `.pcap` or `.pcapng` files in:
   ```
   data/pcap_files/
   ```

2. Run batch analyzer:
   ```bash
   python batch_analyzer.py
   ```

**What it does:**
- Monitors `data/pcap_files/` directory
- Extracts flows from each PCAP
- Runs all 3 analysis engines
- Saves results to `data/batch_results/`
- Generates CSV summary report
- Logs high-confidence alerts

**Output:**
```
data/batch_results/
├── batch_prediction_YYYYMMDD_HHMMSS.csv
├── batch_summary.csv
├── pcap_name_analysis.json
├── pcap_name_timing.json
├── pcap_name_fingerprint.json
└── pcap_name_gnn.json
```

**Example:**
```bash
# Add sample PCAP
cp /path/to/traffic.pcap data/pcap_files/

# Run analysis
python batch_analyzer.py
```

---

### Option C: Live Traffic Monitoring

**Monitor real-time network traffic:**

```bash
python live_monitor.py
```

**What it does:**
- Captures 60-second traffic windows
- Detects Tor flows in real-time
- Runs analysis engines on captured traffic
- Generates alerts for high-confidence guard nodes
- Saves analysis to `data/batch_results/live_*`

**Requirements:**
- Admin/root privileges (packet capture)
- Linux/macOS or Windows with Npcap installed

**Example (Linux):**
```bash
sudo python live_monitor.py
```

---

### Option D: Web Dashboard

**Launch interactive web UI:**

```bash
python visualization/dashboard.py
```

**Access the dashboard:**
- Open browser: `http://localhost:5000`

**Features:**
- Real-time metrics
- Guard node alerts
- Network map visualization
- Batch upload for PCAPs
- Model performance metrics
- Activity timeline

**Stop dashboard:**
- Press `Ctrl+C` in terminal
- Or visit `http://localhost:5000/shutdown`

---

### Option E: Train/Fine-tune Models

**Combine and train models:**

```bash
python scripts/combine_and_train.py
```

**What it does:**
- Combines feature datasets
- Trains CNN-LSTM fingerprinter
- Trains GNN guard predictor
- Saves models to `ml_models/`

**Time:** ~5-15 minutes (depends on data size)

**Requirements:**
- GPU recommended (NVIDIA CUDA + cuDNN)
- Minimum 4GB RAM

---

## Complete Workflow Example

**Step-by-step to get started:**

```bash
# 1. Navigate to project
cd TorTrace-AI-main

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# OR
venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run quick demo
python demo_prototype.py

# 5. View outputs
# Open: dashboard.html in browser
# Or read: forensic_report.json

# 6. (Optional) Launch web dashboard
python visualization/dashboard.py
# Visit: http://localhost:5000
```

---

## Configuration

### Key Configuration Files

**`batch_analyzer.py` (Lines 1-20):**
```python
PCAP_DIR = "data/pcap_files"
RESULTS_DIR = "data/batch_results"
DB_PATH = "data/tor_relays.db"
CONFIDENCE_THRESHOLD = 0.75  # Alert if > 75%
```

**`live_monitor.py` (Lines 1-20):**
```python
CAPTURE_DURATION = 60  # seconds
SAMPLE_RATE = 0.1  # 10% packet sampling
MIN_PACKETS = 50  # minimum for analysis
```

**`visualization/dashboard.py` (Lines 1-20):**
```python
FLASK_DEBUG = True  # Set False for production
FLASK_HOST = "0.0.0.0"
FLASK_PORT = 5000
```

### Environment Variables

```bash
# Optional: Set Tor relay database path
export TOR_DB_PATH="/custom/path/tor_relays.db"

# Optional: Enable verbose logging
export DEBUG=1

# Optional: Custom model path
export MODEL_PATH="/custom/path/models/"
```

---

## Troubleshooting

### Issue: ModuleNotFoundError

**Error:** `No module named 'torch'` or similar

**Solution:**
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Issue: SQLite Database Not Found

**Error:** `FileNotFoundError: data/tor_relays.db`

**Solution:**
- Download Tor relay consensus:
  ```bash
  python scripts/download_tor_consensus.py
  ```
- Or: Demo uses fallback sample data automatically

### Issue: Permission Denied (Live Monitoring)

**Error:** `Permission denied` when running `live_monitor.py`

**Solution:**
```bash
# Linux/macOS
sudo python live_monitor.py

# Windows (Run PowerShell as Administrator)
python live_monitor.py
```

### Issue: Port Already in Use (Dashboard)

**Error:** `Address already in use` on port 5000

**Solution:**
```bash
# Kill existing process
lsof -ti:5000 | xargs kill -9  # Linux/macOS

# Or use different port
python -c "
import sys
sys.path.insert(0, 'visualization')
from dashboard import app
app.run(port=5001)  # Custom port
"
```

### Issue: Low Confidence Scores

**Possible Causes:**
- Insufficient traffic samples
- Network misconfiguration
- Model needs retraining

**Solutions:**
1. Capture longer traffic windows (5+ minutes)
2. Verify Tor traffic detection: `python traffic_analysis/pcap_analyzer.py sample.pcap`
3. Retrain models: `python scripts/combine_and_train.py`

### Issue: Out of Memory

**Error:** `MemoryError` during batch analysis

**Solution:**
```bash
# Process one PCAP at a time
python batch_analyzer.py --single-threaded

# Or reduce sampling
export SAMPLE_RATE=0.05  # 5% sampling
python batch_analyzer.py
```

---

## Performance Optimization

### For Faster Analysis

1. **Use GPU acceleration:**
   ```bash
   # Verify GPU availability
   python -c "import torch; print(torch.cuda.is_available())"
   ```

2. **Reduce packet sampling:**
   ```python
   # In batch_analyzer.py, set SAMPLE_RATE=0.1 (10%)
   ```

3. **Increase parallelism:**
   ```python
   # In batch_analyzer.py, increase WORKER_THREADS
   WORKER_THREADS = 4  # Default 2
   ```

### For Lower Memory Usage

```bash
# Stream PCAP processing (vs. loading all)
python batch_analyzer.py --stream-mode
```

---

## Integration with External Tools

### Send Results to SIEM

```bash
# Example: Forward alerts to syslog
python batch_analyzer.py | logger -t BIMBO
```

### REST API Integration

```bash
# Start Flask app with API endpoints
python visualization/dashboard.py

# POST PCAP for analysis
curl -X POST -F "file=@capture.pcap" http://localhost:5000/batch_upload
```

### Export to Splunk

```python
# Custom Splunk forwarder (in batch_analyzer.py)
import requests
requests.post("https://splunk-instance:8088/services/collector",
              json={"event": analysis_result})
```

---

## Advanced Usage

### Custom Analysis Pipeline

Create `custom_analysis.py`:

```python
from batch_analyzer import batch_analyze_pcap
from ml_models.gnn_guard_predictor import GNNPredictor
from correlation.timing_correlator import TimingCorrelator

# Load your PCAP
flows = extract_flows("your_traffic.pcap")

# Run custom pipeline
timing = TimingCorrelator(flows).correlate()
gnn = GNNPredictor(flows).predict()

# Combine results
results = {
    'timing_confidence': timing,
    'gnn_confidence': gnn,
}

print(results)
```

### Batch Processing Script

```bash
#!/bin/bash
# Process all PCAPs in a directory

for pcap in data/pcap_files/*.pcap; do
    echo "Processing: $pcap"
    python batch_analyzer.py "$pcap"
done

# Generate combined report
python report_generator.py data/batch_results/
```

---

## Testing

### Run Unit Tests

```bash
python -m pytest tests/ -v
```

### Test Individual Components

```bash
# Test traffic analyzer
python tests/feature_list.py data/pcap_files/sample.pcap

# Test model evaluation
python tests/evaluate_model.py

# Test system
python test_system.py
```

---

## Documentation Files

- **[README.md](README.md)** — Project overview
- **[system archicture.md](system%20archicture.md)** — Architecture details
- **[techstack.md](techstack.md)** — Technology stack
- **[workflow.md](workflow.md)** — Operational workflow
- **[gapidentification.md](gapidentification.md)** — Known limitations
- **[expectedoutcomes.md](expectedoutcomes.md)** — Performance metrics

---

## Quick Reference Commands

```bash
# Quick demo
python demo_prototype.py

# Batch analysis
python batch_analyzer.py

# Live monitoring
sudo python live_monitor.py

# Web dashboard
python visualization/dashboard.py

# View help
python batch_analyzer.py --help

# Test installation
python test_system.py

# Clean outputs
rm -rf data/batch_results/*.json data/batch_results/*.csv
```

---

## Support & Troubleshooting

**For issues:**
1. Check error messages in terminal
2. Review log files in `data/batch_results/`
3. Run `test_system.py` for diagnostics
4. Verify dependencies: `pip list`
5. Check Python version: `python --version`

**Common issues:**
- Missing PCAP files → Add to `data/pcap_files/`
- Database errors → Run `scripts/download_tor_consensus.py`
- Model errors → Retrain with `scripts/combine_and_train.py`

---

**Last Updated:** December 2025

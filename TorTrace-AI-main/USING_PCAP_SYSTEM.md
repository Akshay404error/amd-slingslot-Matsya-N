# USING YOUR RUNNING PCAP SYSTEM - QUICK GUIDE

## 🎯 What's Running Right Now

✅ **Flask Web Server** - http://127.0.0.1:5001 (LIVE)  
✅ **Analysis Engine** - Ready to process PCAP files  
✅ **Database** - 9,196 Tor relays loaded  
✅ **Browser Interface** - Open and ready for uploads  

---

## 3 WAYS TO USE IT RIGHT NOW

### 1️⃣ DRAG & DROP IN BROWSER (EASIEST)

The web interface is already open in your browser.

**What to do:**
1. Open http://127.0.0.1:5001 in your browser
2. Find a PCAP file (examples in `data/pcap_files/`)
3. Drag it onto the upload area OR click "Select File"
4. Wait for analysis to complete
5. See results appear instantly!

**Expected Results:**
- Packets analyzed
- Network flows detected
- Tor indicators found
- Confidence score (0-100%)
- Results saved automatically

---

### 2️⃣ PYTHON CODE (FOR YOUR SCRIPTS)

Use this in your batch_analyzer.py, dashboard.py, or any Python script:

```python
from pcap_upload_handler import PCAPAnalysisHandler

# Initialize once
handler = PCAPAnalysisHandler()

# Analyze a PCAP file
result = handler.analyze_uploaded_pcap("file.pcap", "file.pcap")

# Check the results
print(f"Packets: {result['total_packets']}")
print(f"Tor Indicators: {result['potential_tor_flows']}")
print(f"Confidence: {result['confidence_average']*100:.1f}%")

# Results automatically saved to data/batch_results/
```

**Complete Example - Batch Process Multiple Files:**

```python
from pathlib import Path
from pcap_upload_handler import PCAPAnalysisHandler

handler = PCAPAnalysisHandler()

for pcap_file in Path("data/pcap_files").glob("*.pcap"):
    print(f"Analyzing {pcap_file.name}...")
    
    result = handler.analyze_uploaded_pcap(str(pcap_file), pcap_file.name)
    
    if result['success']:
        print(f"  ✓ {result['confidence_average']*100:.1f}% confidence")
        print(f"  ✓ {result['potential_tor_flows']} Tor indicators")
    else:
        print(f"  ✗ Error: {result['error']}")
```

---

### 3️⃣ HTTP REQUEST (FOR REMOTE SYSTEMS)

If you have another application or machine that needs to upload:

```bash
# Using curl
curl -F "file=@myfile.pcap" http://127.0.0.1:5001/upload_pcap

# Using Python requests
import requests

with open('myfile.pcap', 'rb') as f:
    files = {'file': (f.name, f)}
    response = requests.post('http://127.0.0.1:5001/upload_pcap', files=files)
    result = response.json()
    print(result)
```

---

## UNDERSTANDING THE RESULTS

When you analyze a PCAP, you get:

```json
{
  "filename": "live_20251109_200456.pcap",
  "total_packets": 318,
  "tcp_flows": 4,
  "potential_tor_flows": 1,
  "confidence_average": 0.85,
  "tor_ports_detected": ["443"],
  "flows": [...]
}
```

**What Each Field Means:**

- **filename** - Name of the PCAP file analyzed
- **total_packets** - Total packets in the PCAP
- **tcp_flows** - Network connections detected
- **potential_tor_flows** - How many flows look like Tor
- **confidence_average** - Confidence score (0.0 to 1.0)
- **tor_ports_detected** - Which Tor ports were seen
- **flows** - Detailed info about each network connection

---

## CHECK YOUR RESULTS

**Where are results saved?**
```
data/batch_results/pcap_analysis_*.json
```

**List all results:**
```bash
ls -la data/batch_results/pcap_analysis_*.json
```

**View a specific result:**
```bash
cat data/batch_results/pcap_analysis_live_20251109_200456_20251222_110543.json
```

**View analysis history in Python:**
```python
from pcap_upload_handler import PCAPAnalysisHandler

handler = PCAPAnalysisHandler()
history = handler.list_results()

for analysis in history:
    print(f"{analysis['pcap_file']}: {analysis['packets']} packets")
```

---

## EXAMPLES: REAL-WORLD USE

### Use Case 1: Check if a PCAP has Tor activity

```python
from pcap_upload_handler import PCAPAnalysisHandler

handler = PCAPAnalysisHandler()
result = handler.analyze_uploaded_pcap("suspect.pcap", "suspect.pcap")

if result['potential_tor_flows'] > 0:
    print(f"ALERT: Found {result['potential_tor_flows']} Tor flows!")
    print(f"Confidence: {result['confidence_average']*100:.1f}%")
else:
    print("No Tor activity detected")
```

### Use Case 2: Analyze all PCAPs in a directory

```python
from pathlib import Path
from pcap_upload_handler import PCAPAnalysisHandler

handler = PCAPAnalysisHandler()
results_summary = []

for pcap_file in Path("network_traffic").glob("*.pcap"):
    result = handler.analyze_uploaded_pcap(str(pcap_file), pcap_file.name)
    
    results_summary.append({
        'file': pcap_file.name,
        'confidence': result['confidence_average'],
        'tor_flows': result['potential_tor_flows']
    })

# Print summary
for r in sorted(results_summary, key=lambda x: x['confidence'], reverse=True):
    print(f"{r['file']:40} {r['confidence']*100:5.1f}% confidence")
```

### Use Case 3: Generate a forensic report

```python
import json
from pathlib import Path
from pcap_upload_handler import PCAPAnalysisHandler

handler = PCAPAnalysisHandler()
result = handler.analyze_uploaded_pcap("evidence.pcap", "evidence.pcap")

# Create forensic report
report = {
    'analysis_date': '2025-12-22',
    'file': result['filename'],
    'packets_analyzed': result['total_packets'],
    'network_flows': result['tcp_flows'],
    'tor_indicators': result['potential_tor_flows'],
    'confidence_score': f"{result['confidence_average']*100:.1f}%",
    'conclusion': 'POTENTIAL TOR USAGE' if result['potential_tor_flows'] > 0 else 'NO TOR DETECTED'
}

# Save report
with open('forensic_report.json', 'w') as f:
    json.dump(report, f, indent=2)

print("Report saved to forensic_report.json")
```

---

## TROUBLESHOOTING

### "Server not responding"
```bash
# Restart the server
python pcap_upload_app.py
```

### "File won't upload"
- Make sure file is a valid PCAP (.pcap or .pcapng)
- File size should be reasonable (< 1 GB)
- Check file permissions

### "No results saving"
Create the directory:
```bash
mkdir -p data/batch_results
```

### "Import error - pcap_upload_handler not found"
Make sure you're in the right directory:
```bash
cd c:\Users\DHANARAJ\Downloads\TorTrace-AI-main\TorTrace-AI-main
python your_script.py
```

### "Database error"
The database should load automatically. If not:
```bash
python -c "from pcap_upload_handler import PCAPAnalysisHandler; print('OK')"
```

---

## QUICK COMMANDS

### Run the demo again
```bash
python demo_pcap_system.py
```

### Check if server is running
```bash
netstat -ano | findstr 5001
```

### Restart the server
```bash
# Kill current process and restart
python pcap_upload_app.py
```

### View recent results
```bash
dir /b /o-d data\batch_results\pcap_analysis_*.json | head
```

---

## INTEGRATION CHECKLIST

- [ ] Web server is running (`python pcap_upload_app.py`)
- [ ] Browser shows http://127.0.0.1:5001
- [ ] Demo script passes (`python demo_pcap_system.py`)
- [ ] Results save to `data/batch_results/`
- [ ] Can import handler in Python
- [ ] Ready to integrate into your code

---

## NEXT STEPS

1. **Try uploading a file** - Use the browser interface
2. **Check the results** - Look in `data/batch_results/`
3. **Integrate into your code** - Use the Python API examples
4. **Batch process files** - Automate PCAP analysis

---

## DOCUMENTATION

- **Quick Start:** `QUICK_START_PCAP.md`
- **Full Guide:** `PCAP_ANALYSIS_COMPLETE.md`
- **Status Report:** `STATUS_REPORT_PCAP.md`
- **This Guide:** `USING_PCAP_SYSTEM.md`

---

## KEY CONTACTS/REFERENCES

**Handler API:** [pcap_upload_handler.py](pcap_upload_handler.py)
- All methods documented with docstrings
- Example usage in each function

**Web Interface:** [pcap_upload_app.py](pcap_upload_app.py)
- Running on http://127.0.0.1:5001
- HTML interface for drag-drop uploads

**Demo:** [demo_pcap_system.py](demo_pcap_system.py)
- Shows complete workflow
- Verification and testing

---

## SUMMARY

Your PCAP upload and analysis system is **fully operational and ready to use**.

**Right now you can:**
✅ Upload files via web browser (drag-drop)
✅ Analyze files via Python code
✅ Get Tor confidence scores
✅ Save results as JSON
✅ Track analysis history
✅ Batch process multiple files

**The system is RUNNING and waiting for you to use it!** 🚀

Pick one of the 3 methods above and start analyzing PCAP files immediately.

---

**Last Updated:** 2025-12-22 11:08 AM  
**Status:** ✅ OPERATIONAL AND READY

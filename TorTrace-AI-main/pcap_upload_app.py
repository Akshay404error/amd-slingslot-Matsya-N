#!/usr/bin/env python3
"""
BIMBO Web Dashboard with PCAP Upload
Flask app with file upload and analysis
"""

from flask import Flask, render_template_string, request, jsonify, send_file
from werkzeug.utils import secure_filename
import os
from pathlib import Path
from datetime import datetime
import json
from io import BytesIO

from pcap_upload_handler import PCAPAnalysisHandler

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB max
app.config['UPLOAD_FOLDER'] = 'data/pcap_files'
ALLOWED_EXTENSIONS = {'pcap', 'pcapng'}

handler = PCAPAnalysisHandler()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# HTML Template
DASHBOARD_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>BIMBO - PCAP Upload & Analysis</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
            color: #fff;
            min-height: 100vh;
            padding: 20px;
        }
        .container { max-width: 1200px; margin: 0 auto; }
        header {
            text-align: center;
            margin-bottom: 40px;
            border-bottom: 2px solid #00d4ff;
            padding-bottom: 20px;
        }
        h1 { color: #00d4ff; font-size: 2.5em; margin-bottom: 10px; }
        .subtitle { color: #8ba4c7; font-size: 1.1em; }
        
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 30px; }
        @media (max-width: 768px) { .grid { grid-template-columns: 1fr; } }
        
        .card {
            background: rgba(20, 25, 40, 0.8);
            border: 1px solid #00d4ff;
            border-radius: 10px;
            padding: 25px;
            backdrop-filter: blur(10px);
        }
        
        .card h2 { color: #00d4ff; margin-bottom: 15px; }
        
        .upload-area {
            border: 2px dashed #00d4ff;
            border-radius: 8px;
            padding: 30px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
        }
        .upload-area:hover {
            background: rgba(0, 212, 255, 0.1);
            border-color: #00ff88;
        }
        .upload-area.dragover {
            background: rgba(0, 212, 255, 0.2);
            border-color: #00ff88;
        }
        
        input[type="file"] { display: none; }
        
        button {
            background: #00d4ff;
            color: #000;
            border: none;
            padding: 12px 24px;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s;
            margin-top: 15px;
        }
        button:hover { background: #00ff88; transform: scale(1.05); }
        button:active { transform: scale(0.95); }
        
        .status {
            margin-top: 20px;
            padding: 15px;
            border-radius: 5px;
            display: none;
        }
        .status.success {
            background: rgba(0, 136, 0, 0.3);
            border: 1px solid #00ff88;
            color: #00ff88;
        }
        .status.error {
            background: rgba(136, 0, 0, 0.3);
            border: 1px solid #ff6b6b;
            color: #ff6b6b;
        }
        .status.loading {
            background: rgba(0, 100, 136, 0.3);
            border: 1px solid #00d4ff;
            color: #00d4ff;
        }
        
        .results-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        .results-table th {
            background: rgba(0, 212, 255, 0.2);
            padding: 12px;
            text-align: left;
            border-bottom: 2px solid #00d4ff;
        }
        .results-table td {
            padding: 12px;
            border-bottom: 1px solid #00d4ff;
        }
        .results-table tr:hover {
            background: rgba(0, 212, 255, 0.1);
        }
        
        .metric {
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px solid rgba(0, 212, 255, 0.2);
        }
        .metric:last-child { border-bottom: none; }
        .metric-value { color: #00ff88; font-weight: bold; }
        
        .progress { background: #0a0e27; height: 20px; border-radius: 10px; overflow: hidden; }
        .progress-bar {
            background: linear-gradient(90deg, #00d4ff, #00ff88);
            height: 100%;
            width: 0%;
            transition: width 0.3s;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🔍 BIMBO PCAP Analyzer</h1>
            <p class="subtitle">Upload and analyze network traffic for Tor attribution</p>
        </header>
        
        <div class="grid">
            <!-- Upload Section -->
            <div class="card">
                <h2>📤 Upload PCAP File</h2>
                <div class="upload-area" id="uploadArea">
                    <p>📁 Drag & drop PCAP file here</p>
                    <p style="font-size: 0.9em; color: #8ba4c7; margin-top: 10px;">or click to browse</p>
                    <input type="file" id="fileInput" accept=".pcap,.pcapng">
                </div>
                <button onclick="document.getElementById('fileInput').click()">Select File</button>
                <div id="uploadStatus" class="status"></div>
            </div>
            
            <!-- Analysis Results -->
            <div class="card">
                <h2>📊 Latest Analysis</h2>
                <div id="analysisResults">
                    <p style="color: #8ba4c7;">No analysis yet. Upload a PCAP file to start.</p>
                </div>
            </div>
        </div>
        
        <!-- Previous Results -->
        <div class="card">
            <h2>📋 Analysis History</h2>
            <table class="results-table" id="resultsTable">
                <thead>
                    <tr>
                        <th>PCAP File</th>
                        <th>Packets</th>
                        <th>Timestamp</th>
                        <th>Download Report</th>
                    </tr>
                </thead>
                <tbody id="resultsBody"></tbody>
            </table>
        </div>
    </div>
                    <tr>
                        <th>PCAP File</th>
                        <th>Packets</th>
                        <th>Timestamp</th>
                    </tr>
                </thead>
                <tbody id="resultsBody">
                </tbody>
            </table>
        </div>
    </div>

    <script>
        const uploadArea = document.getElementById('uploadArea');
        const fileInput = document.getElementById('fileInput');
        const uploadStatus = document.getElementById('uploadStatus');
        
        // Drag & drop
        uploadArea.addEventListener('dragover', e => {
            e.preventDefault();
            uploadArea.classList.add('dragover');
        });
        
        uploadArea.addEventListener('dragleave', () => {
            uploadArea.classList.remove('dragover');
        });
        
        uploadArea.addEventListener('drop', e => {
            e.preventDefault();
            uploadArea.classList.remove('dragover');
            fileInput.files = e.dataTransfer.files;
            uploadFile();
        });
        
        uploadArea.addEventListener('click', () => fileInput.click());
        fileInput.addEventListener('change', uploadFile);
        
        function uploadFile() {
            const file = fileInput.files[0];
            if (!file) return;
            
            if (!file.name.endsWith('.pcap') && !file.name.endsWith('.pcapng')) {
                showStatus('Please select a valid PCAP file', 'error');
                return;
            }
            
            const formData = new FormData();
            formData.append('file', file);
            
            showStatus('Analyzing PCAP file...', 'loading');
            
            fetch('/upload_pcap', {
                method: 'POST',
                body: formData
            })
            .then(r => r.json())
            .then(data => {
                if (data.success) {
                    showStatus(`✓ Analysis complete! Found ${data.tcp_flows} TCP flows`, 'success');
                    displayResults(data);
                    loadHistory();
                } else {
                    showStatus(`✗ Error: ${data.error}`, 'error');
                }
            })
            .catch(e => showStatus(`✗ Upload failed: ${e.message}`, 'error'));
        }
        
        function showStatus(msg, type) {
            uploadStatus.textContent = msg;
            uploadStatus.className = `status ${type}`;
            uploadStatus.style.display = 'block';
        }
        
        function displayResults(data) {
            const results = `
                <div class="metric">
                    <span>Total Packets</span>
                    <span class="metric-value">${data.total_packets}</span>
                </div>
                <div class="metric">
                    <span>TCP Flows</span>
                    <span class="metric-value">${data.tcp_flows}</span>
                </div>
                <div class="metric">
                    <span>Potential Tor Indicators</span>
                    <span class="metric-value">${data.potential_tor_flows}</span>
                </div>
                <div class="metric">
                    <span>Confidence Score</span>
                    <span class="metric-value">${(data.confidence_average * 100).toFixed(1)}%</span>
                </div>
                <div style="margin-top: 15px;">
                    <p style="color: #8ba4c7; font-size: 0.9em;">Analysis complete. Results saved.</p>
                </div>
            `;
            document.getElementById('analysisResults').innerHTML = results;
        }
        
        function loadHistory() {
            fetch('/analysis_history')
            .then(r => r.json())
            .then(results => {
                const tbody = document.getElementById('resultsBody');
                tbody.innerHTML = '';
                results.forEach(r => {
                    const row = `<tr>
                        <td>${r.pcap_file}</td>
                        <td>${r.packets}</td>
                        <td>${new Date(r.timestamp).toLocaleString()}</td>
                        <td><button onclick="downloadReport('${r.filename}')" style="background: #00d4ff; color: #0a0e27; padding: 5px 12px; border: none; border-radius: 4px; cursor: pointer; font-weight: bold;">📥 Download</button></td>
                    </tr>`;
                    tbody.innerHTML += row;
                });
            });
        }
        
        function downloadReport(filename) {
            window.location.href = `/download_report/${filename}`;
        }
        
        // Load history on page load
        loadHistory();
    </script>
</body>
</html>
"""

@app.route('/')
def dashboard():
    """Main dashboard"""
    return render_template_string(DASHBOARD_HTML)

@app.route('/upload_pcap', methods=['POST'])
def upload_pcap():
    """Handle PCAP file upload and analysis"""
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'No file provided'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No file selected'})
    
    if not allowed_file(file.filename):
        return jsonify({'success': False, 'error': 'Invalid file type. Use .pcap or .pcapng'})
    
    # Save file
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    Path(app.config['UPLOAD_FOLDER']).mkdir(parents=True, exist_ok=True)
    file.save(filepath)
    
    # Analyze
    result = handler.analyze_uploaded_pcap(filepath, filename)
    return jsonify(result)

@app.route('/analysis_history')
def analysis_history():
    """Get analysis history"""
    return jsonify(handler.list_results())

@app.route('/health')
def health():
    """Health check"""
    return jsonify({'status': 'ok', 'service': 'BIMBO PCAP Analyzer'})

@app.route('/download_report/<analysis_file>')
def download_report(analysis_file):
    """Download forensic report for an analysis"""
    try:
        results_dir = Path('data/batch_results')
        json_file = results_dir / analysis_file
        
        if not json_file.exists() or not analysis_file.startswith('pcap_analysis_'):
            return jsonify({'success': False, 'error': 'Analysis file not found'}), 404
        
        # Load analysis data
        with open(json_file) as f:
            analysis_data = json.load(f)
        
        # Generate forensic report
        html_report = handler.generate_forensic_report(analysis_data)
        
        # Create filename for download
        pcap_name = analysis_data.get('filename', 'report').rsplit('.', 1)[0]
        report_filename = f"forensic_report_{pcap_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        
        # Return HTML file for download
        return send_file(
            BytesIO(html_report.encode('utf-8')),
            mimetype='text/html',
            as_attachment=True,
            download_name=report_filename
        )
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    print("=" * 70)
    print("BIMBO PCAP Upload & Analysis Server")
    print("=" * 70)
    print("\n🌐 Open: http://127.0.0.1:5001")
    print("📤 Upload and analyze PCAP files")
    print("\nPress CTRL+C to stop\n")
    print("=" * 70)
    
    app.run(host='0.0.0.0', port=5001, debug=False)

# File Tree: TorTrace-AI-main

**Generated:** 2/27/2026, 9:52:39 AM
**Root Path:** `c:\AMD slingslot\TorTrace-AI-main`

```
├── 📁 .claude
│   └── ⚙️ settings.json
├── 📁 .netlify
│   ├── 📁 functions-internal
│   ├── 📁 v1
│   │   └── 📁 functions
│   ├── ⚙️ netlify.toml
│   └── ⚙️ state.json
├── 📁 correlation
│   └── 🐍 timing_correlator.py
├── 📁 data
│   ├── 📁 batch_results
│   │   ├── 📄 Scenario-A-merged_5s.csv
│   │   ├── 📄 Scenario-B-merged_5s.csv
│   │   ├── 📄 all_tor_non_tor_combined.csv
│   │   ├── 📄 batch_prediction_20251115_024907.csv
│   │   ├── 📄 batch_prediction_20251115_025515.csv
│   │   ├── 📄 batch_prediction_20251115_030906.csv
│   │   ├── 📄 batch_prediction_20251115_163548.csv
│   │   ├── 📄 batch_prediction_20251115_165728.csv
│   │   ├── 📄 batch_prediction_20251115_171009.csv
│   │   ├── 📄 batch_prediction_20251115_171144.csv
│   │   ├── 📄 batch_prediction_20251115_171215.csv
│   │   ├── 📄 batch_prediction_20251115_171433.csv
│   │   ├── 📄 batch_summary.csv
│   │   ├── 📄 best_features.txt
│   │   ├── 📄 combined_features.csv
│   │   ├── 📄 combined_features_clean.csv
│   │   ├── 📄 combined_features_final.csv
│   │   ├── 🌐 dashboard.html
│   │   ├── ⚙️ evaluation_results.json
│   │   ├── 🖼️ feature_importances.png
│   │   ├── 🌐 forensic_report.html
│   │   ├── ⚙️ forensic_report.json
│   │   ├── 📄 forensic_summary.csv
│   │   ├── ⚙️ live_20251109_200038_analysis.json
│   │   ├── ⚙️ live_20251109_200145_analysis.json
│   │   ├── ⚙️ live_20251109_200251_analysis.json
│   │   ├── ⚙️ live_20251109_200350_analysis.json
│   │   ├── ⚙️ live_20251109_200456_analysis.json
│   │   ├── ⚙️ live_20251109_201028_analysis.json
│   │   ├── ⚙️ live_20251109_201240_analysis.json
│   │   ├── ⚙️ live_20251109_202006_analysis.json
│   │   ├── 📄 live_20251109_202006_features.csv
│   │   ├── ⚙️ live_20251109_202006_fingerprint.json
│   │   ├── ⚙️ live_20251109_202006_gnn.json
│   │   ├── ⚙️ live_20251109_202113_analysis.json
│   │   ├── 📄 live_20251109_202113_features.csv
│   │   ├── ⚙️ live_20251109_202113_fingerprint.json
│   │   ├── ⚙️ live_20251109_202113_gnn.json
│   │   ├── ⚙️ live_20251109_202230_analysis.json
│   │   ├── 📄 live_20251109_202230_features.csv
│   │   ├── ⚙️ live_20251109_202230_fingerprint.json
│   │   ├── ⚙️ live_20251109_202230_gnn.json
│   │   ├── ⚙️ live_20251109_202411_analysis.json
│   │   ├── ⚙️ live_20251109_202738_analysis.json
│   │   ├── ⚙️ live_20251109_203154_analysis.json
│   │   ├── ⚙️ live_20251109_203652_analysis.json
│   │   ├── ⚙️ live_20251109_205542_analysis.json
│   │   ├── ⚙️ live_20251109_211050_analysis.json
│   │   ├── ⚙️ live_20251109_212532_analysis.json
│   │   ├── ⚙️ live_20251109_213053_analysis.json
│   │   ├── ⚙️ live_20251109_213501_analysis.json
│   │   ├── 📄 live_20251109_213501_features.csv
│   │   ├── ⚙️ live_20251109_213501_fingerprint.json
│   │   ├── ⚙️ live_20251109_213501_gnn.json
│   │   ├── ⚙️ live_20251109_213816_analysis.json
│   │   ├── ⚙️ live_20251113_231338_analysis.json
│   │   ├── ⚙️ live_20251113_233836_analysis.json
│   │   ├── ⚙️ live_20251113_235058_analysis.json
│   │   ├── ⚙️ live_20251113_235427_analysis.json
│   │   ├── ⚙️ live_20251113_235913_analysis.json
│   │   ├── ⚙️ live_20251114_000130_analysis.json
│   │   ├── 📄 model_comparison.csv
│   │   ├── ⚙️ model_features.json
│   │   ├── ⚙️ non_tor_20251116_014311_analysis.json
│   │   ├── 📄 non_tor_20251116_014311_features.csv
│   │   ├── ⚙️ non_tor_20251116_014414_analysis.json
│   │   ├── 📄 non_tor_20251116_014414_features.csv
│   │   ├── ⚙️ non_tor_20251116_031104_analysis.json
│   │   ├── 📄 non_tor_20251116_031104_features.csv
│   │   ├── ⚙️ pcap_analysis_live_20251109_200038_20251222_105505.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200038_20251222_110151.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200038_20251222_110447.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200038_20251222_110543.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200038_20251222_111535.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200038_20251222_111742.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200038_20251222_112749.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200145_20251222_105505.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200145_20251222_110151.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200145_20251222_110447.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200145_20251222_110543.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200145_20251222_111535.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200145_20251222_111742.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200145_20251222_112752.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200251_20251222_105506.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200251_20251222_110151.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200251_20251222_110447.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200251_20251222_110543.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200251_20251222_111536.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200251_20251222_111742.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200251_20251222_112754.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200350_20251222_105506.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200350_20251222_110151.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200350_20251222_110447.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200350_20251222_110543.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200350_20251222_111536.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200350_20251222_111742.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200350_20251222_112756.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200456_20251222_105506.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200456_20251222_110151.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200456_20251222_110447.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200456_20251222_110543.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200456_20251222_111536.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200456_20251222_111742.json
│   │   ├── ⚙️ pcap_analysis_live_20251109_200456_20251222_112758.json
│   │   ├── ⚙️ pcap_analysis_sample_20260227_090836.json
│   │   ├── ⚙️ pcap_analysis_sample_20260227_090841.json
│   │   ├── ⚙️ pcap_analysis_sample_20260227_091101.json
│   │   ├── ⚙️ pcap_analysis_sample_20260227_091455.json
│   │   ├── ⚙️ pcap_analysis_sample_20260227_091556.json
│   │   ├── ⚙️ pcap_analysis_sample_20260227_092710.json
│   │   ├── ⚙️ pcap_analysis_sample_traffic_20251222_110617.json
│   │   ├── ⚙️ pcap_analysis_sample_traffic_20251222_111855.json
│   │   ├── ⚙️ pcap_analysis_sample_traffic_20251222_112505.json
│   │   ├── ⚙️ pcap_analysis_sample_traffic_20251222_112943.json
│   │   ├── ⚙️ real_capture_analysis.json
│   │   ├── 📄 real_capture_features.csv
│   │   ├── ⚙️ real_capture_fingerprint.json
│   │   ├── ⚙️ real_capture_gnn.json
│   │   ├── 🖼️ roc_DecisionTree.png
│   │   ├── 🖼️ roc_RF_Top10.png
│   │   ├── 🖼️ roc_RandomForest.png
│   │   ├── 🖼️ roc_Stacking_Ensemble.png
│   │   ├── 🖼️ roc_Voting_Ensemble.png
│   │   ├── 🖼️ roc_XGBoost_Advanced.png
│   │   ├── 🖼️ roc_XGBoost_Base.png
│   │   ├── ⚙️ sample_analysis.json
│   │   ├── 📄 sample_features.csv
│   │   ├── ⚙️ sample_fingerprint.json
│   │   ├── ⚙️ sample_gnn.json
│   │   ├── 📄 scenario_A_cleaned.csv
│   │   ├── 📄 test_features.csv
│   │   ├── ⚙️ topology_mapping.json
│   │   ├── ⚙️ tor_20251116_015658_analysis.json
│   │   ├── ⚙️ tor_20251116_015716_analysis.json
│   │   ├── ⚙️ tor_20251116_021106_analysis.json
│   │   ├── 📄 tor_detection_model.pkl
│   │   ├── 📄 tor_nontor_features.csv
│   │   ├── 📄 tor_nontor_merged_features.csv
│   │   └── 📄 training_dataset.csv
│   ├── 📁 new_traffic
│   │   ├── 📄 new_data.csv
│   │   └── 📄 predictions.csv
│   ├── 📁 pcap_files
│   │   ├── 📄 live_20251109_200038.pcap
│   │   ├── 📄 live_20251109_200145.pcap
│   │   ├── 📄 live_20251109_200251.pcap
│   │   ├── 📄 live_20251109_200350.pcap
│   │   ├── 📄 live_20251109_200456.pcap
│   │   ├── 📄 live_20251109_201028.pcap
│   │   ├── 📄 live_20251109_201240.pcap
│   │   ├── 📄 live_20251109_202006.pcap
│   │   ├── 📄 live_20251109_202113.pcap
│   │   ├── 📄 live_20251109_202230.pcap
│   │   ├── 📄 live_20251109_202411.pcap
│   │   ├── 📄 live_20251109_202738.pcap
│   │   ├── 📄 live_20251109_203154.pcap
│   │   ├── 📄 live_20251109_203652.pcap
│   │   ├── 📄 live_20251109_205542.pcap
│   │   ├── 📄 live_20251109_211050.pcap
│   │   ├── 📄 live_20251109_212532.pcap
│   │   ├── 📄 live_20251109_213053.pcap
│   │   ├── 📄 live_20251109_213501.pcap
│   │   ├── 📄 live_20251109_213816.pcap
│   │   ├── 📄 live_20251113_231338.pcap
│   │   ├── 📄 live_20251113_233836.pcap
│   │   ├── 📄 live_20251113_235058.pcap
│   │   ├── 📄 live_20251113_235427.pcap
│   │   ├── 📄 live_20251113_235913.pcap
│   │   ├── 📄 live_20251114_000130.pcap
│   │   ├── 📄 non_tor_20251116_014311.pcap
│   │   ├── 📄 non_tor_20251116_014414.pcap
│   │   ├── 📄 non_tor_20251116_031104.pcap
│   │   ├── 📄 pcap_labels.csv
│   │   ├── 📄 real_capture.pcap
│   │   ├── 📄 sample.pcap
│   │   ├── 📄 sample.pcapng
│   │   ├── 📄 sample_traffic.pcap
│   │   ├── 📄 synthetic_tor_test.pcap
│   │   ├── 📄 tor_20251116_015658.pcap
│   │   ├── 📄 tor_20251116_015716.pcap
│   │   └── 📄 tor_20251116_021106.pcap
│   ├── 📁 reports
│   │   ├── 📕 TorTrace_Report_20251109_144200.pdf
│   │   └── 📕 TorTrace_Report_20251109_144947.pdf
│   ├── ⚙️ alert_log.json
│   ├── ⚙️ attribution_report.json
│   ├── ⚙️ geo_cache.json
│   ├── ⚙️ gnn_predictions.json
│   ├── ⚙️ perf_metrics.json
│   ├── ⚙️ test_fingerprint.json
│   ├── ⚙️ test_gnn.json
│   ├── ⚙️ test_set.json
│   ├── 📄 tor_relays.db
│   └── ⚙️ website_fingerprint_report.json
├── 📁 legacy
│   ├── 🐍 json_to_dataframe.py
│   ├── 🐍 merge_clean_tor_data.py
│   ├── 🐍 merge_with_labels.py
│   └── 🐍 predict.py
├── 📁 ml_models
│   ├── 🐍 gnn_guard_predictor.py
│   └── 🐍 website_fingerprinter.py
├── 📁 public
│   ├── 📄 Scenario-A-merged_5s.csv
│   ├── 📄 Scenario-B-merged_5s.csv
│   ├── 📄 all_tor_non_tor_combined.csv
│   ├── 📄 batch_prediction_20251115_024907.csv
│   ├── 📄 batch_prediction_20251115_025515.csv
│   ├── 📄 batch_prediction_20251115_030906.csv
│   ├── 📄 batch_prediction_20251115_163548.csv
│   ├── 📄 batch_prediction_20251115_165728.csv
│   ├── 📄 batch_prediction_20251115_171009.csv
│   ├── 📄 batch_prediction_20251115_171144.csv
│   ├── 📄 batch_prediction_20251115_171215.csv
│   ├── 📄 batch_prediction_20251115_171433.csv
│   ├── 📄 batch_summary.csv
│   ├── 📄 combined_features.csv
│   ├── 📄 combined_features_clean.csv
│   ├── 📄 combined_features_final.csv
│   ├── ⚙️ evaluation_results.json
│   ├── 🌐 forensic_report.html
│   ├── ⚙️ forensic_report.json
│   ├── 📄 forensic_summary.csv
│   ├── 🌐 index.html
│   ├── ⚙️ live_20251109_200038_analysis.json
│   ├── ⚙️ live_20251109_200145_analysis.json
│   ├── ⚙️ live_20251109_200251_analysis.json
│   ├── ⚙️ live_20251109_200350_analysis.json
│   ├── ⚙️ live_20251109_200456_analysis.json
│   ├── ⚙️ live_20251109_201028_analysis.json
│   ├── ⚙️ live_20251109_201240_analysis.json
│   ├── ⚙️ live_20251109_202006_analysis.json
│   ├── 📄 live_20251109_202006_features.csv
│   ├── ⚙️ live_20251109_202006_fingerprint.json
│   ├── ⚙️ live_20251109_202006_gnn.json
│   ├── ⚙️ live_20251109_202113_analysis.json
│   ├── 📄 live_20251109_202113_features.csv
│   ├── ⚙️ live_20251109_202113_fingerprint.json
│   ├── ⚙️ live_20251109_202113_gnn.json
│   ├── ⚙️ live_20251109_202230_analysis.json
│   ├── 📄 live_20251109_202230_features.csv
│   ├── ⚙️ live_20251109_202230_fingerprint.json
│   ├── ⚙️ live_20251109_202230_gnn.json
│   ├── ⚙️ live_20251109_202411_analysis.json
│   ├── ⚙️ live_20251109_202738_analysis.json
│   ├── ⚙️ live_20251109_203154_analysis.json
│   ├── ⚙️ live_20251109_203652_analysis.json
│   ├── ⚙️ live_20251109_205542_analysis.json
│   ├── ⚙️ live_20251109_211050_analysis.json
│   ├── ⚙️ live_20251109_212532_analysis.json
│   ├── ⚙️ live_20251109_213053_analysis.json
│   ├── ⚙️ live_20251109_213501_analysis.json
│   ├── 📄 live_20251109_213501_features.csv
│   ├── ⚙️ live_20251109_213501_fingerprint.json
│   ├── ⚙️ live_20251109_213501_gnn.json
│   ├── ⚙️ live_20251109_213816_analysis.json
│   ├── ⚙️ live_20251113_231338_analysis.json
│   ├── ⚙️ live_20251113_233836_analysis.json
│   ├── ⚙️ live_20251113_235058_analysis.json
│   ├── ⚙️ live_20251113_235427_analysis.json
│   ├── ⚙️ live_20251113_235913_analysis.json
│   ├── ⚙️ live_20251114_000130_analysis.json
│   ├── 📄 model_comparison.csv
│   ├── ⚙️ model_features.json
│   ├── ⚙️ non_tor_20251116_014311_analysis.json
│   ├── 📄 non_tor_20251116_014311_features.csv
│   ├── ⚙️ non_tor_20251116_014414_analysis.json
│   ├── 📄 non_tor_20251116_014414_features.csv
│   ├── ⚙️ non_tor_20251116_031104_analysis.json
│   ├── 📄 non_tor_20251116_031104_features.csv
│   ├── ⚙️ real_capture_analysis.json
│   ├── 📄 real_capture_features.csv
│   ├── ⚙️ real_capture_fingerprint.json
│   ├── ⚙️ real_capture_gnn.json
│   ├── ⚙️ sample_analysis.json
│   ├── 📄 sample_features.csv
│   ├── ⚙️ sample_fingerprint.json
│   ├── ⚙️ sample_gnn.json
│   ├── 📄 scenario_A_cleaned.csv
│   ├── 📄 test_features.csv
│   ├── ⚙️ topology_mapping.json
│   ├── ⚙️ tor_20251116_015658_analysis.json
│   ├── ⚙️ tor_20251116_015716_analysis.json
│   ├── ⚙️ tor_20251116_021106_analysis.json
│   ├── 📄 tor_nontor_features.csv
│   ├── 📄 tor_nontor_merged_features.csv
│   └── 📄 training_dataset.csv
├── 📁 scripts
│   ├── 🐍 batch_analyze.py
│   ├── 🐍 combine_and_train.py
│   └── 🐍 train_model.py
├── 📁 static
│   └── 📁 sounds
│       └── 🎵 notification.wav
├── 📁 tests
│   ├── 🐍 evaluate_model.py
│   └── 🐍 feature_list.py
├── 📁 traffic_analysis
│   └── 🐍 pcap_analyzer.py
├── 📁 utils
│   └── 🐍 geo_locator.py
├── ⚙️ .gitignore
├── 📝 FILE_INDEX.md
├── 📝 PCAP_UPLOAD_SOLUTION.md
├── 📝 PROTOTYPE_FINAL_DELIVERY.md
├── 📝 PROTOTYPE_IMPLEMENTATION_GUIDE.md
├── 📝 PROTOTYPE_QUICK_REFERENCE.md
├── 📝 QUICK_START_PCAP.md
├── 📝 README.md
├── 📝 README_PROTOTYPE.md
├── 📝 STATUS_REPORT_PCAP.md
├── 📝 USING_PCAP_SYSTEM.md
├── 🐍 add_labels.py
├── 🐍 batch_analyzer.py
├── 🐍 data_clean_and_save.py
├── 📝 expectedoutcomes.md
├── 📝 functionalrequriments.md
├── 📝 gapidentification.md
├── 📝 how_to_run_the_project.md
├── 🐍 live_monitor.py
├── ⚙️ netlify.toml
├── 📝 novality.md
├── 📄 output_results.csv
├── ⚙️ output_results.json
├── 🐍 pcap_upload_app.py
├── 🐍 pcap_upload_handler.py
├── 📝 question.md
├── 🐍 report_generator.py
├── 📄 requirements.txt
├── 📄 run.bat
├── 📝 system archicture.md
├── 📝 techstack.md
├── 📄 tor_detection_model.pkl
├── 📄 tor_detection_model_DT.pkl
├── 📄 tor_detection_model_RF.pkl
├── 📄 tor_detection_model_RF_TOP.pkl
├── 📄 tor_detection_model_STACKING.pkl
├── 📄 tor_detection_model_VOTING.pkl
├── 📄 tor_detection_model_XGB.pkl
├── 📄 tor_detection_model_XGB_ADVANCED.pkl
├── 🐍 unified_dashboard.py
└── 📝 workflow.md
```

---
*Generated by FileTree Pro Extension*
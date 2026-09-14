# 🧪 Pilot 100 — Phase Summary

A 100-video pilot run to validate the entire pipeline end-to-end before scaling to the full dataset: video collection → frame extraction → MediaPipe feature extraction → Label Studio annotation → dual-model training (XGBoost + Standard GNN).

---

## 🔁 Pipeline Flow

| Step | Notebook |
|---|---|
| 1️⃣ Video Collection | [`videos_import/videos_import.ipynb`](../videos_import/videos_import.ipynb) |
| 2️⃣ Frame Extraction | `notebooks/pilot_100_Frames_extraction.ipynb` |
| 3️⃣ Feature Extraction | `notebooks/feature_extraction_pilot_100.ipynb` |
| 4️⃣ EDA + Training | `notebooks/training-pilot-100.ipynb` |

---

## 📊 Results

| Model | MAE ⬇️ | RMSE ⬇️ | R² Score ⬆️ | Within ±1 point | Verdict |
|---|---|---|---|---|---|
| **XGBoost** (baseline) | 0.628 | 0.795 | **0.630** | **84.2%** | ✅ Best at this scale |
| **Standard GNN** (primary) | 0.727 | 0.880 | 0.038 | 66.7% | ⚠️ Needs more data |

---

## 🐛 Key Finding — Bug Fixed During EDA

A **blink-rate threshold calibration bug** was discovered and fixed:

- ❌ **Before:** fixed absolute threshold → some videos showed `blink_rate = 1.0` (impossible — "always blinking")
- ✅ **After:** normalized eye-openness by face width + recalibrated threshold from real data (10th percentile)
- 📉 **Result:** average blink_rate dropped from `0.195` → `0.042`, false anomalies eliminated (4 → 0)

---

## ✅ Conclusion

- The full pipeline runs **end-to-end without errors**
- **XGBoost** performs well even on this small pilot — a reliable baseline
- **Standard GNN** needs significantly more data — MAE/RMSE looked only slightly worse than XGBoost, but **R² revealed the real gap** (0.630 vs 0.038), showing GNN isn't yet learning meaningful patterns
- This **validates the dual-model strategy**: XGBoost as a dependable baseline, GNN as the primary model expected to improve substantially once trained on the full ~2000-video dataset

---

## 📁 Contents

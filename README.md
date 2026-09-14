# 🎯 AI-UGC Realism Detection

> An end-to-end ML pipeline that scores how human-realistic AI-generated and real UGC (User-Generated Content) videos look — combining MediaPipe landmark extraction with XGBoost and Graph Neural Network models.

---

## 📌 Overview

AI-generated video ads often look "almost real" but fall short on natural human motion — fixed eye gaze, robotic gestures, unnatural blinking. This project builds a **quality-intelligence layer** that evaluates any UGC-style video and predicts a human realism score, without needing to build another video-generation model.

---

## 🗂️ Repository Structure

| Folder | Description |
|---|---|
| 📁 `videos_import/` | Video collection scripts (Pixabay, Pexels, YouTube) + AI-generated video collection *(in progress)* |
| 📁 `pilot_100/` | 100-video pilot phase — notebooks, data, trained models, results |
| 📁 `reports/` | Project reports, technical documentation, execution guides |

---

## 🚦 Project Status

| Phase | Status |
|---|---|
| Pipeline design & proposal | ✅ Complete |
| Data collection (real videos) | ✅ Complete |
| Pilot 100 — pipeline validation | ✅ Complete |
| Full dataset scaling (1000 real + 1000 AI-generated) | 🔄 In progress |
| Production model training | ⏳ Planned |
| Product (web app) build | ⏳ Planned |

👉 See [`pilot_100/README.md`](./pilot_100/README.md) for full pilot results.

---

## 🧠 Tech Stack

| Category | Tools |
|---|---|
| 🎥 Video Processing | OpenCV, FFmpeg, yt-dlp |
| 🧍 Feature Extraction | MediaPipe (Face + Pose Landmarker) |
| 🤖 ML Models | XGBoost, PyTorch + PyTorch Geometric (GNN) |
| 🏷️ Annotation | Label Studio |
| 📊 Data Handling | Pandas, NumPy, Scikit-learn |
| 🔍 Explainability *(planned)* | SHAP |
| ✍️ Prompt Optimization *(planned)* | Open-source LLM (Llama / Mistral) |
| 🚀 Deployment *(planned)* | FastAPI + Streamlit / React |

---

## 📈 Pilot Results Snapshot

| Model | R² Score | Within ±1 point |
|---|---|---|
| XGBoost (baseline) | **0.630** | **84.2%** |
| Standard GNN (primary) | 0.038 | 66.7% |

*GNN underperforms at pilot scale (94 samples) — expected, and confirms the plan to scale to the full dataset before final evaluation.*

---

## 🔮 Roadmap

- [x] Pipeline validation (pilot 100)
- [ ] Scale to 1000 real + 1000 AI-generated videos
- [ ] Retrain XGBoost + GNN on full dataset
- [ ] Add SHAP-based defect explanation
- [ ] Add real vs AI-generated classification
- [ ] Add LLM-based prompt optimization
- [ ] Build and deploy product UI

---

*This is an ongoing ML project — structure and results will evolve as the dataset scales.*

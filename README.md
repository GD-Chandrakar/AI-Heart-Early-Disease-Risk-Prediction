# 🏥 AI-Heart-Early-Disease-Risk-Prediction Using Machine Learning

An intelligent healthcare prediction system that predicts heart disease risk using Machine Learning algorithms, FastAPI backend, React frontend, and interactive dashboard visualization.

# 🚀 Features

Heart attack and stroke risk prediction using multiple ML models (Logistic Regression, Random Forest, SVM, XGBoost)
Ensemble learning for enhanced accuracy
Interactive Streamlit dashboard for real-time predictions
Geospatial risk visualization using Folium
Feature importance analysis to explain model decisions
ROC curves and confusion matrix for performance evaluation

# 🧠 Machine Learning Models Used

- Logistic Regression: Simple and interpretable for baseline classification.
- Random Forest: Robust and handles nonlinearity well.
- SVM: Effective for high-dimensional data.
- XGBoost: High-performing boosting algorithm with regularization.
- Ensemble: Voting classifier combines strengths of all models for better generalization.


# 🏗️ System Architecture

```text
Frontend (React + Vite)
        ↓
FastAPI Backend
        ↓
Machine Learning Model (.pkl)
        ↓
Prediction Output
        ↓
Visualization Dashboard

📊 Dataset

Dataset Used:

UCI Heart Disease Dataset

Dataset contains:

Age
Cholesterol
Blood Pressure
Chest Pain Type
ECG Results
Maximum Heart Rate
Other clinical features

⚙️ Tech Stack
Frontend
React.js
Vite
CSS
Chart Libraries
Backend
FastAPI
Python
Machine Learning
Scikit-learn
XGBoost
Pandas
NumPy
Matplotlib
Seaborn

📈 Evaluation Metrics

The system evaluates model performance using:

Accuracy
Precision
Recall
F1 Score
ROC-AUC Curve
Confusion Matrix

📂 Project Structure
AI-Heart-Early-Disease-Risk-Prediction/
│
├── frontend/
├── backend/
├── dataset/
├── notebook/
├── screenshots/
├── README.md
├── requirements.txt
└── .gitignore

▶️ Installation & Setup
Clone Repository
git clone https://github.com/GD-Chandrakar/AI-Heart-Early-Disease-Risk-Prediction.git
Backend Setup
pip install -r requirements.txt
uvicorn main:app --reload
Frontend Setup
npm install
npm run dev

🌍 Future Scope
Real-time hospital integration
Mobile healthcare application
IoT wearable device integration
Deep Learning implementation
Multi-disease prediction system

📌 Research Contribution

This project combines:

Multiple Machine Learning models
Ensemble Learning
Visualization dashboards
GIS-based healthcare analytics

into a unified healthcare prediction system.

👨‍💻 Authors
Gagandeep Chandrakar
Team Members

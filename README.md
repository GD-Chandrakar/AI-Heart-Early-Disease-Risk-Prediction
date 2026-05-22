🏥 AI-Heart-Early-Disease-Risk-Prediction Using Machine Learning

An intelligent healthcare prediction system that predicts heart disease risk using Machine Learning algorithms and an interactive Streamlit dashboard for prediction and visualization.

Next Gen Project 


🚀 Features
Heart attack and stroke risk prediction using multiple ML models (Logistic Regression, Random Forest, SVM, XGBoost)
Ensemble learning for enhanced accuracy
Interactive Streamlit dashboard for real-time predictions
Geospatial risk visualization using Folium
Feature importance analysis to explain model decisions
ROC curves and confusion matrix for performance evaluation

🧠 Machine Learning Models Used
Logistic Regression: Simple and interpretable for baseline classification.
Random Forest: Robust and handles nonlinearity well.
SVM: Effective for high-dimensional data.
XGBoost: High-performing boosting algorithm with regularization.
Ensemble: Voting classifier combines strengths of all models for better generalization.


🏗️ System Architecture
Frontend (Streamlit Dashboard)
        ↓
Machine Learning Model
        ↓
Prediction Output
        ↓
Visualization (Plots, GIS)

📊 Dataset

Dataset Used:

UCI Heart Disease Dataset

Dataset contains:

- Age
- Cholesterol
- Blood Pressure
- Chest Pain Type
- ECG Results
- Maximum Heart Rate
- Other clinical features

⚙️ Tech Stack

- **Frontend**: Streamlit
- **Machine Learning**: scikit-learn, XGBoost, Pandas, NumPy, Matplotlib, Seaborn

📈 Evaluation Metrics

The system evaluates model performance using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Curve
- Confusion Matrix

📂 Project Structure


AI-Heart-Early-Disease-Risk-Prediction/
│
├── app.py
├── dataset/
├── notebook/
├── screenshots/
├── README.md
├── requirements.txt
└── .gitignore


▶️ Installation & Setup

1. Clone Repository
   ```bash
   git clone https://github.com/GD-Chandrakar/AI-Heart-Early-Disease-Risk-Prediction.git

Backend & Dashboard Setup

pip install -r requirements.txt
streamlit run app.py

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

...into a unified healthcare prediction system.

👨‍💻 Authors
Gagandeep Chandrakar
Akansh 
Palkin
Arnav

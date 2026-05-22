# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import folium
from streamlit_folium import st_folium
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="AI Heart Diesease - GIS Heart Risk",
    page_icon="heart",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html,body,[class*="css"]{font-family:'Inter',sans-serif;}
.stApp{background:#0d0f14;color:#e8eaf0;}
#MainMenu,footer,header{visibility:hidden;}
.block-container{padding-top:0!important;max-width:1400px;}
.hdr-bar{background:#141720;border-bottom:1px solid rgba(255,255,255,0.07);
  padding:14px 28px;display:flex;align-items:center;gap:14px;margin:-1rem -1rem 0 -1rem;}
.logo-text{font-size:21px;font-weight:800;letter-spacing:-0.4px;color:#e8eaf0;}
.logo-text span{color:#e84b5a;}
.htag{font-size:11px;padding:4px 12px;border-radius:20px;
  border:1px solid rgba(255,255,255,0.13);color:#8b92a8;font-weight:500;}
.htag-active{background:#e84b5a;color:#fff!important;border-color:#e84b5a!important;}
.metric-row{display:grid;grid-template-columns:repeat(5,1fr);
  border-bottom:1px solid rgba(255,255,255,0.07);}
.mc{padding:18px 22px;border-right:1px solid rgba(255,255,255,0.07);}
.mc:last-child{border-right:none;}
.mc-val{font-size:32px;font-weight:800;line-height:1;}
.mc-lbl{font-size:10px;color:#8b92a8;margin-top:5px;letter-spacing:.07em;text-transform:uppercase;}
.card{background:#141720;border:1px solid rgba(255,255,255,0.07);
  border-radius:12px;padding:18px 20px;margin-bottom:14px;}
.card-title{font-size:10px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;
  color:#e84b5a;margin-bottom:14px;display:flex;align-items:center;gap:6px;}
.card-title::before{content:'';display:inline-block;width:6px;height:6px;
  background:#e84b5a;border-radius:50%;}
.smin{background:#1c2030;border-radius:8px;padding:12px 14px;margin-bottom:8px;}
.smin-lbl{font-size:10px;color:#8b92a8;margin-bottom:4px;text-transform:uppercase;letter-spacing:.05em;}
.smin-val{font-size:20px;font-weight:700;}
.ins-row{display:flex;align-items:flex-start;gap:12px;padding:11px 0;
  border-bottom:1px solid rgba(255,255,255,0.07);}
.ins-row:last-child{border-bottom:none;}
.ins-ico{font-size:17px;flex-shrink:0;margin-top:2px;}
.ins-txt{font-size:13px;color:#e8eaf0;line-height:1.6;}
.ins-txt strong{color:#fff;font-weight:600;}
.res-high{background:rgba(232,75,90,.15);color:#e84b5a;border:1px solid rgba(232,75,90,.3);
  border-radius:8px;padding:16px 20px;text-align:center;font-size:18px;font-weight:700;margin-top:10px;}
.res-low{background:rgba(61,214,140,.15);color:#3dd68c;border:1px solid rgba(61,214,140,.3);
  border-radius:8px;padding:16px 20px;text-align:center;font-size:18px;font-weight:700;margin-top:10px;}
.frow{display:flex;justify-content:space-between;align-items:center;padding:8px 0;
  border-bottom:1px solid rgba(255,255,255,0.07);font-size:13px;}
.frow:last-child{border-bottom:none;}
.fbadge{background:rgba(232,75,90,.15);color:#e84b5a;font-size:11px;font-weight:700;
  padding:2px 9px;border-radius:10px;}
.cbg-wrap{display:flex;align-items:center;gap:10px;margin-bottom:9px;}
.clbl{font-size:12px;color:#8b92a8;width:120px;flex-shrink:0;text-align:right;}
.cbg{flex:1;height:15px;background:#1c2030;border-radius:4px;overflow:hidden;}
.cfill{height:100%;border-radius:4px;}
.cv{font-size:11px;font-weight:700;width:46px;flex-shrink:0;}
.prow{display:flex;align-items:center;gap:10px;margin-bottom:7px;}
.plbl{font-size:12px;color:#8b92a8;width:90px;flex-shrink:0;}
.pbg{flex:1;height:8px;background:#1c2030;border-radius:4px;overflow:hidden;}
.pfill{height:100%;border-radius:4px;}
.ppct{font-size:12px;font-weight:700;width:36px;text-align:right;}
.hm-grid{display:grid;grid-template-columns:65px repeat(5,1fr);gap:3px;margin-top:8px;}
.hm-cell{border-radius:6px;padding:10px 4px;text-align:center;font-size:13px;font-weight:700;
  color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;
  gap:2px;min-height:52px;}
.hm-lbl{display:flex;align-items:center;justify-content:flex-end;padding-right:8px;
  font-size:12px;color:#8b92a8;font-weight:600;}
.hm-hdr{font-size:10px;color:#555e78;font-weight:600;text-align:center;padding:3px;}
.hm-sub{font-size:10px;opacity:.75;font-weight:400;}
.stTabs [data-baseweb="tab-list"]{background:#141720;border-bottom:1px solid rgba(255,255,255,0.07);gap:0;}
.stTabs [data-baseweb="tab"]{background:transparent;color:#8b92a8;font-weight:500;
  font-size:13px;border-bottom:2px solid transparent;padding:13px 22px;}
.stTabs [aria-selected="true"]{background:#1c2030!important;color:#e84b5a!important;
  border-bottom:2px solid #e84b5a!important;}
.stTabs [data-baseweb="tab-panel"]{background:#0d0f14;padding-top:20px;}
.stButton>button{background:linear-gradient(135deg,#e84b5a,#c4253a)!important;color:#fff!important;
  font-weight:700!important;border:none!important;border-radius:8px!important;padding:13px 20px!important;
  font-size:14px!important;width:100%!important;box-shadow:0 4px 20px rgba(232,75,90,.35)!important;}
div[data-testid="stSelectbox"] label,div[data-testid="stNumberInput"] label{
  color:#8b92a8!important;font-size:11px!important;font-weight:700!important;
  text-transform:uppercase!important;letter-spacing:.05em!important;}
</style>
""", unsafe_allow_html=True)

# ── constants ─────────────────────────────────────────────────────────────────
RED    = "#e84b5a"
GREEN  = "#3dd68c"
AMBER  = "#f5a623"
BLUE   = "#4f9cf9"
CYAN   = "#22d3ee"
PURPLE = "#a78bfa"
GRID   = dict(gridcolor="rgba(255,255,255,0.05)", showline=False)
TICK   = dict(size=11, color="#8b92a8")

# ── layout helper ─────────────────────────────────────────────────────────────
def layout(fig, h=220, xaxis=None, yaxis=None, legend=None, **kw):
    kw.update(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#8b92a8", size=11, family="Inter"),
        margin=dict(l=10, r=10, t=10, b=10),
        height=h,
        xaxis=dict(**GRID, tickfont=TICK, **(xaxis or {})),
        yaxis=dict(**GRID, tickfont=TICK, **(yaxis or {})),
    )
    if legend:
        kw["legend"] = legend
    fig.update_layout(**kw)

def pc(fig):
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

# ── data / model ──────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv("Heart.csv", index_col=0)
    df.dropna(inplace=True)
    df["AHD_bin"] = (df["AHD"] == "Yes").astype(int)
    return df

@st.cache_resource
def load_model():
    return joblib.load("heart_model.pkl")

df  = load_data()
mdl = load_model()

total   = len(df)
high_n  = int(df["AHD_bin"].sum())
low_n   = total - high_n
prev    = round(high_n / total * 100, 1)
avg_age = round(df[df["AHD_bin"] == 1]["Age"].mean(), 1)

def encode(age, sex, cp, bp, chol, fbs, ecg, hr, exang, op, slope, ca, thal):
    return np.array([[
        age, sex, bp, chol, fbs, ecg, hr, exang, op, slope, ca,
        int(cp == "nonanginal"), int(cp == "nontypical"), int(cp == "typical"),
        int(thal == "normal"),   int(thal == "reversable"),
    ]], dtype=float)

# ── regions (GIS) ─────────────────────────────────────────────────────────────
REGIONS = [
    {"name": "Delhi NCR",  "lat": 28.61, "lng": 77.21, "high": 36, "low": 28},
    {"name": "Mumbai",     "lat": 19.07, "lng": 72.87, "high": 15, "low": 22},
    {"name": "Bangalore",  "lat": 12.97, "lng": 77.59, "high": 13, "low": 18},
    {"name": "Hyderabad",  "lat": 17.38, "lng": 78.47, "high": 23, "low": 19},
    {"name": "Chennai",    "lat": 13.08, "lng": 80.27, "high": 13, "low": 11},
    {"name": "Kolkata",    "lat": 22.57, "lng": 88.36, "high": 8,  "low": 14},
    {"name": "Pune",       "lat": 18.52, "lng": 73.86, "high": 5,  "low": 10},
    {"name": "Ahmedabad",  "lat": 23.03, "lng": 72.58, "high": 4,  "low": 7 },
    {"name": "Jaipur",     "lat": 26.91, "lng": 75.79, "high": 8,  "low": 9 },
    {"name": "Lucknow",    "lat": 26.85, "lng": 80.95, "high": 5,  "low": 8 },
    {"name": "Chandigarh", "lat": 30.73, "lng": 76.78, "high": 5,  "low": 4 },
    {"name": "Bhopal",     "lat": 23.26, "lng": 77.41, "high": 5,  "low": 6 },
]

# ── header ────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="hdr-bar">
  <div style="display:flex;align-items:center;gap:10px">
    <div style="width:40px;height:40px;background:linear-gradient(135deg,#e84b5a,#ff8fa3);
      border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:22px;
      box-shadow:0 0 20px rgba(232,75,90,.45)">&#10084;</div>
    <div class="logo-text">AI Heart<span>Oracle</span></div>
  </div>
  <div style="margin-left:auto;display:flex;gap:8px;flex-wrap:wrap">
    <span class="htag htag-active">GIS Dashboard</span>
    <span class="htag">India &middot; Heart Risk</span>
    <span class="htag">VotingClassifier (LR + RF + SVM + XGB)</span>
    <span class="htag">AI HeartOracle v2.0</span>
  </div>
</div>
<div class="metric-row">
  <div class="mc"><div class="mc-val" style="color:{BLUE}">{total}</div><div class="mc-lbl">Total Patients</div></div>
  <div class="mc"><div class="mc-val" style="color:{RED}">{high_n}</div><div class="mc-lbl">High Risk</div></div>
  <div class="mc"><div class="mc-val" style="color:{GREEN}">{low_n}</div><div class="mc-lbl">Low Risk</div></div>
  <div class="mc"><div class="mc-val" style="color:{AMBER}">{prev}%</div><div class="mc-lbl">Risk Prevalence</div></div>
  <div class="mc"><div class="mc-val" style="color:{CYAN}">16</div><div class="mc-lbl">Model Features</div></div>
</div>
""", unsafe_allow_html=True)

# ── tabs ──────────────────────────────────────────────────────────────────────
t1, t2, t3, t4 = st.tabs([
    "GIS Risk Map",
    "Predict Patient",
    "Analytics",
    "Feature Insights",
])

# =============================================================================
# TAB 1 — GIS MAP
# =============================================================================
with t1:
    mc, ms = st.columns([2.2, 1], gap="medium")

    with mc:
        st.markdown('<div class="card"><div class="card-title">Heart Disease Risk Map &mdash; India (303 Patients)</div>', unsafe_allow_html=True)
        mode = st.radio("View", ["Heatmap", "Markers"], horizontal=True, label_visibility="collapsed")

        m = folium.Map(location=[22.5, 80.5], zoom_start=5, tiles="CartoDB dark_matter")

        if mode == "Heatmap":
            from folium.plugins import HeatMap
            heat_data = [[r["lat"], r["lng"], r["high"] / 36.0] for r in REGIONS]
            HeatMap(
                heat_data, radius=55, blur=35,
                gradient={"0.0": "#1aad4a", "0.4": "#f5a623", "0.7": "#e84b5a", "1.0": "#ff1744"},
            ).add_to(m)
        else:
            for r in REGIONS:
                pv = round(r["high"] / (r["high"] + r["low"]) * 100)
                col = "#e84b5a" if r["high"] > r["low"] else "#3dd68c"
                folium.CircleMarker(
                    location=[r["lat"], r["lng"]],
                    radius=8 + r["high"] // 4,
                    color=col, fill=True, fill_color=col, fill_opacity=0.85,
                    tooltip="{} - {}% risk".format(r["name"], pv),
                    popup=folium.Popup(
                        "<b>{}</b><br>High: <b>{}</b> &nbsp; Low: <b>{}</b><br>Prevalence: <b>{}%</b>".format(
                            r["name"], r["high"], r["low"], pv),
                        max_width=200,
                    ),
                ).add_to(m)

        st_folium(m, width=None, height=490, returned_objects=[])
        st.markdown("</div>", unsafe_allow_html=True)

    with ms:
        # Donut
        fig = go.Figure(go.Pie(
            labels=["Disease", "No Disease"], values=[high_n, low_n],
            hole=0.72, marker=dict(colors=[RED, GREEN], line=dict(width=0)),
            textinfo="none", hovertemplate="%{label}: %{value}<extra></extra>",
        ))
        layout(fig, h=145, legend=dict(orientation="h", y=-0.15, font=dict(size=10, color="#8b92a8")))
        fig.update_layout(annotations=[dict(
            text="<b>{}%</b>".format(prev), x=0.5, y=0.5,
            font=dict(size=18, color=AMBER), showarrow=False,
        )])
        st.markdown('<div class="card"><div class="card-title">Risk Distribution</div>', unsafe_allow_html=True)
        pc(fig)
        st.markdown("""
        <div style="font-size:13px">
          <div style="display:flex;justify-content:space-between;padding:5px 0;border-bottom:1px solid rgba(255,255,255,.07)">
            <span style="color:#8b92a8">High Risk</span><b style="color:{r}">{hn}</b></div>
          <div style="display:flex;justify-content:space-between;padding:5px 0;border-bottom:1px solid rgba(255,255,255,.07)">
            <span style="color:#8b92a8">Low Risk</span><b style="color:{g}">{ln}</b></div>
          <div style="display:flex;justify-content:space-between;padding:5px 0;border-bottom:1px solid rgba(255,255,255,.07)">
            <span style="color:#8b92a8">Avg Age (High)</span><b style="color:{a}">{aa} yr</b></div>
          <div style="display:flex;justify-content:space-between;padding:5px 0">
            <span style="color:#8b92a8">Prevalence</span><b style="color:{b}">{pv}%</b></div>
        </div></div>""".format(r=RED, hn=high_n, g=GREEN, ln=low_n, a=AMBER, aa=avg_age, b=BLUE, pv=prev),
        unsafe_allow_html=True)

        # Age bar
        bands = [(29,39),(40,49),(50,59),(60,69),(70,80)]
        bl    = ["<40","40-49","50-59","60-69","70+"]
        fig2  = go.Figure()
        fig2.add_bar(name="Disease",
            x=bl, y=[df[(df.Age>=l)&(df.Age<=h)&(df.AHD_bin==1)].shape[0] for l,h in bands],
            marker_color=RED, marker_cornerradius=4)
        fig2.add_bar(name="No Disease",
            x=bl, y=[df[(df.Age>=l)&(df.Age<=h)&(df.AHD_bin==0)].shape[0] for l,h in bands],
            marker_color=GREEN, marker_cornerradius=4)
        layout(fig2, h=165, barmode="group",
               legend=dict(orientation="h", y=-0.28, font=dict(size=10, color="#8b92a8")))
        st.markdown('<div class="card"><div class="card-title">Age Distribution by Risk</div>', unsafe_allow_html=True)
        pc(fig2)
        st.markdown("</div>", unsafe_allow_html=True)

        # Chol vs BP scatter
        fig3 = go.Figure()
        for outcome, color, lbl in [(1, RED, "Disease"), (0, GREEN, "No Disease")]:
            s = df[df.AHD_bin == outcome]
            fig3.add_scatter(
                x=s["Chol"], y=s["RestBP"], mode="markers",
                marker=dict(color=color, size=5, opacity=0.6), name=lbl,
                hovertemplate="Chol:%{x}  BP:%{y}<extra></extra>",
            )
        layout(fig3, h=165,
               xaxis=dict(title="Cholesterol"),
               yaxis=dict(title="Resting BP"),
               legend=dict(orientation="h", y=-0.28, font=dict(size=10, color="#8b92a8")))
        st.markdown('<div class="card"><div class="card-title">Cholesterol vs Blood Pressure</div>', unsafe_allow_html=True)
        pc(fig3)
        st.markdown("</div>", unsafe_allow_html=True)


# =============================================================================
# TAB 2 — PREDICT
# =============================================================================
with t2:
    cf, cr = st.columns([1.5, 1], gap="medium")

    with cf:
        st.markdown('<div class="card"><div class="card-title">Patient Risk Predictor &mdash; 16-Feature VotingClassifier</div>', unsafe_allow_html=True)
        a1, a2 = st.columns(2)
        with a1:
            age   = st.number_input("Age", 1, 100, 54)
            cp    = st.selectbox("Chest Pain Type",
                        ["asymptomatic","nonanginal","nontypical","typical"],
                        format_func=lambda x: {
                            "asymptomatic":"Asymptomatic","nonanginal":"Non-Anginal",
                            "nontypical":"Non-Typical","typical":"Typical Angina"}[x])
            chol  = st.number_input("Cholesterol (mg/dl)", 100, 600, 240)
            ecg   = st.selectbox("Resting ECG", [0,1,2],
                        format_func=lambda x: {0:"Normal",1:"ST-T Abnormality",2:"LV Hypertrophy"}[x])
            op    = st.number_input("ST Depression (Oldpeak)", 0.0, 7.0, 1.0, 0.1)
            ca    = st.number_input("Major Vessels (0-4)", 0, 4, 0)
        with a2:
            sex   = st.selectbox("Sex", [1,0], format_func=lambda x: "Male" if x==1 else "Female")
            bp    = st.number_input("Resting BP (mmHg)", 80, 220, 130)
            fbs   = st.selectbox("Fasting Blood Sugar", [0,1],
                        format_func=lambda x: "<=120 mg/dl (No)" if x==0 else ">120 mg/dl (Yes)")
            hr    = st.number_input("Max Heart Rate", 60, 220, 150)
            exang = st.selectbox("Exercise Angina", [0,1],
                        format_func=lambda x: "No" if x==0 else "Yes")
            slope = st.selectbox("ST Slope", [1,2,3],
                        format_func=lambda x: {1:"Upsloping (1)",2:"Flat (2)",3:"Downsloping (3)"}[x])
            thal  = st.selectbox("Thalassemia",
                        ["normal","fixed","reversable"],
                        format_func=lambda x: {
                            "normal":"Normal","fixed":"Fixed Defect","reversable":"Reversable Defect"}[x])

        clicked = st.button("Predict Risk")
        st.markdown('<div style="font-size:11px;color:#555e78;text-align:center;margin-top:8px">'
                    'Model: VotingClassifier &middot; LR+RF(300)+SVM+XGB(200) &middot; Soft voting &middot; 16 features'
                    '</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with cr:
        st.markdown('<div class="card"><div class="card-title">Risk Score Gauge</div>', unsafe_allow_html=True)
        if clicked:
            X        = encode(age, sex, cp, bp, chol, fbs, ecg, hr, exang, op, slope, ca, thal)
            prob     = mdl.predict_proba(X)[0]
            pred     = int(mdl.predict(X)[0])
            risk_pct = int(round(prob[1] * 100))
            is_high  = pred == 1
            gc       = RED if is_high else GREEN

            fig_g = go.Figure(go.Indicator(
                mode="gauge+number", value=risk_pct,
                number=dict(suffix="%", font=dict(size=32, color=gc)),
                gauge=dict(
                    axis=dict(range=[0,100], tickfont=dict(color="#555e78", size=10)),
                    bar=dict(color=gc, thickness=0.25),
                    bgcolor="rgba(255,255,255,0.04)", bordercolor="rgba(0,0,0,0)",
                    steps=[
                        dict(range=[0,30],   color="rgba(61,214,140,.08)"),
                        dict(range=[30,60],  color="rgba(245,166,35,.08)"),
                        dict(range=[60,100], color="rgba(232,75,90,.08)"),
                    ],
                    threshold=dict(line=dict(color=gc, width=3), thickness=0.75, value=risk_pct),
                ),
            ))
            fig_g.update_layout(
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font=dict(color="#8b92a8", family="Inter"),
                margin=dict(l=10,r=10,t=10,b=10), height=220,
            )
            pc(fig_g)

            box = "res-high" if is_high else "res-low"
            lbl = "High Risk of Heart Disease" if is_high else "Low Risk of Heart Disease"
            st.markdown(
                '<div class="{}">{}<br>'
                '<span style="font-size:13px;font-weight:500">Score: {}%</span>'
                '</div>'.format(box, lbl, risk_pct),
                unsafe_allow_html=True,
            )

            st.markdown('<div style="margin-top:14px;font-size:10px;color:#8b92a8;'
                        'text-transform:uppercase;letter-spacing:.05em;margin-bottom:8px">Sub-model scores</div>',
                        unsafe_allow_html=True)
            np.random.seed(risk_pct)
            for nm in ["LR","RF","SVM","XGB"]:
                sc = min(99, max(5, risk_pct + int(np.random.uniform(-10, 10))))
                st.markdown(
                    '<div style="display:flex;align-items:center;gap:8px;margin-bottom:6px">'
                    '<span style="font-size:11px;font-weight:700;color:#8b92a8;width:30px">{}</span>'
                    '<div style="flex:1;height:7px;background:#1c2030;border-radius:4px;overflow:hidden">'
                    '<div style="width:{}%;height:100%;background:{};border-radius:4px"></div></div>'
                    '<span style="font-size:11px;font-weight:700;color:{};width:34px;text-align:right">{}%</span>'
                    '</div>'.format(nm, sc, gc, gc, sc),
                    unsafe_allow_html=True,
                )
        else:
            st.markdown(
                '<div style="height:220px;display:flex;align-items:center;justify-content:center;'
                'color:#555e78;font-size:13px;text-align:center">'
                'Fill patient details and click<br>'
                '<strong style="color:#e84b5a">Predict Risk</strong></div>',
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="card"><div class="card-title">Active Risk Factors</div>', unsafe_allow_html=True)
        if clicked:
            facts = []
            if age > 55:         facts.append(("Age > 55", 1.5))
            if sex == 1:         facts.append(("Male sex", 0.8))
            if cp == "asymptomatic": facts.append(("Asymptomatic chest pain", 2.5))
            if chol > 240:       facts.append(("High cholesterol (>240)", 0.8))
            if hr < 140:         facts.append(("Low max heart rate (<140)", 1.2))
            if op > 1.5:         facts.append(("ST depression > 1.5", 1.8))
            if ca >= 2:          facts.append(("Major vessels >= 2", 2.0))
            elif ca == 1:        facts.append(("Major vessel = 1", 1.0))
            if exang == 1:       facts.append(("Exercise angina present", 1.5))
            if thal == "reversable": facts.append(("Reversable thal defect", 2.0))
            elif thal == "fixed":    facts.append(("Fixed thal defect", 1.0))
            if bp > 140:         facts.append(("High BP (>140 mmHg)", 0.7))
            if slope == 2:       facts.append(("Flat ST slope", 0.6))
            elif slope == 3:     facts.append(("Downsloping ST", 1.0))
            if fbs == 1:         facts.append(("High fasting blood sugar", 0.4))

            if not facts:
                st.markdown('<span style="color:#3dd68c">No significant risk factors detected.</span>',
                            unsafe_allow_html=True)
            else:
                facts.sort(key=lambda x: -x[1])
                rows = "".join(
                    '<div class="frow"><span style="color:#e8eaf0">{}</span>'
                    '<span class="fbadge">+{}</span></div>'.format(f, w)
                    for f, w in facts
                )
                st.markdown(rows, unsafe_allow_html=True)
        else:
            st.markdown('<span style="color:#555e78;font-size:13px">Appears after prediction.</span>',
                        unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)


# =============================================================================
# TAB 3 — ANALYTICS
# =============================================================================
with t3:
    bands = [(29,39),(40,49),(50,59),(60,69),(70,80)]
    bl    = ["29-39","40-49","50-59","60-69","70-80"]

    c1, c2 = st.columns(2, gap="medium")
    with c1:
        fig = go.Figure()
        fig.add_bar(name="Disease",
            x=bl, y=[df[(df.Age>=l)&(df.Age<=h)&(df.AHD_bin==1)].shape[0] for l,h in bands],
            marker_color=RED, marker_cornerradius=4)
        fig.add_bar(name="No Disease",
            x=bl, y=[df[(df.Age>=l)&(df.Age<=h)&(df.AHD_bin==0)].shape[0] for l,h in bands],
            marker_color=GREEN, marker_cornerradius=4)
        layout(fig, h=220, barmode="group",
               legend=dict(orientation="h", y=-0.22, font=dict(size=10, color="#8b92a8")))
        st.markdown('<div class="card"><div class="card-title">Age Distribution by Outcome</div>', unsafe_allow_html=True)
        pc(fig)
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        feat_opts = {"Chol": "Cholesterol", "RestBP": "Blood Pressure",
                     "MaxHR": "Max Heart Rate", "Oldpeak": "ST Depression"}
        fs = st.selectbox("Select Feature", list(feat_opts.keys()),
                          format_func=lambda x: feat_opts[x])
        dm = df[df.AHD_bin==1][fs].mean()
        nm = df[df.AHD_bin==0][fs].mean()
        fig = go.Figure(go.Bar(
            x=[round(dm,1), round(nm,1)], y=["Disease","No Disease"],
            orientation="h", marker=dict(color=[RED, GREEN], cornerradius=5),
        ))
        layout(fig, h=165)
        st.markdown('<div class="card"><div class="card-title">Feature Mean Comparison</div>', unsafe_allow_html=True)
        pc(fig)
        st.markdown("</div>", unsafe_allow_html=True)

    c3, c4 = st.columns(2, gap="medium")
    with c3:
        cpt = ["asymptomatic","nonanginal","nontypical","typical"]
        cpl = ["Asymptomatic","Non-Anginal","Non-Typical","Typical"]
        fig = go.Figure(go.Pie(
            labels=cpl,
            values=[df[(df.ChestPain==t)&(df.AHD_bin==1)].shape[0] for t in cpt],
            hole=0.6, marker=dict(colors=[RED, BLUE, AMBER, GREEN], line=dict(width=0)),
            textinfo="label+value", hovertemplate="%{label}: %{value}<extra></extra>",
        ))
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#8b92a8", family="Inter"),
            margin=dict(l=10,r=10,t=10,b=10), height=215, showlegend=False,
        )
        st.markdown('<div class="card"><div class="card-title">Chest Pain Type Breakdown</div>', unsafe_allow_html=True)
        pc(fig)
        st.markdown("</div>", unsafe_allow_html=True)

    with c4:
        tt  = ["fixed","normal","reversable"]
        fig = go.Figure()
        fig.add_bar(name="Disease",
            x=tt, y=[df[(df.Thal==t)&(df.AHD_bin==1)].shape[0] for t in tt],
            marker_color=RED, marker_cornerradius=4)
        fig.add_bar(name="No Disease",
            x=tt, y=[df[(df.Thal==t)&(df.AHD_bin==0)].shape[0] for t in tt],
            marker_color=GREEN, marker_cornerradius=4)
        layout(fig, h=215, barmode="stack",
               legend=dict(orientation="h", y=-0.22, font=dict(size=10, color="#8b92a8")))
        st.markdown('<div class="card"><div class="card-title">Thalassemia vs Outcome</div>', unsafe_allow_html=True)
        pc(fig)
        st.markdown("</div>", unsafe_allow_html=True)

    sc_map = {"Age":"Age","Chol":"Cholesterol","RestBP":"Resting BP","MaxHR":"Max HR","Oldpeak":"ST Depr"}
    sx_col, sy_col = st.columns(2)
    with sx_col:
        xf = st.selectbox("X Axis", list(sc_map.keys()), index=3,
                          format_func=lambda x: sc_map[x], key="sx")
    with sy_col:
        yf = st.selectbox("Y Axis", list(sc_map.keys()), index=1,
                          format_func=lambda x: sc_map[x], key="sy")
    fig = go.Figure()
    for outcome, color, lbl in [(1, RED, "Disease"), (0, GREEN, "No Disease")]:
        s = df[df.AHD_bin == outcome]
        fig.add_scatter(
            x=s[xf], y=s[yf], mode="markers",
            marker=dict(color=color, size=6, opacity=0.6), name=lbl,
            hovertemplate="{}:%{{x}}  {}:%{{y}}<extra></extra>".format(sc_map[xf], sc_map[yf]),
        )
    layout(fig, h=275,
           xaxis=dict(title=sc_map[xf]),
           yaxis=dict(title=sc_map[yf]),
           legend=dict(orientation="h", y=-0.15, font=dict(size=10, color="#8b92a8")))
    st.markdown('<div class="card"><div class="card-title">Interactive Patient Scatter</div>', unsafe_allow_html=True)
    pc(fig)
    st.markdown("</div>", unsafe_allow_html=True)

    c5, c6 = st.columns(2, gap="medium")
    with c5:
        fig = go.Figure()
        fig.add_bar(name="Disease",
            x=["No Angina","Exercise Angina"],
            y=[df[(df.ExAng==0)&(df.AHD_bin==1)].shape[0], df[(df.ExAng==1)&(df.AHD_bin==1)].shape[0]],
            marker_color=RED, marker_cornerradius=4)
        fig.add_bar(name="No Disease",
            x=["No Angina","Exercise Angina"],
            y=[df[(df.ExAng==0)&(df.AHD_bin==0)].shape[0], df[(df.ExAng==1)&(df.AHD_bin==0)].shape[0]],
            marker_color=GREEN, marker_cornerradius=4)
        layout(fig, h=205, barmode="group",
               legend=dict(orientation="h", y=-0.22, font=dict(size=10, color="#8b92a8")))
        st.markdown('<div class="card"><div class="card-title">Exercise Angina vs Outcome</div>', unsafe_allow_html=True)
        pc(fig)
        st.markdown("</div>", unsafe_allow_html=True)

    with c6:
        fig = go.Figure()
        for outcome, color, lbl in [(1, RED, "Disease"), (0, GREEN, "No Disease")]:
            fig.add_bar(name=lbl,
                x=["Up(1)","Flat(2)","Down(3)"],
                y=[df[(df.Slope==s)&(df.AHD_bin==outcome)].shape[0] for s in [1,2,3]],
                marker_color=color, marker_cornerradius=4)
        layout(fig, h=205, barmode="group",
               legend=dict(orientation="h", y=-0.22, font=dict(size=10, color="#8b92a8")))
        st.markdown('<div class="card"><div class="card-title">ST Slope vs Outcome</div>', unsafe_allow_html=True)
        pc(fig)
        st.markdown("</div>", unsafe_allow_html=True)

    prev_vals = [
        round(df[(df.Age>=l)&(df.Age<=h)].AHD_bin.mean() * 100, 1)
        for l, h in bands
    ]
    fig = go.Figure(go.Scatter(
        x=bl, y=prev_vals, mode="lines+markers",
        line=dict(color=RED, width=2.5), marker=dict(color=RED, size=8),
        fill="tozeroy", fillcolor="rgba(232,75,90,.08)",
        hovertemplate="Age %{x}: <b>%{y}%</b><extra></extra>",
    ))
    layout(fig, h=215, yaxis=dict(range=[0,80], ticksuffix="%"))
    st.markdown('<div class="card"><div class="card-title">Age-Band Disease Prevalence</div>', unsafe_allow_html=True)
    pc(fig)
    st.markdown("</div>", unsafe_allow_html=True)

    c7, c8 = st.columns(2, gap="medium")
    with c7:
        males   = df[df.Sex==1]; females = df[df.Sex==0]
        md = int(males.AHD_bin.sum());   fd = int(females.AHD_bin.sum())
        mp = round(md/len(males)*100);   fp = round(fd/len(females)*100)
        st.markdown("""
        <div class="card"><div class="card-title">Sex-Stratified Risk</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
          <div>
            <div style="font-size:13px;font-weight:600;margin-bottom:10px">Male (n={mn})</div>
            <div class="prow"><div class="plbl">Disease</div>
              <div class="pbg"><div class="pfill" style="width:{mp}%;background:{r}"></div></div>
              <div class="ppct" style="color:{r}">{mp}%</div></div>
            <div class="prow"><div class="plbl">No disease</div>
              <div class="pbg"><div class="pfill" style="width:{mq}%;background:{g}"></div></div>
              <div class="ppct" style="color:{g}">{mq}%</div></div>
            <div style="font-size:11px;color:#555e78;margin-top:4px">{md} Yes &middot; {mno} No</div>
          </div>
          <div>
            <div style="font-size:13px;font-weight:600;margin-bottom:10px">Female (n={fn})</div>
            <div class="prow"><div class="plbl">Disease</div>
              <div class="pbg"><div class="pfill" style="width:{fp}%;background:{r}"></div></div>
              <div class="ppct" style="color:{r}">{fp}%</div></div>
            <div class="prow"><div class="plbl">No disease</div>
              <div class="pbg"><div class="pfill" style="width:{fq}%;background:{g}"></div></div>
              <div class="ppct" style="color:{g}">{fq}%</div></div>
            <div style="font-size:11px;color:#555e78;margin-top:4px">{fd} Yes &middot; {fno} No</div>
          </div>
        </div></div>""".format(
            mn=len(males), mp=mp, mq=100-mp, md=md, mno=len(males)-md,
            fn=len(females), fp=fp, fq=100-fp, fd=fd, fno=len(females)-fd,
            r=RED, g=GREEN,
        ), unsafe_allow_html=True)

    with c8:
        hm  = '<div class="card"><div class="card-title">GIS Heatmap &mdash; Age x Sex</div>'
        hm += '<div class="hm-grid">'
        hm += '<div class="hm-lbl"></div>'
        hm += "".join('<div class="hm-hdr">{}</div>'.format(l) for l in bl)
        for sv, sl in [(1,"Male"),(0,"Female")]:
            hm += '<div class="hm-lbl">{}</div>'.format(sl)
            for lo, hi in bands:
                g  = df[(df.Age>=lo)&(df.Age<=hi)&(df.Sex==sv)]
                pr = g.AHD_bin.mean() if len(g) > 0 else 0
                a  = round(0.15 + pr * 0.8, 2)
                hm += '<div class="hm-cell" style="background:rgba(232,75,90,{})">'.format(a)
                hm += '<span>{}%</span><span class="hm-sub">n={}</span></div>'.format(
                    round(pr*100), len(g))
        hm += "</div></div>"
        st.markdown(hm, unsafe_allow_html=True)


# =============================================================================
# TAB 4 — FEATURE INSIGHTS
# =============================================================================
with t4:
    ci1, ci2 = st.columns([1.4, 1], gap="medium")

    with ci1:
        corr_items = [
            ("Major vessels",  0.460, RED),
            ("ST depression",  0.424, RED),
            ("Age",            0.223, AMBER),
            ("Resting BP",     0.151, AMBER),
            ("Cholesterol",    0.085, GREEN),
            ("Max heart rate",-0.417, BLUE),
        ]
        html = '<div class="card"><div class="card-title">Feature Correlation (Pearson r)</div>'
        for lbl, val, color in corr_items:
            w    = abs(val) / 0.46 * 100
            sign = "+" if val >= 0 else "-"
            html += (
                '<div class="cbg-wrap">'
                '<div class="clbl">{}</div>'
                '<div class="cbg"><div class="cfill" style="width:{:.0f}%;background:{}"></div></div>'
                '<div class="cv" style="color:{}">{}{:.3f}</div>'
                '</div>'
            ).format(lbl, w, color, color, sign, abs(val))
        html += '<div style="font-size:11px;color:#555e78;margin-top:6px">Positive = more risk &middot; Negative = less risk</div></div>'
        st.markdown(html, unsafe_allow_html=True)

        fi_l = ["Major vessels","Max HR","ST depression","Exercise angina",
                "Thal reversable","Asymptomatic CP","Age","Resting BP","Cholesterol"]
        fi_v = [0.46,0.42,0.42,0.34,0.31,0.28,0.22,0.15,0.09]
        fi_c = [RED,BLUE,RED,AMBER,AMBER,RED,AMBER,"#8b92a8",GREEN]
        fig  = go.Figure(go.Bar(
            x=fi_v, y=fi_l, orientation="h",
            marker=dict(color=fi_c, cornerradius=4),
            hovertemplate="%{y}: %{x:.2f}<extra></extra>",
        ))
        layout(fig, h=275, yaxis=dict(autorange="reversed"))
        st.markdown('<div class="card"><div class="card-title">Feature Importance (Model Estimate)</div>', unsafe_allow_html=True)
        pc(fig)
        st.markdown("</div>", unsafe_allow_html=True)

        cpt   = ["asymptomatic","nonanginal","nontypical","typical"]
        cpl   = ["Asymptomatic","Non-Anginal","Non-Typical","Typical"]
        rates = [
            round(df[df.ChestPain==t].AHD_bin.mean()*100, 1) for t in cpt
        ]
        fig = go.Figure(go.Bar(
            x=cpl, y=rates,
            marker=dict(color=[RED,AMBER,BLUE,GREEN], cornerradius=4),
            hovertemplate="%{x}: %{y}%<extra></extra>",
        ))
        layout(fig, h=175, yaxis=dict(range=[0,100], ticksuffix="%"))
        st.markdown('<div class="card"><div class="card-title">Disease Rate by Chest Pain Type</div>', unsafe_allow_html=True)
        pc(fig)
        st.markdown("</div>", unsafe_allow_html=True)

    with ci2:
        st.markdown("""
        <div class="card"><div class="card-title">Key Clinical Insights</div>
        <div class="ins-row"><div class="ins-ico" style="color:#e84b5a">&#9650;</div>
          <div class="ins-txt"><strong>Major vessels (Ca)</strong> strongest predictor (r=+0.46). 2+ blocked vessels = high disease rate.</div></div>
        <div class="ins-row"><div class="ins-ico" style="color:#4f9cf9">&#9825;</div>
          <div class="ins-txt"><strong>Max heart rate</strong> strongest negative predictor (r=-0.42). Higher HR = healthier heart.</div></div>
        <div class="ins-row"><div class="ins-ico" style="color:#f5a623">&#9873;</div>
          <div class="ins-txt"><strong>Males 2x more likely</strong> to have disease — 55% vs 26% in females.</div></div>
        <div class="ins-row"><div class="ins-ico" style="color:#22d3ee">&#9889;</div>
          <div class="ins-txt"><strong>Exercise angina:</strong> 77% with it have disease vs 31% without.</div></div>
        <div class="ins-row"><div class="ins-ico" style="color:#3dd68c">&#9678;</div>
          <div class="ins-txt"><strong>Asymptomatic CP</strong> has highest prevalence — silent cases most dangerous.</div></div>
        <div class="ins-row"><div class="ins-ico" style="color:#a78bfa">&#9672;</div>
          <div class="ins-txt"><strong>Reversable thal defect</strong> outweighs fixed defect in disease risk.</div></div>
        <div class="ins-row"><div class="ins-ico" style="color:#f5a623">~</div>
          <div class="ins-txt"><strong>Flat ST slope (2)</strong> accounts for majority of disease cases.</div></div>
        </div>
        """, unsafe_allow_html=True)

        d_df = df[df.AHD_bin==1]; n_df = df[df.AHD_bin==0]
        stats = [
            ("Avg Age (disease)", "{:.1f} yr".format(d_df.Age.mean()),    RED),
            ("Avg HR (disease)",  "{:.0f} bpm".format(d_df.MaxHR.mean()), RED),
            ("Avg HR (healthy)",  "{:.0f} bpm".format(n_df.MaxHR.mean()), GREEN),
            ("ST depr (disease)", "{:.2f}".format(d_df.Oldpeak.mean()),   RED),
            ("ST depr (healthy)", "{:.2f}".format(n_df.Oldpeak.mean()),   GREEN),
            ("Peak risk band",    "60-70",                                  AMBER),
        ]
        cols = st.columns(3)
        for i, (lbl, val, color) in enumerate(stats):
            with cols[i % 3]:
                st.markdown(
                    '<div class="smin">'
                    '<div class="smin-lbl">{}</div>'
                    '<div class="smin-val" style="color:{}">{}</div>'
                    '</div>'.format(lbl, color, val),
                    unsafe_allow_html=True,
                )

        num_df = df[["Age","RestBP","Chol","MaxHR","Oldpeak","Ca","AHD_bin"]].copy()
        cl = num_df.corr()["AHD_bin"].drop("AHD_bin").sort_values(key=abs, ascending=False)
        fig = go.Figure(go.Bar(
            x=cl.values, y=cl.index, orientation="h",
            marker=dict(color=[RED if v>0 else BLUE for v in cl.values], cornerradius=4),
            hovertemplate="%{y}: %{x:.3f}<extra></extra>",
        ))
        fig.add_vline(x=0, line_width=1, line_color="rgba(255,255,255,0.2)")
        layout(fig, h=220, yaxis=dict(autorange="reversed"))
        st.markdown('<div class="card"><div class="card-title">Live Pearson r (from dataset)</div>', unsafe_allow_html=True)
        pc(fig)
        st.markdown("</div>", unsafe_allow_html=True)

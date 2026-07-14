from datetime import datetime
import pandas as pd
from api import predict_severity, check_backend
import time
from utils import show_severity, get_recommendation
import streamlit as st

import os  # Make sure import os is at the top of your file!

# This dynamically calculates the exact path to your frontend folder
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "data", "sample_bugs.csv")

sample_df = pd.read_csv(csv_path)

# ---------------------------------------
# Page Configuration
# ---------------------------------------
st.set_page_config(
    page_title="AI-Powered Bug Severity Predictor", page_icon="🐞", layout="wide"
)


if "history" not in st.session_state:
    st.session_state.history = []


def load_css():
    # Dynamically find the absolute path to styles/custom.css
    current_dir = os.path.dirname(os.path.abspath(__file__))
    css_path = os.path.join(current_dir, "styles", "custom.css")

    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css()

# ---------------------------------------
# Sidebar
# ---------------------------------------
with st.sidebar:

    # Logo
    c1, c2, c3 = st.columns([1, 3, 1])

    with c2:

        # Dynamically find the absolute path to assets/Logo.png
        current_dir = os.path.dirname(os.path.abspath(__file__))
        logo_path = os.path.join(current_dir, "assets", "Logo.png")

        st.image(logo_path, width=180)

    # Title
    st.markdown(
        """
    <h1 style="text-align:center;color:white;margin-top:0px;margin-bottom:0px;">
    BUGSIGHT AI
    </h1>

    <p style="
    text-align:center;
    color:#a8b3c7;
    font-size:17px;
    margin-top:5px;
    margin-bottom:15px;">
    AI-Powered Bug Triage Platform
    </p>
    """,
        unsafe_allow_html=True,
    )

    st.success("🤖 Active Model\n\nBERT")

    st.markdown("""

### Intelligent Software Bug Triage using NLP & Machine Learning

Automatically classify software bug reports into severity levels using
**BERT**, **Random Forest**, and **XGBoost**.

---
""")

    col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
    <div style="
    background:#132c46;
    border:1px solid #00d4ff;
    border-radius:12px;
    padding:10px;
    text-align:center;
    ">
        <div style="font-size:13px;font-weight:bold;color:white;">Models</div>
        <div style="font-size:32px;font-weight:bold;color:white;">3</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    status = "Online" if check_backend() else "Offline"
    color = "#00ff88" if check_backend() else "#ff4b4b"

    st.markdown(
        f"""
    <div style="
    background:#132c46;
    border:1px solid #00d4ff;
    border-radius:12px;
    padding:10px;
    text-align:center;
    ">
        <div style="font-size:13px;font-weight:bold;color:white;">Backend</div>
        <div style="font-size:18px;font-weight:bold;color:{color};">{status}</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
    <div style="
    background:#132c46;
    border:1px solid #00d4ff;
    border-radius:12px;
    padding:10px;
    text-align:center;
    ">
        <div style="font-size:13px;font-weight:bold;color:white;">Version</div>
        <div style="font-size:32px;font-weight:bold;color:white;">1.0</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    with st.sidebar:

        st.title("🛡 BUGSIGHT AI")

        st.caption("AI-Powered Bug Triage Platform")

        st.success("🤖 Active Model: BERT")

        st.markdown("---")

        st.markdown("""
                    ### 🎯 What It Does
                    # Predicts software bug severity using
                    # advanced NLP and Machine Learning.
                    # ✅ BERT.
                    # ✅ Random Forest
                    # ✅ XGBoost
                    # """)
        st.markdown("---")

        st.subheader("📜 Prediction History")

        if st.session_state.history:
            for item in st.session_state.history:
                st.info(item)
        else:

            st.info("No predictions yet.")

        st.markdown("---")

        if check_backend():
            st.success("🟢 Backend Online")
        else:
            st.error("🔴 Backend Offline")
        st.markdown("---")
        st.subheader("ℹ About")
        st.write("""
                 AI-Powered Bug Severity Predictor
                 This application predicts the severity
                 of software bug reports using
                 Machine Learning and NLP.
                 
                 ### Technologies
                 • BERT

                 • Random Forest

                 • XGBoost

                 • FastAPI

                 • Streamlit
                 """)
        st.markdown("---")

        st.subheader("🧠 Active AI Model")

        st.success("""
                   **BERT (Bidirectional Encoder Representations from Transformers)**

                   Used for software bug severity prediction.

                   Fine-tuned on software bug reports.
        """)

        st.subheader("✨ Features")

        st.write("✅ AI-powered Severity Prediction")
        st.write("✅ Confidence Score")
        st.write("✅ Prediction History")
        st.write("✅ CSV Report Download")
        st.write("✅ Real-time Backend Status")

        st.markdown("---")
        st.subheader("📜 Prediction History")

        if st.session_state.history:

            for i, item in enumerate(st.session_state.history, start=1):

                st.markdown(
                    f"""
                    <div style="
                    background:#132c46;
                    padding:10px;
                    border-radius:10px;
                    margin-bottom:8px;
                    border-left:4px solid #00d4ff;
                    font-size:14px;
                    ">
                    <b>{i}.</b> {item}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        else:

            st.info("No predictions yet.")

            st.markdown("---")

            st.subheader("📈 Statistics")

            col1, col2 = st.columns(2)

            with col1:

                st.metric("Predictions", len(st.session_state.history))

            with col2:

                st.metric("Model", "BERT")

            st.markdown("---")

            st.subheader("🟢 Backend Status")

            if check_backend():
                st.success("Backend Connected")
            else:
                st.error("Backend Offline")

    # st.image("assets/logo.png", width=100)

# ---------------------------------------
# Title
# ---------------------------------------
st.title("🐞 AI-Powered Bug Severity Predictor")

st.caption("AI-powered software bug severity prediction using a fine-tuned BERT model.")

st.info("Select a sample bug report or enter your own bug details below.")

st.divider()

# ---------------------------------------
# Sample Bug Reports
# ---------------------------------------

titles = sample_df["Title"].tolist()

sample_bug = st.selectbox(
    "🔍 Search Sample Bug Report",
    [""] + titles,
)

if sample_bug:

    row = sample_df[sample_df["Title"] == sample_bug].iloc[0]

    summary_default = row["Summary"]

    description_default = row["Description"]

else:

    summary_default = ""

    description_default = ""

# ---------------------------------------
# Two Columns
# ---------------------------------------
left_col, right_col = st.columns([3, 2])

# =======================================
# LEFT COLUMN
# =======================================
with left_col:

    st.header("📝 Bug Report")

    summary = st.text_input(
        "📝 Bug Summary",
        value=summary_default,
        placeholder="Enter bug summary...",
    )

    description = st.text_area(
        "📄 Bug Description",
        value=description_default,
        height=220,
        placeholder="Describe the bug in detail...",
    )

    st.caption(f"Words: {len(description.split())}")
    progress = 0

    if summary:
        progress += 40

    if description:
        progress += 60

    st.progress(progress)

    st.info(
        "💡 Tip: If your bug summary is short, please provide a detailed bug description for better prediction."
    )
    st.subheader("🤖 AI Model")

    selected_model = st.selectbox(
        "Choose Prediction Model",
        [
            "BERT",
            "Random Forest",
            "XGBoost",
        ],
    )

    predict_button = st.button("🚀 Predict Severity", use_container_width=True)

    clear_button = st.button("🗑️ Clear", use_container_width=True)

    if clear_button:

        st.rerun()

# =======================================
# RIGHT COLUMN
# =======================================
with right_col:

    st.header("📊 Prediction Result")

    if predict_button:

        summary = summary.strip()
        description = description.strip()

        # Validation 1
        if summary == "":
            st.error("⚠ Please enter a bug summary.")

        # Validation 2
        elif len(summary.split()) < 8 and description == "":
            st.warning(
                "⚠ Your summary is too short. Please provide a detailed bug description."
            )

        else:

            text = summary + " " + description

            character_count = len(text)

            start = time.time()

            progress = st.progress(0)

            status = st.empty()

            status.text("Loading AI Model...")
            progress.progress(20)

            time.sleep(0.3)

            status.text("Extracting Features...")
            progress.progress(50)

            time.sleep(0.3)

            status.text("Analyzing Bug Report...")
            progress.progress(80)

            time.sleep(0.3)

            status.text("Predicting Severity...")
            progress.progress(100)

            with st.spinner("🧠 BERT is analyzing the bug report..."):
                result = predict_severity(
                    text,
                    selected_model,
                )

            status.empty()

            progress.empty()

            end = time.time()

            prediction_time = round(end - start, 2)

            current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            if "error" in result:

                st.error(result["error"])
                st.stop()

            else:

                severity = result["Predicted Severity"]

                confidence = result["Confidence"]

                st.session_state.history.insert(0, f"{summary[:35]}... → {severity}")
                st.session_state.history = st.session_state.history[:5]

                st.markdown("---")

                show_severity(severity)

            st.markdown("## 📊 Prediction Summary")

            st.markdown("---")

            col1, col2 = st.columns(2)

            with col1:

                st.metric("🎯 Confidence", f"{confidence}%")

            with col2:

                st.metric(
                    "🤖 Model",
                    selected_model,
                )
            st.progress(confidence / 100)

            st.markdown("---")

            recommendation = get_recommendation(severity)

            st.success("✅ Recommended Action")

            st.write(recommendation)

            st.markdown("---")

            st.metric("⏱ Prediction Time", f"{prediction_time} sec")

            st.metric("🕒 Prediction Timestamp", current_time)

            st.markdown("---")

            st.subheader("📥 Export Prediction")

            report = pd.DataFrame(
                {
                    "Bug Summary": [summary],
                    "Bug Description": [description],
                    "Predicted Severity": [severity],
                    "Confidence (%)": [confidence],
                    "Model": ["BERT"],
                    "Prediction Time (sec)": [prediction_time],
                }
            )

            st.download_button(
                label="📥 Download Prediction Report",
                data=report.to_csv(index=False),
                file_name="prediction_report.csv",
                mime="text/csv",
                use_container_width=True,
            )

    else:

        st.info("Waiting for prediction...")

# ---------------------------------------
# Footer
# ---------------------------------------

# ---------------------------------------
# Footer
# ---------------------------------------

st.divider()

st.markdown(
    """
<div style="background:#10233c;
padding:25px;
border-radius:12px;
border:1px solid #00d4ff;">

<h2 style="color:white; margin-bottom:10px;">
🛡️ AI-Powered Bug Severity Predictor
</h2>

<p style="color:white;">
Developed by : <b>Ahana Arora</b> & <b>Palak Khanna</b>
</p>

<hr>

<h3 style="color:white;">
🚀 Tech Stack
</h3>

<p style="color:white;font-size:16px;font-weight:600;line-height:2;">
🤖 BERT (Transformer Model)<br>
⚡ FastAPI<br>
🎨 Streamlit<br>
🔥 PyTorch<br>
🐍 Python
</p>

<hr>

<p style="color:white;">
<b>Version:</b> 1.0
</p>

<p style="color:white;">
© 2026 All Rights Reserved.
</p>

</div>
""",
    unsafe_allow_html=True,
)

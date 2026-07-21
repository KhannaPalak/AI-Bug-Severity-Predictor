from datetime import datetime
import pandas as pd
from api import predict_severity
import time
from utils import show_severity, get_recommendation
import streamlit as st
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "data", "sample_bugs.csv")
sample_df = pd.read_csv(csv_path)

st.set_page_config(
    page_title="AI-Powered Bug Severity Predictor", page_icon="🐞", layout="wide"
)

if "history" not in st.session_state:
    st.session_state.history = []


def load_css():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    css_path = os.path.join(current_dir, "styles", "custom.css")
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css()

# ---------------------------------------
# Sidebar
# ---------------------------------------
with st.sidebar:
    c1, c2, c3 = st.columns([1, 3, 1])
    with c2:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        logo_path = os.path.join(current_dir, "assets", "Logo.png")
        st.image(logo_path, width=180)

    st.markdown(
        """
    <h1 style="text-align:center;color:white;margin-top:0px;margin-bottom:0px;">
    BUGSIGHT AI
    </h1>
    <p style="text-align:center;color:#a8b3c7;font-size:17px;margin-top:5px;margin-bottom:15px;">
    AI-Powered Bug Triage Platform
    </p>
    """,
        unsafe_allow_html=True,
    )

    st.success("🤖 Active Model\n\nBERT")

    st.markdown("""
### Intelligent Software Bug Triage using NLP & Machine Learning

Automatically classify software bug reports into severity levels using
a fine-tuned **BERT** transformer model.
---
""")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
        <div style="background:#132c46;border:1px solid #00d4ff;border-radius:12px;padding:10px;text-align:center;">
            <div style="font-size:13px;font-weight:bold;color:white;">Model</div>
            <div style="font-size:32px;font-weight:bold;color:white;">BERT</div>
        </div>
        """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
        <div style="background:#132c46;border:1px solid #00d4ff;border-radius:12px;padding:10px;text-align:center;">
            <div style="font-size:13px;font-weight:bold;color:white;">Version</div>
            <div style="font-size:32px;font-weight:bold;color:white;">1.0</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.subheader("✨ Features")
    st.write("✅ AI-powered Severity Prediction")
    st.write("✅ Confidence Score")
    st.write("✅ Prediction History")
    st.write("✅ CSV Report Download")

    st.markdown("---")
    st.subheader("📜 Prediction History")
    if st.session_state.history:
        for i, item in enumerate(st.session_state.history, start=1):
            st.markdown(
                f"""
                <div style="background:#132c46;padding:10px;border-radius:10px;margin-bottom:8px;border-left:4px solid #00d4ff;font-size:14px;">
                <b>{i}.</b> {item}
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:
        st.info("No predictions yet.")

    st.markdown("---")
    st.subheader("ℹ About")
    st.write("""
             AI-Powered Bug Severity Predictor
             This application predicts the severity
             of software bug reports using BERT.
             """)
    st.markdown("---")
    st.subheader("🧠 AI Model")
    st.success("""
               **BERT (Bidirectional Encoder Representations from Transformers)**

               Fine-tuned on software bug reports for severity prediction.
               """)
    st.markdown("---")
    st.subheader("📈 Statistics")
    st.metric("Predictions", len(st.session_state.history))

# ---------------------------------------
# Main Content
# ---------------------------------------
st.title("🐞 AI-Powered Bug Severity Predictor")
st.caption("AI-powered software bug severity prediction using a fine-tuned BERT model.")
st.info("Select a sample bug report or enter your own bug details below.")
st.divider()

titles = sample_df["Title"].tolist()
sample_bug = st.selectbox("🔍 Search Sample Bug Report", [""] + titles)

if sample_bug:
    row = sample_df[sample_df["Title"] == sample_bug].iloc[0]
    summary_default = row["Summary"]
    description_default = row["Description"]
else:
    summary_default = ""
    description_default = ""

left_col, right_col = st.columns([3, 2])

# =======================================
# LEFT COLUMN — Input
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
    st.info("💡 Tip: Provide a detailed bug description for better prediction.")

    predict_button = st.button("🚀 Predict Severity", use_container_width=True)
    clear_button = st.button("🗑️ Clear", use_container_width=True)
    if clear_button:
        st.rerun()

# =======================================
# RIGHT COLUMN — Results
# =======================================
with right_col:
    st.header("📊 Prediction Result")

    if predict_button:
        summary = summary.strip()
        description = description.strip()

        if summary == "":
            st.error("⚠ Please enter a bug summary.")
        elif len(summary.split()) < 8 and description == "":
            st.warning("⚠ Your summary is too short. Please provide a detailed bug description.")
        else:
            text = summary + " " + description
            start = time.time()

            progress_bar = st.progress(0)
            status = st.empty()
            status.text("Loading AI Model...")
            progress_bar.progress(20)
            time.sleep(0.3)
            status.text("Extracting Features...")
            progress_bar.progress(50)
            time.sleep(0.3)
            status.text("Analyzing Bug Report...")
            progress_bar.progress(80)
            time.sleep(0.3)
            status.text("Predicting Severity...")
            progress_bar.progress(100)

            with st.spinner("🧠 BERT is analyzing the bug report..."):
                result = predict_severity(text)

            status.empty()
            progress_bar.empty()
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
                st.metric("🤖 Model", "BERT")
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
st.divider()
st.markdown(
    """
<div style="background:#10233c;padding:25px;border-radius:12px;border:1px solid #00d4ff;">
<h2 style="color:white;margin-bottom:10px;">🛡️ AI-Powered Bug Severity Predictor</h2>
<p style="color:white;">Developed by: <b>Ahana Arora</b> & <b>Palak Khanna</b></p>
<hr>
<h3 style="color:white;">🚀 Tech Stack</h3>
<p style="color:white;font-size:16px;font-weight:600;line-height:2;">
🤖 BERT (Transformer Model)<br>
⚡ FastAPI<br>
🎨 Streamlit<br>
🔥 PyTorch<br>
🐍 Python
</p>
<hr>
<p style="color:white;"><b>Version:</b> 1.0</p>
<p style="color:white;">© 2026 All Rights Reserved.</p>
</div>
""",
    unsafe_allow_html=True,
)

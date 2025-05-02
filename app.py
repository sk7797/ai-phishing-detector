import streamlit as st
from email_parser import extract_email_content
from phishing_rules import rule_based_analysis
from ai_analysis import ai_phishing_check

st.title("📧 AI-Powered Phishing Email Detector (Offline)")
st.markdown("Paste your email or upload `.eml` file to detect phishing signs.")

# Upload file
uploaded_file = st.file_uploader("Upload .eml file", type=["eml"])

if uploaded_file:
    raw_email = uploaded_file.read().decode("utf-8")
else:
    raw_email = st.text_area("Or paste raw email content here")

if st.button("Analyze"):
    if not raw_email.strip():
        st.warning("Please provide email content.")
    else:
        subject, sender, body, links = extract_email_content(raw_email)
        rule_score = rule_based_analysis(subject, sender, body, links)
        ai_result = ai_phishing_check(body)

        st.subheader("🔍 Detection Result")
        st.write(f"**Rule-Based Score:** {rule_score}")
        st.write(f"**AI Verdict:** {ai_result}")

        st.subheader("📨 Email Body")
        st.code(body[:1000])

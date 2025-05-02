# 🛡 AI-Powered Phishing Email Detector

This project detects phishing and spam emails using an **offline rule-based system** and a simple web interface built with **Streamlit**.

It parses email content, identifies obfuscated text and suspicious language patterns, and gives a phishing verdict without relying on cloud APIs or machine learning models.

---

## 🚀 Features

- ✅ Offline email phishing detection
- 📥 Accepts `.eml` file uploads or pasted email content
- 📊 Detects:
  - Obfuscated spam
  - Enhancement/medical scams
  - Financial fraud
  - Clickbait and phishing phrases
- ⚡ Fast, lightweight, privacy-respecting

---

## 🛠 Setup & Run Locally

```bash
git clone https://github.com/sk7797/ai-phishing-detector.git
cd ai-phishing-detector
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py

## 📜 License

This project is licensed under the [MIT License](LICENSE) © Soham Kandhare

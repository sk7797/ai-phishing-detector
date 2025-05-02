import pandas as pd
from email_parser import extract_email_content
from phishing_rules import rule_based_analysis
from ai_analysis import ai_phishing_check

# Load and preprocess datasets
phish_df = pd.read_csv('phishing_email.csv')
enron_df = pd.read_csv('Enron.csv')

phish_df = phish_df.rename(columns={'text_combined': 'body'})
enron_df = enron_df.rename(columns={'body': 'body'})

phish_df['label'] = 1
enron_df['label'] = 0

phish_df['subject'] = ''
enron_df['subject'] = enron_df['subject'].fillna('')

combined_df = pd.concat([phish_df, enron_df], ignore_index=True).sample(10)

# Run detection
for idx, row in combined_df.iterrows():
    raw_email = f"Subject: {row['subject']}\n\n{row['body']}"
    subject, sender, body, links = extract_email_content(raw_email)
    score = rule_based_analysis(subject, sender, body, links)
    ai_result = ai_phishing_check(body)

    print("\n--- Email #", idx, "---")
    print(f"Actual Label: {'Phishing' if row['label'] == 1 else 'Legitimate'}")
    print(f"Rule-Based Score: {score}")
    print(f"AI Result: {ai_result}")
    print("EMAIL BODY SAMPLE:")
    print(body[:500])  # print first 500 characters for review


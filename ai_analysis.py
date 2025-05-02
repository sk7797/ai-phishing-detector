import re

def ai_phishing_check(body_text):
    body = body_text.lower()
    score = 0
    reasons = []

    # Check for obfuscated words (e.g., viiagrra, cllick)
    if re.search(r'([a-z])\1{2,}', body):
        score += 1
        reasons.append("obfuscated text")

    # Spammy terms (expanded for drug, enhancement, financial, urgency)
    keyword_groups = {
        "enhancement": ["orgasm", "sperm", "viiagrra", "ciallis", "erection", "enlargement", "manhood", "cum"],
        "financial": ["get rich", "investment opportunity", "win money", "lottery", "free cash"],
        "sales": ["click here", "buy now", "special offer", "discount", "limited time", "prescription free"],
        "weightloss": ["lose weight", "fat burner", "adipren", "burn fat", "diet pill"]
    }

    for category, words in keyword_groups.items():
        for word in words:
            if word in body:
                score += 1
                reasons.append(f"{category}: {word}")

    # Final verdict
    if score >= 3:
        return f"⚠️ Likely Spam/Phishing ({score}): " + ", ".join(reasons)
    elif score == 2:
        return f"⚠️ Suspicious ({score}): " + ", ".join(reasons)
    elif score == 1:
        return f"⚠️ Possibly Suspicious (1): " + reasons[0]
    else:
        return "✅ No obvious phishing content"

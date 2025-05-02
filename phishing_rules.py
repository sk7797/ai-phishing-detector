def rule_based_analysis(subject, sender, body, links):
    score = 0
    keywords = ['verify', 'account update', 'click here', 'urgent', 'password', 'login']
    suspicious_domains = ['bit.ly', 'tinyurl', 'ow.ly']

    for word in keywords:
        if word in body.lower():
            score += 1

    for link in links:
        if any(domain in link for domain in suspicious_domains):
            score += 1

    return score

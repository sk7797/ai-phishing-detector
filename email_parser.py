import re
from email import message_from_string

def get_email_body(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                return part.get_payload(decode=True).decode(errors='ignore')
    else:
        return msg.get_payload(decode=True).decode(errors='ignore')
    return ""

def extract_email_content(raw_email):
    msg = message_from_string(raw_email)
    subject = msg['subject'] or ""
    sender = msg['from'] or ""
    body = get_email_body(msg)
    links = re.findall(r'https?://\S+', body)
    return subject, sender, body, links

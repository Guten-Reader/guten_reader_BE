import re

def clean_text(text):
    text = text.replace('\r', ' ')
    text = text.replace('\n', ' ')
    text = re.sub(r' {2,}', ' ', text)
    return text
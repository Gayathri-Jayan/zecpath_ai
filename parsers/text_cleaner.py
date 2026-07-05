import re

def clean_text(text):

    text = text.lower()

    # Remove unwanted symbols
    text = re.sub(r'[^\w\s@.+#\-\n]', ' ', text)

    # Remove extra spaces BUT preserve newlines
    text = re.sub(r'[ ]+', ' ', text)

    # Remove extra blank lines
    text = re.sub(r'\n+', '\n', text)

    return text.strip()
import re

def clean_text(text):
    """Remove unwanted characters and normalize spacing."""
    text = re.sub(r'\s+', ' ', text)
    text = text.replace("\n", " ")
    text = text.strip()
    return text

def split_text(text, max_words=300):
    """Split long text into safe chunks for the model."""
    words = text.split()
    chunks = []

    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i + max_words])
        chunks.append(chunk)

    return chunks

def clean_summary(summary):
    """Remove repeated spaces, sentences, or artifacts."""
    summary = summary.strip()
    summary = re.sub(r'\s+', ' ', summary)
    summary = summary.replace(" .", ".")
    return summary

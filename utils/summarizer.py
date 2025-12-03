from transformers import pipeline

def load_model():
    summarizer = pipeline(
        "summarization",
        model="facebook/bart-large-cnn"
    )
    return summarizer

def summarize_text(text, model, length_type="Medium", temperature=1.0):
    """Summarize text with adjustable length and creativity."""

    if length_type == "Short":
        min_len, max_len = 30, 80
    elif length_type == "Medium":
        min_len, max_len = 60, 150
    else:
        min_len, max_len = 120, 300

    summary = model(
        text,
        min_length=min_len,
        max_length=max_len,
        do_sample=True if temperature > 1 else False,
        temperature=temperature
    )

    return summary[0]["summary_text"]


def convert_to_bullets(summary):
    """Convert paragraph summary → bullet-point summary."""
    sentences = summary.split(". ")
    bullets = "\n".join([f"• {s.strip()}" for s in sentences if len(s.strip()) > 3])
    return bullets

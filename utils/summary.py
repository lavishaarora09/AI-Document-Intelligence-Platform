from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

def generate_summary(text):

    if len(text) < 100:
        return text

    summary = summarizer(
        text[:3000],
        max_length=150,
        min_length=50,
        do_sample=False
    )

    return summary[0]["summary_text"]
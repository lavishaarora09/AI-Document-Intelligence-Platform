import re
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download("stopwords")

def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z\s]', '', text)

    words = word_tokenize(text)

    stop_words = set(stopwords.words("english"))

    cleaned_words = [
        word for word in words
        if word not in stop_words
    ]

    cleaned_text = " ".join(cleaned_words)

    return cleaned_text
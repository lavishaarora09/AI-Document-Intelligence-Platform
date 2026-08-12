import re

def document_statistics(text, total_pages, keywords):

    total_characters = len(text)

    total_words = len(text.split())

    sentences = re.split(r'[.!?]+', text)
    total_sentences = len([s for s in sentences if s.strip()])

    reading_time = round(total_words / 200, 2)

    stats = {
        "Pages": total_pages,
        "Characters": total_characters,
        "Words": total_words,
        "Sentences": total_sentences,
        "Keywords": len(keywords),
        "Reading Time": reading_time
    }

    return stats
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(text, num_keywords=10):

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform([text])

    feature_names = vectorizer.get_feature_names_out()

    scores = tfidf_matrix.toarray()[0]

    keyword_scores = list(zip(feature_names, scores))

    keyword_scores = sorted(
        keyword_scores,
        key=lambda x: x[1],
        reverse=True
    )

    keywords = []

    for word, score in keyword_scores[:num_keywords]:
        keywords.append(word)

    return keywords
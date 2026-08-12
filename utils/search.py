def search_text(text, query):

    query = query.lower()

    lines = text.split("\n")

    results = []

    for line in lines:
        if query in line.lower():
            results.append(line)

    return results
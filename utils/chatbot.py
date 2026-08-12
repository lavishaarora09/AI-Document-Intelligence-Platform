def chatbot_response(text, question):

    question = question.lower()

    sentences = text.split(".")

    for sentence in sentences:

        if any(word in sentence.lower() for word in question.split()):

            return sentence.strip()

    return "Sorry, I could not find the answer in this document."
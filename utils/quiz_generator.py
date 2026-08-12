import random

def generate_quiz(keywords):

    quiz = []

    for word in keywords[:5]:

        question = {
            "question": f"What is related to '{word}'?",
            "options": [
                word,
                "Python",
                "Database",
                "Network"
            ],
            "answer": word
        }

        random.shuffle(question["options"])

        quiz.append(question)

    return quiz
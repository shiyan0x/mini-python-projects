import json

filename = "questions.json"

def add_question():
    question = input("Enter your question: ")
    answer = input("Enter your answer: ")
    data = {"question": question, "answer": answer}
    try:
        with open(filename, "r") as f:
            content = jason.load(f)
    except:
        content = []

    content.append(data)
    with open(filename, "w") as f:
        json.dump(content, f, indent=4)

add_question()
import json

filename = "questions.json"

def add_question():
    question = input("Enter your question: ")
    answer = input("Enter your answer: ")
    data = [question, answer]
    try:
        with open(filename, "r") as f:
            content = json.load(f)
    except:
        content = []

    content.append(data)
    with open(filename, "w") as f:
        json.dump(content, f, indent=4)

while True:
    add_question()
    choice = input("Do you want to add another question?: ")
    if choice.lower() != "yes" and choice.lower() != "y":
        break

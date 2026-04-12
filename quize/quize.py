import random 
import json

with open("questions.json", "r") as f:
    questions = json.load(f)

print("simple quize")
print("You want play quize ?")
print("yes/no")
choice = input()
if choice.lower().strip() != "yes":
    print("ok bye")
    quit()

print("ok lets play")
score = 0

quize = random.sample(questions, 5)
for q, a in quize:
    answer = input(q)
    if answer.lower().strip() == a:
        print("correct")
        score += 1
    else:
        print("wrong")


print(f"you got {score} out of 5 points")


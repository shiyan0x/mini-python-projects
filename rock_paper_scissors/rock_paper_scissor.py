import random

option = [ "rock", "paper", "scissors"]
score = 0
computer_score = 0

print("welcome to rock paper scissors")
print("you want play quize ?")
print("yes/no")
choice = input()
if choice.lower().strip() != "yes":
    print("ok bye")
    quit()

while True:
    user_input = input("Enter your choice (rock/paper/scissors): ")
    if user_input not in option:
        print("Invalid input. Please try again.")
        continue
    computer_input = random.choice(option)
    print("Computer chose:", computer_input)
    if user_input == computer_input:
        print("It's a tie!")
    elif (user_input == "rock" and computer_input == "scissors") or \
         (user_input == "paper" and computer_input == "rock") or \
         (user_input == "scissors" and computer_input == "paper"):
        print("You win!")
        score += 1
    else:
        print("Computer wins!")
        computer_score += 1
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break

print(f"You scored {score} points")
print(f"Computer scored {computer_score} points")

if score > computer_score:
    print("You win!")
elif score < computer_score:
    print("Computer wins!")
else:
    print("It's a tie!")
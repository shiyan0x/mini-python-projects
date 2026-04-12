import random

r = input("Enter the maximm number (range 0 to ?): ")

if r.isdigit() :
    r = int(r)
    random_number = random.randrange(0,r)
else:
    print("please enter the dight")
    quit()

score = 0

while True:
    score += 1
    choice = int(input("guess the number :"))       
    if choice == random_number:
        print("congratulation! You found the number")
        break
    elif choice > random_number:
        print("your guess is greater than the number.")
    else:
        print("Your guess is lower than the number.")

print(f"you take {score} attempt")
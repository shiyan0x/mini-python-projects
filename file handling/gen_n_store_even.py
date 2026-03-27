import random 

N = int(input("how many number want to generate: "))
low = int(input("enter low limit :"))
high = int(input("enter high limit :"))

with open("even.txt", "w") as file :
  for i in range(N):
    num = random.randint(low, high)
    print("generated number :", num)
    if num % 2 == 0:
      file.write(str(num)+ "\n")

print("store even number in even file")
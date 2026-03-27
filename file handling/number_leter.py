letter = 0
digit = 0

with open("input.txt", "r") as f:
    for line in f:
        for char in line:
            if char.isalpha():
                letter += 1
            elif char.isdigit():
                digit += 1

print("Letters:", letter)
print("Digits:", digit)

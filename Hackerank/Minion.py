def minion_game(s):
    vowels = "AEIOU"
    kevin = 0
    stuart = 0

    n = len(s)

    for i in range(n):
        points = n - i

        if s[i] in vowels:
            kevin += points
        else:
            stuart += points

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")



if __name__ == '__main__':
    s = input()
    minion_game(s)
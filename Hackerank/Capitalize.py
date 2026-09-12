"""def captalie(s):
    words = s.split()
    fw1 = words[0]
    fc1 = fw1[0].upper()
    print(fc1)

    fw2 = words[1]
    fc2 = fw2[0].upper()
    print(fc2)

    print(fc1 + "".join(fw1[1:]) + " "+ fc2 + "".join(fw2[1:]))

if __name__ == "__main__":
    s = input()
    captalie(s)"""


import os


"""def solve(s):
    # Capitalize first letter of every word, preserve original spacing
    result = " ".join(word.capitalize() for word in s.split())
    return result


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)"""

def solve(s):
    words = s.split(" ")
    result = []

    for word in words:
        if word:
            word = word[0].upper() + word[1:]
        result.append(word)

    return " ".join(result)


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
import string


def print_rangoli(size):
    alphabet = string.ascii_lowercase

    lines = []
    for i in range(size):
        s = "-".join(alphabet[i:size])
        row = s[::-1] + s[1:]
        lines.append(row.center(4 * size - 3, "-"))

    rangoli = "\n".join(lines[::-1] + lines[1:])
    print(rangoli)


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
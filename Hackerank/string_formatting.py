def print_formatted(number):
    # Calculate padding width based on binary length of 'number'
    width = len(bin(number)[2:])

    for i in range(1, number + 1):
        dec_val = str(i)
        oct_val = oct(i)[2:]
        hex_val = hex(i)[2:].upper()
        bin_val = bin(i)[2:]

        # Print all values right-aligned to 'width' separated by space
        print(
            f"{dec_val.rjust(width)} {oct_val.rjust(width)} {hex_val.rjust(width)} {bin_val.rjust(width)}"
        )


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
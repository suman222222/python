def sum_of_digits(num_string):
    total = 0

    for ch in num_string:
        if ch.isdigit():
            total += int(ch)

    print("Sum:", total)


# Example
sum_of_digits("24453")

def count_vowels_consonants(word):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in word:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    print(f"Word: {word}")
    print(f"Vowels: {vowel_count}")
    print(f"Consonants: {consonant_count}")

# Example usage
count_vowels_consonants("Hello World")

#char.isalpha() — filters out non-letter characters (spaces, punctuation)
#char.isdigit() — filters out non-digit characters, making it safe for mixed strings like "a1b2c3"
#A generator expression with sum() for a clean, Pythonic one-liner in problem 2

def sum_of_digits(number_string):
    total = sum(int(ch) for ch in number_string if ch.isdigit())
    print(f"Number string: {number_string}")
    print(f"Sum of digits: {total}")

# Example usage
user_input = input("Enter a string of numbers: ")
sum_of_digits(user_input)





def count_vowels_consonants(sumankapri):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0

    for ch in sumankapri:
        if ch.isalpha():   # check only letters
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1

    print("Vowels:", v_count)
    print("Consonants:", c_count)


# Example
count_vowels_consonants("HelloWorld")

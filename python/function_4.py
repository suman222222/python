def vowel_count(s):
    ''' takes a word as input and counts vowels and consonants '''
    vowels = 0        
    consonants = 0

    for each in s:
        if each.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

    print("Word:", s)
    print("Vowel count:", vowels)        
    print("Consonant count:", consonants) 

word = input("Enter a word: ")
vowel_count(word)

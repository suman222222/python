#a function that takes a word as input and counts the number of vowels and consonents present in the word
word=input("enter a word :")

def vowel_count(s):
    ''' takes a word as input and counts vowels and consonants '''
    for each in s:
        if each.lower() in "aeiou":
            vowel_count += 1
        else:
            consonant_count +=1
    print("Word:",word)
    print("Vowel count:", vowel_count)
    print("Consonant count:",consonant_count)

vowel_count(word)
    

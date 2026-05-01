word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

common = []

for letter in word1:
    if letter in word2:
        if letter not in common:  
            common.append(letter)
            
print("Common letters:", common)

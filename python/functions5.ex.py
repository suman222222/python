word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

def unique_letters(word1, word2):
    '''
    Finds letters unique to each word.
    
    A letter is unique if it appears in one word but NOT in the other.
    
    Parameters:
        word1 (str): first word entered by user
        word2 (str): second word entered by user
    
    Returns:
        unique_to_word1 (list): letters only found in word1
        unique_to_word2 (list): letters only found in word2
    
    Example:
        word1 = "nepal"
        word2 = "english"
        unique_to_word1 → ['n', 'p', 'a']
        unique_to_word2 → ['g', 'i', 's', 'h']
    '''


word1 = word1.lower()
word2 = word2.lower()

unique_to_word1 = []
unique_to_word2 = []

# find letters only in word1
for letter in word1:
    if letter not in word2:
        if letter not in unique_to_word1:
            unique_to_word1.append(letter)

# find letters only in word2
for letter in word2:
    if letter not in word1:
        if letter not in unique_to_word2:
            unique_to_word2.append(letter)

print("Word1:", word1)
print("Word2:", word2)
print("Unique to", word1, ":", unique_to_word1)
print("Unique to", word2, ":", unique_to_word2)

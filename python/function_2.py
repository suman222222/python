#write a function that takes a word as input and determine  whether it is palindrome or not

def is_palindrome(word):
    word = word.lower()
    length = len(word)
    
    for i in range(length // 2):
        if word[i] != word[length - 1 - i]:
            return False
    
    return True

# Examples
print(is_palindrome("hello"))    # False
print(is_palindrome("Madam"))    # True
print(is_palindrome("level"))    # True
print(is_palindrome("world"))    # False

w1=input("Enter a word: ")
w2=input("Enter another word: ")

def is_anagram(word1,word2):
    #String formatting
    
    word1=word1.lower().replace(" ", "")
    
    word2=word2.lower().replace(" ","")
    
    #check length
    
    if len(word1)==len(word2):
        for each in word1:
            if each not in word2:
                print("Not anagram")
                return False
            print(f"{word1} & {word2} are anagram")
    else:
        print("Not anagram")
is_anagram(w1,w2)

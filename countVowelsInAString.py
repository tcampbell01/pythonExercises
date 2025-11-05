def wordInput():
    word = input(f"Please enter a word: ")
    print(f"You chose the word {word}")
    
    countVowels(word)
    
def countVowels(word):
    letter_counter = 0
    for char in word:
        
        if char.lower() in "aeiou":
            letter_counter = letter_counter + 1
            print(f"Found vowel: {char}")
            
    printNumberOfVowels(letter_counter, word)
            
def printNumberOfVowels(letter_counter, word):
    
    print(f"The word {word} has {letter_counter} vowels")
    
wordInput()
            
        
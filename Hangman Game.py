import random

def choose_word():
    words = ["python", "java", "hangman", "computer", "science", "programming"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6  # Number of incorrect guesses allowed
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nWord: ", display_word(word, guessed_letters))
        print(f"Attempts left: {attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good job! That letter is in the word.")
        else:
            print("Wrong guess!")
            attempts -= 1
        
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            return
    
    print("\nGame Over! The correct word was:", word)

# Corrected __name__ check
if __name__ == "__main__":
    hangman()

import random

def choose_word():
    words = ["apple","ball","cat","dog","elephant", "frog", "gun","horse", "icecream","igloo","jug","joker", "hangman", "programming", "computer", "algorithm", "debugging"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")

    while attempts_left > 0:
        print("\nAttempts left:", attempts_left)
        display = display_word(word_to_guess, guessed_letters)
        print("Current word:", display)

        if "_" not in display:
            print("\nCongratulations! You guessed the word:", word_to_guess)
            break

        guess = input("Enter a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word_to_guess:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess.")
                guessed_letters.append(guess)
                attempts_left -= 1
        else:
            print("Invalid input. Please enter a single letter.")

    if attempts_left == 0:
        print("\nSorry, you ran out of attempts. The correct word was:", word_to_guess)

if __name__ == "__main__":
    hangman()

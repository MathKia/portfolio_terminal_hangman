from hangman_art import *  # Import hangman stages (graphics)
from hangman_words import *  # Import word list
from random import choice  # Choose a random word
import os  # For clearing the screen


def replace_blank_w_letter(letter, word, blank_word_list):
    """Replace blanks with the guessed letter if it exists in the word."""
    for n in range(len(word)):
        if letter == word[n]:
            blank_word_list[n] = letter


def hang(stage):
    """Print the hangman stage based on remaining lives."""
    print(stages[stage])


def user_letter_guess(list_of_used_letters):
    """Prompt the user for a letter and check if it's valid."""
    letter = input("Type your letter\n").lower()
    if letter.isalpha():
        if letter in list_of_used_letters:
            print("You already used this letter 👁👄👁")
            return user_letter_guess(list_of_used_letters)  # Recursive call for retry
        else:
            list_of_used_letters.append(letter)
            return letter
    else:
        print("That's not a letter ??? dumb a..")
        return user_letter_guess(list_of_used_letters)  # Recursive call for retry


def game_play():
    """Main game loop for Hangman."""
    while True:  # Loop for replayability
        os.system('cls' if os.name == 'nt' else 'clear')  # Clears screen

        word = choice(word_list)  # Select a random word
        list_of_used_letters = []  # Store guessed letters
        blank_word_list = ['_' for _ in word]  # Initialize blanks

        game_on = True
        lives = len(stages) - 1  # Set initial lives
        hang(lives)  # Display hangman stage

        while game_on:
            if '_' in blank_word_list:  # Check if the word is incomplete
                print(' '.join(blank_word_list))
                letter = user_letter_guess(list_of_used_letters)

                if letter in word:
                    print("😄")  # Correct guess
                    replace_blank_w_letter(letter, word, blank_word_list)
                else:
                    print("🙁")  # Incorrect guess
                    if lives > 0:
                        lives -= 1
                        hang(lives)  # Update hangman
                    if lives == 0:  # Game over condition
                        print(f"You killed him!!!!🤢🤮💀 The word was '{word}'")
                        game_on = False
            else:  # Win condition
                print("You win!! 🎉")
                game_on = False

        play_again = input("Play again? Press 'Y' to restart or any other key to exit. ").lower()
        if play_again != 'y':  # End game if the player doesn't choose to replay
            print("Thanks for playing! 👋")
            break  # Exit the loop, ending the game


game_play()  # Start the game


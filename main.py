from hangman_art import *
from hangman_words import *
from random import *


word = choice(word_list)
print(word)

list_of_used_letters = []

blank_word_list = ['_' for letter in word]


def replace_blank_w_letter(letter):

    for n in range(len(word)):
        if letter == word[n]:
            blank_word_list[n] = letter


def hang(stage):
    print(stages[stage])


def user_letter_guess():

    letter = input("Type your letter\n")
    if letter.isalpha():
        if letter in list_of_used_letters:
            print("You already used this letter 👁👄👁")
            return user_letter_guess()
        else:
            list_of_used_letters.append(letter)
            return letter
    else:
        print("That's not a letter ??? dumb ass")
        return user_letter_guess()


def game_play():

    game_on = True
    lives = len(stages)-1
    hang(lives)

    while game_on:

        if '_' in blank_word_list:
            blanks = ' '.join(blank_word_list)
            print(blanks)
            letter = user_letter_guess()

            if letter in word:
                print("😄")
                replace_blank_w_letter(letter)
            else:
                print("🙁")
                if lives > 0:
                    lives -= 1
                    hang(lives)
                if lives == 0:
                    print("you killed him!!!!🤢🤮💀")
                    game_on = False
        else:
            print("You win!!")
            game_on = False


game_play()

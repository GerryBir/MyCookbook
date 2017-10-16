#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from string import ascii_lowercase


def random_word():
    word = [line.strip().lower() for line in open("/home/gerry/PycharmProjects/wordlist.txt")]
    word = random.choice(word)
    return word


def display_word(word, index):
    displayed_word = "".join([letter if index[i] else '*' for i, letter in enumerate(word)])
    return displayed_word.strip()


def get_next_letter(remaining_letters):
    if len(remaining_letters) == 0:
        raise ValueError("There are no remaining letters")
    while True:
        next_letter = input("Choose next letter: ").lower()
        if len(next_letter) != 1:
            print("{0} is not a single character".format(next_letter))
        elif next_letter not in ascii_lowercase:
            print("{0} is not a letter".format(next_letter))
        elif next_letter not in remaining_letters:
            print("{0} has been guessed already".format(next_letter))
        else:
            remaining_letters.remove(next_letter)
            return next_letter


def hangman():
    attempts = 12
    print('''    This is the game of hangman,the computer will
    choose a random word of any length from a list of 1000
    of the most common words. All words will be lower case and no
    numerals. Your objective will be to guess the random word.
    You will have 12 attempts to guess the hidden word
        ****************Good Luck ****************''')
    print()
    print("Starting a game of hangman....")

    print("Randomly selecting a word....")
    word = random_word()
    print()
    index = [letter not in ascii_lowercase for letter in word]
    remaining_letters = set(ascii_lowercase)
    wrong_letters = []
    word_solved = False

    while attempts > 0 and not word_solved:
        attempts -= 1
        print("Word : {0}".format(display_word(word, index)))
        print("\nRemaining Attempts: {0}".format(attempts))
        print("Previous Guesses: {0}".format("".join(wrong_letters)))
        next_letter = get_next_letter(remaining_letters)

        if next_letter in word:
            print("{0} is in the word!!".format(next_letter))

            for i in range(len(word)):
                if word[i] == next_letter:
                    index[i] = True
        else:
            print("{0} is Not in the Word!!".format(next_letter))

            wrong_letters.append(next_letter)

        if False not in index:
            word_solved = True

        print()

    print("The word is {0}".format(word))

    if word_solved:
        print("Congratulations You Won!")
    else:
        print("Better Luck next time.")

    try_again = input("Would you like to try again if so type ['y'or'Y'] If not press any key to leave")
    return try_again.lower() == 'y'


if __name__ == '__main__':
    while hangman():
        print()

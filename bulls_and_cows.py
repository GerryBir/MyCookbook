#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generate a unique 4 digit number with the random module
Set digits to choose from "123456789"
Set size of choice to = 4
Set guesses_taken to 0
Get input from user and make sure it is 4 digits long with no repeated numbers
compare each digit in the random choice to see if it matches the user choice
if equal add one to the bulls counter, if it is not in the correct position add
1 to the cows counter
"""
import random
import collections
import sys

digits = "123456789"
size = 4
guesses_taken = 0

choice = random.sample(digits, size)  # Random generated number
sys.stdout.write("\033[1;36m")
print('''This is the game of Bulls and Cows, the object of tne game is to guess
the computer generated random number.No number will be the same and all 
will be in the range of 1 to 9. No Zero's!.Enter only digits no letters Good Luck.''')
sys.stdout.write("\033[1;34m")
print("Enter a unique 4 digit number. All numbers must be different and no repeats.")
#  print(choice)
sys.stdout.write("\033[;1m")
while True:
    guess = input("Guess Number"'{}:'.format([guesses_taken])).strip()
    guess = list(guess)
    guess = [s for s in guess if s.isdigit()]

    compare = set(digits).intersection(guess)
    if len(compare) != size:
        print("Numbers must be in the range 1 to 9 No zero's. No letters.")

    if len(guess) != size:
        print("And It must be a 4 digit number! Game over")
        break

    if [item for item, count in collections.Counter(guess).items() if count > 1]:
        print("And a number has been repeated! Game Over.")
        break

    if guess == choice:
        print("Congratulations you guessed correctly in {} attempts".format(guesses_taken))
        break

    bulls, cows = 0, 0
    for digit in range(size):
        if guess[digit] == choice[digit]:
            bulls += 1
        elif guess[digit] in choice:
            cows += 1
    print(f"{bulls} Bulls")
    print(f"{cows} Cows")
    guesses_taken += 1  # Update guesses taken

choice = ",".join(choice)
print(f"The number that you where looking for was {choice}")

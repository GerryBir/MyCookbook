#!/usr/bin/env python
"""
Computer guesses a random number between 1 and 20
User tries to guess the number
Computer tell user whether guess is to high too low or correct
User has 3 guesses before loosing game
"""
import random

'''Game set up'''
user_won = False
number_of_guesses = 3  # user has 3 guesses before loosing the game
print("Welcome to the guessing Game")

'''Computer guesses the random number'''
correct_answer = random.randint(1, 20)
while number_of_guesses > 0:

    '''User tries to guess the answer'''
    user_guess = input("Guess my number? ")
    user_guess = int(user_guess)

    '''Computer tell user whether guess was too high or low'''
    if user_guess == correct_answer:
        print("Good guess ")
        print("You are correct")
        user_won = True  # update variable to be true
        break
    elif user_guess > correct_answer:
        print("Sorry you guessed too high ")
    elif user_guess < correct_answer:
        print("Sorry you guessed to low")

    number_of_guesses -= 1
if user_won:
    print("You Win")
else:
    print("You loose")

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Generic greeting for users"""
def greet_user():
    print("Hello")
    print("Welcome")


def greet_user_by_name(name,greeting):  # you can give the arguments a default value: name = 'user',greeting='hello'
    """Customised greeting """
    print(greeting + "," + name)

def cube(base_number):
    cubed_value = base_number * base_number * base_number
    return cubed_value



greet_user()
greet_user_by_name(input('What is your name? '),'Welcome')

eleven_cube = cube(11)
print(eleven_cube)

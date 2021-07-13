#!/usr/bin/env python

import prompt


def welcome_user():
    print("Welcome to the Brain Games, my dear friend!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}'.format(name))
    return name

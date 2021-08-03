#!/usr/bin/env python

from random import randint

question_text = ('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(number):

    if number % 2 == 0:
        return True
    return False


def get_question_and_answer():
    question = randint(1, 1000)
    right_answer = "no"

    if is_even(question) is True:
        right_answer = "yes"

    return question, right_answer

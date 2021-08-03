#!/usr/bin/env python

from random import randint

question_text = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    divider = 2

    if number < 2:
        return False

    while divider <= number / 2:

        if number % divider == 0:
            return False

        divider += 1

    return True


def get_question_and_answer():
    question = randint(1, 50)
    right_answer = "no"

    if is_prime(question) is True:
        right_answer = "yes"

    return question, right_answer

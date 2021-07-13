#!/usr/bin/env python

from random import randint

question_text = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    number = randint(1, 50)

    if prime_calc(number) is True:
        right_answer = "yes"

    else:
        right_answer = "no"

    question = ("Question: {}".format(number))

    return question, right_answer


def prime_calc(number):
    divider = 2

    if number < 2:
        return False

    while divider <= number / 2:

        if number % divider == 0:
            return False

        divider += 1

    return True

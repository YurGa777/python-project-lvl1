#!/usr/bin/env python

from random import randint

question_text = ('Answer "yes" if the number is even, otherwise answer "no".')


def get_question_and_answer():
    number = randint(1, 1000)

    if number % 2 == 0:
        right_answer = "yes"

    else:
        right_answer = "no"

    question = ("Question: {} ".format(number))

    return question, right_answer

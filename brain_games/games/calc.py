#!/usr/bin/env python

from random import choice, randint

question_text = 'What is the result of the expression?'


def get_question_and_answer():
    number_one = randint(1, 100)
    number_two = randint(1, 100)
    operation = choice('+-*')

    if operation == '+':
        right_answer = number_one + number_two

        question = "Question: {} + {}".format(number_one, number_two)

    elif operation == '-':
        right_answer = number_one - number_two

        question = "Question: {} - {}".format(number_one, number_two)

    else:
        right_answer = number_one * number_two

        question = "Question: {} * {}".format(number_one, number_two)

    return question, right_answer

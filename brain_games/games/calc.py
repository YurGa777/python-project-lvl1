#!/usr/bin/env python

from random import choice, randint


question_text = 'What is the result of the expression?'


def get_expression(number_one, number_two, operation):

    if operation == '+':
        result = number_one + number_two

    elif operation == '-':
        result = number_one - number_two

    else:
        result = number_one * number_two

    return result


def get_question_and_answer():
    first_number = randint(1, 10)
    second_number = randint(1, 10)
    symbol = choice('+-*')

    question = '{} {} {}'.format(first_number, symbol, second_number)
    right_answer = str(get_expression(first_number, second_number, symbol))

    return question, right_answer

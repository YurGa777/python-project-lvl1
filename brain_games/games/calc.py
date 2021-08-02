#!/usr/bin/env python

from random import choice, randint


question_text = 'What is the result of the expression?'


def get_expression():
    number_one = randint(1, 10)
    number_two = randint(1, 10)
    operation = choice('+-*')

    expression = '{} {} {}'.format(number_one, operation, number_two)

    if operation == '+':
        result = number_one + number_two

    elif operation == '-':
        result = number_one - number_two

    else:
        result = number_one * number_two

    result = str(result)

    return expression, result


def get_question_and_answer():

    question, right_answer = get_expression()

    return question, right_answer

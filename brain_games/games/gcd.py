#!/usr/bin/env python

from random import randint

question_text = 'Find the greatest common divisor of given numbers'


def get_question_and_answer():
    number_one = randint(1, 50)
    number_two = randint(1, 50)

    question = ("Question: {} {}".format(number_one, number_two))

    right_answer = get_gcd(number_one, number_two)

    return question, right_answer


def get_gcd(number_one, number_two):

    if number_one >= number_two:
        common_div = number_two

    else:
        common_div = number_one

    while common_div > 0:

        if number_two % common_div == 0 and number_one % common_div == 0:
            return common_div

        common_div -= 1

    return common_div

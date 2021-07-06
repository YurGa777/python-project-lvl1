#!/usr/bin/env python

from random import randint

question_text = 'What is the result of the expression?'


def get_question_and_answer():

    number_one = randint(1, 100)
    number_two = randint(1, 100)
    random_operation = randint(1, 3)

    if random_operation == 1:
        right_answer = number_one + number_two
        question = "Question: {} + {}".format(number_one, number_two)

    elif random_operation == 2:
        right_answer = number_one - number_two
        question = "Question: {} - {}".format(number_one, number_two)

    else:
        right_answer = number_one * number_two
        question = "Question: {} * {}".format(number_one, number_two)

    return question, right_answer


def main():
    get_question_and_answer()


if __name__ == '__main__':
    main()

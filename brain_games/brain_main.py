#!/usr/bin/env python

import prompt


def welcome_user():
    print("Welcome to the Brain Games, my dear friend!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}'.format(name))
    return name


def get_user_answer(question):
    print("Question: {}".format(question))
    answer = prompt.string('Your answer: ')
    return answer


def game_engine(game_module):

    name = welcome_user()

    print(game_module.question_text)

    number_of_attempts = 3
    attempt_count = 1

    while attempt_count <= number_of_attempts:
        question, right_answer = game_module.get_question_and_answer()
        answer = get_user_answer(question)

        if answer == right_answer:
            print('Correct !')
            attempt_count += 1

        else:
            print("'{}' is wrong answer ;(.".format(answer))
            print("Correct answer was '{}'.".format(right_answer))
            print("Let's try again, {}!".format(name))

            return

    return print('Congratulations, {}!'.format(name))

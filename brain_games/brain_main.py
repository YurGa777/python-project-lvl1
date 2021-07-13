#!/usr/bin/env python

import prompt
from brain_games.cli import welcome_user


def game_engine(game_module):

    name = welcome_user()

    print(game_module.question_text)

    attempt_number = 1

    while attempt_number <= 3:
        question, right_answer = game_module.get_question_and_answer()
        print(question)
        answer = prompt.string('Your answer: ')

        if str(answer) == str(right_answer):
            print('Correct !')

        else:
            return print(''''{}' is wrong answer ;(. Correct answer was '{}'.
Let's try again, {}!'''.format(answer, right_answer, name))
        attempt_number = attempt_number + 1
    return print('Congratulations, {}!'.format(name))

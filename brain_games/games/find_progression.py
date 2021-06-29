#!/usr/bin/env python

from random import randint
import prompt
from brain_games.cli import welcome_user

name = welcome_user()


def find_progression():

    # Giving number of attemts
    attempt_number = 1

    print('What number is missing in the progression?')

# generating progression parameters
    while attempt_number <= 3:
        number_start = randint(1, 50)
        progression_int = randint(1, 10)
        number_quantity = randint(5, 10)
        number_stop = number_start + number_quantity * progression_int

# generating progression
        progression = list(range(number_start, number_stop, progression_int))

# generating random position in progression
        missed_number_count = randint(0, number_quantity - 1)

# saving right answer
        right_answer = progression[missed_number_count]

# hiding right answer
        progression[missed_number_count] = ".."

# transforming progresiion from list into string
        progression_text = str('')
        for i in progression:
            progression_text = progression_text + str(i) + ' '

        print("Question: {}".format(progression_text))

        answer = prompt.string('Your answer: ')

        if answer == str(right_answer):
            print('Correct !')

        else:
            return print(''''{}' is wrong answer ;(. Correct answer was '{}'.
Let's try again, {}!'''.format(answer, right_answer, name))
        attempt_number = attempt_number + 1
    return print('Congratulations, {}!'.format(name))


def main():
    find_progression()


if __name__ == '__main__':
    main()

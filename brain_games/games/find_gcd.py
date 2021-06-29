#!/usr/bin/env python

from random import randint
import prompt
from brain_games.cli import welcome_user
from brain_games.gcd_calc import gcd_calc

name = welcome_user()


def find_gcd():

    # Giving number of attemts
    attempt_number = 1


# Finding right answer
    print('Find the greatest common divisor of given numbers')
    while attempt_number <= 3:
        number_one = randint(1, 50)
        number_two = randint(1, 50)

        print("Question: {} {}".format(number_one, number_two))

        right_answer = gcd_calc(number_one, number_two)

        answer = prompt.string('Your answer: ')

        if answer == str(right_answer):
            print('Correct !')

        else:
            return print(''''{}' is wrong answer ;(. Correct answer was '{}'.
Let's try again, {}!'''.format(answer, right_answer, name))
        attempt_number = attempt_number + 1
    return print('Congratulations, {}!'.format(name))


def main():
    find_gcd()


if __name__ == '__main__':
    main()

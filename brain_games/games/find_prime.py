#!/usr/bin/env python

from random import randint
import prompt
from brain_games.cli import welcome_user
from brain_games.prime_calc import prime_calc

name = welcome_user()


def find_prime():

    # Giving number of attemts
    attempt_number = 1


# Finding right answer
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while attempt_number <= 3:
        number = randint(1, 50)

        if prime_calc(number) is True:
            right_answer = "yes"

        else:
            right_answer = "no"

        print("Question: {}".format(number))
        answer = prompt.string('Your answer: ')

        if str.lower(answer) == right_answer:
            print('Correct !')

        else:
            return print(''''{}' is wrong answer ;(. Correct answer was '{}'.
Let's try again, {}!'''.format(answer, right_answer, name))
        attempt_number = attempt_number + 1
    return print('Congratulations, {}!'.format(name))


def main():
    find_prime()


if __name__ == '__main__':
    main()

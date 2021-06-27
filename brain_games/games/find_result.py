#!/usr/bin/env python

from random import randint
import prompt
from brain_games.cli import welcome_user

name = welcome_user()


def find_result():

    # Giving number of attemts
    attempt_number = 1


# Finding right answer
    print('What is the result of the expression?')
    while attempt_number <= 3:
        number_one = randint(1, 100)
        number_two = randint(1, 100)
        random_operation = randint(1, 3)

        if random_operation == 1:
            right_answer = number_one + number_two
            print("Question: {} + {}".format(number_one, number_two))

        elif random_operation == 2:
            right_answer = number_one - number_two
            print("Question: {} - {}".format(number_one, number_two))
        else:
            right_answer = number_one * number_two
            print("Question: {} * {}".format(number_one, number_two))

        answer = prompt.string('Your answer: ')

        if answer == str(right_answer):
            print('Correct !')

        else:
            return print(''''{}' is wrong answer ;(. Correct answer was '{}'.
Let's try again, {}!'''.format(answer, right_answer, name))
        attempt_number = attempt_number + 1
    return print('Congratulations, {}!'.format(name))


def main():
    find_result()


if __name__ == '__main__':
    main()

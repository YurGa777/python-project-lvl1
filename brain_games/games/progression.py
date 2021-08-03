#!/usr/bin/env python

from random import randint

question_text = 'What number is missing in the progression?'


def get_progression(first_namber, interval, quantity):

    number_stop = first_namber + quantity * interval

# generating progression
    progression = list(range(first_namber, number_stop, interval))

    return progression


def get_question_and_answer():
    start_number = randint(1, 50)
    step = randint(1, 10)
    num_quantity = randint(5, 10)

    brain_progression = get_progression(start_number, step, num_quantity)

# generating random position in progression
    missed_number_count = randint(0, num_quantity - 1)

# saving right answer
    right_answer = str(brain_progression[missed_number_count])

# hiding right answer
    brain_progression[missed_number_count] = ".."

# transforming progresiion list into question string
    question = str('')

    for i in brain_progression:
        question += str(i) + ' '

    question = question[:-1]

    return question, right_answer

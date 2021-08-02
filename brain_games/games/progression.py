#!/usr/bin/env python

from random import randint

question_text = 'What number is missing in the progression?'


def generate_progression():
    number_start = randint(1, 50)
    progression_int = randint(1, 10)
    number_quantity = randint(5, 10)
    number_stop = number_start + number_quantity * progression_int

# generating progression
    progression = list(range(number_start, number_stop, progression_int))

# generating random position in progression
    missed_number_count = randint(0, number_quantity - 1)

# saving right answer
    missed_number = str(progression[missed_number_count])

# hiding right answer
    progression[missed_number_count] = ".."

# transforming progresiion from list into string
    progression_text = str('')

    for i in progression:
        progression_text += str(i) + ' '

    progression_text = progression_text[:-1]

    return progression_text, missed_number


def get_question_and_answer():

    question, right_answer = generate_progression()

    return question, right_answer

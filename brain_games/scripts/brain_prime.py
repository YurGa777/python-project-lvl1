#!/usr/bin/env python

from brain_games.games.find_prime import get_question_and_answer
from brain_games.games.find_prime import question_text
from brain_games.games.brain_main import game_engine


def main():
    game_engine(question_text, get_question_and_answer)


if __name__ == '__main__':
    main()

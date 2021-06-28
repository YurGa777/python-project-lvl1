#!/usr/bin/env python


def prime_calc(number):

    divider = 2

    if number < 2:
        return False

    while divider <= number / 2:

        if number % divider == 0:
            return False

        divider += 1

    return True

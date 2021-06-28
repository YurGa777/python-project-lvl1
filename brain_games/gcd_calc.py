#!/usr/bin/env python


def gcd_calc(number_one, number_two):
    if number_one >= number_two:
        common_div = number_two
    else:
        common_div = number_one

    while common_div > 0:
        if number_two % common_div == 0 and number_one % common_div == 0:
            return common_div
        common_div -= 1

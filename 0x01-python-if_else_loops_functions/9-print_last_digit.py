#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    lastdigit = number % 10
    print("{}\n".format(lastdigit))
    return lastdigit

#!/usr/bin/python3
def print_last_digit(number):
    '''prints the last digit of a number'''
    ld = abs(number) % 10
    print(f"{ld}", end='')
    return (ld)

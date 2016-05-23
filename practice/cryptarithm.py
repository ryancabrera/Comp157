"""
    Based off of solution here:
        https://programmingpraxis.com/2012/07/31/send-more-money-part-1/
"""

import random
import string
import itertools
__author__ = 'Ryan Cabrera'


def main():
    word_1 = list("send")
    word_2 = list("more")
    letters = set(word_1 + word_2)
    print(letters)
    rand_numbers = random.sample(range(1, 27), 26)
#   print(len(rand_numbers), rand_numbers)

    nums_and_chars = zip(rand_numbers, string.ascii_lowercase)

    for value in nums_and_chars:
        num_val = value[0]
        #print(num_val)

        for numbers_to_check in range(num_val):
            newval = 0

    #print(solve2())


def solve2():
    letters = ('s', 'e', 'n', 'd', 'm', 'o', 'r', 'y')
    digits = range(10)
    pv = itertools.permutations(digits, len(letters))
    print(pv)

    for x in pv:
        for y in x:
            print(y)

    for perm in pv:
        sol = dict(zip(letters, perm))
        if sol['s'] == 0 or sol['m'] == 0:
            continue
        send = 1000 * sol['s'] + 100 * sol['e'] + 10 * sol['n'] + sol['d']
        more = 1000 * sol['m'] + 100 * sol['o'] + 10 * sol['r'] + sol['e']
        money = 10000 * sol['m'] + 1000 * sol['o'] + 100 * sol['n'] + 10 * sol['e'] + sol['y']
        if send + more == money:
            return send, more, money


if __author__:
    main()
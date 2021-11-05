#!/usr/bin/env python3

import random

__author__ = 'Buğra Kağan Acar'


def main():
    target: int = random.randint(0, 100)

    guess: int = -1  # outside of target range
    while guess != target:
        guess: int = int(input('Guess: '))
        verb: str = 'Increase' if target > guess else 'Decrease'
        print(f'{verb} your number!')

    print('Correct!')


if __name__ == '__main__':
    main()


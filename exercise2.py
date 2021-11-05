#!/usr/bin/env python3

import random

__author__ = 'Buğra Kağan Acar'


def main():
    target: int = random.randint(0, 100)

    # := is the walrus operator, not shown in lectures but it both
    # assigns and returns the value as an expression.
    while (guess := int(input('Guess: '))) != target:
        verb: str = 'Increase' if target > guess else 'Decrease'
        print(f'{verb} your number!')

    print('Correct!')


if __name__ == '__main__':
    main()


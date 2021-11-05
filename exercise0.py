#!/usr/bin/env python3

__author__ = 'Buğra Kağan Acar'


def main():
    # Based on summation formulas for arithmetic sequences.
    # I would normally go in to more detail documenting the script,
    # but I am a bit constrained on time at the moment so I'll do
    # the assignments as fast as possible instead.
    target: int = int(input('Number: '))

    odd_sum: int = int((target + 1) / 2) ** 2
    print('Sum of odd numbers:', odd_sum)

    even_sum: int = target * (target + 1) / 2 - odd_sum
    even_count: int = int((target - 2) / 2 + 1)
    print('Average of even numbers:', even_sum // even_count)


if __name__ == '__main__':
    main()


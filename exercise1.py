#!/usr/bin/env python3

__author__ = 'Buğra Kağan Acar'


def is_valid_email(text: str) -> bool:
    # This is not exactly a good way to test if an e-mail is valid
    # or not but I am a bit time constrained at the moment.
    return '@' in text and '.' in text


def main():
    valid: bool = is_valid_email(input('E-mail:'))
    print(f'This is an {"" if valid else "in"}valid e-mail address.')


if __name__ == '__main__':
    main()


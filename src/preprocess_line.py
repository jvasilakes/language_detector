#! /usr/bin/python2

import re


def test(func):

    string = "There once were 2 men who had a 16x4 in gobledigook, &&&"

    return func(string)


# JAKE
def preprocess_line(file_string):
    '''
    # Reads in file string returned by read_file()
    # and removes all characters that are not
    # whitespace, [a-z][A-Z], comma, or period.
    # Changes all characters to lowercase and
    # converts numerals to 0.
    '''

    processed_string = file_string.lower()
    processed_string = re.sub(r'[^\d\sa-z,.]', r'', processed_string)
    processed_string = re.sub(r'\d', r'0', processed_string)

    processed_string = re.sub(r'\s', r'_', processed_string)

    return processed_string


if __name__ == '__main__':
    print test(preprocess_line)

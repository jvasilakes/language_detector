#! /usr/bin/python2

from sys import argv

# JAKE
def read_file(text_file):
    '''
    # Opens and reads text_file. Returns
    # file contents as a string.
    # If open or read fails, returns None
    '''

    try:
        f = open(text_file, 'r')
        file_string = f.read()
        f.close()

    except Exception as e:
        print e
        return None

    return file_string


if __name__ == '__main__':
    print read_file(argv[1])

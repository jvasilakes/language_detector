#! /usr/bin/python2

# Imports only needed for test function
import string
import math
import random

def test(write_func):
    '''
    # Generate a dummy dictionary of trigrams
    # with random probabilities.
    '''

    # Generate dummy trigram probability model
    alphabet = list(string.ascii_lowercase)

    random.seed()

    test_dict = {}

    for i in xrange(random.randint(100, 300)):
        trigram = ''.join(random.sample(alphabet, 3))
        prob = math.pow(random.random(), random.randint(5, 8))
        test_dict.update({trigram: prob})

    write_func(test_dict)

    return "Write succeeded."


# JAKE
def write_file(trigram_probs_dict):
    '''
    # Writes contents of trigram_probs_dict to
    # a new file.
    '''

    with open('trigram_model.txt', 'w') as f:
        f.write("TRIGRAM    PROBABILITY\n\n")
        for key in trigram_probs_dict.keys():
            f.write("  {0}  :  {1}\n" .format(key, trigram_probs_dict[key]))
    
    return 


if __name__ == '__main__':
    print test(write_file)

#! /usr/bin/python2

import numpy


# JAKE
def calc_perplexity(test_counts_dict, trigram_probs_dict):
    '''
    # Calculates perplexity of contents of file_string
    # according to probabilities in trigram_probs_dict.
    '''

    test_probs = []

    for trigram, count in test_counts_dict:

        # If the trigram doesn't appear in our model, just skip it.
        try:
            test_probs.append(trigrams_probs_dict[trigram] * count)
        except KeyError:
            pass

    numpy.prod(test_probs)
        

    return 0
    # return perplexity


#! /usr/bin/python2

import numpy


# JAKE
def calc_perplexity(test_counts_dict, trigram_probs_dict):
    '''
    # Calculates perplexity of contents of file_string
    # according to probabilities in trigram_probs_dict.
    '''

    test_probs = []

    for trigram, count in test_counts_dict.items():

        # If the trigram doesn't appear in our model, just skip it.
        try:
            test_probs.append(test_counts_dict[trigram] * count)
        except KeyError:
            pass

    perplexity = numpy.power(numpy.prod(test_probs), len(test_counts_dict))

    return perplexity

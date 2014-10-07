#! /usr/bin/python2

from __future__ import division

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
        default = min(trigram_probs_dict.values())
        for n in range(count):
            logprob = numpy.log10(trigram_probs_dict.get(trigram, default))
            test_probs.append(logprob)

    logprob = sum(test_probs)

    norm = logprob / len(test_probs)

    perplexity = numpy.power(2, -norm)

    return perplexity

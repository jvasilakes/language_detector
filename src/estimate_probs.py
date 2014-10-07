#! /usr/bin/python2

# from the __future__ package, import division
# to allow float division

from __future__ import division


def estimate_probs(trigram_counts_dict):
    '''
    # Estimates probabilities of trigrams using
    # trigram_counts_dict and returns a new dictionary
    # with the probabilities.
    '''
    
    # variable that creates a new dictionary called
    # trigram_probs_dict which is a copy of trigram_counts_dict.
    trigram_probs_dict = trigram_counts_dict.copy()
    
 	# sets the variable sum_counts to the sum
    # of all the values in trigram_couns_dict
    sum_counts = sum(trigram_counts_dict.values())
    
    # a for loop that iterates over all the keys in trigram_probs_dict
    # and sets the value of that key (which is currently the count)
    # to be the probability of that key by dividing the value by the sum
    # of all values (MLE). Once all keys are iterated over,
    # trigram_probs_dict is returned
    for key, value in trigram_probs_dict.items():
    	trigram_probs_dict[key] = value / sum_counts
    return trigram_probs_dict
    
#--------------------------------------------------------#
'''
# This is a test string
'''

if __name__ == '__main__':
	s = {
	' a ': 1, 's i': 1, 'his': 1, 'str': 1, 's a': 1,
	' is': 1, 'ing': 1, ' st': 1, 'rin': 1, 'tri': 1, 'thi': 1,
	'a s': 1, 'is ': 2
	}
	
	print estimate_probs(s)

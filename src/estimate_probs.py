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
    # trigram_probs_dict with the keys of trigram_counts_dict
    # and assigns the value 'None' to every key.
    trigram_probs_dict = dict.fromkeys(trigram_counts_dict)	
    
    # sets the variable sum_counts to the sum
    # of all the values in trigram_couns_dict
    sum_counts = sum(trigram_counts_dict.values())
    
    # sets the variable probs to an empty list
    probs = []
    
    # a for loop that iterates through all the values in
    # trigram_counts_dict and sets that value to be the
    # value divided by the sum of all values (MLE)
    # and appends this new value to the list probs.
    for i in trigram_counts_dict.values():
    	i = i / sum_counts
    	probs.append(i)
    
    # i is set to 0 to allow iteration over the items in probs	
    i = 0
    
    # a for loop that iterates over all the keys in trigram_probs_dict
    # and sets the value of that key (which is 'None') to be
    # the next value in the list probs. The index of probs is then
    # incremented by 1 to get to the next value.
    # Once all keys are iterated over, trigram_probs_dict is returned
    for key in trigram_probs_dict:
    	trigram_probs_dict[key] = probs[i]
    	i += 1
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

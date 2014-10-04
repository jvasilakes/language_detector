# from the __future__ package, import division
# to allow float division

from __future__ import division

def estimate_probs(trigram_counts_dict):
    '''
    # Estimates probabilities of trigrams using
    # trigram_counts_dict and returns a new dictionary
    # with the probabilities.
    '''
    trigram_probs_dict = dict.fromkeys(trigram_counts_dict)	
    sum_counts = sum(trigram_counts_dict.values())
    probs = []
    for i in trigram_counts_dict.values():
    	i = i / sum_counts
    	probs.append(i)
    	
    i = 0
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
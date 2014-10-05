#! /usr/bin/python2


import sys
import numpy as np
from numpy.random import random_sample
import random

def gen_random_output(trigram_probs_dict):
	random_string = np.random.choice(trigram_probs_dict.keys(), 50, trigram_probs_dict.values())
	random_string = ''.join(random_string)
	return random_string


#--------------------------------------------------------#
'''
# This is a test string
'''

if __name__ == '__main__':
	s = {
	'tri': 0.07142857142857142, 's i': 0.07142857142857142,
	'rin': 0.07142857142857142, 'his': 0.07142857142857142,
	'thi': 0.07142857142857142, 'str': 0.07142857142857142,
	's a': 0.07142857142857142, ' a ': 0.07142857142857142,
	'is ': 0.07142857142857142, 'ing': 0.07142857142857142,
	'a s': 0.07142857142857142, ' is': 0.07142857142857142,
	' st': 0.14285714285714285
	}

	print gen_random_output(s)

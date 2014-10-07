#! /usr/bin/python2

import numpy as np
import collections


def gen_random_output(trigram_probs_dict):
        od = collections.OrderedDict()
        od.update(trigram_probs_dict)
        random_string = np.random.choice(od.keys(), size=50, p=od.values())
        random_string = ''.join(random_string)
        return random_string


# --------------------------------------------------------#
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

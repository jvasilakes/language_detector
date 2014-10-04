#! /usr/bin/python

from __future__ import division

# Currently does not work, discounted trigrams
# will sum up to the same number as the undiscounted trigrams.
def gt_discounter(tri_counts):
    '''
    # Good-Turing discounter.
    # Calculates Good-Turing probability of
    # zero-count trigrams, and disocunts
    # all counts in tri_counts accordingly.
    '''

    new_counts = tri_counts

    # Calculate the probability of trigrams with zero count.
    N_1 = len([i for i in new_counts.itervalues() if i == 1])
    N = sum(new_counts.values())
    Pgt_0 = (N_1 / N)

    # Calculate updated counts and update values.
    for i in range(1, max(new_counts.values()) + 1):

        for key, value in new_counts.items():
            if value == i:

                # Compute both numerators and denominator
                # for the discounted counts equation.
                num1 = i + 1
                num2 = len([n for n in tri_counts.itervalues() if n == i+1])
                denom = len([n for n in tri_counts.itervalues() if n == i])

                # Update value with the new count
                new_counts[key] = (num1 * num2) / denom

    return Pgt_0, new_counts

#! /usr/bin/python

from __future__ import division

# Currently does not work, discounted trigrams
# will sum up to the same number as the undiscounted trigrams.
def gt_discount(tri_counts):
    '''
    # Good-Turing discounter.
    # Calculates Good-Turing probability of
    # zero-count trigrams, and disocunts
    # all counts in tri_counts accordingly.
    '''

    new_counts = tri_counts.copy()

    # Calculate the probability for trigrams with zero count.
    N_1 = len([i for i in new_counts.itervalues() if i == 1])
    N = sum(new_counts.values())
    zero_count_probs = (N_1 / N)

    # Calculate updated counts and update values.
    for key, value in tri_counts.iteritems():
        num1 = value + 1

        if not num1 in tri_counts.values():
            pass

        else:
            num2 = 0
            while not num2:
                num2 = len([n for n in tri_counts.itervalues() if n == num1])
                num1 += 1

            denom = len([n for n in tri_counts.itervalues() if n == value])

            # Update value with the new count
            new_counts[key] = (num1 * num2) / denom

    return zero_count_probs, new_counts

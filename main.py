#! /usr/bin/env python2

'''
# ****************** LANGUAGE DETECTOR ******************
#
# Using a set of training data in a variety of languages,
# determines the language of a test documents using ngram
# character counts.
#
# *******************************************************
'''

from __future__ import division

import os
import re
import numpy
import collections


# Set number of grams here.
NGRAMS = 3


def main():

    if NGRAMS <= 1:
        print "Sorry, NGRAMS must be >= 2."
        return

    # If we've already built some models before,
    # rename the file to keep them separate.
    if os.path.isfile(str(NGRAMS) + 'gram_model.txt'):
        os.rename(str(NGRAMS) + 'gram_model.txt', str(NGRAMS) + 'gram_model.old')

    # Make sure training as test files are named correctly!
    training_data_en = 'training.en'
    training_data_es = 'training.es'
    training_data_de = 'training.de'
    test_data_file = 'test_file.txt'

    # Train the ngram models
    print "Building English model."
    en_model = build_model(training_data_en, model_name='en_model')
    print "Building Spanish model."
    es_model = build_model(training_data_es, model_name='es_model')
    print "Building German model."
    de_model = build_model(training_data_de, model_name='de_model')
    print "Models written to file '"+str(NGRAMS)+"gram_model.txt'."

    # Classify the test data file
    test_data_str = read_file(test_data_file)
    test_processed = preprocess_line(test_data_str)
    test_counts = count_ngrams(NGRAMS, test_processed)

    print "Testing models."
    en_perplexity = calc_perplexity(test_counts, en_model)
    print "English model perplexity is {0}" .format(en_perplexity)
    es_perplexity = calc_perplexity(test_counts, es_model)
    print "Spanish model perplexity is {0}" .format(es_perplexity)
    de_perplexity = calc_perplexity(test_counts, de_model)
    print "German model perplexity is {0}" .format(de_perplexity)

    result = min(en_perplexity, es_perplexity, de_perplexity)

    if result == en_perplexity:
        lang = "English"
    elif result == es_perplexity:
        lang = "Spanish"
    else:
        lang = "German"

    print "Test document probably written in {0}" .format(lang)


# ------- BUILD MODEL -------------------------------------

def build_model(training_data_file, model_name=None):
    '''
    # Builds a ngram probability model for
    # for training_data_file and returns that
    # model as a dictionary.
    '''

    # Read in the file.
    data_file_str = read_file(training_data_file)

    # Remove unwanted characters.
    processed_data_str = preprocess_line(data_file_str)

    # Count ngrams.
    ngram_counts = count_ngrams(NGRAMS, processed_data_str)

    # Discount using Good-Turing discounting.
    n_discounts = gt_discount(ngram_counts)

    # Trigram_probs is a defaultdict with ngrams as keys
    # and their probabilities as values.
    ngram_probs = estimate_probs(n_discounts)

    # Write the model to a file.
    write_file(ngram_probs, model_name=model_name)

    return ngram_probs


# JAKE
# Implemented in read_file.py
def read_file(text_file):
    '''
    # Opens and reads text_file. Returns
    # file contents as a string.
    '''

    with open(text_file, 'r') as f:
        file_string = f.read()

    return file_string


# JAKE
# Implemented in preprocess_line.py
def preprocess_line(file_string):
    '''
    # Reads in file string returned by read_file()
    # and removes all characters that are not
    # whitespace, [a-z][A-Z], comma, or period.
    # Changes all characters to lowercase and
    # converts numerals to 0. Replace whitespace
    # with an underscore for ease of viewing.
    '''

    # Convert to lowercase.
    processed_string = file_string.lower()

    # Delete any characters that are not a digit,
    # whitespace, a-z, comma, or period.
    processed_string = re.sub(r'[^\d\sa-z,.]', r'', processed_string)

    # Convert all digits to 0.
    processed_string = re.sub(r'\d', r'0', processed_string)

    # Replace whitespace with underscore
    processed_string = re.sub(r'\s', r'_', processed_string)

    return processed_string


# ROMI
def count_ngrams(n, processed_string):
    '''
    # Counts all character ngrams in processed_string
    # and creates a dictionary of those ngram counts
    # called ngram_counts_dict.
    '''

    # This empty dictionary will be filled with
    # the ngrams in processed_string and their frequencies
    ngram_counts_dict = {}

    # i and j are set to the start positions of
    # the indices within processed_string
    # (print s[0:3] prints the first three characters of s)
    i = 0
    j = n

    # This for loop iterates over the characters
    # in processed_line, pairs them into ngrams
    # and increments the count of the indices i and j.
    # If the resulting ngram is a key in ngram_counts_dict,
    # the value is incremented by 1.
    # If the ngram is not a key in ngram_counts_dict,
    # a key is added with value 1.
    # Once there are no more ngrams to be iterated over,
    # ngram_counts_dict is returned.
    for char in processed_string:
        if len(processed_string[i:j]) == n:
            ngram = processed_string[i:j]
            i += 1
            j += 1
            if ngram in ngram_counts_dict:
                ngram_counts_dict[ngram] += 1
            else:
                ngram_counts_dict[ngram] = 1

    return ngram_counts_dict


def gt_discount(n_counts):
    '''
    # Good-Turing discounter.
    # Calculates Good-Turing probability of
    # zero-count ngrams, and disocunts
    # all counts in n_counts accordingly.
    # Recasts n_counts as a defaultdict with
    # zero_count_probs as the default value.
    '''

    # Calculate the probability for ngrams with zero count.
    # Equation: P_gt_0 = N_1 / N_total
    N_1 = len([i for i in n_counts.itervalues() if i == 1])
    N = sum(n_counts.itervalues())
    zero_count_probs = (N_1 / N)

    # Calculate updated counts and update values.
    # Equation: discount_c = (c+1) * (N_c+1 / N_c)
    for key, value in n_counts.iteritems():

        # Calculate first numerator (c+1)
        num1 = value + 1
        if num1 not in n_counts.itervalues():
            pass

        else:
            # Calculate second numerator (N_c+1)
            num2 = len([n for n in n_counts.itervalues() if n == num1])

            # Calculate denominator (N_c)
            denom = len([n for n in n_counts.itervalues() if n == value])

            # Calculate the new count and
            # update the count dict with the new count
            n_counts[key] = (num1 * num2) / denom

    # Cast n_counts as a defaultdict with zero_count_probs as the default.
    # Default values used in calc_perplexity.
    new_counts = collections.defaultdict(lambda: zero_count_probs, n_counts)

    return new_counts


# ROMI
def estimate_probs(ngram_counts_dict):
    '''
    # Estimates probabilities of ngrams using
    # ngram_counts_dict and returns a new dictionary
    # with the probabilities.
    '''

    # variable that creates a new dictionary called
    # ngram_probs_dict which is a copy of ngram_counts_dict.
    ngram_probs_dict = ngram_counts_dict.copy()

    # a for loop that iterates over all the keys in ngram_probs_dict
    # and sets the value of that key (which is currently the count)
    # to be the probability of that key by dividing the value by the sum
    # of all values (MLE). Once all keys are iterated over,
    # ngram_probs_dict is returned
    for key, value in ngram_counts_dict.items():
        bigrams = [ngram_counts_dict[k] for k in ngram_counts_dict.keys() if k.startswith(key[:len(key)-1])]
        ngram_probs_dict[key] = value / sum(bigrams)

    return ngram_probs_dict


# JAKE
# Implemented in write_file.py
def write_file(ngram_probs_dict, model_name=None):
    '''
    # Writes nicely formatted contents
    # of ngram_probs_dict to a file,
    # called [NGRAMS]gram_model.txt. If the file
    # already exists, each new model is
    # appended to the end of the file.
    '''

    # Default model_name
    if not model_name:
        model_name = "UNTITLED MODEL"
    else:
        model_name = model_name.upper()

    # Open ngram_model.txt (create it if it doesn't exist)
    # in append mode.
    with open(str(NGRAMS) + 'gram_model.txt', 'a') as f:

        # Write the model_name and column headers
        f.write(" \t\t**** {0} ****\n\n" .format(model_name))

        # Write the contents of the ngram model
        entries = 0
        for key, value in sorted(ngram_probs_dict.items()):
            f.write("  {0}  :  {1},  " .format(key, value))

            if entries == 5:
                f.write('\n')
                entries = 0
            else:
                entries += 1

        f.write('\n\n\n')

    return

# -----------------------------------------------------


# JAKE
def calc_perplexity(test_counts_dict, ngram_probs_dict):
    '''
    # Calculates perplexity of contents of file_string
    # according to probabilities in ngram_probs_dict.
    '''

    test_probs = []

    for ngram, count in test_counts_dict.items():

        # If the ngram doesn't appear in our model, just skip it.
        for n in range(count):

            # Since ngram_probs_dict is a defaultdict as created
            # in gt_discount, it will return the zero count probability
            # if ngram not in ngram_probs_dict.
            logprob = numpy.log2(ngram_probs_dict[ngram])
            test_probs.append(logprob)

    logprob = sum(test_probs)

    norm = logprob / len(test_probs)

    perplexity = numpy.power(2, -norm)

    return perplexity


# ROMI
def gen_random_output(ngram_probs_dict, n=300):
    '''
    # Generate n characters of output randomly selected
    # from the keys of ngram_probs_dict according to
    # those keys probability values.
    # OrderedDict is used to ensure that each key is
    # paired with its associated value.
    '''

    od = collections.OrderedDict(ngram_probs_dict)
    random_string = numpy.random.choice(od.keys(), size=50, p=od.values())
    random_string = ''.join(random_string)
    return random_string


if __name__ == '__main__':
    main()

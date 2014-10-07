#! /usr/bin/python2

'''
# ****************** LANGUAGE DETECTOR ******************
#
# Using a set of training data in a variety of languages,
# determines the language of a test documents using trigram
# character counts.
#
# *******************************************************
'''

from __future__ import division
import numpy


def main():

    # Train the trigram models
    en_model = build_model(training_data_en, model_name='en_model')
    es_model = build_model(training_data_es, model_name='es_model')
    de_model = build_model(training_data_de, model_name='de_model')

    # Classify the test data file
    test_data_str = read_file(test_data_file)
    test_counts = count_trigrams(test_data_str)
    en_perplexity = calc_perplexity(test_counts, en_model)
    es_perplexity = calc_perplexity(test_counts, es_model)
    de_perplexity = calc_perplexity(test_counts, de_model)

    result = min(en_perplexity, es_perplexity, de_perplexity)

    return


# ------- BUILD MODEL -------------------------------------


def build_model(training_data_file, model_name=None):
    '''
    # Builds a trigram probability model for
    # for training_data_file and returns that
    # model as a dictionary.
    '''

    data_file_str = read_file(training_data_file)

    processed_data_str = preprocess_line(data_file_str)
    
    trigram_counts = count_trigrams(processed_data_str)

    # Discount using Good-Turing discounting.
    ## Discount applied by changing trigram_counts
    ## in-place.
    zero_count_prob = gt_discount(trigram_counts)

    trigram_probs = estimate_probs(trigram_counts)

    write_file(trigram_probs, model_name=model_name)

    # trigram_probs is a dict with trigrams as keys
    ## and their probabilities as values.
    return trigram_probs


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
    ## whitespace, a-z, comma, or period.
    processed_string = re.sub(r'[^\d\sa-z,.]', r'', processed_string)

    # Convert all digits to 0.
    processed_string = re.sub(r'\d', r'0', processed_string)

    # Replace whitespace with underscore
    processed_string = re.sub(r'\s', r'_', processed_string)

    return processed_string


# ROMI
def count_trigrams(processed_string):
    '''
    # Counts all character trigrams in processed_string
    # and creates a dictionary of those trigram counts
    # called trigram_counts_dict.
    '''

    # This empty dictionary will be filled with
    # the trigrams in processed_string and their frequencies
    trigram_counts_dict = {}

    # i and j are set to the start positions of
    # the indices within processed_string
    # (print s[0:3] prints the first three characters of s)
    i = 0
    j = 3

    # This for loop iterates over the characters
    # in processed_line, pairs them into trigrams
    # and increments the count of the indices i and j.
    # If the resulting trigram is a key in trigram_counts_dict,
    # the value is incremented by 1.
    # If the trigram is not a key in trigram_counts_dict,
    # a key is added with value 1.
    # Once there are no more trigrams to be iterated over,
    # trigram_counts_dict is returned.
    for char in processed_string:
        if len(processed_string[i:j]) == 3:
            trigram = processed_string[i:j]
            i += 1
            j += 1
            if trigram in trigram_counts_dict:
                trigram_counts_dict[trigram] += 1
            else:
                trigram_counts_dict[trigram] = 1

    return trigram_counts_dict


# ROMI
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


# JAKE
# Implemented in write_file.py
def write_file(trigram_probs_dict, model_name=None):
    '''
    # Writes nicely formatted contents
    # of trigram_probs_dict to a file,
    # called trigram_model.txt. If the file
    # already exists, each new model is
    # appended to the end of the file.
    '''

    # Default model_name
    if not model_name:
        model_name = "UNTITLED MODEL"
    else:
        model_name = model_name.upper()

    # Open trigram_model.txt (create it if it doesn't exist)
    ## in append mode.
    with open('trigram_model.txt', 'a') as f:

        # Write the model_name and column headers
        f.write(" **** {0} ****\n\n" .format(model_name))
        f.write("TRIGRAM    PROBABILITY\n\n")

        # Write the contents of the trigram model
        for key, value in sorted(trigram_probs_dict.items()):
            f.write("  {0}  :  {1}\n" .format(key, value))

        f.write('\n')
    
    return 

# -----------------------------------------------------


# JAKE
def calc_perplexity(test_counts_dict, trigram_probs_dict, default_prob):
    '''
    # Calculates perplexity of contents of file_string
    # according to probabilities in trigram_probs_dict.
    '''

    test_probs = []

    for trigram, count in test_counts_dict.items():

        # If the trigram doesn't appear in our model, just skip it.
        for n in range(count):
            logprob = numpy.log10(trigram_probs_dict.get(trigram, default_prob))
            test_probs.append(logprob)

    logprob = sum(test_probs)

    norm = logprob / len(test_probs)

    perplexity = numpy.power(2, -norm)

    return perplexity


# ROMI
def gen_random_output(trigram_probs_dict):
    '''
    # Generate random output based on
    # probabilities in trigram_probs_dict.
    '''

    od = collections.OrderedDict()
    od.update(trigram_probs_dict)
    random_string = numpy.random.choice(od.keys(), size=50, p=od.values())
    random_string = ''.join(random_string)
    return random_string

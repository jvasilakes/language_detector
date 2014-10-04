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


def main():

    # Train the trigram models
    en_model = build_model(training_data_en, model_name='en_model')
    es_model = build_model(training_data_es, model_name='es_model')
    de_model = build_model(training_data_de, model_name='de_model')

    # Classify the test data file
    test_data_str = read_file(test_data_file)
    en_perplexity = calc_perplexity(test_data_str, en_model)
    es_perplexity = calc_perplexity(test_data_str, es_model)
    de_perplexity = calc_perplexity(test_data_str, de_model)

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

    trigram_probs = estimate_probs(trigram_counts)

    write_file(trigram_probs, model_name=model_name)

    return trigram_probs


# JAKE
# Implemented in read_file.py
def read_file(text_file):
    '''
    # Opens and reads text_file. Returns
    # file contents as a string.
    '''

    return 0    # temporary
    # return file_string


# JAKE
# Implemented in preprocess_line.py
def preprocess_line(file_string):
    '''
    # Reads in file string returned by read_file()
    # and returns a string with all characters removed
    # that are not whitespace, [a-z][A-Z], comma,
    # or period. Changes all characters to lowercase
    # and converts numerals to 0.
    '''

    return 0    # temporary
    # return processed_string


# ROMI
def count_trigrams(processed_string):
    '''
    # Counts all character trigrams in processed_string
    # and creates a dictionary of those trigram counts.
    '''

    return 0    # temporary
    # return trigram_counts_dict


# ROMI
def estimate_probs(trigram_counts_dict):
    '''
    # Estimates probabilities of trigrams using
    # trigram_counts_dict and returns a new dictionary
    # with the probabilities.
    '''

    return 0    # temporary
    # return trigram_probs_dict


# JAKE
# Implemented in write_file.py
def write_file(trigram_probs_dict, model_name=None):
    '''
    # Writes contents of trigram_probs_dict to
    # a new file.
    '''

    return 0     # temporary
    # return success or failure

# -----------------------------------------------------


# JAKE
def calc_perplexity(file_string, trigram_probs_dict):
    '''
    # Calculates perplexity of contents of file_string
    # according to probabilities in trigram_probs_dict.
    '''

    return 0     # temporary
    # return perplexity


# ROMI
def gen_random_output(trigram_probs_dict):
    '''
    # Generate random output based on
    # probabilities in trigram_probs_dict.
    '''

    return 0     # temporary
    # return random_string


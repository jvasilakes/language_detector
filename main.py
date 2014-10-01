    '''
    # ****************** LANGUAGE DETECTOR ******************
    # 
    # Using a set of training data in a variety of languages,
    # determines the language of a test documents using trigram
    # character counts.
    # 
    # *******************************************************
    '''



def read_file(text_file):
    '''
    # Opens and reads text_file. Returns 
    # file contents as a string.
    '''

    return 0    # temporary
    # return file_string


def preprocess_line(file_string):
    '''
    # Reads in file string returned by read_file()
    # and removes all characters that are not
    # whitespace, [a-z][A-Z], comma, or period. 
    # Changes all characters to lowercase and
    # converts numerals to 0.
    ''' 

    return 0    # temporary
    # return processed_string


def count_trigrams(processed_string):
    '''
    # Counts all character trigrams in processed_string
    # and creates a dictionary of those trigram counts.
    '''

    return 0    # temporary
    # return trigram_counts_dict


def estimate_probs(trigram_counts_dict):
    '''
    # Estimates probabilities of trigrams using
    # trigram_counts_dict and return a new dictionary
    # with the probabilities.
    '''

    return 0    # temporary
    # return trigram_probs_dict


def write_file(trigram_probs_dict):
    '''
    # Writes contents of trigram_probs_dict to
    # a new file.
    '''

    return 0     # temporary
    # return success or failure


def gen_random_output(trigram_probs_dict):
    '''
    # Generate random output based on
    # probabilities in trigram_probs_dict.
    '''

    return 0     # temporary
    # return random_string


def calc_perplexity(file_string, trigram_probs_dict):
    '''
    # Calculates perplexity of contents of file_string
    # according to probabilities in trigram_probs_dict.
    '''

    return 0     # temporary
    # return perplexity 

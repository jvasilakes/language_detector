from read_file import read_file
from preprocess_line import preprocess_line
from count_trigrams import count_trigrams
from estimate_probs import estimate_probs
from calc_perplexity import calc_perplexity


class Tester(object):

    def __init__(self):

        self.train_file_str = ''
        self.train_pfs = ''
        self.train_counts = {}
        self.train_probs = {}

        self.test_file_str = ''
        self.test_pfs = ''
        self.test_counts = {}
        self.perplexity = None

    def train(self, training_data_file):

        self.train_file_str = read_file(training_data_file)
        self.train_pfs = preprocess_line(self.train_file_str)
        self.train_counts = count_trigrams(self.train_pfs)
        self.train_probs = estimate_probs(self.train_counts)

    def test(self, test_data_file):

        self.test_file_str = read_file(test_data_file)
        self.test_pfs = preprocess_line(self.test_file_str)
        self.test_counts = count_trigrams(self.test_pfs)
        self.perplexity = calc_perplexity(self.test_counts, self.train_probs)

    def attr(self):

        print "CLASS ATTRIBUTES\n"
        print "self.train_file_str"
        print "self.test_file_str"
        print "self.train_pfs"
        print "self.test_pfs"
        print "self.train_counts"
        print "self.test_counts"
        print "self.train_probs"
        print "self.test_perplex"
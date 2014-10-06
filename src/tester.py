from read_file import read_file
from preprocess_line import preprocess_line
from count_trigrams import count_trigrams
from estimate_probs import estimate_probs
from calc_perplexity import calc_perplexity


class Tester(object):

    def __init__(self, training_data_file)

        self.train_file_str = ''
        self.test_file_str = ''

        self.train_pfs = ''
        self.test_pfs = ''

        self.train_counts = {}
        self.test_counts = {}

        self.train_probs = {}

        self.test_perplex = None


    def build_model(self, training_data_file):

        self.train_file_str = read_file(training_data_file)

        self.train_pfs = preprocess_line(self.train_file_str)

        self.train_counts = count_trigrams(self.train_pfs)

        self.train_probs = estimate_probs(self.train_counts)


    def test(self, test_data_file):

        self.test_file_str = read_file(test_data_file)

        self.test_pfs = preprocess_line(self.test_file_str)

        self.test_counts = count_trigrams(self.test_pfs)

        self.test_perplex = calc_perplexity(self.test_counts)

import numpy
import sys
from scipy.spatial import distance


class SimilarWords:
    """ Determines similarity between 2 words using GloVe """

    embedding_dict = dict()
    file_name = ""

    # Default to using 100 dimension vectors from glove.6B.100d.txt
    # Data from Wikipedia 2014 + Gigaword 5
    # https://nlp.stanford.edu/projects/glove/
    def __init__(self, f="./wiki-data/glove.6B.100d.txt"):
        self.file_name = f
        self.initialize_dict()

    def initialize_dict(self):
        """ Load GloVe word vectors into memory """
        file = open(self.file_name, "r", encoding="utf8")
        for line in file:
            values = line.split()
            word = values[0]
            word_vec = numpy.asarray(values[1:], dtype=numpy.float32)
            self.embedding_dict[word] = word_vec
        file.close()

    def get_distance(self, word_0, word_1):
        """ Calculates Euclidean distance between two words based on GloVe
        vector """
        if (word_0 not in self.embedding_dict or \
                word_1 not in self.embedding_dict):
            return sys.float_info.max
        return distance.euclidean(self.embedding_dict[word_0],
                                  self.embedding_dict[word_1])

#This class is reponsable of loading diferent datasets
#it's always returns 3 datasets,   Train, Validate, Test
import cPickle
import gzip
import os
import urllib
import numpy

def load_mnist():
    

    filepath = './mnist.pkl.gz'

    # Download the MNIST dataset if it is not present
    if not os.path.isfile(filepath):

        origin = 'http://www.iro.umontreal.ca/~lisa/deep/data/mnist/mnist.pkl.gz'
        print 'Downloading data from %s' % origin
        urllib.urlretrieve(origin, filepath)

    # Load the dataset
    print '... loading data'

    #We have to descompress it
    f = gzip.open(filepath, 'rb')
    train_set, valid_set, test_set = cPickle.load(f)
    f.close()

    return train_set, valid_set, test_set

def load_dictionary():

    dictionary = numpy.zeros(26, dtype='c1, (5,3)u1')
    dictionary[:] = [('A',[[1, 0, 1],[0, 1, 0],[0, 0, 0],[0, 1, 0],[0, 1, 0]]),
                    ('B',[[0, 0, 1],[0, 1, 0],[0, 0, 1],[0, 1, 0],[0, 0, 1]]),
                    ('C',[[0, 0, 0],[0, 1, 1],[0, 1, 1],[0, 1, 1],[0, 0, 0]]),
                    ('D',[[0, 0, 1],[0, 1, 0],[0, 1, 0],[0, 1, 0],[0, 0, 1]]),
                    ('E',[[0, 0, 0],[0, 1, 1],[0, 0, 1],[0, 1, 1],[0, 0, 0]]),
                    ('F',[[0, 0, 0],[0, 1, 1],[0, 0, 1],[0, 1, 1],[0, 1, 1]]),
                    ('G',[[0, 0, 0],[0, 1, 1],[0, 1, 1],[0, 1, 0],[0, 0, 0]]),
                    ('H',[[0, 1, 0],[0, 1, 0],[0, 0, 0],[0, 1, 0],[0, 1, 0]]),
                    ('I',[[0, 0, 0],[1, 0, 1],[1, 0, 1],[1, 0, 1],[0, 0, 0]]),
                    ('J',[[0, 0, 0],[1, 1, 0],[1, 1, 0],[0, 1, 0],[0, 0, 0]]),
                    ('K',[[0, 1, 0],[0, 0, 1],[0, 1, 1],[0, 0, 1],[0, 1, 0]]),
                    ('L',[[0, 1, 1],[0, 1, 1],[0, 1, 1],[0, 1, 1],[0, 0, 0]]),
                    ('M',[[0, 1, 0],[0, 0, 0],[0, 1, 0],[0, 1, 0],[0, 1, 0]]),
                    ('N',[[0, 1, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 1, 0]]),
                    ('O',[[1, 0, 1],[0, 1, 0],[0, 1, 0],[0, 1, 0],[1, 0, 1]]),
                    ('P',[[0, 0, 0],[0, 1, 0],[0, 0, 0],[0, 1, 1],[0, 1, 1]]),
                    ('Q',[[1, 0, 1],[0, 1, 0],[0, 1, 0],[1, 0, 1],[1, 1, 0]]),
                    ('R',[[0, 0, 1],[0, 1, 0],[0, 0, 0],[0, 0, 1],[0, 1, 0]]),
                    ('S',[[1, 0, 0],[0, 1, 1],[1, 0, 1],[1, 1, 0],[0, 0, 1]]),
                    ('T',[[0, 0, 0],[1, 0, 1],[1, 0, 1],[1, 0, 1],[1, 0, 1]]),
                    ('U',[[0, 1, 0],[0, 1, 0],[0, 1, 0],[0, 1, 0],[0, 0, 0]]),
                    ('V',[[0, 1, 0],[0, 1, 0],[0, 1, 0],[0, 1, 0],[1, 0, 1]]),
                    ('W',[[0, 1, 0],[0, 1, 0],[0, 1, 0],[0, 0, 0],[0, 1, 0]]),
                    ('X',[[0, 1, 0],[0, 1, 0],[1, 0, 1],[0, 1, 0],[0, 1, 0]]),
                    ('Y',[[0, 1, 0],[0, 1, 0],[1, 0, 1],[1, 0, 1],[1, 0, 1]]),
                    ('Z',[[0, 0, 0],[1, 1, 0],[1, 0, 1],[0, 1, 1],[0, 0, 0]])]

    return dictionary
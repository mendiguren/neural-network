#This class is reponsable of loading diferent datasets
#it's always returns 3 datasets,   Train, Validate, Test
import cPickle
import gzip
import os
import urllib

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

    return (train_set, valid_set, test_set)

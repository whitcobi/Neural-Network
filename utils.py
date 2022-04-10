import numpy as np
import os
import gzip
from six.moves import cPickle as pickle
import os
import platform

def load_mnist_datasets(path='data/mnist.pkl.gz'):
    if not os.path.exists(path):
        raise Exception('Cannot find %s' % path)
    with gzip.open(path, 'rb') as f:
        train_set, val_set, test_set = load_pickle(f)
        train_inputs = [np.reshape(x, (784, 1)) for x in train_set[0]]
        train_results = [vectorized_result(y) for y in train_set[1]]
        train_data = list(zip(train_inputs, train_results))

        val_inputs = [np.reshape(x, (784, 1)) for x in val_set[0]]
        val_results = [vectorized_result(y) for y in val_set[1]]
        val_data = list(zip(val_inputs, val_results))

        test_inputs = [np.reshape(x, (784, 1)) for x in test_set[0]]
        test_results = [vectorized_result(y) for y in test_set[1]]
        test_data = list(zip(test_inputs, test_results))
        
        return train_data,val_data,test_data

def vectorized_result(y):
    e = np.zeros((10, 1))
    e[y] = 1.0
    return e

def load_pickle(f):
    version = platform.python_version_tuple()
    if version[0] == '2':
        return pickle.load(f)
    elif version[0] == '3':
        return pickle.load(f, encoding='latin1')
    raise ValueError("invalid python version: {}".format(version))

# print(len(load_mnist_datasets('data/mnist.pkl.gz')))
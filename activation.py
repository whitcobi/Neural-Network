import numpy as np

def sigmoid_forward(z):
    return 1 / (1 + np.exp(-z))

def softmax(x):
    return np.exp(x) / np.sum(np.exp(x))

def relu(x):
    return np.maximum(0, x)

def relu_gradient(x):
    return x > 0
from tqdm import *
import numpy

import dataset
from nets import simpleNet

mnist = dataset.load_mnist()

nn = simpleNet(architecture=numpy.array([784 ,100, 10]))

input = mnist[0][0][255,:]

nn.forward(input)
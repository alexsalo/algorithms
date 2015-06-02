__author__ = 'alex'
import numpy as np
from numpy import linalg
from random import random
from matplotlib import pyplot as plt
from matplotlib import pylab

N = 2
M = 100
X = np.zeros((M, N))
X[:, 0] = 1
X[:, 1] = xrange(1, M + 1)

noise = [random() * 5 * np.log(i) for i in xrange(M)]
y = np.dot(X,  [1.6, 0.25]) + noise


print X
print y

plt.plot(X[:, 1], y, 'bo')
print linalg.inv(np.dot(X.T, X))
print (X.T * y)
Theta = linalg.inv(np.dot(X.T, X)) * (X.T * y)
print Theta


pylab.show()
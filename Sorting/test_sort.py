__author__ = 'alex'
import random
import time

import matplotlib.pyplot as plt

import quicksort


N = [100, 1000, 10000, 10000, 100000, 1000000]
q = []
m = []

for n in N:
    data = []

    for i in xrange(0, n):
        data.append(random.randint(0, 10000))

    s = time.time()
    quicksort.qsort(data)
    q.append(time.time() - s)

    s = time.time()
    quicksort.qsort(data)
    m.append(time.time() - s)

print q
print m

plt.plot(q, m, linewidth=2.0)
plt.show()
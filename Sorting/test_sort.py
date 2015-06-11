__author__ = 'alex'
import random
import time

import matplotlib.pyplot as plt

import quicksort, mergesort, repminsort, insertionsort


N = [100, 1000, 10000]
q = []
m = []
r = []
ins = []

for n in N:
    data = []

    for i in xrange(0, n):
        data.append(random.randint(0, 10000))

    s = time.time()
    quicksort.qsort(data)
    q.append(time.time() - s)

    s = time.time()
    mergesort.msort(data)
    m.append(time.time() - s)

    s = time.time()
    repminsort.repminsort(data)
    r.append(time.time() - s)

    s = time.time()
    insertionsort.insertionsort(data)
    ins.append(time.time() - s)

print q
print m

plt.plot(N, r, 'r-', linewidth=2.0, label = 'Rep Min Sort')
plt.plot(N,ins, 'c-', linewidth=2.0, label = 'Insertion Sort')
plt.plot(N,q, 'g-', linewidth=2.0, label = 'Quick Sort')
plt.plot(N,m, 'b-', linewidth=2.0, label = 'Merge Sort')
plt.legend(loc=2)
plt.yscale('log')
plt.xscale('log')
plt.show()
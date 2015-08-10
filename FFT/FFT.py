__author__ = 'alex'
import scipy.io.wavfile as wav
import matplotlib, pylab
from pylab import *
import matplotlib.pyplot as plt

audio = wav.read('harris.wav')
print len(audio[1])
#data = audio[1][1:5000]
# wav.write('test.wav', audio[0],data)

data = audio[1]
#plt.plot(data)

# t = arange(0.0, 23.0, 0.01)
# plt.plot(t, sin(t) + cos(1.5*t), 'b-')

#grid(True)
#pylab.show()

def FFT(sample):
    n = len(sample)
    if n== 1:
        return sample
    else:
        m = n / 2
        evens = FFT(sample[::2])
        odds = FFT(sample[1::2])

        for j in xrange(m - 1):
            unity_root = exp(-2*pi*j/n)
            x = odds[j] * unity_root
            sample[j] = evens[j] + x
            sample[2**(k-1) + j] = evens[j] - x

print data
print FFT(data, )

# def iter_FFT(sample):
#     N = len(sample)
#     transformed = N*[None]
#     for i in xrange(0, N, 2):
#         s1 = sample[f(i)]
#         s2 = sample[f(i+1)]
#         transformed[i] = s1 + s2
#         transformed[i+1] = s1 - s2


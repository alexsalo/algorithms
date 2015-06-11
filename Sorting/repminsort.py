__author__ = 'alex'
basicOperationCounter = 0
def repminsort(arr):
    global basicOperationCounter
    n = len(arr)
    for i in xrange(0, n):
        for j in xrange(i + 1, n):
            if arr[i] > arr[j]:
                basicOperationCounter += 1
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# array = [11, 50, 2, 43, 6, 100, 8, 20, 3, 15]
# print repminsort(array)
print 'RepMin Sort finished. Basic operation performed: %s' % basicOperationCounter
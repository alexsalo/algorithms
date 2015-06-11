__author__ = 'alex'
basicOperationCounter = 0
def insertionsort(arr):
    global basicOperationCounter
    n = len(arr)
    for i in xrange(1, n):
        #print arr
        x = arr[i]
        j = i
        while j > 0 and arr[j-1] > x:
            basicOperationCounter += 1
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = x
    return arr

array = [11, 50, 2, 43, 6, 100, 8, 20, 3, 15]
print insertionsort(array)
print 'Insertion Sort finished. Basic operation performed: %s' % basicOperationCounter
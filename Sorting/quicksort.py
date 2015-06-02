__author__ = 'alex'

def qsort(arr):
    #print arr
    if len(arr) < 2:
        return arr
    pivots = [x for x in arr if x == arr[0]]
    lo = qsort([x for x in arr if x < arr[0]])
    hi = qsort([x for x in arr if x > arr[0]])

    return lo + pivots + hi


array = [11, 50, 2, 43, 6, 100, 8, 20, 3, 15]
print qsort(array)
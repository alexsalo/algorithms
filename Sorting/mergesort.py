__author__ = 'alex'

basicOperationCounter = 0

def merge(l, r):
    global basicOperationCounter
    result = []
    i = j = 0
    while i < len(l) and j < len(r):
        basicOperationCounter += 1
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    result += l[i:]
    result += r[j:]
    return result

def msort(a):
    #print a
    if len(a) == 1:
        return a
    mid = len(a) / 2
    return merge(msort(a[:mid]), msort(a[mid:]))

# array = [101, 50, 2, 43, 6, 100, 8, 20, 3, 15]
# print msort(array)
print 'Msort finished. Basic operation performed: %s' % basicOperationCounter
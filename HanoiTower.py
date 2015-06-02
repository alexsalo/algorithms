__author__ = 'alex'

N_disks = 8
basicOperationCounter = 0

tower1 = [N_disks - i for i in xrange(N_disks)]
tower2 = []
tower3 = []

def printTowers():
    print tower1
    print tower2
    print tower3
    print '-------------------'

def moveDisk(out, to):
    disk = out[-1] # top element
    out.remove(disk)
    to.append(disk)

    global basicOperationCounter
    basicOperationCounter += 1
    printTowers()

def move(n, out, to, work):
    if n > 1:
        move(n - 1, out, work, to)
    moveDisk(out, to)
    if n > 1:
        move(n - 1, work, to, out)


printTowers()
move(N_disks, tower1, tower2, tower3)
print 'Move completed in %s steps. Theoretical bound is 2^n-1 = % s' % (basicOperationCounter, 2 ** N_disks - 1)
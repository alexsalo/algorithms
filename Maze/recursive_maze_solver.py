__author__ = 'alex'
from tabulate import tabulate

# 0 clear
# 1 wall
# 2 was here
# 8 start
# 9 finish
maze = [
        [0, 0, 1, 0, 1],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 0, 9]
]

def readMaze(filename):
    maze_mapping = {'S' : 0, 'F' : 9, ' ' : 0, '+' : 1, '-' : 1, '|' : 1}
    return [[maze_mapping[char] for char in line[:-1]] for line in open(filename)]

maze = readMaze('maze.txt')
print maze

width = len(maze)
height = len(maze[0])
print 'Maze width: %s, height %s' % (width, height)

FoundWayOut = False

def move(x, y):
    global FoundWayOut
    if FoundWayOut:
        return

    print tabulate(maze)

    if (x < 0 or x > width - 1 or y < 0 or y > height - 1):
        print 'Out of bounds'; return
    if (maze[x][y] == 9):
        FoundWayOut = True
        print 'Got it!'; return
    if (maze[x][y] == 1):
        print 'That is wall'; return
    if (maze[x][y] == 2):
        print 'Was here before'; return
    maze[x][y] = 2

    move(x + 1, y) # East
    move(x, y + 1) # South
    move(x - 1, y) # West
    move(x, y - 1) # North

#move(0, 0)
move(10,1)
if not FoundWayOut:
    print 'There is no way out of this!'

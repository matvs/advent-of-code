import re
from enum import Enum
from queue import Queue



def parseInput(lines):
    return [list(line.strip()) for line in lines]


def findPosition(grid, needle = 'S'):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == needle:
                return (x,y)
            
    return (-1,-1)

def count(grid, needle = 'S'):
    countNumber = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == needle:
                countNumber += 1
            
    return countNumber

def printGrid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], end = '')
        print()

def isLegalMove(x,y,grid):
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y]) and grid[y][x] == '.'

def dfs(x, y, grid, count = 0):
    count += 1
    grid[y][x] = '0'
    movements = [(0,1),(0,-1),(1,0),(-1,0)]
    for movement in movements:
        dx = x + movement[0]
        dy = y + movement[1]
        if isLegalMove(dx,dy,grid):
            dfs(dx,dy,grid,count)
    return count

def bfs(x,y, grid, maxDepth = 65):
    queue = Queue()
    queue.put((x,y,0))
     
    while not queue.empty():
        currentNode = queue.get()
        x,y,depth = currentNode
        print(depth)
        grid[y][x] = str(depth)
        movements = [(0,1),(0,-1),(1,0),(-1,0)]
        for movement in movements:
            dx = x + movement[0]
            dy = y + movement[1]
            if isLegalMove(dx,dy,grid) and depth + 1 < maxDepth:
                queue.put((dx,dy,depth + 1))
        


with open('/home/matvs/Projects/advent-of-code/2023/day21.input.txt') as f:
    lines = f.readlines()
    grid = parseInput(lines)
    #print(grid)
    startingPosition = findPosition(grid)
    print(startingPosition)
    #dfs(startingPosition[0], startingPosition[1], grid)
   
    bfs(startingPosition[0], startingPosition[1], grid)
    printGrid(grid)
    
    print(count(grid, '64'))
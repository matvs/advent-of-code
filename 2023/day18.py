import re

class Edge:
    def __init__(self, node1, node2, color, label):
        self.fromNode = node1
        self.toNode = node2
        self.color = color
        self.label =label

class Node:
    def __init__(self):
        self.edges = []
        
    def addEdge(self, edge):
        self.edges.append(edge)
        
def createGrid(start: Node):
    directions = { 'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}
    grid = [['#']]
    currentNode = start
    x = 0
    y = 0
    maxColumns = 0
    while len(currentNode.edges) > 0:

        x += directions[currentNode.edges[0].label][0]
        y += directions[currentNode.edges[0].label][1]
        if y >= len(grid):
            grid.append([])
        if y < 0:
            grid.insert(0, [])
            y = 0
        if x >= len(grid[y]):
            for i in range(x - len(grid[y])):
                grid[y].append('.')
        if x < 0:
            grid[y].insert(0, '.')
            x = 0
        #grid[y].insert(x,currentNode.edges[0].label)
        if x >= len(grid[y]): 
            #grid[y].insert(x, currentNode.edges[0].label)
            grid[y].insert(x, '#')
        else:
            #grid[y][x] = currentNode.edges[0].label
            grid[y][x] = '#'
        currentNode = currentNode.edges[0].toNode
        maxColumns = max(maxColumns, len(grid[y]))
    for row in grid:
        for i in range(maxColumns - len(row)):
            row.append('.')
    return grid

if __name__ == '__main__':
    with open('/home/matvs/Projects/advent-of-code/2023/day18.input.txt') as f:
        lines = f.read()
        steps = re.findall(r'(R|D|U|L) (\d+) \((#[a-z\d]+)\)', lines)
        print(steps)
        currentNode = start = Node()
        for step in steps:
            direction, distance, color = step
            distance = int(distance)
            for i in range(distance):
                nextNode = Node()
                edge = Edge(currentNode, nextNode, color, direction)
                currentNode.addEdge(edge)
                currentNode = nextNode
                
                
        grid = createGrid(start)
        for row in grid:
            for edge in row:
                print(edge, end='')
            print()
            
        for y, row in enumerate(grid):
            start = None
            end = None
            for x, edge in enumerate(row):
                if start is None and edge == '#':
                    start = x
                if start is not None and edge == '#':
                    end = x
            end = end if end is not None else len(row)
            #print(f'{y},{start} - {y},{end}')
            for x in range(start, end):
                grid[y][x] = '#'
               
        print()     
        for row in grid:
            for edge in row:
                print(edge, end='')
            print()
            
            
        emptyCount = 0
        for row in grid:
            for edge in row:
                if edge == '.':
                    emptyCount += 1
                    
        diggedCount = 0
        for row in grid:
            for edge in row:
                if edge == '#':
                    diggedCount += 1
    
        print(len(grid) * len(grid[0]) - emptyCount)
        print(diggedCount)
                
import re
import math

class Node:
    def __init__(self, value,y = 0,x = 0):
        self.value = value
        self.visited = False
        self.y = y  
        self.x = x  
    def __repr__(self):
        return f'Node({self.value, self.visited, self.y, self.x})'
    
    def __str__(self):
        return f'Node({self.value, self.visited, self.y, self.x})'
    
    def __eq__(self, other) -> bool:
        return self.value == other.value
    

def find_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None  # Return None if the value is not found


pipesTypes = {
            '|': ('north', 'south'),
            '-': ('east', 'west'),
            'L': ('north', 'east'),
            'J': ('north', 'west'),
            '7': ('south', 'west'),
            'F': ('south', 'east'),
            '.': ('ground', 'ground'),
            'S': ('start', 'start')
        }
        
     
        
movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]
moveToDirection = {
            (0, 1): 'east',
            (1, 0): 'south',
            (0, -1): 'west',
            (-1, 0): 'north'
        }
        
directionToMove = {
            'east': (0, 1),
            'south': (1, 0),
            'west': (0, -1),
            'north': (-1, 0)
        }
        
flipDirection = {
            'east': 'west',
            'west': 'east',
            'north': 'south',
            'south': 'north'
        }
        

def inRange(grid, nextY, nextX):
    return 0 <= nextY < len(grid) and 0 <= nextX < len(grid[0])        
def findAdjacentValidPipes(y,x):
    pipes = []
    for move in movements:
        nextY = y + move[0]
        nextX = x + move[1]
        currentPipeType = pipesTypes[grid[y][x].value]
        if inRange(grid,nextY, nextX) and grid[nextY][nextX] != Node('.'):
            if moveToDirection[(move[0], move[1])] in currentPipeType:
                pipeType = pipesTypes[grid[nextY][nextX].value]
                dir = flipDirection[moveToDirection[(move[0], move[1])]]
                if dir in pipeType:
                    #print(grid[nextY][nextX], pipeType, dir)
                    #pipes.append([grid[nextY][nextX],(move[0], move[1])])
                    pipes.append(grid[nextY][nextX])  
    return pipes   

if __name__ == '__main__':
    grid = []
    with open('/home/matvs/Projects/advent-of-code/2023/day10.input.txt') as f:
        grid = f.readlines()
        grid = [line.strip() for line in grid]
        for i in range(len(grid)):
            grid[i] = list(grid[i])
            
        grid = [[Node(field,y,x) for x,field in enumerate(row)] for y,row in enumerate(grid)]
        
            
      
        startingPosition = None
        missingPipe = None
        for y in range(len(grid)):
            for x in range(len(grid[i])):
                if grid[y][x] == Node('S'):
                    startingPosition = (y, x)
                    for pipe in ['|', '-', 'L', 'J', '7', 'F']:
                        grid[y][x] = Node(pipe,y,x)      
                        pipes = findAdjacentValidPipes(y, x)
                        #print(pipes, pipe)
                        if len(pipes) == 2:
                            #pipes = [moveToDirection[pipe[1]] for pipe in pipes]
                            missingPipe = Node(pipe,y,x)
                            break
                        
                        #print(pipes)
                    #missingPipe = find_key_by_value(pipesTypes, (pipes[0], pipes[1])) if find_key_by_value(pipesTypes, (pipes[0], pipes[1])) else find_key_by_value(pipesTypes, (pipes[1], pipes[0]))
        print(missingPipe)
        
        
        missingPipe = grid[startingPosition[0]][startingPosition[1]]
        grid[startingPosition[0]][startingPosition[1]].visited = True
        pipes = findAdjacentValidPipes(startingPosition[0], startingPosition[1])
        #print(grid)
        currentPipe= pipes[0]
        
        distance = 0
        #print(currentPipe, missingPipe)
        while currentPipe:
           # print(currentPipe)
            distance += 1
            currentPipe.visited = True
            pipes = findAdjacentValidPipes(currentPipe.y, currentPipe.x)
            currentPipe = None
            for pipe in pipes:
                if pipe.visited == False:
                    currentPipe = pipe
                    break
          
        print(math.ceil(distance/2))     
            
      
    
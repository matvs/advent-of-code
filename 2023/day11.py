import re
import math

from collections import deque

def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def findOverlaps(numbers, start, end):
    overlapped = []
    start = min(start, end)
    end = max(start, end)      
    for number in numbers:
        if start < number < end:
            overlapped.append(number)
    print(overlapped )
    return len(overlapped)
    

def shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = deque([(start, 0, None)])
    distances = []

    while queue:
        (x, y), distance, source = queue.popleft()

        if (x, y) == end:
            return distance
        
        if (x, y) in visited: #or ((x,y) != start and grid[x][y] == "#"):
            continue

        visited.add((x, y))

        # Explore neighbors (up, down, left, right)
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < cols:  # Check for valid position
                #if grid[nx][ny] != "#" or (nx, ny) == end:
                queue.append(((nx, ny), distance + 1, (x, y)))
        
    #print(distances)   
    return min(distances) if distances else -1  # No path found
   # return -1  # No path found
        
if __name__ == '__main__':
    grid = []
    with open('/home/matvs/Projects/advent-of-code/2023/day11.input.txt') as f:
        grid = f.readlines()
        grid = [line.strip() for line in grid]
        emptyRows = []
        for i,row in enumerate(grid):
            if len(row) == len(re.findall(r'\.', row)):
                emptyRows.append(i)
                
        print(emptyRows)
        for i in range(len(grid)):
            grid[i] = list(grid[i])
        
    
        emptyColumns = []
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[y][x] != '.':
                    break
            if y == len(grid) - 1 and grid[y][x] == '.':
                emptyColumns.append(x)
        
        print(emptyColumns)

        
        galaxies = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '#':
                   galaxies.append((i,j))
        print(len(galaxies))
        
        sum = 0
        #shortest_paths = {}
        emptyMultiplier = 2
        for i in range (len(galaxies)):
            for j in range(i+1, len(galaxies)):
                distance = manhattan_distance(galaxies[i], galaxies[j])
                distance += findOverlaps(emptyRows, galaxies[i][0], galaxies[j][0]) * (emptyMultiplier - 1)
                distance += findOverlaps(emptyColumns, galaxies[i][1], galaxies[j][1]) * (emptyMultiplier - 1)
                #shortest_paths[galaxies[i], galaxies[j]] = distance
                #shortest_paths[galaxies[j], galaxies[i]] = distance
                sum += distance
                #print(galaxies[i][1], galaxies[j][1])
                #print(galaxies[i][0], galaxies[j][0])
                print('d =',distance, i + 1, '<->', j + 1,)
                
        print(sum)
        
        

        
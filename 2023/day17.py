import re
import math
from enum import Enum
import time
import os
import heapq
clear = lambda: os.system('clear')
                    
def parseInput(file):
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    
    return lines

def dijkstra(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    # Check if a move is valid
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    # State: (total_cost, x, y, last_direction, consecutive_moves)
    start_state = (0, start[0], start[1], -1, 0)
    visited = set()
    queue = []
    heapq.heappush(queue, start_state)

    while queue:
        cost, x, y, last_dir, consec_moves = heapq.heappop(queue)
        
        if (x, y) == end:
            return cost

        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy

            if is_valid(nx, ny) and (nx, ny) not in visited:
                new_cost = cost + grid[nx][ny]
                #print(nx,ny, new_cost)
                new_consec_moves = consec_moves + 1 if i == last_dir else 1

                # Check direction constraint
                if new_consec_moves <= 3:
                    new_state = (new_cost, nx, ny, i, new_consec_moves)
                    heapq.heappush(queue, new_state)

        visited.add((x, y))

    return -1  # Path not found 
         
if __name__ == '__main__':
    with open('/home/matvs/Projects/advent-of-code/2023/day17.input.txt') as f:
        lines = parseInput(f)
        
        grid = [[int(field) for field in row] for row in lines]
        print(dijkstra(grid, (0,0), (len(grid)-1, len(grid[0])-1)))
        
                

        
        
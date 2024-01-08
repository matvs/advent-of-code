import re
import math
from enum import Enum
import time
import os
import heapq
clear = lambda: os.system('clear')

def getMovementDirection(node, nextNode):
    return (nextNode.x - node.x, nextNode.y - node.y)

def dijkstra(graph, start, end):
    # Initialize distances and priority queue
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start, (0,0), 0)]

    while priority_queue:
        current_distance, current_node, lastMove, moveCount = heapq.heappop(priority_queue)
        
        #if current_node == end:
           # return distances[current_node]  

        # Only proceed if we have found a shorter way to current_node
        if current_distance > distances[current_node]:
            continue

        for neighbor in current_node.neighbors:
            if neighbor.isVisited:
                continue
            
            move = getMovementDirection(current_node, neighbor)
            consequentMoveCount = moveCount + 1 if move == lastMove else 1
            
            if consequentMoveCount > 3:
                continue
            
            distance = current_distance + neighbor.value
     
            # If a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor, move, consequentMoveCount))
        
        current_node.isVisited = True
    
    return distances


class Node:
    def __init__(self, value,x,y) -> None:
        self.value = int(value)
        self.isVisited = False
        self.neighbors = []
        self.x = x
        self.y = y
        
    def __str__(self) -> str:
        return str(self.value)
        
    def __repr__(self) -> str:
        return str(self.value)
    
    def __eq__(self, other: object) -> bool:
        if other == None:
            return False
        return self.value == other.value
    
    def __lt__(self, other: object) -> bool:
        return self.value < other.value
    
    def __hash__(self) -> int:
        return hash(str(self.value) + str(self.x) + str(self.y))
            

def addNeighbours(nodes):
    for y in range(len(nodes)):
        for x in range(len(nodes[y])):
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for dir in directions:
                newX = x + dir[0]
                newY = y + dir[1]
                if newX >= 0 and newX < len(nodes[y]) and newY >= 0 and newY < len(nodes):
                    nodes[y][x].neighbors.append(nodes[newY][newX])
                    
def parseInput(file):
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    
    return lines

def mapToNodes(lines):
    nodes = [[Node(field,x,y) for x,field in enumerate(row)] for y,row in enumerate(lines)]
    addNeighbours(nodes)
    # flatten nodes
    nodes = [node for sublist in nodes for node in sublist]  
    return nodes 


def find_shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # Right, Down, Up, Left
    dir_names = ["R", "D", "U", "L"]

    # Check if a move is valid
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and grid[x][y] != -1

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
        nodes = mapToNodes(lines)
        
        grid = [[int(field) for x,field in enumerate(row)] for y,row in enumerate(lines)]
        print(grid)
        
        print(find_shortest_path(grid, (0,0), (len(grid)-1, len(grid[0])-1)))
        print(dijkstra(nodes, nodes[0], nodes[-1]))
        
                

        
        
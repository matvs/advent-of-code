import re
import math
from enum import Enum
import time
import os
import heapq
clear = lambda: os.system('clear')


def dijkstra(graph, start):
    # Initialize distances and priority queue
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Only proceed if we have found a shorter way to current_node
        if current_distance > distances[current_node]:
            continue

        for neighbor in current_node.neighbors:
            distance = current_distance + neighbor.value

            # If a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


class Node:
    def __init__(self, value,x,y) -> None:
        self.value = int(value)
        self.isVisited = False
        self.neighbors = []
        self.sameDirectionMovesCount = 0
        self.x = x
        self.y = y
        
    def __str__(self) -> str:
        return str(self.value)
        
    def __repr__(self) -> str:
        return str(self.value)
    
    def __eq__(self, other: object) -> bool:
        return self.value == other.value
    
    def __lt__(self, other: object) -> bool:
        return self.value < other.value
    
    def __hash__(self) -> int:
        return hash(str(self.value) + str(self.x) + str(self.y))
            
        
if __name__ == '__main__':
    with open('/home/matvs/Projects/advent-of-code/2023/day17.input.txt') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        
        nodes = [[Node(field,x,y) for x,field in enumerate(row)] for y,row in enumerate(lines)]
        
        # add neighbors
        for y in range(len(nodes)):
            for x in range(len(nodes[y])):
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for dir in directions:
                    newX = x + dir[0]
                    newY = y + dir[1]
                    if newX >= 0 and newX < len(nodes[y]) and newY >= 0 and newY < len(nodes):
                        nodes[y][x].neighbors.append(nodes[newY][newX])
         
        # flatten nodes
        nodes = [node for sublist in nodes for node in sublist]              
        print(dijkstra(nodes, nodes[0]))
        
                

        
        
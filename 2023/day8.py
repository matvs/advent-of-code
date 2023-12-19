import re
from math import lcm
class Node():
    def __init__(self, label, left, right):
        self.left = left
        self.right = right
        self.label = label
        
    def __str__(self) -> str:
        return f"{self.label}, {self.left}, {self.right})"
    
    
def part2Runner(start, nodes):
    i = 0
    steps = 0
    while start.label[2] != 'Z':
        nextMove = instructions[i]
            
        if nextMove == 'L':    
            start = nodes[start.left]
        else:    
            start = nodes[start.right]
            
        steps += 1
        i += 1
        i = i % len(instructions)
    return steps    

if __name__ == '__main__':
    grid = []
    with open('/home/matvs/Projects/advent-of-code/2023/day8.input.txt') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        instructions = lines[0]
        nodes = {}
        for line in lines[2:]:
            labels = re.findall('([A-Z]+)', line)
            nodes[labels[0]] = Node(labels[0], labels[1], labels[2])
            
        start = nodes['AAA']
        
        i = 0
        steps = 0
        while start != nodes['ZZZ']:
            nextMove = instructions[i]
            
            if nextMove == 'L':    
                start = nodes[start.left]
            else:    
                start = nodes[start.right]
            
            steps += 1
            i += 1
            i = i % len(instructions)
            
        print(steps)
        ## part 2
        
        i = 0
        steps = 0
        
        startingNodes = list(filter(lambda node: node.label[2] == 'A', nodes.values()))
        for node in startingNodes:
            print(node)
        
        allSteps = [part2Runner(node, nodes) for node in startingNodes]
            
        print(lcm(*allSteps))
            
          

        

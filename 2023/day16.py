import re
import math
from enum import Enum
import time
import os
clear = lambda: os.system('clear')

class Grid:
    def __init__(self, rows, columns) -> None:
        self.rows = rows
        self.columns = columns
        self.grid = [[0 for _ in range(columns)] for _ in range(rows)]
        
    def getNumberOfEnergizedCells(self):
        energizedCells = 0
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if self.grid[y][x].isEnergized:
                    energizedCells += 1
        return energizedCells
        
        
    def render(self, beams):
        energizedCells = {}
        while len(beams) != 0:
            #clear()
            beamsToBeMoved = []
            for y in range(len(lines)):
                for x in range(len(lines[y])):
                    foundBeams = list(filter(lambda beam: beam.position == (x,y), beams))
                    if len(foundBeams) != 0:
                        #print('>', end = '')
                        for beam in foundBeams:
                            beamsToBeMoved.append(beam)
                            grid.grid[beam.position[1]][beam.position[0]].isEnergized = True
                            energizedCells[(beam.position[0], beam.position[1], beam.direction)] = True
                    else:
                        pass
                        #print(self.grid[y][x], end = '')
                #print()
                
            for beam in beamsToBeMoved:
                moveResult = beam.move(self)
                if moveResult == None:
                    beams.remove(beam)
                elif len(moveResult) == 2:
                    beams.append(moveResult[1])
                    
                if moveResult != None:
                    for beam in moveResult:
                        if energizedCells.get((beam.position[0], beam.position[1], beam.direction)) != None:
                            beams.remove(beam)
            #time.sleep(0.5)  
            
        return self.getNumberOfEnergizedCells()
        
class Space:
    def __init__(self, symbol) -> None:
        self.symbol = symbol
        
class Splitter(Space):
    def __init__(self, symbol) -> None:
        super().__init__(symbol)

class Mirror(Space):
    def __init__(self, symbol) -> None:
        super().__init__(symbol)
        
class EmptySpace(Space):
    def __init__(self, symbol) -> None:
        super().__init__(symbol)        
                
        
class Cell:
    def __init__(self, content, isEnergized = False) -> None:
        self.isEnergized = isEnergized
        self.content = content
        
    def __repr__(self) -> str:
        return self.content.symbol  

class Direction(Enum):
    Up = (0, -1)
    Down = (0, 1)
    Left = (-1, 0)
    Right = (1, 0)
    

class Beam:
    def __init__(self, x = 0, y = 0, direction = Direction.Right) -> None:
        self.position = (x,y)
        self.direction = direction
        
    def __str__(self) -> str:
        return f'Beam: {self.position} {self.direction}'
    
    def __repr__(self) -> str:
        return f'Beam: {self.position} {self.direction}'
    
    def caluculateNextPosition(self):
        x, y = self.position
        dx, dy = self.direction.value
        x += dx
        y += dy
        return (x,y)
    
    def checkIfInBounds(self, position, grid: Grid):
        x, y = position
        if x >= 0 and x < grid.columns and y >= 0 and y < grid.rows:
            return True
        return False
    
    def move(self, grid: Grid):
        position = self.caluculateNextPosition()
        if not self.checkIfInBounds(position, grid):
            return None
        
        self.position = position
        
        cellContent = grid.grid[position[1]][position[0]].content
        if isinstance(cellContent, Mirror):
            if self.direction == Direction.Right:
                if cellContent.symbol == '/':
                    self.direction = Direction.Up
                elif cellContent.symbol == '\\':    
                    self.direction = Direction.Down
            elif self.direction == Direction.Left:
                if cellContent.symbol == '/':
                    self.direction = Direction.Down
                elif cellContent.symbol == '\\':    
                    self.direction = Direction.Up
            elif self.direction == Direction.Up:
                if cellContent.symbol == '/':
                    self.direction = Direction.Right
                elif cellContent.symbol == '\\':    
                    self.direction = Direction.Left
            elif self.direction == Direction.Down:
                if cellContent.symbol == '/':
                    self.direction = Direction.Left
                elif cellContent.symbol == '\\':    
                    self.direction = Direction.Right
    
        elif isinstance(cellContent, Splitter):
            if cellContent.symbol == '-':
                if self.direction == Direction.Up or self.direction == Direction.Down:
                    self.direction = Direction.Right
                    newBeam = Beam(position[0], position[1], Direction.Left)
                    return [self, newBeam]
            elif cellContent.symbol == '|':
                if self.direction == Direction.Left or self.direction == Direction.Right:
                    self.direction = Direction.Up
                    newBeam = Beam(position[0], position[1], Direction.Down)
                    return [self, newBeam]
        
        return [self]
        
            
        
if __name__ == '__main__':
    with open('/home/matvs/Projects/advent-of-code/2023/day16.input.txt') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        grid = Grid(len(lines), len(lines[0]))
        
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] == '/' or lines[y][x] == '\\':
                    grid.grid[y][x] = Cell(Mirror(lines[y][x]))
                elif lines[y][x] == '|' or lines[y][x] == '-':
                    grid.grid[y][x] = Cell(Splitter(lines[y][x]))
                elif lines[y][x] == '.':
                    grid.grid[y][x] = Cell(EmptySpace(lines[y][x]))
                    
        #print(grid.grid)
        
        beams = [Beam(-1,0)]
        beams[0].move(grid)
        print(grid.render(beams))
        maxEnergizedCells = 0
        for y in range(len(lines)):
            beams = [Beam(-1,y, Direction.Right)]
            beams[0].move(grid)
            maxEnergizedCells = max(maxEnergizedCells, grid.render(beams))
        
        for y in range(len(lines)):
            beams = [Beam(len(lines),y, Direction.Left)]
            beams[0].move(grid)
            maxEnergizedCells = max(maxEnergizedCells, grid.render(beams))
            
        for x in range(len(lines)):
            beams = [Beam(x,-1, Direction.Down)]
            beams[0].move(grid)
            maxEnergizedCells = max(maxEnergizedCells, grid.render(beams))
            
        for x in range(len(lines)):
            beams = [Beam(x,len(lines), Direction.Up)]
            beams[0].move(grid)
            maxEnergizedCells = max(maxEnergizedCells, grid.render(beams))
            
        print(maxEnergizedCells)

      
                

        
        
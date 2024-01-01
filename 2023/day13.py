import re
import math
import copy
            
        
if __name__ == '__main__':
    with open('/home/matvs/Projects/advent-of-code/2023/day13.input.txt') as f:
        lines = f.read().split('\n\n')
        for i in range(len(lines)):
            lines[i] = lines[i].split('\n')

        grids = lines
        for grid in grids:
            for y in range(len(grid)):
                grid[y] = list(grid[y])
        #print(lines)

        

        def checkIfSymmetry(x,grid):
            for y in range(len(grid)):
                row = grid[y]
                left = x - 1
                right = x
                while left >=0 and right < len(grid[y]):
                    #print(x,left, right)
                    if row[left] != row[right]:
                    #print(y,x,left,right,line[left], line[right])
                        return False
                    left -= 1
                    right += 1
            return True
        
        def printGridWithSymmetryLine(grid,symmetryLine):
            for y in range(len(grid)):
                for x in range(len(grid[y])):
                    if x == symmetryLine:
                        print('|', end='')
                    print(grid[y][x], end='')
                print()
            print()
            
        def printGrid(grid):
            for y in range(len(grid)):
                for x in range(len(grid[y])):
                    print(grid[y][x], end='')
                print()
            print()
                        
        def findAllSymmetries(grid, symmetries = []):
            for x in range(1,len(grid[0])):
                symmetry = checkIfSymmetry(x,grid)
                if symmetry:
                    symmetries.append(x)
                    #printGridWithSymmetryLine(grid,x)
        
        def findVerticalSymmetries(grids):
            verticalSymmetries = []
       
            for grid in grids:
              findAllSymmetries(grid, verticalSymmetries)

            return verticalSymmetries
        
        def findHorizontalSymmetries(grids):
            horizontalSymmetries = []
  
            for grid in grids:
                grid = list(zip(*grid))
                #print(line)
                findAllSymmetries(grid, horizontalSymmetries)

                        
            return horizontalSymmetries
        
        def calculateScore(verticalSymmetries, horizontalSymmetries):
            sumOfSymmetries = sum(verticalSymmetries)
            horizontalSymmetries = [ x*100 for x in horizontalSymmetries]
            sumOfSymmetries += sum(horizontalSymmetries)
            return sumOfSymmetries
        
        
        verticalSymmetries = findVerticalSymmetries(grids)
        horizontalSymmetries = findHorizontalSymmetries(grids)

 
        print(calculateScore(verticalSymmetries, horizontalSymmetries))
        
        def getSymmetriesForOneGrid(grid):
            verticalSymmetries = findVerticalSymmetries([grid])
            horizontalSymmetries = findHorizontalSymmetries([grid])
            return verticalSymmetries, horizontalSymmetries
        
        
        def modifyGrid(grid, x, y):
            copyOfGrid = copy.deepcopy(grid)
            copyOfGrid[y][x] = '.' if copyOfGrid[y][x] == '#' else '#'
            return copyOfGrid
        
        
        def removeOriginalSymmetries(verticalSymmetries, originalVerticalSymmetries, horizontalSymmetries, originalHorizontalSymmetries):
            for symmetry in originalVerticalSymmetries:
                if symmetry in verticalSymmetries:
                    verticalSymmetries.remove(symmetry)
                
            for symmetry in originalHorizontalSymmetries:
                if symmetry in horizontalSymmetries:
                    horizontalSymmetries.remove(symmetry)
                    
        def addUniqueSymmetries(allSymmetries, newSymmetries): 
            allSymmetries += list(set(newSymmetries))
            
        def findNewSymmetriesAftreOneChange(grids):
            allVertivalSymmetries, allHorizontalSymmetries = [], []
            for grid in grids:
                originalVerticalSymmetries,originalHorizontalSymmetries = getSymmetriesForOneGrid(grid)
                verticalSymmetries, horizontalSymmetries = [], []
                for y in range(len(grid)):
                    for x in range(len(grid[y])):
                        copyOfGrid = modifyGrid(grid,x,y)
                        verticalSymmetries += findVerticalSymmetries([copyOfGrid])
                        horizontalSymmetries += findHorizontalSymmetries([copyOfGrid])
                        removeOriginalSymmetries(verticalSymmetries, originalVerticalSymmetries, horizontalSymmetries, originalHorizontalSymmetries)
            
                addUniqueSymmetries(allVertivalSymmetries, verticalSymmetries)
                addUniqueSymmetries(allHorizontalSymmetries, horizontalSymmetries)       
                
            print(calculateScore(allVertivalSymmetries, allHorizontalSymmetries))
            
            
        findNewSymmetriesAftreOneChange(grids)
                    
                    
            
        
        
        
                
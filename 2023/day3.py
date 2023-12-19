import re


def resetState(grid): 
    for x in range(0, columns):
        for y in range(0, rows):
            if isinstance(grid[y][x],NumberClass):
                grid[y][x].checked = False

class NumberClass:
    def __init__(self, value):
        self.value = value
        self.checked = False
    
    def size(self):
        return len(str(self.value))
    
    def __str__(self):
        return str(self.value)
if __name__ == '__main__':
    grid = []
    with open('/home/matvs/Projects/advent-of-code/2023/day3.input.txt') as f:
        sum = 0
        lines = f.readlines()
        for y,line in enumerate(lines):
            grid.append([])
            number = ''
            for char in line:
                if char.isdigit():
                    number += char
                else:
                    if number != '':
                        numberObject = NumberClass(int(number))
                        for i in range(0, numberObject.size()):
                            grid[y].append(numberObject)
                        number = ''
                    if char != '\n':
                        grid[y].append(char)
        columns = len(grid[0])
        rows = len(grid)
        print(columns, rows)
        sum = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        for x in range(0, columns):
            for y in range(0, rows):
                if isinstance(grid[y][x],NumberClass) and not grid[y][x].checked:
                    for directionX, directionY in directions:
                        newX = x + directionX
                        newY = y + directionY
                        if newX >= 0 and newX < columns and newY >= 0 and newY < rows:
                            if not isinstance(grid[newY][newX], NumberClass) and grid[newY][newX] != '.':
                                #print(grid[y][x])
                                grid[y][x].checked = True
                                sum += grid[y][x].value
        print(sum)

        #part 2
        sum = 0
        for x in range(0, columns):
            for y in range(0, rows):
                resetState(grid)
                partialNumbers = []
                if grid[y][x] == '*':
                    for directionX, directionY in directions:
                        newX = x + directionX
                        newY = y + directionY
                        if newX >= 0 and newX < columns and newY >= 0 and newY < rows:
                            if isinstance(grid[newY][newX],NumberClass) and not grid[newY][newX].checked:
                                grid[newY][newX].checked = True
                                partialNumbers.append(grid[newY][newX].value)
                    if len(partialNumbers) == 2:
                        sum += partialNumbers[0] * partialNumbers[1]    
        print(sum)
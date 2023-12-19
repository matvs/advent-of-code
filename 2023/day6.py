import re
from functools import reduce
import math

def solve_quadratic(a, b, c):
    # Oblicz deltę
    delta = math.sqrt(b**2 - 4*a*c)

    # Oblicz oba pierwiastki
    root1 = (-b + delta) / (2*a)
    root2 = (-b - delta) / (2*a)

    return root1, root2

def findNumberOfWaysToWin(time, distance):
    roots = solve_quadratic(-1, time, -distance)
    
    left = math.ceil(min(roots))
    if min(roots).is_integer():
        left += 1   
    right = math.floor(max(roots))
    if max(roots).is_integer():
        right -= 1
    return right - left + 1
if __name__ == '__main__':
    grid = []
    with open('/home/matvs/Projects/advent-of-code/2023/day6.input.txt') as f:
        lines = f.readlines()

        times = [int(x) for x in re.split(r' +', lines[0])[1:]]
        distances = [int(x) for x in re.split(r' +', lines[1])[1:]]
        print(times)
        print(distances)
        
        numberOfWaysToWin = []
        for i in range(len(times)):
            numberOfWaysToWin.append(findNumberOfWaysToWin(times[i], distances[i]))
            
        print(numberOfWaysToWin)
        print(reduce(lambda x, y: x*y, numberOfWaysToWin,1))
        
        time = int(reduce(lambda x, y: str(x)+str(y), times))
        distance = int(reduce(lambda x, y: str(x)+str(y), distances))
        print(findNumberOfWaysToWin(time, distance))
import re



class Point:
    def __init__(self, x, y, z) -> None:
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        
    def __repr__(self) -> str:
        return f'x={self.x},y={self.y},z={self.z}'
    
    def substract(self, other):
        x = abs(self.x - other.x + 1)
        y = abs(self.y - other.y + 1)
        z = abs(self.z - other.z + 1)
        
        return Point(x,y,z)
        
class Brick:
    def __init__(self, pointA, pointB, label) -> None:
        self.pointA = pointA
        self.pointB = pointB

        self.setMinimums(pointA,pointB)
        self.setMaximums(pointA,pointB)
        
        self.label = label
        
    def setMinimums(self,pointA, pointB):      
        self.minX = min(pointA.x, pointB.x)
        self.minX = min(pointA.x, pointB.x)
        
        self.minY = min(pointA.y, pointB.y)
        self.minY = min(pointA.y, pointB.y)
        
        self.minZ = min(pointA.z, pointB.z)
        self.minZ = min(pointA.z, pointB.z)
        
    def setMaximums(self,pointA, pointB):      
        self.maxX = max(pointA.x, pointB.x)
        self.maxX = max(pointA.x, pointB.x)
        
        self.maxY = max(pointA.y, pointB.y)
        self.maxY = max(pointA.y, pointB.y)
        
        self.maxZ = max(pointA.z, pointB.z)
        self.maxZ = max(pointA.z, pointB.z)        
    def __repr__(self) -> str:
        return f'{self.label}: {self.pointA} {self.pointB}'
    
    def volume(self):
        diff = self.pointA.substract(self.pointB)
        return diff.x * diff.y * diff.z
    
    def occupies(self, point):
        return point.x >= self.minX and point.x <= self.maxX and point.y >= self.minY and point.y <= self.maxY and point.z >= self.minZ and point.z <= self.maxZ
        
    def occupiesXZ(self, point):
        point.y = self.minY
        return self.occupies(point)

    def occupiesYZ(self, point):
        point.x = self.minX
        return self.occupies(point)
    
    def __eq__(self, other: object) -> bool:
        return self.minZ == other.minZ
    
    def __lt__(self, other):
        return self.minZ - other.minZ
        
def parseInput(lines):
    bricks = []
    lines = [(line.strip()) for line in lines]
    label = 1
    for line in lines:
        pointA, pointB = line.split('~')
        
        x,y,z = pointA.split(',')
        pointA = Point(x,y,z)
        
        x,y,z = pointB.split(',')
        pointB = Point(x,y,z)
        
        bricks.append(Brick(pointA,pointB, label))
        label += 1
        
    return bricks


def printZX(bricks):
    for z in range(10,0,-1):
        for x in range(3):
            renderedBrick = False
            for brick in bricks:
                if brick.occupiesXZ(Point(x,0,z)):
                        print(brick.label, end='')
                        renderedBrick = True
                        break
            if not renderedBrick:
                print('.', end='')
        print()
        
def printYZ(bricks):
    for z in range(10,0,-1):
        for y in range(3):
            renderedBrick = False
            for brick in bricks:
                if brick.occupiesYZ(Point(0,y,z)):
                        print(brick.label, end='')
                        renderedBrick = True
                        break
            if not renderedBrick:
                print('.', end='')
        print()     

def generateBricksMaxZ(bricks):
    bricksMaxZ = {}
    for brick in bricks:
        bricksMaxZ = {brick.maxZ: brick}
        
    return bricksMaxZ
def fallOneStep(bricks,bricksMinZ):
    bricks.sort()
    bricks = bricks[::-1]
    didSomethingFell = False
    for brick in bricks:
        z = brick.minZ - 1
        if z >= 1 and z not in bricksMinZ:
            didSomethingFell = True
            
        
    return didSomethingFell
        
    

with open('/home/matvs/Projects/advent-of-code/2023/day22.input.txt') as f:
    lines = f.readlines()
    bricks = parseInput(lines)
    
    print(bricks)
    bricks.sort()
    bricks = bricks[::-1]
    print(bricks)

    printZX(bricks)
    print()
    printYZ(bricks)
    
    minZs = generateBricksMaxZ(bricks)
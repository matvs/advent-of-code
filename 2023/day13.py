import re
import math
            
        
if __name__ == '__main__':
    with open('/home/matvs/Projects/advent-of-code/2023/day13.input.txt') as f:
        lines = f.read().split('\n\n')

        for i in range(len(lines)):

            lines[i] = lines[i].split('\n')

        

        print(lines)

        

        def findSymmetry(x,lines):

            for y in range(len(lines)):

                line = lines[y]

                left = x - 1

                right = x

                while left >=0 and right < len(lines[y]):

                    #print(x,left, right)

                    if line[left] != line[right]:

                        #print(y,x,left,right,line[left], line[right])

                        return False

                    left -= 1

                    right += 1

            return True

        

            

        verticalSymmetries = []

        horizontalSymmetries = []

        for line in lines:

            for x in range(1,len(line[0]) - 2):

                symmetry = findSymmetry(x,line)

                if symmetry:

                    verticalSymmetries.append(x)

                

        print(verticalSymmetries)

        

        

        

        for line in lines:

            line = list(zip(*line))

            #print(line)

            for x in range(1,len(line[0]) - 2):

                symmetry = findSymmetry(x,line)

                if symmetry:

                    horizontalSymmetries.append(x)

                

        print(horizontalSymmetries)

        

        sumOfSymmetries = sum(verticalSymmetries)

        horizontalSymmetries = [ x*100 for x in horizontalSymmetries]

        sumOfSymmetries += sum(horizontalSymmetries)

        

        print(sumOfSymmetries)
                
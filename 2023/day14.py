import re
import math


            
        
if __name__ == '__main__':
    with open('/home/matvs/Projects/advent-of-code/2023/day14.input.txt') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        for y in range(len(lines)):

            lines[y] = list(lines[y])

        

        for y, line in enumerate(lines):

            for x, field in enumerate(line):

            #  print(x, ' ', y, ' ', field)

                if field == 'O':

                    start = y

                    while start > 0 and (lines[start - 1][x] != '#' and lines[start - 1][x] != 'O'):

                        start -= 1

                    lines[y][x] = '.'

                    lines[start][x] = 'O'

                    print(y,'/',start)

        

        sum = 0

        for y, line in enumerate(lines):

            for x, field in enumerate(line):

            #  print(x, ' ', y, ' ', field)

                if field == 'O':

                    sum += len(lines) - y         

                    
        print(lines)
        print(sum)         

        #for y, line in enumerate(lines):

        #   for x,field in enumerate(line):

        #      print(field, sep='')

        # print()

        

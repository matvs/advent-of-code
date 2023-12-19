import re
import math


            
        
if __name__ == '__main__':
    with open('/home/matvs/Projects/advent-of-code/2023/day12.input.txt') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        tokens = []
        for line in lines:
            tokens.append(line.split(' '))
            tokens[-1][1] = [int(x) for x in tokens[-1][1].split(',')]

        

        print(tokens)

        

        def isValid(tokens):
            currentGroupIndex = 0
            currentSymbol = ''

            for char in tokens[0]:

                if char == '#':

                    currentSymbol += char

                else:

                    if len(currentSymbol) > 0:

                        if (currentGroupIndex >= len(tokens[1]) or len(currentSymbol) != tokens[1][currentGroupIndex]):

                            return False

                        else:

                            currentGroupIndex += 1

                    currentSymbol = ''

                

            if len(currentSymbol) > 0:

                if currentGroupIndex >= len(tokens[1]):

                    return False

            if currentGroupIndex == len(tokens[1]) - 1:

                return len(currentSymbol) == tokens[1][currentGroupIndex]

            if currentGroupIndex < len(tokens[1]):

                return False

            return True

        

            

        def generate(s, i=0, current = ''):

            if i == len(s):

                return [current]

            if s[i] == '?':

                return generate(s, i + 1, current + '.') + generate(s, i + 1, current + '#')

            else:

                return generate(s, i + 1, current + s[i])

        

            

        sum = 0   

        for token in tokens:

            subSum = 0

            all = generate(token[0])

            for s in all:

                if isValid([s,token[1]]):

                    subSum += 1

                    sum += 1

                    print(s)

            print(token[0], ' ', subSum, ' ', token[1])

            print()

        print(sum)
                
                
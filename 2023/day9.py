import re

def nextSequence(sequence):
    return [sequence[i+1] - sequence[i] for i in range(len(sequence) - 1)]

def allZero(sequence):
    for num in sequence:
        if num != 0:
            return False
    return True

if __name__ == '__main__':
    grid = []
    with open('/home/matvs/Projects/advent-of-code/2023/day9.input.txt') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [line.split(' ') for line in lines]
        lines = [[int(num) for num in line] for line in lines]
        sum = 0
        for line in lines:
            sequences = [line]
            
            while not allZero(line):
               line = nextSequence(line)
               sequences.append(line)
            for i in range(len(sequences) - 1, 0, -1):
                # PART 1
                #sequences[i - 1].append(sequences[i - 1][-1] + sequences[i][-1])
                sequences[i - 1] = [sequences[i - 1][0] - sequences[i][0]] + sequences[i - 1]
            print(sequences)
            # PART 1
            #sum += sequences[0][-1]
            sum += sequences[0][0]
            
        print(sum)

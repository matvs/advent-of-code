import re

def scoreCards(line,winnings,lines, index):
    tokens = line.split(':')[1].split('|' ) 
    winningNumbers = re.findall(r'\d+', tokens[0])
    selectedNumbers = re.findall(r'\d+', tokens[1])
    numberOfWinnings = 0
    for (i, number) in enumerate(selectedNumbers):
        if number in winningNumbers:
            numberOfWinnings += 1
    for i in range(index + 2, numberOfWinnings + index + 2):
        if i in winnings:
            winnings[i] += 1
        else:
            winnings[i] = 1
        #print ('card no ' + str(index + 1) + ' won card no ' + str(i))
        scoreCards(lines[i - 1], winnings, lines, i - 1)
    return  
if __name__ == '__main__':
    grid = []
    with open('/home/matvs/Projects/advent-of-code/2023/day4.input.txt') as f:
        sum = 0
        winnings = {}
        copies = []
        lines = f.readlines()
        for index, line in enumerate(lines):
            tokens = line.split(':')[1].split('|' ) 
            winningNumbers = re.findall(r'\d+', tokens[0])
            selectedNumbers = re.findall(r'\d+', tokens[1])
            numberOfWinnings = 0
            for (i, number) in enumerate(selectedNumbers):
                if number in winningNumbers:
                    numberOfWinnings += 1
            if numberOfWinnings > 0:
                sum += pow(2, numberOfWinnings - 1)
     
        print(sum)
        for index, line in enumerate(lines):
            scoreCards(line, winnings, lines, index)
        #print(winnings)
        sum = 0
        for key, value in winnings.items():
            sum += value
        print(sum + len(lines))

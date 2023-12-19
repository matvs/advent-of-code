import re
if __name__ == '__main__':
    with open('/home/matvs/Projects/advent-of-code/2023/day1.input.txt') as f:
        lines = f.readlines()
        digits = { 'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e',
                   'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9n'}
        newLines = []
        for line in lines:
            #print(line, end='')
            word = re.search(r'(one|two|three|four|five|six|seven|eight|nine)', line)
            while word != None:
                line = line.replace(word.group(0), digits[word.group(0)], 1)
                word = re.search(r'(one|two|three|four|five|six|seven|eight|nine)', line)
            newLines.append(line)
            #print(line, end='')
            #print()


        sum = 0
        for line in newLines:
           # print(line)
            firstDigit = None;
            secondDigit = None;   
            for char in line:
                if char.isdigit():
                    if firstDigit == None:
                        firstDigit = char
                    secondDigit = char
            #print(int(firstDigit + secondDigit))
            sum += int(firstDigit + secondDigit)
        print(sum)

       
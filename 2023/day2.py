import re

def isPossible(sums):
    tresholds = {'red': 12, 'green': 13, 'blue': 14}
    for key in sums.keys():
        if sums[key] > tresholds[key]:
            return False
    return True


if __name__ == '__main__':
    with open('/home/matvs/Projects/advent-of-code/2023/day2.input.txt') as f:
        sum = 0
        
        lines = f.readlines()
        for line in lines:
            tokens = line.split(':')
            gameId = re.findall(r'\d+', tokens[0])[0]
            games = tokens[1].split(';')
        
            wasAGamePossible = False
            for game in games:
                game = re.findall(r'(\d+) (red|green|blue)', game)
                sums = {'red': 0, 'green': 0, 'blue': 0}
                for g in game:
                    sums[g[1]] += int(g[0])
                #print(gameId, sums, isPossible(sums))
                wasAGamePossible = isPossible(sums)
                if not wasAGamePossible:
                    break
            if wasAGamePossible:
                sum += int(gameId)
        print(sum)
        
        sum = 0
        for line in lines:
            tokens = line.split(':')
            gameId = re.findall(r'\d+', tokens[0])[0]
            games = tokens[1].split(';')
        
            max = {'red': 0, 'green': 0, 'blue': 0}
            for game in games:
                game = re.findall(r'(\d+) (red|green|blue)', game)
                sums = {'red': 0, 'green': 0, 'blue': 0}
                for g in game:
                    sums[g[1]] += int(g[0])
                for key in sums.keys():
                    if sums[key] > max[key]:
                        max[key] = sums[key]
            factor = 1
            for key in max.keys():
                factor *= max[key]
            sum += factor
        print(sum)




import re

class Mapper:
    def __init__(self,source, destination, mappingsUnParsed) -> None:
        self.source = source
        self.destination = destination
        self.mappings = {}
        self.mappingsUnParsed = []
        for mapping in mappingsUnParsed:
            mapping =  [int(x) for x in re.findall(r'(\d+)', mapping)]
            self.mappingsUnParsed.append(mapping)
          #  print(mapping)
         #   for i in range(mapping[2]):
          #      self.mappings[mapping[1] + i] = mapping[0] + i
        #print(self.mappings)
        
def mapToLocation(seeds, mappers):
    values = []
    for value in seeds:
        for mapper in mappers:
            if value in mapper.mappings:
                value = mapper.mappings[value]
                #print (mapper.source, '==>', mapper.destination, value, mapper.mappings[value])
         #   else:
                #print (mapper.source, '==>', mapper.destination, value, value)
        values.append(value)
    return values

def mapToLocation2(seeds, mappers):
    values = []
    for value in seeds:
        for mapper in mappers:
            for mapping in mapper.mappingsUnParsed:
                if value >= mapping[1] and value < mapping[1] + mapping[2]:
                    oldVal = value
                #    print(value, mapping[0], mapping[1], mapping[2])
                    value = mapping[0] + value - mapping[1]
              #      print(value)
                   # print (mapper.source, '==>', mapper.destination, oldVal, value)
                    break
              #  else:
                  #  print (mapper.source, '==>', mapper.destination, value, value)
        values.append(value)
    return values

def mapToLocation3(seeds, mappers):
    values = []
    for value in seeds:
        for mapper in mappers:
            for mapping in mapper.mappingsUnParsed:
                if value >= mapping[1] and value < mapping[1] + mapping[2]:
                    oldVal = value
                #    print(value, mapping[0], mapping[1], mapping[2])
                    value = mapping[0] + value - mapping[1]
              #      print(value)
                   # print (mapper.source, '==>', mapper.destination, oldVal, value)
                    break
              #  else:
                  #  print (mapper.source, '==>', mapper.destination, value, value)
        values.append(value)
    return values

class Range:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
    
    def findCommonPart(self, other):
        if self.end < other.start or self.start > other.end:
            return None
        return Range(max(self.start, other.start), min(self.end, other.end))
                     
    def __str__(self) -> str:
        return f'[{self.start}, {self.end}]'


if __name__ == '__main__':
    grid = []
    with open('/home/matvs/Projects/advent-of-code/2023/day5.input.txt') as f:
        sum = 0
        winnings = {}
        copies = []
        lines = f.read()
        tokens = lines.split('\n\n')
        seeds = [int(x) for x in re.findall(r'(\d+)', tokens[0])]
        print(seeds)
        mappers = []
        for i in range(1, len(tokens)):
            mapTokens = tokens[i].split('\n')
            mappings = mapTokens[1:]
            sourceDestinations = mapTokens[0].split(' ')[0].split('-to-')
            mappers.append(Mapper(sourceDestinations[0], sourceDestinations[1], mappings))
        
        #seeds = [14]
  
        print(min(mapToLocation2(seeds, mappers)))
        
        # Part 2 
        newSeeds = []
        for i in range(0, len(seeds) - 1, 2):
            newSeeds.append(Range(seeds[i], seeds[i] + seeds[i + 1] - 1))
        
      #  for seed in newSeeds:
       #     print(seed)
            
        allMappings = []
        for i in range(1, len(tokens)):
            mapTokens = tokens[i].split('\n')
            mappings = mapTokens[1:]
            mappings = [[int(x) for x in re.findall(r'(\d+)', mapping)] for mapping in mappings]
            allMappings.append([(Range(mapping[1], mapping[1] + mapping[2] - 1 ), Range(mapping[0], mapping[0] + mapping[2] - 1)) for mapping in mappings])
            
        for mappings in allMappings:
            for mapping in mappings:
                for seed in newSeeds:
                    nextValues = []
                    common = seed.findCommonPart(mapping[0])
                    if common:
                        offsetStart = common.start - mapping[0].start
                        offsetEnd = mapping[0].end - common.end
                        Range(mapping[1].start + offsetStart, mapping[1].end - offsetEnd)
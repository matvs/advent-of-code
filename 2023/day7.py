import re

class Hand:
    def __init__(self, cards,bid):
        self.cards = cards
        self.bid = bid
        self.type = calculateType(cards)
        
    def __str__(self) -> str:
        return f"{self.cards}, {self.type}, {self.bid})"
        
        
    # Define less than ("<") comparison
    def __lt__(self, other):
        if self == other:
            mapping = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
            for i in range(len(self.cards)):
                selfCard = self.cards[i]
                otherCard = other.cards[i]
                if selfCard in mapping:
                    selfCard = mapping[selfCard]    
                if otherCard in mapping:
                    otherCard = mapping[otherCard]
                if selfCard == otherCard:
                    continue
                else:
                    return int(selfCard) < int(otherCard)
            return True
        
        return self.type[0] > other.type[0]

    # Define equal to ("==") comparison
    def __eq__(self, other):
        return self.type[0] == other.type[0]
    
def calculateType(cards):
    counts = {}
    for card in cards:
        if card in counts:
            counts[card] += 1
        else:
            counts[card] = 1
    if len(counts) == 1:
        return (0, 'fiveOfAKind')
    elif len(counts) == 2:
        if 4 in counts.values():
            return (1, 'fourOfAKind')
        else:
            return (2, 'fullHouse')
    elif len(counts) == 3:
        if 3 in counts.values():
            return (3, 'threeOfAKind')
        else:
            return (4, 'twoPairs')
    elif len(counts) == 4:  
        return (5, 'onePair')
    else:
        return (6, 'highCard')

        
        # partTwo
        
class Hand2:
    def __init__(self, cards,bid):
        self.cards = cards
        self.bid = bid
        self.type = calculateType2(cards)
        
    def __str__(self) -> str:
        return f"{self.cards}, {self.type}, {self.bid})"
        
        
    # Define less than ("<") comparison
    def __lt__(self, other):
        if self == other:
            mapping = {'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14}
            for i in range(len(self.cards)):
                selfCard = self.cards[i]
                otherCard = other.cards[i]
                if selfCard in mapping:
                    selfCard = mapping[selfCard]    
                if otherCard in mapping:
                    otherCard = mapping[otherCard]
                if selfCard == otherCard:
                    continue
                else:
                    return int(selfCard) < int(otherCard)
            return True
        
        return self.type[0] > other.type[0]
    
        # Define equal to ("==") comparison
    def __eq__(self, other):
        return self.type[0] == other.type[0]
            
def calculateType2(cards):
    counts = {}
    for card in cards:
        if card in counts:
            counts[card] += 1
        else:
            counts[card] = 1
   
    
    if 'J' in counts and counts['J'] != 5:
        numberOfJokers = len(re.findall('J', cards))   
        del counts['J']
        maxCounts = max(counts.values())
        #print(numberOfJokers, cards)   
        for key in counts:
            #print(counts)
            if counts[key] == maxCounts:
                counts[key] += numberOfJokers
                break
        
            #  print(counts)

        #  print(counts)
            
    if len(counts) == 1:
        return (0, 'fiveOfAKind')
    elif len(counts) == 2:
        if 4 in counts.values():
            return (1, 'fourOfAKind')
        else:
            return (2, 'fullHouse')
    elif len(counts) == 3:
        if 3 in counts.values():
            return (3, 'threeOfAKind')
        else:
            return (4, 'twoPairs')
    elif len(counts) == 4:  
        return (5, 'onePair')
    else:
        return (6, 'highCard')
                

if __name__ == '__main__':
    grid = []
    with open('/home/matvs/Projects/advent-of-code/2023/day7.input.txt') as f:
        lines = f.readlines()
        cards = [line.split(' ')[0] for line in lines]
        bids = [int(line.split(' ')[1]) for line in lines]
        hands = []
        hands2 = []
        for i in range(len(cards)):
            hands.append(Hand(cards[i], bids[i]))
            hands2.append(Hand2(cards[i], bids[i]))

         
        print(hands2[-1] < hands2[-2])
     #   for hand in hands:
     #       print(hand)
        
        print('-------------------')
      #  for hand in sorted(hands):
      #      print(hand)
            
        sum = 0
        hands = sorted(hands)
        for i in range(len(hands)):
            sum += hands[i].bid * (i+1) 
            
        print(sum)
        
        #for hand in sorted(hands2):
           # print(hand)
        
        
        sum = 0
        hands2 = sorted(hands2)
        for i in range(len(hands2)):
            sum += hands2[i].bid * (i+1) 
            
        print(sum)
        

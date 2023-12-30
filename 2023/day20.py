import re
from enum import Enum

class State(Enum):
    LOW = "low"
    HIGH = "high"

def flip(state):
    if state == state.LOW:
        return State.HIGH
    return State.LOW

def parseInput(lines):
    broadcasters = re.findall(r'broadcaster -> (.+)',lines)
    flipflops = re.findall(r'%(\w+) -> (.+)',lines)
    conjunctions = re.findall(r'&(\w+) -> (.+)',lines)
    return (broadcasters,flipflops,conjunctions)



allParts = {}
def assignConjuctionsInputs():
    for label,part in allParts.items():
    #print(label, part)
        for output in part.outputs:
            if output in allParts:
                if isinstance(allParts[output],Conjunction):
                    allParts[output].inputs[label] = State.LOW

def initAllParts(flipflops, conjunctions):
    for flipflop in flipflops:
        allParts[flipflop[0]] = FlipFlop([], flipflop[1].split(','),flipflop[0])

    for conjunction in conjunctions:
        allParts[conjunction[0]] = Conjunction([], conjunction[1].split(','),conjunction[0])
        
    assignConjuctionsInputs()


counts = {State.LOW: 0, State.HIGH: 0}

def count(state):
    counts[state] += 1


class Part:
    def __init__(self,inputs, outputs, label):
        self.inputs = [input.strip() for input in inputs]
        self.outputs = [output.strip() for output in outputs]
        self.label = label

class FlipFlop(Part):
    def __init__(self,inputs, outputs, label):
        super().__init__(inputs, outputs, label)
        self.state = State.LOW
        
    def updateState(self, pulse, input = None):
        if pulse == State.LOW:
            self.state = flip(self.state)

    def receive(self,pulse, input = None):
        if pulse == State.LOW:
            for output in self.outputs:
                allParts[output].updateState(pulse, self.label)
          
            for output in self.outputs:
                if output in allParts:
                    count(self.state)
                    print(self.label,' -', self.state,' ', output)
                    allParts[output].receive(self.state, self.label)

class Conjunction(Part):
    def __init__(self,inputs, outputs, label):
        super().__init__(inputs, outputs, label)
        self.inputs = {}
        self.state = State.LOW
        
    def updateState(self, pulse, input = None):
        self.inputs[input] = pulse
        self.state = State.LOW
        for key,value in allParts.items():
            if value == State.LOW:
                self.state = State.HIGH
                break


    def receive(self,pulse,input = None):
        for output in self.outputs:
            allParts[output].updateState(pulse, self.label)
        for output in self.outputs:
            if output in allParts:
                count(self.state)
                print(self.label,' -', self.state,' ', output)
                allParts[output].receive(self.state, self.label)

class Broadcast(Part):
    def __init__(self,inputs, outputs, label):
        super().__init__(inputs, outputs, label)

    def receive(self,pulse, input = None):
        for output in self.outputs:
             allParts[output].updateState(pulse, self.label)
        for output in self.outputs:
            count(pulse)
            print(self.label,' -', pulse,' ', output)
            allParts[output].receive(pulse, self.label)





with open('/home/matvs/Projects/advent-of-code/2023/day20.input.txt') as f:
    lines = f.read()
    broadcasters, flipflops, conjunctions = parseInput(lines)
    broadcaster = Broadcast([], broadcasters[0].split(','), 'broadcaster')
    
    initAllParts(flipflops, conjunctions)
 
    broadcaster.receive(State.LOW)
    count(State.LOW)

    print(counts)
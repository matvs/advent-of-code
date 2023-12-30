import re
from enum import Enum
from queue import Queue

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
def assignOutputParts():
    pass
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
        
    allParts['output'] = Part([],[], 'ouput')
    allParts['rx'] = Part([],[], 'rx')
        
    assignConjuctionsInputs()


counts = {State.LOW: 0, State.HIGH: 0}

def count(state):
    counts[state] += 1


class Part:
    def __init__(self,inputs, outputs, label):
        self.inputs = [input.strip() for input in inputs]
        self.outputs = [output.strip() for output in outputs]
        self.label = label
        self.state = None
        
    def propagate(self,pulse, input = None):
        transitions = []
        for output in self.outputs:
            def receive(output):
                return lambda: allParts[output].receive(pulse, self.label)
            #print(f'{self.label} -{pulse}-> {output}')
            count(pulse)
            transitions.append(receive(output))
        return transitions
    
    def receive(self, pulse, input):
        return self.propagate(self.state, input)

class FlipFlop(Part):
    def __init__(self,inputs, outputs, label):
        super().__init__(inputs, outputs, label)
        self.state = State.LOW
        
    def updateState(self, pulse, input = None):
        if pulse == State.LOW:
            self.state = flip(self.state)

    def receive(self,pulse, input = None):
        print(f'{input} -{pulse}-> {self.label}')
        if pulse == State.LOW:
            self.updateState(pulse)
            
            return self.propagate(self.state, input)
        return []
          
           
                    
    def __repr__(self) -> str:
        return f'FlipFlop {self.state}'

class Conjunction(Part):
    def __init__(self,inputs, outputs, label):
        super().__init__(inputs, outputs, label)
        self.inputs = {}
        self.state = State.LOW
        
    def updateState(self, pulse, input = None):
        self.inputs[input] = pulse
        self.state = State.LOW
        for key,value in self.inputs.items():
            if value == State.LOW:
                self.state = State.HIGH
                break


    def receive(self,pulse,input = None):
        print(f'{input} -{pulse}-> {self.label}')
        self.updateState(pulse, input)
        
        return self.propagate(self.state, input)
                
    def __repr__(self) -> str:
        return f'Conjunction {self.state}'

class Broadcast(Part):
    def __init__(self,inputs, outputs, label):
        super().__init__(inputs, outputs, label)



            
        





with open('/home/matvs/Projects/advent-of-code/2023/day20.input.txt') as f:
    lines = f.read()
    broadcasters, flipflops, conjunctions = parseInput(lines)
    broadcaster = Broadcast([], broadcasters[0].split(','), 'broadcaster')
    
    initAllParts(flipflops, conjunctions)
    
    for i in range(1000):
        transitions = Queue()
        transitions.put(lambda: broadcaster.propagate(State.LOW))
        count(State.LOW)
        
        while not transitions.empty():
            currentTransition = transitions.get()
            nextTransitions = currentTransition()
            for trans in nextTransitions:
                transitions.put(trans)

    print(counts[State.HIGH] * counts[State.LOW])
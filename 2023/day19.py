import re

class Machine:
    def __init__(self,x,m,a,s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s
        self.parts = {'x':int(x), 'm':int(m), 'a':int(a), 's':int(s)}
        
    def __repr__(self) -> str:
        return f'Machine: {self.x} {self.m} {self.a} {self.s}'

class Workflow:
    def __init__(self,label, rawRules):
        self.label = label
        self.rules = self.parseRules(rawRules)

    def parseRules(self,rawRules):
        rawRules = rawRules.split(',')
        rules = []
        for rule in rawRules:
            if ':' in rule:
                machinePart, comparision, value, destination  = re.findall(r'(\w+)(<|>)(\d+):(\w+)',rule)[0]
                #print(CompareRule(machinePart, comparision, value, destination))
                rules.append(CompareRule(machinePart, comparision, value, destination))
            else:
                if rule == 'A':
                    rules.append(AcceptRule())
                elif rule == 'R':
                    rules.append(RejectRule())
                else:
                    rules.append(Rule(rule))
        #print(rules)
        return rules
    
    def isAccepted(self, machine, workflows):
        for rule in self.rules:
            if isinstance(rule, AcceptRule):
                return True
            elif isinstance(rule, RejectRule):
                return False
            elif isinstance(rule, CompareRule):
                if not self.compare(rule, machine):
                    continue
                else:
                    return workflows[rule.destination].isAccepted(machine, workflows)
            else:
                return workflows[rule.destination].isAccepted(machine, workflows)
        return False
    
    def compare(self, rule, machine):
        if rule.comparision == '<':
            return machine.parts[rule.machinePart] < rule.value
        elif rule.comparision == '>':
            return machine.parts[rule.machinePart] > rule.value
        else:
            raise Exception('Unknown comparision')
class Rule:
    def __init__(self, destination):
        self.destination = destination
        
    def __repr__(self) -> str:
        return  f' {self.destination}'

class AcceptRule(Rule):
    def __init__(self):
        super().__init__('A')

class RejectRule(Rule):
    def __init__(self):
        super().__init__('R')

class CompareRule(Rule):
    def __init__(self, machinePart, comparision, value, destination ):
        super().__init__(destination)
        self.comparision = comparision
        self.machinePart = machinePart
        self.value = int(value)
        
    def __repr__(self) -> str:
        return  f' {self.machinePart} {self.comparision} {str(self.value)} -> {self.destination}'
    
    
def generate_all_routes(workflow_name, rule = None, path=[]):
    """
    Generate all possible routes in the workflow graph using DFS.
    """
    # Add current workflow to the path
    path.append((workflow_name, rule))

    # Base case: If the current workflow leads to Accept or Reject, return the path
    if workflow_name in ['A', 'R']:
        return [path]

    # Recursive case: Explore all destinations from the current workflow
    all_routes = []
    current_workflow = workflows[workflow_name]
    for rule in current_workflow.rules:
        if (rule.destination, rule) not in path:  # Avoid cycles
            new_paths = generate_all_routes(rule.destination, rule, path.copy())
            all_routes.extend(new_paths)

    return all_routes

if __name__ == '__main__':
    with open('/home/matvs/Projects/advent-of-code/2023/day19.input.txt') as f:
        lines = f.read()
        workflows, machines = lines.split('\n\n')

        workflows = [Workflow(wf[0],wf[1]) for wf in re.findall(r'(\w+)\{(.+)\}',workflows)]
        workflows = {wf.label:wf for wf in workflows}
        workflows['A'] = Workflow('A','A')
        workflows['R'] = Workflow('R','R')

        machines = re.findall(r'x=(\d+),m=(\d+),a=(\d+),s=(\d+)',machines)
        machines = [Machine(machine[0],machine[1],machine[2],machine[3]) for machine in machines]
        #print(workflows[0].label, workflows[0].rules)
        
        startWorkflow = workflows['in']
        acceptedMachines = []
        for machine in machines:
            if startWorkflow.isAccepted(machine, workflows):
                acceptedMachines.append(machine)
                
        #print((acceptedMachines))
        
        sum = 0
        
        for machine in acceptedMachines:
            for key, value in machine.parts.items():
                sum += value
                
        print(sum)
        all_paths = generate_all_routes('in')
        #print(all_paths)
        acceptedPaths = list(filter(lambda path: path[-1][0] == 'A', all_paths))
        #print(list(acceptedPaths))
        
        
        allCombinations = []
        for i,path in enumerate(acceptedPaths):
            minMax = {'s':[0,4001], 'x':[0,4001], 'm':[0,4001], 'a':[0,4001]}
            for node in path:
                rule = node[1]
                if isinstance(rule, CompareRule):
                    #print(rule.machinePart, rule.comparision, rule.value)
                    if rule.comparision == '<': 
                        if rule.value < minMax[rule.machinePart][1]:
                            minMax[rule.machinePart][1] = rule.value
                    elif rule.comparision == '>':
                        if rule.value > minMax[rule.machinePart][0]:
                            minMax[rule.machinePart][0] = rule.value
                    
            allCombinations.append(minMax)
            print(minMax) 
         
        allCombinationsSum = 0 
        
        overlapping = {}
        
        def isOverlapping(minmax1, minmax2):
            for key, value in minmax1.items():
                minUpper = min(value[0], minmax2[key][0])
                maxUpper = max(value[0], minmax2[key][0])
                minLower = min(value[1], minmax2[key][1])
                maxLower = max(value[1], minmax2[key][1])
                if not(minUpper <= maxLower and maxUpper <= minLower):
                    return False
            return True
        
        for i, minMax in enumerate(allCombinations):
            for y in range(i+1, len(allCombinations)):
                minMax2 = allCombinations[y]
                if (isOverlapping(minMax, minMax2)):
                    #print('Overlapping',minMax, minMax2)
                    minMaxOverlap = {'s':[max(minMax['s'][0], minMax2['s'][0]), min(minMax['s'][1], minMax2['s'][1])], 
                              'x':[max(minMax['x'][0], minMax2['x'][0]), min(minMax['x'][1], minMax2['x'][1])], 
                              'm':[max(minMax['m'][0], minMax2['m'][0]), min(minMax['m'][1], minMax2['m'][1])], 
                              'a':[max(minMax['a'][0], minMax2['a'][0]), min(minMax['a'][1], minMax2['a'][1])]}
                    #print(minMaxOverlap)
                    partialSum = 1
                    for key, value in minMaxOverlap.items():
                        partialSum = partialSum * (value[1] - value[0] - 1)
                    allCombinationsSum -= partialSum

                    #allCombinationsSum -= abs(partialSum1 - partialSum2)     
                    
        #print(allCombinations)   
                    
        for minMax in allCombinations:
            partialSum = 1
            calculation = ''
            for key, value in minMax.items():
                partialSum = partialSum * (value[1] - value[0] - 1)
                calculation += f'({value[1]} - {value[0]} - 1) * '
            print(partialSum)
            allCombinationsSum += partialSum
           
                        
                            
            
        print(allCombinationsSum)
   

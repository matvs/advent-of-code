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
        

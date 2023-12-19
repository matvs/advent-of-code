import re
import math

class Input:
    def __init__(self,parts,brokenPartsNumber) -> None:
        self.parts = parts
        self.brokenPartsNumber = brokenPartsNumber.split(',')
        self.brokenPartsNumber = [int(part) for part in self.brokenPartsNumber]
        #print(self.brokenPartsNumber)
        
    def __str__(self) -> str:
        return f'Input: {self.parts} {self.brokenPartsNumber}'
    
    def __repr__(self) -> str:
        return f'Input: {self.parts} {self.brokenPartsNumber}' 
    
    def isValid(self):
        i = 0
        length = 0
        for group in self.brokenPartsNumber:
            
        
if __name__ == '__main__':
    with open('/home/matvs/Projects/advent-of-code/2023/day12.input.txt') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        tokens = [line.split(' ') for line in lines]
        inputs = [Input(token[0], token[1]) for token in tokens]
        #print(inputs)
        
        
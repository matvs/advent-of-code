import re
import math

def findLabel(box, label):
    for i in range(len(box)):
        if box[i][0] == label:
            return (box[i],i)
    return None
            
        
if __name__ == '__main__':
    with open('/home/matvs/Projects/advent-of-code/2023/day15.input.txt') as f:
        line = f.read()
        tokens = line.split(',')
        
        #print(inputs)
        
        #print(tokens)        
        def hash(line):

            currentValue = 0

            for char in line:

                currentValue += ord(char)

                currentValue *= 17

                currentValue %= 256

            return currentValue

        

        print (hash('HASH'))

        sum = 0

        for line in tokens:

            sum += hash(line)

        

        print(sum)
        
        
        boxes = {}
        
        for label in tokens:
            if '=' in label:
                label = label.split('=')
                focalLength = int(label[1])
                label = label[0]
                #print(label)
            else:
                label = label.split('-')[0]
                focalLength = -1
                #print(label)
                
            boxId = hash(label)
            #print(boxId)
            if boxId in boxes:
                item = findLabel(boxes[boxId],label)
                if focalLength != -1:
                    if item == None:
                        boxes[boxId].append((label,focalLength))
                    else:
                        boxes[boxId].remove(item[0])
                        boxes[boxId].insert(item[1], (label,focalLength))
                elif item != None:
                    boxes[boxId].remove(item[0])
            else:
                if focalLength != -1:
                    boxes[boxId] = [(label,focalLength)]
                    
    sum = 0
    for key, box in boxes.items():
        boxId = int(key) + 1
        for i, item in enumerate(box):
            sum += (i + 1) * item[1] * boxId
            
    print(sum)
                    

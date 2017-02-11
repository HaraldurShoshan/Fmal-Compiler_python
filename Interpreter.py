import sys
import re
from pprint import pprint

class Interpreter():
    def __init__(self):
        file = open(sys.argv[1], 'r')
        #file = sys.stdin
        self.code = file.read().split()
        self.stackList = self.code
        self.pos = 0
        self.dict = {}
        self.stack = []
        self.initialize()
        
        #pprint(self.stackList)

    def initialize(self):
        for index, item in enumerate(self.stackList):
            if(item == 'PUSH'):
                elem = self.stackList[index+1]
                self.stack.append(elem)
            elif(item == 'ASSIGN'):
                firstValue = self.stack.pop()
                secondValue = self.stack.pop()
                self.dict[secondValue] = firstValue
            elif(item == 'ADD'):
                firstValue = self.stack.pop()
                secondValue = self.stack.pop()
                newS = 0
                newF = 0

                if(self.isDigit(firstValue) == False):
                    for key, value in self.dict.items():
                        if key == firstValue:
                            newF = value
                else:
                    newF = firstValue
                
                if(self.isDigit(secondValue) == False):
                    for key, value in self.dict.items():
                        if key == secondValue:
                            newF = value
                else:
                    newS = secondValue
                
                newValue = int(newS) + int(newF)
                self.stack.append(newValue)
                
            elif(item == 'SUB'):
                firstValue = self.stack.pop()
                secondValue = self.stack.pop()
                newS = 0
                newF = 0

                if(self.isDigit(firstValue) == False):
                    for key, value in self.dict.items():
                        if key == firstValue:
                            newF = int(value)
                else:
                    newF = int(firstValue)
                
                if(self.isDigit(secondValue) == False):
                    for key, value in self.dict.items():
                        if key == secondValue:
                            newF = int(value)
                else:
                    newS = int(secondValue)
                
                newValue = newS - newF
                self.stack.append(newValue)
            elif(item == 'MULT'):
                firstValue = self.stack.pop()
                secondValue = self.stack.pop()
                newS = 0
                newF = 0

                if(self.isDigit(firstValue) == False):
                    for key, value in self.dict.items():
                        if key == firstValue:
                            newF = int(value)
                else:
                    newF = int(firstValue)
                
                if(self.isDigit(secondValue) == False):
                    for key, value in self.dict.items():
                        if key == secondValue:
                            newF = int(value)
                else:
                    newS = int(secondValue)
                
                newValue = newS * newF
                self.stack.append(newValue)
            elif(item == 'PRINT'):
                print(self.stack(-1))
                
            
            
            
        
        
        
    def isDigit(self,elem):
        # if(re.search("[0-9]+", elem)):
        #     return True
        # else:
        #     return False
        return elem.isdigit()

    def add(self):
        pass
    def sub(self):
        pass    
    def mult(self):
        pass

Interpreter()   

        
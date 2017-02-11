import sys
import re
from pprint import pprint

class Interpreter():
    def __init__(self):
        # file = open(sys.argv[1], 'r')
        file = sys.stdin
        self.code = file.read().split()
        self.stackList = self.code
        self.pos = 0
        self.dict = {}
        self.stack = []
        self.initialize()
        
    def initialize(self):
        for index, item in enumerate(self.stackList):
            if(item == 'PUSH'):
                
                elem = self.stackList[index+1]
                self.stack.append(elem)
                #print('Push...' + elem)
            elif(item == 'ASSIGN'):
                firstValue = self.stack.pop()
                secondValue = self.stack.pop()
                #print('assign: ' + secondValue +"="+firstValue)
                self.dict[secondValue] = firstValue
            elif(item == 'ADD'):
                #pprint(self.stack)
                firstValue = self.stack.pop()
                secondValue = self.stack.pop()
                newS = ""
                newF = ""

                if '-' in firstValue:
                    firstValue = firstValue.replace('-',"")
                if '-' in secondValue:
                    secondValue = secondValue.replace('-',"")

                if(self.isDigit(firstValue) == False):
                    for key, value in self.dict.items():
                        if key == firstValue:
                            newF = value
                else:
                    newF = firstValue
                
                if(self.isDigit(secondValue) == False):
                    for key, value in self.dict.items():
                        if key == secondValue:
                            newS = value
                else:
                    newS = secondValue
                
                newValue = newF + "+" + newS
                #print(newValue)
                self.stack.append(str(eval(newValue)))
                
            elif(item == 'SUB'):
                #pprint(self.stack)
                firstValue = self.stack.pop()
                secondValue = self.stack.pop()
                newS = ""
                newF = ""

                if '-' in firstValue:
                    firstValue = firstValue.replace('-',"")
                if '-' in secondValue:
                    secondValue = secondValue.replace('-',"")

                if(self.isDigit(firstValue) == False):
                    for key, value in self.dict.items():
                        if key == firstValue:
                            newF = value
                else:
                    newF = firstValue
                
                if(self.isDigit(secondValue) == False):
                    for key, value in self.dict.items():
                        if key == secondValue:
                            newS = value
                else:
                    newS = secondValue
                
                newValue = newF + "-" + newS
                #print(newValue)
                self.stack.append(str(eval(newValue)))
            elif(item == 'MULT'):
                #pprint(self.stack)
                firstValue = self.stack.pop()
                secondValue = self.stack.pop()
                newS = ""
                newF = ""

                if '-' in firstValue:
                    firstValue = firstValue.replace('-',"")
                if '-' in secondValue:
                    secondValue = secondValue.replace('-',"")

                if(self.isDigit(firstValue) == False):
                    for key, value in self.dict.items():
                        if key == firstValue:
                            newF = value
                else:
                    
                    newF = firstValue
                
                if(self.isDigit(secondValue) == False):
                    for key, value in self.dict.items():
                        if key == secondValue:
                            newS = value
                else:
                    newS = secondValue

                newValue = newF + "*" + newS
                # print(newValue)
                self.stack.append(str(eval(newValue)))
                #pprint(self.stack)
            elif(item == 'PRINT'):
                # pprint(self.stack)
                elem = self.stack[-1]
                for key, value in self.dict.items():
                    if key == elem:
                        print(value)
            
                
            
            
            
        
        
        
    def isDigit(self,elem):
        return elem.isdigit()

Interpreter()   

        
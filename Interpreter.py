import sys
from pprint import pprint

class Interpreter():
    def __init__(self):
        file = open(sys.argv[1], 'r')
        # file = sys.stdin
        self.code = file.read().split()
        self.stackList = self.code
        self.dict = {}
        self.stack = []
        self.initialize()
    
    def error(self):
        raise exception("Error")
        
    def initialize(self):
        for index, item in enumerate(self.stackList):
            if(item == 'PUSH'):
                elem = self.stackList[index+1]
                self.stackList.pop(index+1)
                self.stack.append(elem)
            elif(item == 'ASSIGN'):
                first = self.stack.pop()
                second = self.stack.pop()

                self.dict[second] = first
            elif(item == 'ADD'):
                first = self.stack.pop()
                second = self.stack.pop()

                first = self.getValue(first)
                second = self.getValue(second)

                self.stack.append(str(second+first))
            elif(item == 'SUB'):
                first = self.stack.pop()
                second = self.stack.pop()

                first = self.getValue(first)
                second = self.getValue(second)

                self.stack.append(str(second-first))
            elif(item == 'MULT'):
                first = self.stack.pop()
                second = self.stack.pop()

                first = self.getValue(first)
                second = self.getValue(second)

                self.stack.append(str(second*first))
            elif(item == 'PRINT'):
                elem = self.stack[-1]
                for key, value in self.dict.items():
                    if key == elem:
                        print(value)
            else:
                print('Error for operator: ' + item)
                self.error()
            
    def findValue(self,s):
        for key, value in self.dict.items():
            if key == s:
                return value

    def getValue(self, s):
        if(self.isDigit(s)):
            s = int(s)
        else:
            s = int(self.findValue(s))
        
        return s
        
    def isDigit(self,s):
        if s[0] in ('-', '+'):
            return s[1:].isdigit()
        return s.isdigit()

Interpreter()   

        
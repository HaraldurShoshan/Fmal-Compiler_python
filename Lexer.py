from Token import *

import sys
import re

class Lexer(object):
    def __init__(self):
        file = open(sys.argv[1], 'r')
        #file = sys.stdin
        self.code = file.read()
        self.codeList = []
        self.pos = -1;
        self.splitCode()

    def nextToken(self):
        self.pos = self.pos + 1

        if self.codeList[self.pos] == '(':
            return Token(self.codeList[self.pos], TokenCode.LPAREN)
        elif self.codeList[self.pos] == ')':
            return Token(self.codeList[self.pos], TokenCode.RPAREN)
        elif self.codeList[self.pos] == '*':
            return Token(self.codeList[self.pos], TokenCode.MULT)
        elif self.codeList[self.pos] == '-':
            return Token(self.codeList[self.pos], TokenCode.SUB)
        elif self.codeList[self.pos] == '+':
            return Token(self.codeList[self.pos], TokenCode.ADD)
        elif self.codeList[self.pos] == 'print':
            return Token(self.codeList[self.pos], TokenCode.PRINT)
        elif self.codeList[self.pos] == 'end':
            return Token(self.codeList[self.pos], TokenCode.END)
        elif self.codeList[self.pos] == 'error':
            return Token(self.codeList[self.pos], TokdenCode.ERROR)
        elif self.codeList[self.pos] == ';':
            return Token(self.codeList[self.pos], TokenCode.SEMICOL)
        elif self.codeList[self.pos] == '=':
            return Token(self.codeList[self.pos], TokenCode.ASSIGN)
        elif(re.search("[A-Za-z]+", self.codeList[self.pos])):
            return Token(self.codeList[self.pos], TokenCode.ID)
        elif(re.search("[0-9]+", self.codeList[self.pos])):
            return Token(self.codeList[self.pos], TokenCode.INT)
        
    def printToken(self, token):
        print(token)
    
    def splitCode(self):
        self.code = self.code.replace('\n', ' ').replace(';', ' ; ').replace('(', ' ( ').replace(')', ' ) ').replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('=', ' = ').replace('end', ' end')
        self.code = ' '.join(self.code.split())
        self.codeList = self.code.split()
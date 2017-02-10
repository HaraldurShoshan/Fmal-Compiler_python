from Token import Token
import sys

class Lexer(object):
    def __init__(self):
        self.TokenCode = Token.tCode
        self.code = ""
        file = open(sys.argv[1], 'r')
        self.code = file.read()
        self.codeList = []

    def nextToken(self):
        s = input()
        return s

    def printToken(self, token):
        print(token)
    
    def splitCode(self):
        self.code = self.code.replace('\n', ' ').replace(';', ' ; ').replace('(', ' ( ').replace(')', ' ) ').replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('=', ' = ').replace('end', ' end')
        self.code = ' '.join(self.code.split())
        self.codeList = self.code.split()
        print(self.codeList)

        
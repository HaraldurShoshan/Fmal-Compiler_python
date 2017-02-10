from Token import Token
import sys

class Lexer(object):
    def __init__(self):
        self.TokenCode = Token.tCode
        file = open(sys.argv[1], 'r')
        self.code = file.read()
        self.codeList = []
        self.splitCode()
        self.pos = -1;

    def nextToken(self):
        
        if(re.search("[A-Za-z]+", self.codeList[pos])):
            return Token(self.codeList[pos], ID)
        elif(re.search)

        if(self.codeList[pos] == '='):
            token = Token(self.codeList[pos], 'ASSIGN')
            return token 
        token = Token(self.codeList[pos], )
        self.pos = self.pos + 1
        return self.codeList[self.pos]

    def printToken(self, token):
        print(token)
    
    def splitCode(self):
        self.code = self.code.replace('\n', ' ').replace(';', ' ; ').replace('(', ' ( ').replace(')', ' ) ').replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('=', ' = ').replace('end', ' end')
        self.code = ' '.join(self.code.split())
        self.codeList = self.code.split()

    def intCheck(self, tokens):
        if(re.search("[0-9]+", tokens)):
            return True
        else:
            return False

    def idCheck(self, tokens):
        if(re.search("[A-Za-z]+", tokens)):
            return True
        else:
            return False
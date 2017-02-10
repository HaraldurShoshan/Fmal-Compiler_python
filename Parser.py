from Lexer import Lexer
import re

class Parser(object):
    def __init__(self, myLexer):
        self.Lexer = myLexer
        self.nextT = self.Lexer.nextToken()
        
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

    def statements(self):
        #nextT = self.Lexer.nextToken()
        
        statement()

        if(nextT == self.Lexer.TokenCode.SEMICOL):
            expr()

        statement()

    def statement():
        
    def expr():

    def term():

    def factor:    
        

    
    
            
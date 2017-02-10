from Lexer import Lexer
import re

class Parser(object):
    def __init__(self, myLexer):
        self.Lexer = myLexer
        self.nextT = ""
        
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

    def parse(self):    
        self.statements()
    
    def statements(self):
        self.statement()
        if(self.nextT == self.Lexer.TokenCode.ADD or self.nextT == self.Lexer.TokenCode.SUB):
            self.nextT = self.Lexer.nextToken()
            self.statement()
        else:
            self.error()

    def statement(self):
        self.nextT = self.Lexer.nextToken()
        return self.nextT
    
    def error(self):
        print('Syntax error')
        
        
        
        '''self.nextT = self.Lexer.nextToken
        if(self.nextT == self.Lexer.TokenCode.):
            statements()'''

'''    def expr(self):

    def term(self):
        
    def factor(self): '''   
        
 
    
    
            
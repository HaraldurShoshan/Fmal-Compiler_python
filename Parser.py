from Lexer import Lexer
import re

class Parser(object):
    def __init__(self, myLexer):
        self.Lexer = myLexer
        self.nextT = ""
        
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
        if self.idCheck(self.nextT):
            self.Lexer.printToken(self.nextT)
            self.nextT = self.Lexer.nextToken()
            if(self.nextT == self.Lexer.TokenCode.ASSIGN):
                self.Lexer.printToken(self.nextT)
                self.expr()
        elif self.nextT == 'print':
            print('print')
        else:
            self.error()
    
    def expr(self):
        print('expr')
  
  
  # def term(self):
        
  # def factor(self):

   def error(self):
        print('Syntax error')
        
 
    
    
            
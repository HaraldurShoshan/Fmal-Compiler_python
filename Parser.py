from Lexer import Lexer
import re
from Token import *

class Parser(object):
    def __init__(self, myLexer):
        self.Lexer = myLexer
        self.nextT = ""
        self.opList = []

    def parse(self):    
        self.nextT = self.lex()
        self.statements()
        
    def statements(self):
        if(self.nextT.tCode == TokenCode.END):
            pass
        self.statement()
        if(self.nextT.tCode == TokenCode.SEMICOL):
             self.nextT = self.lex()
             self.statements()             

    def statement(self):
        if(self.nextT.tCode == TokenCode.ID ):
            print("PUSH " + self.nextT.lexeme)
            self.nextT = self.lex()
            if(self.nextT.tCode == TokenCode.ASSIGN):
                self.nextT = self.lex()                                
                self.expr()  
                print("ASSIGN")                                
        elif(self.nextT.tCode == TokenCode.PRINT):
            self.nextT = self.lex()
            print("PUSH " + self.nextT.lexeme)
            print("PRINT")
            self.nextT = self.lex()
            
    def expr(self):
        self.term()
        if(self.nextT.tCode == TokenCode.ADD):
            self.nextT = self.lex()
            if(self.nextT.tCode == TokenCode.ID or self.nextT.tCode == TokenCode.INT or self.nextT.tCode == TokenCode.LPAREN):
                self.expr()
                print("ADD")
            else:
                print("Syntax Error")
        elif(self.nextT.tCode == TokenCode.SUB):
            self.nextT = self.lex()
            if(self.nextT.tCode == TokenCode.ID or self.nextT.tCode == TokenCode.INT or self.nextT.tCode == TokenCode.LPAREN):
                self.expr()
                print("SUB")
            else:
                print("Syntax Error")
    
    def term(self):
        self.factor()
        self.nextT = self.lex()
        if(self.nextT.tCode == TokenCode.MULT):
            self.nextT = self.lex()
            if(self.nextT.tCode == TokenCode.ID or self.nextT.tCode == TokenCode.INT or self.nextT.tCode == TokenCode.LPAREN):
                self.term()
                print("MULT")
            else:
                print("Syntax error")

    def factor(self):
        if(self.nextT.tCode == TokenCode.INT):
            print("PUSH " + self.nextT.lexeme)
        elif(self.nextT.tCode == TokenCode.ID):
            print("PUSH " + self.nextT.lexeme)
        elif(self.nextT.tCode == TokenCode.LPAREN):
            self.nextT = self.lex()
            self.expr()
            if(self.nextT.tCode != TokenCode.RPAREN):
                print("Syntax error")
        else:
            print("Syntax error")
               
    def lex(self):
        return self.Lexer.nextToken()
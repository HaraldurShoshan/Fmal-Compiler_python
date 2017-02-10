import re
from enum import Enum

class TokenCode(Enum):
    ASSIGN = 1
    SEMICOL = 2
    ADD = 3
    SUB = 4
    MULT = 5
    LPAREN = 6
    RPAREN = 7
    END = 8
    ERROR = 9
    PRINT = 10
    ID = 11
    INT = 12
    
class Token(object):
    def __init__(self, lex, tCode):
        self.lexeme = lex
        self.tCode = tCode
import re

class TokenCode(object):
    ASSIGN
    SEMICOL
    ADD
    SUB
    MULT
    LPAREN
    RPAREN
    END
    ERROR

class Token(object):
    def __init__(self, lex, tCode):
        self.lexeme = lex
        self.TokenCode = tCode


'''class TokenCode(object):
    ASSIGN = '='
    SEMICOL = ';'
    ADD = '+'
    SUB = '-'
    MULT = '*'
    LPAREN = '('
    RPAREN = ')'
    END
    ERROR'''
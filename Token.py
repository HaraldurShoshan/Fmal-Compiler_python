import re

class TokenCode(object):
    ASSIGN = '='
    SEMICOL = ';'
    ADD = '+'
    SUB = '-'
    MULT = '*'
    LPAREN = '('
    RPAREN = ')'
    END = 'end'
    #INT = '2'
    #INT = [0-9]+
    #ID = [A-Za-z]+

class Token(object):
    lexeme = ""
    tCode = TokenCode

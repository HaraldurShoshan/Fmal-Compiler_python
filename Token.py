import re
import enum

class TokenCode(object):
    ASSIGN = '='
    SEMICOL = ';'
    ADD = '+'
    SUB = '-'
    MULT = '*'
    LPAREN = '('
    RPAREN = ')'
    END = 'end'

class Token(object):
    lexeme = ""
    tCode = TokenCode

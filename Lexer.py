from Token import Token
import sys

class Lexer(object):
    def __init__(self):
        self.TokenCode = Token.tCode

    def nextToken(self):
        s = input()
        return s

    def tokenIs(self):
        return self.tokenIs
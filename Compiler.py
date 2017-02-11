from Parser import Parser
from Lexer import Lexer
import sys

class Compiler():
    def __init__(self):
        myLexer = Lexer()
        myParser = Parser(myLexer)
        myParser.parse()

Compiler()
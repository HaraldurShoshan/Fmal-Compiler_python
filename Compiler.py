from Parser import Parser
from Lexer import Lexer
import sys

def main():
    myLexer = Lexer()
    myParser = Parser(myLexer)
    myParser.parse()

print(main())
from Parser import Parser
from Lexer import Lexer
import sys

def main():
    #for line in sys.stdin:
    #    print(line)
    
    myLexer = Lexer()
    myParser = Parser(myLexer)

print(main())
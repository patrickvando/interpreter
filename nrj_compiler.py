import sys
import os
from Lexer.Buffer import Buffer
from Lexer.Lexer import Lexer
from Parser.Statement_parser import Statement_parser
from Compiler.Compiler_main import Compiler_main

def compile(filename):
    lex  = Lexer(filename)
    stat_parser = Statement_parser(lex)
    stat_list = stat_parser.parse_statement_list()
    head, tail = os.path.split(filename)
    compiler = Compiler_main(head + ".asm")
    compiler.compile_ast(stat_list)

arg_len = len(sys.argv)
if arg_len != 2:
    print("USAGE: python3 simpleinterpreter.py filename")
    print("For example: python3 simpleinterpreter.py gcd.simple")
    sys.exit()
filename = sys.argv[1]
compile(filename)

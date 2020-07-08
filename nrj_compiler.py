import sys
import os
from Lexer.Buffer import Buffer
from Lexer.Lexer import Lexer
from Parser.Statement_parser import Statement_parser
from Compiler.Compiler_main import Compiler_main

def main(filename):
    """Call the lexer, parser, and compiler."""
    lex  = Lexer(filename)
    stat_parser = Statement_parser(lex)
    stat_list = stat_parser.parse_to_end()
    head, tail = os.path.splitext(filename)
    compiler = Compiler_main(head + ".asm")
    compiler.compile_ast(stat_list)

if __name__ == '__main__':
    arg_len = len(sys.argv)
    if arg_len != 2:
        print("USAGE: python nrj_compiler.py filename.nrj")
        sys.exit()
    filename = sys.argv[1]
    main(filename)

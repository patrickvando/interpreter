import sys
import os
from Lexer.Buffer import Buffer
from Lexer.Lexer import Lexer
from Parser.Statement_parser import Statement_parser
from Compiler.Compiler_main import Compiler_main

def main(filename):
    """Turn a .nrj source file into a .asm assembly file.
    
    Works in three stages:
        1. The source file is turned into a stream of lexical tokens 
        via the Lexer.
        2. The stream of lexical tokens is parsed into an Abstract 
        Syntax Tree (AST) via the Parser.
        3. The Abstract Syntax Tree (AST) is traversed and turned
        into assembly instructions via the Compiler."""
    lex  = Lexer(filename) # Create the stream of lexical tokens
    stat_parser = Statement_parser(lex)
    stat_list = stat_parser.parse_to_end() # Turn the stream into an AST
    head, tail = os.path.splitext(filename) 
    compiler = Compiler_main(head + ".asm")
    compiler.compile_ast(stat_list) # Turn the AST into assembly code

if __name__ == '__main__':
    arg_len = len(sys.argv)
    if arg_len != 2:
        print("USAGE: python nrj_compiler.py filename.nrj")
        sys.exit()
    filename = sys.argv[1]
    main(filename)

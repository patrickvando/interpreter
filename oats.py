from Lexer.Lexer import Lexer
from Parser.StatementParser import StatementParser
from Interpreter.StatementInterpreter import StatementInterpreter
from Common.Common import *
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file", nargs=1, help="Filename of the .oats file to be interpreted")
parser.add_argument("-d", "--debug", action='store_true')
args = parser.parse_args()
lexer = Lexer(args.file[0])
parser = StatementParser(lexer)
root = parser.parse_main()
if args.debug: 
    print("-"*50)
    print("PARSE TREE")
    print("-"*50)
    root.print_recursive()
    print("-"*50)
    print("PROGRAM")
    print("-"*50)
sym_tab = [dict()]
interpreter = StatementInterpreter(sym_tab)
interpreter.interpret_statement_list(root)

import sys
from Lexer.Buffer import Buffer
from Lexer.Lexer import Lexer
from Parser.Statement_parser import Statement_parser
from Executor.Statement_executor import Statement_executor
from Executor.Symbol_table import *


def execute(filename):
    lex  = Lexer(filename)
    stat_parser = Statement_parser(lex)
    stat_list = stat_parser.parse_statement_list()
    st_stack = Symbol_table_stack()
    st_stack.push_table()
    stat_executor = Statement_executor(st_stack)
    stat_executor.execute_statement_list(stat_list)

arg_len = len(sys.argv)
if arg_len != 2:
    print("USAGE: python3 simpleinterpreter.py filename")
    print("For example: python3 simpleinterpreter.py gcd.toy")
    sys.exit()
filename = sys.argv[1]
execute(filename)

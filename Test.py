from Lexer.Buffer import Buffer
from Lexer.Lexer import Lexer
from Parser.Statement_parser import Statement_parser
from Executor.Statement_executor import Statement_executor
from Executor.Symbol_table import *

def test_buffer(filename):
    print("Testing Buffer")
    buf = Buffer(filename)

    c = buf.go_forward()
    while c != "":
        print("c: " + c)
        c = buf.go_forward()
    
    c = buf.go_backward()
    while c != "":
        print("c: " + c)
        c = buf.go_backward()
    print("Done testing Buffer")

def test_lexer(filename):
    print("Testing Lexer")
    lex = Lexer(filename)
    token = lex.next_token()
    while token.typ != "END":
        token = lex.next_token()
        lex.print_token(token)
    print("Done testing Lexer")

def test_parser(filename):
    print("Testing Parser")
    lex  = Lexer(filename)
    stat_parser = Statement_parser(lex)
    stat_list = stat_parser.parse_statement_list()
    print_parse_tree(stat_list, 0)
    print("Done testing Parser")

def print_parse_tree(root, indent):
    st = "\t"*indent + " " + root.typ
    if root.attributes:
        st += " Attributes: {}".format(root.attributes)
    print(st)
    for child in root.children:
        print_parse_tree(child, indent + 1)

def test_executor(filename):
    print("Testing Executor")
    lex  = Lexer(filename)
    stat_parser = Statement_parser(lex)
    stat_list = stat_parser.parse_statement_list()
    print_parse_tree(stat_list, 0)
    st_stack = Symbol_table_stack()
    st_stack.push_table()
    stat_executor = Statement_executor(st_stack)
    stat_executor.execute_statement_list(stat_list)
    print(st_stack)
    print("Done testing Executor")

def test_symbol_table():
    st_stack = Symbol_table_stack()
    st_stack.push_table()
    st_stack.insert("x", 1)
    st_stack.push_table()
    st_stack.insert("x", 2)
    print(st_stack)
    print(st_stack.get("x"))
    st_stack.pop_table()
    print(st_stack.get("x"))
    print(st_stack)

def test_if_parser():
    print("Testing if Parser")
    lex  = Lexer("if.toy")
    stat_parser = Statement_parser(lex)
    stat_list = stat_parser.parse_statement_list()
    print_parse_tree(stat_list, 0)
    print("Done testing if Parser")


test_executor("g.toy")
#test_parser("g.toy")

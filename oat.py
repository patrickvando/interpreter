from Lexer.Lexer import Lexer
from Parser.StatementParser import StatementParser
from Interpreter.StatementInterpreter import StatementInterpreter
from Common.Common import *
tn = Node(Node.NUMBER_TYPE, 99)
tn.children.append(Node(Node.NUMBER_TYPE, 56))
lexer = Lexer("test.oats")
parser = StatementParser(lexer)
root = parser.parse_main()
root.print_recursive()
sym_tab = []
interpreter = StatementInterpreter(sym_tab)
interpreter.interpret_statement_list(root)
print(sym_tab)

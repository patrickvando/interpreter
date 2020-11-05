from Lexer.Lexer import Lexer
from Parser.StatementParser import StatementParser
from Common.Common import *
tn = Node(Node.NUMBER_TYPE, 99)
tn.children.append(Node(Node.NUMBER_TYPE, 56))

lex = Lexer("test.oats")
prs = StatementParser(lex)
print(prs.parse_main())

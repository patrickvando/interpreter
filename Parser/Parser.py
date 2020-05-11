from .Statement_parser import Statement_parser
from .Node import Node
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer 
        self.root = Node()
        self.root.kind = "root"
        self.sp = Statement_parser(lexer)

    def parse(self):
        current_token = self.lexer.next_token()
        while current_token.kind != "END":
            self.root.add_child(self.sp.parse_statement())
            current_token = self.lexer.next_token()

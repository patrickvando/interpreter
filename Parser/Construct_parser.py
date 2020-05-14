from .Expression_parser import Expression_parser
class Construct_parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.exp_parser = Expression_parser(lexer)
        self.stat_parser = Parser.Statement_parser(lexer)

    def parse_construct(self):
        ct = self.lexer.current_token()
        if ct.lexeme == "if":
            return self.parse_if()
        elif ct.lexeme == "while":
            pass
        elif ct.lexeme == "for":
            pass

    def parse_if(self):
        #consume if
        ct = self.lexer.next_token()
        #consume (
        ct = self.lexer.next_token()
        if_node = Node()
        if_node.typ = "IF"
        if_node.add_child(self.exp_parser.parse_expression())
        #consume )
        ct = self.lexer.next_token()
        if_node.add_child(self.stat_parser.parse_statement_list())


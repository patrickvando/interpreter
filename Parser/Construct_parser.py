from .Node import Node
from .Utilities import Utilities
class Construct_parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.util = Utilities(lexer)

    def parse_construct(self):
        ct = self.lexer.current_token()
        if ct.lexeme == "if":
            return self.parse_if()
        elif ct.lexeme == "while":
            return self.parse_while()
        elif ct.lexeme == "for":
            return self.parse_for()
  
    def parse_for(self):
        self.util.match("for")
        self.util.match("(")
        for_node = Node()
        for_node.typ = "FOR"
        stat_parser = Statement_parser(self.lexer)
        exp_parser = Expression_parser(self.lexer)
        #parse the "assignment" section of the for loop statement
        for_node.add_child(stat_parser.parse_statement())
        self.util.match(";")
        #parse the "evaluation" section of the for loop statement
        for_node.add_child(exp_parser.parse_expression())
        self.util.match(";")
        #parse the "increment" section of the for loop statement
        for_node.add_child(stat_parser.parse_statement())
        self.util.match(")")
        #parse the body
        for_node.add_child(stat_parser.parse_body())
        return for_node

    def parse_while(self):
        self.util.match("while")
        self.util.match("(")
        while_node = Node()
        while_node.typ = "WHILE"
        exp_parser = Expression_parser(self.lexer)
        while_node.add_child(exp_parser.parse_expression())
        self.util.match(")")
        stat_parser = Statement_parser(self.lexer)
        while_node.add_child(stat_parser.parse_body())
        return while_node

    def parse_if(self):
        self.util.match("if") 
        self.util.match("(")
        if_node = Node()
        if_node.typ = "IF"
        exp_parser = Expression_parser(self.lexer)
        if_node.add_child(exp_parser.parse_expression())
        self.util.match(")")
        stat_parser = Statement_parser(self.lexer)
        if_node.add_child(stat_parser.parse_body())
        return if_node


from .Expression_parser import Expression_parser
from .Statement_parser import Statement_parser

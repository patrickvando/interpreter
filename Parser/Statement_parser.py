from .Data_types import Data_types
from .Node import Node
from .Expression_parser import Expression_parser
class Statement_parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_node = Node()
        self.ep = Expression_parser(lexer)

    def parse_statement(self):
        ct = self.lexer.current_token()
        val = ct.attributes["val"]
        if val in Data_types.types:
            self.current_node.attributes["type"] = val
            self.current_node.attributes["identifier"] = self.lexer.next_token()
            ct = self.lexer.next_token()
            val = ct.attributes["val"]
            if val == "(":
                self.current_node = self.parse_function_declaration()
            elif val == "=":
                self.current_node = self.parse_variable_declaration()
            #check for semicolon?
        else:
            self.current_node.attributes["identifier"] = val
            ct = self.lexer.next_token()
            val = ct.attributes["val"]
            if val == "(":
                self.current_node = self.parse_function_call()
            elif val == "=":
                self.current_node = self.parse_variable_assignment()
            #checn for semicolon?
        return self.current_node

    def parse_variable_declaration(self):
        self.current_node.kind = "VARIABLE"
        assign_node = Node()
        assign_node.kind = "ASSIGN"
        assign_node.add_child(self.current_node)
        self.lexer.next_token()
        assign_node.add_child(ep.parse_expression())
        return assign_node

    def parse_function_declaration(self):
        pass

    def parse_function_call(self):
        pass

    def parse_variable_assignment():
        pass



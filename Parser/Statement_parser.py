from .Data_types import Data_types
from .Node import Node
from .Expression_parser import Expression_parser
from .Construct_parser import Construct_parser

class Statement_parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.exp_parser = Expression_parser(lexer)
    
    def parse_statement_list(self):
        current_token = self.lexer.next_token()
        list_node = Node()
        list_node.typ = "STATEMENT_LIST"
        while current_token.typ != "END":
            list_node.add_child(self.parse_statement())
            current_token = self.lexer.current_token()
        return list_node        

    def parse_body(self):
        #consume {
        ct = self.lexer.next_token()
        list_node = Node()
        list_node.typ = "STATEMENT_LIST"
        while ct.typ != "}":
            list_node.add_child(self.parse_statement())
            ct = self.lexer.current_token()
        #consume }
        self.lexer.next_token()
        return list_node
    
    def parse_statement(self):
        ct = self.lexer.current_token()
        st_node = Node()
        res_node = None
        if ct.lexeme in Data_types.types:
            st_node.attributes["type"] = ct.lexeme
            ct = self.lexer.next_token()
            st_node.attributes["identifier"] = ct.lexeme
            ct = self.lexer.next_token()
            if ct.lexeme == "(":
                res_node = self.parse_function_declaration(st_node)
            elif ct.lexeme == "=":
                res_node = self.parse_variable_declaration(st_node)
        elif ct.lexeme in Data_types.constructs:
            pass
        else:
            st_node.attributes["identifier"] = ct.lexeme
            ct = self.lexer.next_token()
            if ct.lexeme == "(":
                res_node = self.parse_function_call(st_node)
            elif ct.lexeme == "=":
                res_node = self.parse_variable_assignment(st_node)
        #Consume semicolon
        self.lexer.next_token()
        return res_node

    def parse_variable_declaration(self, st_node):
        st_node.typ = "VARIABLE"
        assign_node = Node()
        assign_node.typ = "DECLARE"
        assign_node.add_child(st_node)
        self.lexer.next_token()
        assign_node.add_child(self.exp_parser.parse_expression())
        return assign_node

    def parse_function_declaration(self):
        pass

    def parse_function_call(self):
        pass

    def parse_variable_assignment():
        st_node.typ = "VARIABLE"
        assign_node = Node()
        assign_node.typ = "ASSIGN"
        assign_node.add_child(st_node)
        self.lexer.next_token()
        assign_node.add_child(self.exp_parser.parse_expression())
        return assign_node



from .Node import Node
from .Data_types import Data_types
from .Utilities import Utilities
from .Expression_parser import Expression_parser
class Statement_parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.util = Utilities(lexer)
    
    def parse_statement_list(self):
        current_token = self.lexer.next_token()
        listat_node = Node()
        listat_node.typ = "STATEMENT_LIST"
        while current_token.typ != "END":
            listat_node.add_child(self.parse_statement())
            current_token = self.lexer.current_token()
        return listat_node        

    def parse_body(self):
        self.util.match("{")
        ct = self.lexer.current_token()
        listat_node = Node()
        listat_node.typ = "STATEMENT_LIST"
        while ct.lexeme != "}":
            listat_node.add_child(self.parse_statement())
            ct = self.lexer.current_token()
        self.util.match("}")
        return listat_node
    
    def parse_statement(self):
        ct = self.lexer.current_token()
        stat_node = Node()
        res_node = None
        if ct.lexeme == "return":
            res_node = self.parse_return_statement()
            self.util.match(";")
        elif ct.lexeme in Data_types.types:
            ct = self.lexer.next_token()
            stat_node.attributes["identifier"] = ct.lexeme
            ct = self.lexer.next_token()
            if ct.lexeme == "(":
                stat_node.attributes["return_type"] = ct.lexeme
                res_node = self.parse_function_declaration(stat_node)
            elif ct.lexeme == "=":
                stat_node.attributes["type"] = ct.lexeme
                res_node = self.parse_variable_declaration(stat_node)
                self.util.match(";")
        elif ct.lexeme in Data_types.constructs:
            con_parser = Construct_parser(self.lexer)
            res_node = con_parser.parse_construct()
        else:
            stat_node.attributes["identifier"] = ct.lexeme
            ct = self.lexer.next_token()
            if ct.lexeme == "(":
                exp_parser = Expression_parser(self.lexer)
                res_node = exp_parser.parse_function_call(stat_node)
                self.util.match(";")
            elif ct.lexeme == "=":
                res_node = self.parse_variable_assignment(stat_node)
                self.util.match(";")
        return res_node
    
    def parse_return_statement(self):
        return_node = Node()
        return_node.typ = "RETURN"
        self.lexer.next_token()
        exp_parser = Expression_parser(self.lexer)
        return_node.add_child(exp_parser.parse_expression())
        return return_node 

    def parse_variable_declaration(self, stat_node):
        stat_node.typ = "VARIABLE"
        assign_node = Node()
        assign_node.typ = "VARIABLE_DECLARATION"
        assign_node.add_child(stat_node)
        self.lexer.next_token()
        exp_parser = Expression_parser(self.lexer)
        assign_node.add_child(exp_parser.parse_expression())
        return assign_node

    
    def parse_function_declaration(self, stat_node):
        stat_node.typ = "FUNCTION"
        self.util.match("(")
        ct = self.lexer.current_token()
        arg_node = Node()
        arg_node.typ = "ARGUMENTS"
        while ct.lexeme != ")":
            var_node = Node()
            var_node.typ = "VARIABLE"
            var_node.attributes["type"] = self.lexer.current_token().lexeme
            var_node.attributes["identifier"] = self.lexer.next_token().lexeme
            self.lexer.next_token()
            self.util.match_if_present(",")
            arg_node.add_child(var_node)
            ct = self.lexer.current_token()
        self.util.match(")")
        stat_node.add_child(arg_node)
        stat_node.add_child(self.parse_body())
        return stat_node

    def parse_variable_assignment(self, stat_node):
        stat_node.typ = "VARIABLE"
        assign_node = Node()
        assign_node.typ = "ASSIGN"
        assign_node.add_child(stat_node)
        self.util.match("=")
        exp_parser = Expression_parser(self.lexer)
        assign_node.add_child(exp_parser.parse_expression())
        return assign_node

from .Expression_parser import Expression_parser
from .Construct_parser import Construct_parser
   

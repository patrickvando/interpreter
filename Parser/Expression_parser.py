from .Data_types import Data_types
from .Node import Node
class Expression_parser:
    def __init__(self, lexer):
        self.lexer = lexer

    def parse_expression(self):
        left_node = self.parse_simple_expression()
        ct = self.lexer.current_token()
        if ct.lexeme in Data_types.relational_ops:
            rel_node = Node()
            rel_node.typ = ct.lexeme
            rel_node.add_child(current_node)
            rel_node.add_child(self.parse_simple_expression())
            return rel_node
        else:
            return left_node

    def parse_simple_expression(self):
        ct = self.lexer.current_token()
        if ct.lexeme == "+" or ct.lexeme == "-":
            sign_node = Node()
            sign_node.typ = ct.lexeme
            left = sign_node
            left.add_child(self.parse_term())
        else:
            left = self.parse_term()

        ct = self.lexer.current_token()
        if ct.lexeme in Data_types.simple_ops:
            op_node = Node()
            op_node.typ = ct.lexeme
            op_node.add_child(left)
            self.lexer.next_token()
            op_node.add_child(self.parse_simple_expression())
            return op_node
        else:
            return left 

    #HERE -> WRITE OUT PARSE TERM
    def parse_term(self):
        left = self.parse_factor() 
        ct = self.lexer.current_token()
        if ct.lexeme in Data_types.term_ops:
            op_node = Node()
            op_node.typ = ct.lexeme
            self.lexer.next_token()
            op_node.add_child(left)
            op_node.add_child(self.parse_term())
            return op_node
        else:
            return left

    def parse_factor(self):
        ct = self.lexer.current_token()
        self.lexer.next_token()
        if ct.typ == "double":
            res_node = Node()
            res_node.typ = "CONSTANT"
            res_node.attributes["type"] = ct.typ
            res_node.attributes["val"] = float(ct.lexeme)
            return res_node
        if ct.typ == "int":
            res_node = Node()
            res_node.typ = "CONSTANT" 
            res_node.attributes["type"] = ct.typ
            res_node.attributes["val"] = int(ct.lexeme)
            return res_node
        if ct.lexeme in Data_types.booleans:
            res_node = Node()
            res_node.typ = "CONSTANT"
            res_node.attributes["type"] = "bool"
            res_node.attributes["val"] = Data_types.booleans[ct.lexeme]
            return res_node
        if ct.lexeme == "(":
            res_node = self.parse_expression()
            #Consume closing )
            self.lexer.next_token()
            return res_node

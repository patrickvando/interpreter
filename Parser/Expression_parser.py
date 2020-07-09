from .Data_types import Data_types
from .Node import Node
from .Utilities import Utilities
class Expression_parser:
    """The Expression_parser class is part of a recursive descent parser that builds an Abstract Syntax Tree (AST) from a stream of lexical tokens supplied by the Lexer class.

    The Expression_parser class is responsible for parsing sequences of tokens
    that represent "expressions", which evaluate to some result.
    Examples of expressions include arithmetic expressions, like (1*2)+(3/4),
    and function calls that return a number."""

    def __init__(self, lexer):
        self.lexer = lexer
        self.util = Utilities(lexer)

    def parse_expression(self, left=None):
        """Return an expression node.

        Relational operators (<,>,=,...) are considered to have the lowest 
        precedence, so they are parsed here, after the parser has recursively
        processed all operators of higher precedence."""
        ct = self.lexer.current_token()
        if not left:
            left = self.parse_simple_expression()
        ct = self.lexer.current_token()
        if ct.lexeme in Data_types.relational_ops:
            rel_node = Node()
            rel_node.typ = ct.lexeme
            rel_node.add_child(left)
            self.lexer.next_token()
            rel_node.add_child(self.parse_simple_expression())
            return self.parse_expression(rel_node)
        else:
            return left

    def parse_simple_expression(self, left=None):
        """Return a "simple expression" node.

        Simple operators (+,-) are considered to have the next lowest 
        precedence, so they are parsed here, after the parser has recursively
        processed all operators of higher precedence."""
        Simple operators 
        ct = self.lexer.current_token()
        if not left:
            left = self.parse_term()
        ct = self.lexer.current_token()
        if ct.lexeme in Data_types.simple_ops:
            op_node = Node()
            op_node.typ = ct.lexeme
            op_node.add_child(left)
            self.lexer.next_token()
            op_node.add_child(self.parse_term())
            return self.parse_simple_expression(op_node)
        else:
            return left 

    def parse_term(self, left=None):
        """Return a "term" node.

        Term operators (*,/) are considered to have the next lowest 
        precedence, so they are parsed here, after the parser has recursively
        processed all operators of higher precedence."""
        if not left:
            left = self.parse_factor() 
        ct = self.lexer.current_token()
        if ct.lexeme in Data_types.term_ops:
            op_node = Node()
            op_node.typ = ct.lexeme
            op_node.add_child(left)
            self.lexer.next_token()
            op_node.add_child(self.parse_factor())
            return self.parse_term(op_node)
        else:
            return left

    def parse_factor(self):
        """Return a "factor" node.

        Variable identifiers, parenthesis, increment/decrement and
        negation/non-negation signs have the highest level of 
        precedence and are processed here. In the case of parenthesis,
        the recursion starts again from the expression stage."""
        ct = self.lexer.current_token()
        if ct.lexeme == "+" or ct.lexeme == "-":
            sign_node = Node()
            sign_node.typ = ct.lexeme
            self.lexer.next_token() #consume + or -
            sign_node.add_child(self.parse_factor())
            return sign_node
        if ct.typ == "double":
            res_node = Node()
            res_node.typ = "CONSTANT"
            res_node.attributes["type"] = ct.typ
            res_node.attributes["val"] = float(ct.lexeme)
            self.lexer.next_token()
            return res_node
        elif ct.typ == "int":
            res_node = Node()
            res_node.typ = "CONSTANT" 
            res_node.attributes["type"] = ct.typ
            res_node.attributes["val"] = int(ct.lexeme)
            self.lexer.next_token()
            return res_node
        elif ct.typ == "word":
            nt = self.lexer.next_token()
            if nt.lexeme == "(":
                self.lexer.prev_token()
                return self.parse_function_call()
            elif nt.lexeme == "++" or nt.lexeme == "--":
                self.lexer.prev_token()
                return self.parse_postincrement_postdecrement()
            elif ct.lexeme == "true":
                res_node = Node()
                res_node.typ = "CONSTANT"
                res_node.attributes["type"] = "bool"
                res_node.attributes["val"] = True
                return res_node
            elif ct.lexeme == "false":
                res_node = Node()
                res_node.typ = "CONSTANT"
                res_node.attributes["type"] = "bool"
                res_node.attributes["val"] = False
                return res_node
            else:
                res_node = Node()
                res_node.typ = "VARIABLE"
                res_node.attributes["identifier"] = ct.lexeme
                return res_node
        elif ct.lexeme == "++" or ct.lexeme == "--":
            return self.parse_preincrement_predecrement()
        elif ct.lexeme in Data_types.booleans:
            res_node = Node()
            res_node.typ = "CONSTANT"
            res_node.attributes["type"] = "bool"
            res_node.attributes["val"] = Data_types.booleans[ct.lexeme]
            self.lexer.next_token()
            return res_node
        elif ct.lexeme == "(":
            self.util.match("(")
            res_node = self.parse_expression()
            self.util.match(")")
            return res_node

    def parse_preincrement_predecrement(self):
        """Return a preincrement/predecrement node."""
        ct = self.lexer.current_token()
        op_node = Node()
        op_node.typ = ct.lexeme
        op_node.attributes["pre"] = True #consume ++ or --
        ct = self.lexer.next_token()
        res_node = Node()
        res_node.attributes["identifier"] = ct.lexeme
        res_node.typ = "VARIABLE"
        op_node.add_child(res_node)
        self.lexer.next_token()
        return op_node

    def parse_postincrement_postdecrement(self):
        """Return a postincrement/postdecrement node."""
        ct = self.lexer.current_token()
        var_node = Node()
        var_node.attributes["identifier"] = ct.lexeme
        var_node.typ = "VARIABLE"
        ct = self.lexer.next_token() #consume identifier
        op_node = Node()
        op_node.typ = ct.lexeme
        op_node.attributes["pre"] = False
        op_node.add_child(var_node)
        self.lexer.next_token()
        return op_node

    def parse_function_call(self):
        """Return a function call node."""
        ct = self.lexer.current_token()
        func_node = Node()
        func_node.attributes["identifier"] = ct.lexeme
        func_node.typ = "FUNCTION_CALL"
        ct = self.lexer.next_token() #consume identifier
        self.util.match("(")
        ct = self.lexer.current_token()
        arg_node = Node()
        arg_node.typ = "ARGUMENTS"
        while ct.lexeme != ")":
            arg_node.add_child(self.parse_expression())
            self.util.match_if_present(",")
            ct = self.lexer.current_token()
            """
            var_node = Node()
            var_node.typ = "VARIABLE"
            var_node.attributes["identifier"] = self.lexer.current_token().lexeme
            self.lexer.next_token()
            self.util.match_if_present(",")
            arg_node.add_child(var_node)
            ct = self.lexer.current_token()
            """
        self.util.match(")")
        func_node.add_child(arg_node)
        return func_node

from .Node import Node
from .Data_types import Data_types
from .Utilities import Utilities
from .Expression_parser import Expression_parser
class Statement_parser:
    """The Statement_parser class is part of a recursive descent parser that builds an Abstract Syntax Tree (AST) from a stream of lexical tokens supplied by the Lexer class.

    The Statement_parser class is responsible for parsing sequences of tokens that
    represent the beginnings of statements or lists of statements. Variable 
    assignments, function definitions, function calls, increment/decrement and 
    return statements are all considered to be statements."""

    def __init__(self, lexer):
        self.lexer = lexer
        self.util = Utilities(lexer)
  
    def parse_to_end(self):
        """Return a statement list node containing all top level statements."""
        current_token = self.lexer.next_token()
        listat_node = Node()
        listat_node.typ = "STATEMENT_LIST"
        while current_token.typ != "END":
            listat_node.add_child(self.parse_body_statement())
            current_token = self.lexer.current_token()
        return listat_node        

    def parse_body(self):
        """Return a statement list node containing all top level statements within a function definition or a while/if/for construct."""
        self.util.match("{")
        ct = self.lexer.current_token()
        listat_node = Node()
        listat_node.typ = "STATEMENT_LIST"
        while ct.lexeme != "}":
            listat_node.add_child(self.parse_body_statement())
            ct = self.lexer.current_token()
        self.util.match("}")
        return listat_node
 
    def parse_body_statement(self):
        """Return a node representing any statement that can occur at the top level of a construct or function definition, or at the top level of the source file."""
        ct = self.lexer.current_token()
        if ct.lexeme == "return":
            res_node = self.parse_return_statement()
            self.util.match(";")
            return res_node
        elif ct.lexeme in Data_types.constructs:
            con_parser = Construct_parser(self.lexer)
            res_node = con_parser.parse_construct()
            res_node.attributes["CONSTRUCT"] = True
            return res_node
        elif ct.lexeme in Data_types.types:
            ct = self.lexer.next_token() #match data type
            ct = self.lexer.next_token() #match identifier
            self.lexer.prev_token() #backtrack
            self.lexer.prev_token() #backtrack
            if ct.lexeme == "(":
                res_node = self.parse_function_declaration()
                return res_node
        res_node = self.parse_statement() #parse remaining statement options
        self.util.match(";")
        return res_node

    def parse_statement(self):
        """Return a node representing a statement that is not a function declaration, construct, or return statement."""
        ct = self.lexer.current_token()
        # parse variable declaration
        if ct.lexeme in Data_types.types:
            ct = self.lexer.next_token() # match data type
            ct = self.lexer.next_token() # match identifier
            self.lexer.prev_token() # backtrack
            self.lexer.prev_token() # backtrack
            if ct.lexeme == "=":
                res_node = self.parse_variable_declaration()
                return res_node
        # parse increment / decrement
        elif ct.lexeme == "++" or ct.lexeme == "--":
            exp_parser = Expression_parser(self.lexer)
            res_node = exp_parser.parse_preincrement_predecrement()
            return res_node
        else: 
            # parse function calls
            ct = self.lexer.next_token()
            self.lexer.prev_token()
            if ct.lexeme == "(":
                exp_parser = Expression_parser(self.lexer)
                res_node = exp_parser.parse_function_call()
                return res_node
            #parse variable assignment
            elif ct.lexeme == "=":
                res_node = self.parse_variable_assignment()
                return res_node
            #parse postincrement/postdecrement
            elif ct.lexeme == "++" or ct.lexeme == "--":
                exp_parser = Expression_parser(self.lexer)
                res_node = exp_parser.parse_postincrement_postdecrement()
                return res_node
        return None
    
    def parse_return_statement(self):
        """Return a statement node representing a return statement."""
        return_node = Node()
        return_node.typ = "RETURN"
        self.util.match("return")
        exp_parser = Expression_parser(self.lexer)
        return_node.add_child(exp_parser.parse_expression())
        return return_node 
    
    def parse_variable_declaration(self):
        """Return a statement node representing a variable declaration."""
        stat_node = Node()
        ct = self.lexer.current_token()
        stat_node.attributes["type"] = ct.lexeme
        #consume type
        ct = self.lexer.next_token()
        #consume identifier
        stat_node.attributes["identifier"] = ct.lexeme
        ct = self.lexer.next_token()
        stat_node.typ = "VARIABLE"
        assign_node = Node()
        assign_node.typ = "VARIABLE_DECLARATION"
        assign_node.add_child(stat_node)
        self.lexer.next_token()
        exp_parser = Expression_parser(self.lexer)
        assign_node.add_child(exp_parser.parse_expression())
        return assign_node

    
    def parse_function_declaration(self):
        """Return a statement node representing a function definition."""
        stat_node = Node()
        ct = self.lexer.current_token()
        stat_node.attributes["return_type"] = ct.lexeme
        ct = self.lexer.next_token() # consume type
        stat_node.attributes["identifier"] = ct.lexeme
        ct = self.lexer.next_token() # consume identifier
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

    def parse_variable_assignment(self):
        """Return a statement node representing a variable assignment."""
        ct = self.lexer.current_token()
        stat_node = Node()
        stat_node.attributes["identifier"] = ct.lexeme
        stat_node.typ = "VARIABLE"
        self.lexer.next_token() # consume identifier
        assign_node = Node()
        assign_node.typ = "ASSIGN"
        assign_node.add_child(stat_node)
        self.util.match("=")
        exp_parser = Expression_parser(self.lexer)
        assign_node.add_child(exp_parser.parse_expression())
        return assign_node

from .Expression_parser import Expression_parser
from .Construct_parser import Construct_parser
   

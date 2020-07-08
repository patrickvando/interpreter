from .Node import Node
from .Utilities import Utilities
class Construct_parser:
    """The Construct_parser class is part of a recursive descent parser that builds an Abstract Syntax Tree (AST) from a stream of lexical tokens supplied by the Lexer class.
    The Construct_parser class is responsible for parsing sequences of tokens that
    represent for loops, while loops, and if-elseif-else constructs."""

    def __init__(self, lexer):
        self.lexer = lexer
        self.util = Utilities(lexer)

    def parse_construct(self):
        """Return a construct node representing a while loop, for loop, or if-elseif-else construct."""
        ct = self.lexer.current_token()
        if ct.lexeme == "if":
            return self.parse_if()
        elif ct.lexeme == "while":
            return self.parse_while()
        elif ct.lexeme == "for":
            return self.parse_for()
  
    def parse_for(self):
        """Return a construct node representing a for loop."""	
        self.util.match("for")
        self.util.match("(")
        for_node = Node()
        for_node.typ = "FOR"
        stat_parser = Statement_parser(self.lexer)
        exp_parser = Expression_parser(self.lexer)
        #parse the "assignment" section of the for loop
        for_node.add_child(stat_parser.parse_statement())
        self.util.match(";")
        #parse the "condition" section of the for loop
        for_node.add_child(exp_parser.parse_expression())
        self.util.match(";")
        #parse the "increment/decrement" section of the for loop
        for_node.add_child(stat_parser.parse_statement())
        self.util.match(")")
        #parse the body
        for_node.add_child(stat_parser.parse_body())
        return for_node

    def parse_while(self):
        """Return a construct node representing a while loop."""
        self.util.match("while")
        self.util.match("(")
        while_node = Node()
        while_node.typ = "WHILE"
        #parse the "condition" section of the while loop
        exp_parser = Expression_parser(self.lexer)
        while_node.add_child(exp_parser.parse_expression())
        self.util.match(")")
        stat_parser = Statement_parser(self.lexer)
        while_node.add_child(stat_parser.parse_body())
        return while_node

    def parse_if(self):
        """Return a construct node representing an if-elseif-else construct."""	
        self.util.match("if") 
        self.util.match("(")
        if_node = Node()
        if_node.typ = "IF"
        exp_parser = Expression_parser(self.lexer)
        option_node = Node()
        option_node.typ = "OPTION"
        if_node.add_child(option_node)
        #parse the first condition of the if-elseif-else construct
        option_node.add_child(exp_parser.parse_expression())
        self.util.match(")")
        stat_parser = Statement_parser(self.lexer)
        option_node.add_child(stat_parser.parse_body())
        ct = self.lexer.current_token()
        while ct.lexeme == "elseif":
            #parse the remaining condition of the if-elseif-else construct
            if_node.add_child(self.parse_elseif())
            ct = self.lexer.current_token()
        if ct.lexeme == "else":
            #if necessary add a default branch to the if-elseif-else construct
            if_node.add_child(self.parse_else())
        return if_node

    def parse_elseif(self):
        """Return an option node corresponding to an elseif condition."""
        self.util.match("elseif") 
        self.util.match("(")
        exp_parser = Expression_parser(self.lexer)
        option_node = Node()
        option_node.typ = "OPTION"
        option_node.add_child(exp_parser.parse_expression())
        self.util.match(")")
        stat_parser = Statement_parser(self.lexer)
        option_node.add_child(stat_parser.parse_body())
        return option_node

    def parse_else(self):
        self.util.match("else") 
        exp_parser = Expression_parser(self.lexer)
        option_node = Node()
        option_node.typ = "OPTION"
        true_node = Node()
        true_node.typ = "CONSTANT"
        true_node.attributes["type"] = "bool"
        true_node.attributes["val"] = True
        option_node.add_child(true_node)
        stat_parser = Statement_parser(self.lexer)
        option_node.add_child(stat_parser.parse_body())
        return option_node


from .Expression_parser import Expression_parser
from .Statement_parser import Statement_parser

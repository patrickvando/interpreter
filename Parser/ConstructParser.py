from Common.Common import *
class ConstructParser:
    def __init__(self, lexer):
        self.lex = lexer

    def parse_construct(self):
        ct = self.lex.current_token()
        if ct.lexeme == Lexeme.FUNC:
            return self.parse_function_declaration()
        elif ct.lexeme == Lexeme.IF:
            return self.parse_if()
        elif ct.lexeme == Lexeme.WHILE:
            return self.parse_while()
        elif ct.lexeme == Lexeme.FOR:
            return self.parse_for()
        else:
            illegal_token(ct, "Not a valid construct.")

    def parse_function_declaration(self):
        ct = self.lex.next_token()
        check_valid_name(ct) 
        func_def_node = Node(Node.FUNC_DEF_TYPE, ct.lexeme)
        plist_node = Node(Node.PARAMETER_LIST_TYPE)
        func_def_node.children.append(plist_node)
        self.lex.next_token()
        self.lex.match(Lexeme.OPEN_PAREN)
        ct = self.lex.current_token()
        if ct.lexeme == Lexeme.CLOSE_PAREN:
            self.lex.next_token()
            func_def_node.children.append(self.parse_body())
            return func_def_node
        while True:
            if ct.type_ == Token.WORD_TYPE and ct.lexeme not in Lexeme.RESERVED: 
                plist_node.children.append(Node(Node.VARIABLE_TYPE, ct.lexeme))
            else:
                illegal_token(ct, "Expected variable.")
            ct = self.lex.next_token()
            if ct.lexeme == Lexeme.COMMA:
                self.lex.next_token()
            elif ct.lexeme == Lexeme.CLOSE_PAREN:
                self.lex.next_token()
                break
            else:
                illegal_token(ct)
            ct = self.lex.current_token()
        func_def_node.children.append(self.parse_body())
        return func_def_node
    
    def parse_if(self):
        self.lex.match(Lexeme.IF)
        self.lex.match(Lexeme.OPEN_PAREN)
        ct = self.lex.current_token()
        if_node = Node(Node.IF_TYPE)
        eparse = ExpressionParser(self.lex)
        if_node.children.append(eparse.parse_expression())
        self.lex.match(Lexeme.CLOSE_PAREN)
        if_node.children.append(self.parse_body())
        ct = self.lex.current_token()
        while ct.lexeme == Lexeme.ELSEIF:
            self.lex.next_token()
            self.lex.match(Lexeme.OPEN_PAREN)
            if_node.children.append(eparse.parse_expression())
            self.lex.match(Lexeme.CLOSE_PAREN)
            if_node.children.append(self.parse_body())
            ct = self.lex.current_token()
        if ct.lexeme == Lexeme.ELSE:
            self.lex.next_token()
            if_node.children.append(Node(Node.NUMBER_TYPE, 1))
            if_node.children.append(self.parse_body())
        return if_node
    
    def parse_while(self):
        self.lex.match(Lexeme.WHILE)
        self.lex.match(Lexeme.OPEN_PAREN)
        ct = self.lex.current_token()
        while_node = Node(Node.WHILE_TYPE)
        eparse = ExpressionParser(self.lex)
        while_node.children.append(eparse.parse_expression())
        self.lex.match(Lexeme.CLOSE_PAREN)
        while_node.children.append(self.parse_body())
        return while_node

    def parse_for(self):
        self.lex.match(Lexeme.FOR)
        self.lex.match(Lexeme.OPEN_PAREN)
        for_node = Node(Node.FOR_TYPE)
        sparser = StatementParser(self.lex)
        for_node.children.append(sparser.parse_assignment())
        self.lex.match(Lexeme.SEMICOLON)
        eparser = ExpressionParser(self.lex)
        for_node.children.append(eparser.parse_expression())
        self.lex.match(Lexeme.SEMICOLON)
        for_node.children.append(sparser.parse_assignment())
        self.lex.match(Lexeme.CLOSE_PAREN)
        for_node.children.append(self.parse_body())
        return for_node

    def parse_body(self):
        self.lex.match(Lexeme.OPEN_BRACE)
        ct = self.lex.current_token()
        slist_node = Node(Node.STATEMENT_LIST_TYPE)
        sparser = StatementParser(self.lex)
        while ct.type_ != Token.END_TYPE and ct.lexeme != Lexeme.CLOSE_BRACE:
            slist_node.children.append(sparser.parse_statement())
            ct = self.lex.current_token()
        self.lex.match(Lexeme.CLOSE_BRACE)
        return slist_node

from .ExpressionParser import ExpressionParser
from .StatementParser import StatementParser

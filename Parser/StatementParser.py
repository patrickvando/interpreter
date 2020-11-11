from Common.Common import * 
from collections import deque
class StatementParser:
    def __init__(self, lexer):
        self.lex = lexer

    def parse_main(self):
        slist_node = Node(Node.STATEMENT_LIST_TYPE)
        ct = self.lex.next_token()
        while(ct.type_ != Token.END_TYPE):
            slist_node.children.append(self.parse_statement())
            ct = self.lex.current_token()
        return slist_node 

    def parse_statement(self):
        ct = self.lex.current_token()
        if ct.lexeme in Lexeme.CONSTRUCTS:
            cparser = ConstructParser(self.lex)
            statement_node = cparser.parse_construct()
        elif ct.lexeme == Lexeme.RETURN:
            statement_node = self.parse_return()
            self.lex.match(Lexeme.SEMICOLON)
        elif ct.type_ == Token.WORD_TYPE:
            #Look ahead for function call or assignment
            nt = self.lex.next_token()
            self.lex.prev_token()
            if nt.lexeme == Lexeme.OPEN_PAREN:
                eparser = ExpressionParser(self.lex)
                statement_node = eparser.parse_function_call()
                self.lex.match(Lexeme.SEMICOLON)
            elif nt.lexeme == Lexeme.EQUALS or nt.lexeme == Lexeme.COMMA:
                statement_node = self.parse_assignment()
                self.lex.match(Lexeme.SEMICOLON)
            else:
                illegal_token(ct, 'Expected assignment or function call.')
        else:
            illegal_token(ct, 'Expected assignment, function call, function definition, or boolean construct.')
        return statement_node

    def parse_assignment(self):
        assignment_node = Node(Node.ASSIGNMENT_TYPE)
        ct = self.lex.current_token()
        check_valid_name(ct)
        queue = deque([Node(Node.VARIABLE_TYPE, ct.lexeme, ct)])
        ct = self.lex.next_token()
        nt = self.lex.next_token()
        while ct.lexeme == Lexeme.COMMA and nt.type_ == Token.WORD_TYPE:
            check_valid_name(nt)
            queue.append(Node(Node.VARIABLE_TYPE, nt.lexeme, ct))
            ct = self.lex.next_token()
            nt = self.lex.next_token()
        self.lex.prev_token()
        self.lex.match(Lexeme.EQUALS)
        eparser = ExpressionParser(self.lex)
        assignment_node.children.append(queue.popleft())
        assignment_node.children.append(eparser.parse_expression())
        ct = self.lex.current_token()
        while ct.lexeme == Lexeme.COMMA:
            if not queue:
                illegal_token(ct, "Too many operands on right side.")
            self.lex.match(Lexeme.COMMA)
            assignment_node.children.append(queue.popleft())
            assignment_node.children.append(eparser.parse_expression())
            ct = self.lex.current_token()
        if queue:
            illegal_token(ct, "Too many operands on left side.")
        return assignment_node

    def parse_return(self):
        self.lex.match(Lexeme.RETURN)
        return_node = Node(Node.RETURN_TYPE)
        eparser = ExpressionParser(self.lex)
        return_node.children.append(eparser.parse_expression())
        return return_node


from .ConstructParser import ConstructParser
from .ExpressionParser import ExpressionParser

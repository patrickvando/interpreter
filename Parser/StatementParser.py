from Common.Common import * 
from collections import deque
class StatementParser:
    def __init__(self, lexer):
        self.lex = lexer

    def parse_main(self):
        root = Node(Node.STATEMENT_LIST_TYPE)
        current_token = self.lex.next_token()
        while(current_token.type_ != Token.END_TYPE):
            root.children.append(self.parse_statement())
            current_token = self.lex.next_token()
        return root

    def parse_statement(self):
        ct = self.lex.current_token()
        if ct.lexeme in CONSTRUCT_LEXEMES:
            cparser = ConstructParser(self.lex)
            return cparser.parseConstruct()
        elif ct.type_ == Token.WORD_TYPE:
            #Look ahead for function call or assignment
            nt = self.lex.next_token()
            self.lex.prev_token()
            if nt.lexeme == "(":
                return self.parse_function_call()
            elif nt.lexeme == "=" or nt.lexeme == ",":
                return self.parse_assignment()
            else:
                illegal_token(ct, 'Expected assignment or function call.')
        else:
            illegal_token(ct, 'Expected assignment, function call, function definition, or boolean construct.')

    def parse_assignment(self):
        root = Node(Node.ASSIGNMENT_TYPE)
        ct = self.lex.current_token()
        check_valid_name(ct)
        queue = deque([Node(Node.VARIABLE_TYPE, ct.lexeme, ct)])
        ct = self.lex.next_token()
        nt = self.lex.next_token()
        while ct.lexeme == "," and nt.type_ == Token.WORD_TYPE:
            check_valid_name(nt)
            queue.append(Node(Node.VARIABLE_TYPE, nt.lexeme, ct))
            ct = self.lex.next_token()
            nt = self.lex.next_token()
        self.lex.prev_token()
        match_lexeme(self.lex, "=")
        eparser = ExpressionParser(self.lex)
        root.children.append(queue.popleft())
        root.children.append(eparser.parseExpression())
        ct = self.lex.current_token()
        while ct.lexeme == ",":
            if not queue:
                illegal_token(ct, "Too many operands on right side.")
            match_lexeme(self.lex, ",")
            root.children.append(queue.popleft())
            root.children.append(eparser.parseExpression())
            ct = self.lex.current_token()
        if queue:
            illegal_token(ct, "Too many operands on left side.")
        match_lexeme(self.lex, ";")
        return root

        


    def parse_function_call(self):
        pass

from .ConstructParser import ConstructParser
from .ExpressionParser import ExpressionParser

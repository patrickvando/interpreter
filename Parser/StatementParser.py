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
            current_token = self.lex.current_token()
        return root

    def parse_statement(self):
        ct = self.lex.current_token()
        if ct.lexeme in Lexeme.CONSTRUCTS:
            cparser = ConstructParser(self.lex)
            return cparser.parseConstruct()
        elif ct.type_ == Token.WORD_TYPE:
            #Look ahead for function call or assignment
            nt = self.lex.next_token()
            self.lex.prev_token()
            if nt.lexeme == Lexeme.OPEN_PAREN:
                return self.parse_function_call()
            elif nt.lexeme == Lexeme.EQUALS or nt.lexeme == Lexeme.COMMA:
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
        while ct.lexeme == Lexeme.COMMA and nt.type_ == Token.WORD_TYPE:
            check_valid_name(nt)
            queue.append(Node(Node.VARIABLE_TYPE, nt.lexeme, ct))
            ct = self.lex.next_token()
            nt = self.lex.next_token()
        self.lex.prev_token()
        self.lex.match(Lexeme.EQUALS)
        eparser = ExpressionParser(self.lex)
        root.children.append(queue.popleft())
        root.children.append(eparser.parse_expression())
        ct = self.lex.current_token()
        while ct.lexeme == Lexeme.COMMA:
            if not queue:
                illegal_token(ct, "Too many operands on right side.")
            self.lex.match(Lexeme.COMMA)
            #change name from root to more descriptive - statement node?
            root.children.append(queue.popleft())
            root.children.append(eparser.parse_expression())
            ct = self.lex.current_token()
        if queue:
            illegal_token(ct, "Too many operands on left side.")
        self.lex.match(Lexeme.SEMICOLON)
        return root

    #function calls belong in expressions, FIX IT
    # -------------------HERE 
    def parse_function_call(self):
        ct = current_token()
        #maybe dont check this here? check it beforehand? maybe the lexer should filter out all reserved words in the first place?
        check_valid_name(ct) 
        call_node = Node(Node.FUNC_CALL_TYPE, ct.lexeme) 
        self.lex.match(Lexeme.OPEN_PAREN)
        ct = self.lex.current_token()
        if ct.lexeme != Lexeme.CLOSE_PAREN:
            expression_par
            call_node.children.append(
        while ct.lexeme == Lexeme.
        pass

from .ConstructParser import ConstructParser
from .ExpressionParser import ExpressionParser

from Common.Common import *
class ConstructParser:
    def __init__(self, lexer):
        self.lex = lexer

    def parseConstruct(self):
        ct = self.lex.current_token()
        if ct.lexeme == Lexeme.FUNC:
            return self.parseFunctionDeclaration()

    def parseFunctionDeclaration(self):
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
            func_def_node.children.append(self.parseBody())
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
        func_def_node.children.append(self.parseBody())
        return func_def_node


        
    def parseBody(self):
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

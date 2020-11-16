from Common.Common import *
class ExpressionParser:
    def __init__(self, lexer):
        self.lex = lexer

    def parse_expression(self, left=None):
        if not left:
            left = self.parse_simple_expression()
        ct = self.lex.current_token()
        if ct.lexeme in Lexeme.EXPS:
            op_node = Node(Node.LEXEME_TO_TYPE[ct.lexeme], token=ct)
            op_node.children.append(left)
            self.lex.next_token()
            op_node.children.append(self.parse_simple_expression())
            return self.parse_expression(op_node)
        else:
            return left

    def parse_simple_expression(self, left=None):
        if not left:
            left = self.parse_term()
        ct = self.lex.current_token()
        if ct.lexeme in Lexeme.SIMPLE_EXPS:
            op_node = Node(Node.LEXEME_TO_TYPE[ct.lexeme], token=ct)
            op_node.children.append(left)
            self.lex.next_token()
            op_node.children.append(self.parse_term())
            return self.parse_simple_expression(op_node)
        else:
            return left

    def parse_term(self, left=None):
        if not left:
            left = self.parse_factor()
        ct = self.lex.current_token()
        if ct.lexeme in Lexeme.TERMS:
            op_node = Node(Node.LEXEME_TO_TYPE[ct.lexeme], token=ct)
            op_node.children.append(left)
            self.lex.next_token()
            op_node.children.append(self.parse_factor())
            return self.parse_term(op_node)
        else:
            return left

    def parse_factor(self):
        ct = self.lex.current_token()
        self.lex.next_token()
        if ct.type_ == Token.NUMBER_TYPE:
            return Node(Node.NUMBER_TYPE, ct.lexeme, ct)
        elif ct.lexeme == Lexeme.SUB:
            negation_node = Node(Node.SUB_TYPE, token=ct)
            negation_node.children.append(self.parse_factor())
            return negation_node
        elif ct.lexeme == Lexeme.NOT:
            not_node = Node(Node.NOT_TYPE, token=ct)
            not_node.children.append(self.parse_factor())
            return not_node
        elif ct.lexeme == Lexeme.OPEN_PAREN:
            exp_node = self.parse_expression()
            self.lex.match(Lexeme.CLOSE_PAREN)
            return exp_node
        elif ct.type_ == Token.WORD_TYPE:
            nt = self.lex.current_token()
            if nt.lexeme == Lexeme.OPEN_PAREN:
                self.lex.prev_token()
                return self.parse_function_call()
            else:
                return Node(Node.VARIABLE_TYPE, ct.lexeme, ct)
        else:
            illegal_token(ct)

    def parse_function_call(self):
        ct = self.lex.current_token()
        if ct.lexeme in Lexeme.BUILT_INS:
            call_node = Node(Node.LEXEME_TO_TYPE[ct.lexeme], token=ct)
        elif ct.lexeme not in Lexeme.RESERVED:
            call_node = Node(Node.FUNC_CALL_TYPE, ct.lexeme, ct)
        else:
            illegal_token(ct)
        self.lex.next_token()
        self.lex.match(Lexeme.OPEN_PAREN)
        ct = self.lex.current_token()
        if ct.lexeme == Lexeme.CLOSE_PAREN:
            self.lex.next_token()
            return call_node
        call_node.children.append(self.parse_expression())
        ct = self.lex.current_token()
        while ct.lexeme == Lexeme.COMMA:
            self.lex.next_token()
            call_node.children.append(self.parse_expression())
            ct = self.lex.current_token()
        self.lex.match(Lexeme.CLOSE_PAREN)
        return call_node

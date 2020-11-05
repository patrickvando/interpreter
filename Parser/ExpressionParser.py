from Common.Common import *
class ExpressionParser:
    def __init__(self, lexer):
        self.lex = lexer

    def parseExpression(self, left=None):
        if not left:
            left = self.parseSimpleExpression()
        ct = self.lex.current_token()
        if ct.lexeme in EXP_LEXEMES:
            op_node = Node(Node.LEXEME_TO_TYPE[ct.lexeme])
            op_node.children.append(left)
            self.lex.next_token()
            op_node.children.append(self.parseSimpleExpression())
            return self.parseExpression(op_node)
        else:
            return left

    def parseSimpleExpression(self, left=None):
        if not left:
            left = self.parseTerm()
        ct = self.lex.current_token()
        if ct.lexeme in SIMPLE_EXP_LEXEMES:
            op_node = Node(Node.LEXEME_TO_TYPE[ct.lexeme])
            op_node.children.append(left)
            self.lex.next_token()
            op_node.children.append(self.parseTerm())
            return self.parseSimpleExpression(op_node)
        else:
            return left

    def parseTerm(self, left=None):
        if not left:
            left = self.parseFactor()
        ct = self.lex.current_token()
        if ct.lexeme in TERM_LEXEMES:
            op_node = Node(Node.LEXEME_TO_TYPE[ct.lexeme])
            op_node.children.append(left)
            self.lex.next_token()
            op_node.children.append(self.parseFactor())
            return self.parseTerm(op_node)
        else:
            return left


    def parseFactor(self):
        ct = self.lex.current_token()
        self.lex.next_token()
        if ct.type_ == Token.NUMBER_TYPE:
            return Node(Node.NUMBER_TYPE, ct.lexeme, ct)
        elif ct.type_ == TOKEN.WORD_TYPE:
            return Node(Node.VARIABLE_TYPE, ct.lexeme, ct)

from .Common import *
class ExpressionParser:
    def __init__(self, lexer):
        self.lex = lexer

    def parseExpression(self):
        ct = self.lex.current_token()
        nt = self.lex.next_token()
        return Node(Node.NUMBER_TYPE, ct.lexeme, ct)

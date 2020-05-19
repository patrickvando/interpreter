class Utilities:
    def __init__(self, lexer):
        self.lexer = lexer

    def match(self, expected):
        ct = self.lexer.current_token()
        if ct.lexeme == expected:
            self.lexer.consume()
            self.lexer.next_token()
        else:
            raise Exception("Unexpected token")

    def match_if_present(self, expected):
        ct = self.lexer.current_token()
        if ct.lexeme == expected:
            self.lexer.next_token()

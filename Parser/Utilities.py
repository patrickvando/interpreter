class Utilities:
    """The Utilities class provides utility functions used by multiple classes in the Parser."""

    def __init__(self, lexer):
        self.lexer = lexer

    def match(self, expected):
        """Consume the current token from the Lexer if it matches the expected token, or else raise an error."""
        ct = self.lexer.current_token()
        if ct.lexeme == expected:
            self.lexer.consume()
            self.lexer.next_token()
        else:
            raise Exception("Unexpected token")

    def match_if_present(self, expected):
        """Consume the current token from the Lexer if it matches the expected token."""
        ct = self.lexer.current_token()
        if ct.lexeme == expected:
            self.lexer.next_token()

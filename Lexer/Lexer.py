import re
import sys
from Common.Common import *
class Lexer:
    """The Lexer is used to break down an Oats source file into Tokens.
    
    The raw text of the source file is read line by line and translated into number, symbol, or word Tokens."""
    def __init__(self, filename):
        try:
            self.f = open(filename)
        except IOError:
            print('File "{}" could not be found.'.format(filename))
            exit(0)
        self.line_num = 1
        self.token_buffer = []    
        self.current = -1

    def next_token(self):
        """Get the next token from the token buffer.
        
        If the next token is outside of the token buffer, the token buffer will be expanded by processing the next line."""
        self.current += 1
        return self.current_token()

    def prev_token(self):
        """Get the previous token from the token buffer.
        
        If the previous token is outside the token buffer, None will be returned."""
        self.current -= 1
        return self.current_token()

    def current_token(self):
        """Get the current token."""
        self.current = min(len(self.token_buffer), self.current)
        self.current = max(-1, self.current)
        while self.current == len(self.token_buffer):
            if not self.process_line():
                break
        if self.current == len(self.token_buffer):
            return Token(Token.END_TYPE, "End of File", self.line_num)
        if self.current == -1:
            return None
        return self.token_buffer[self.current]

    def consume(self):
        """Empty the token buffer."""
        self.token_buffer = self.token_buffer[self.current + 1:]
        self.current = -1

    def match(self, expected_lexeme):
        """Consume the current token if its lexeme matches the expected lexeme."""
        ct = self.current_token()
        self.consume()
        if ct.lexeme != expected_lexeme:
            exit('Unexpected token "{}" on line {}.\nExpected token "{}"'.format(ct.lexeme, ct.line_num, expected_lexeme))
        self.next_token()

    def process_line(self):
        """Find all tokens in the next line, add them to the token buffer."""
        if self.f.closed:
            return False
        line = self.f.readline()
        while (re.search("^(\s)*#", line)): # Throw away commented lines.
            line = self.f.readline()
            self.line_num += 1
        if not line:
            self.f.close()
            return False
        token_pattern = "({})|({})|({})|(\S+)".format(Token.SPECIAL_PATTERN, Token.NUMBER_PATTERN, Token.WORD_PATTERN)
        for match in re.findall(token_pattern, line):
            special, number, word, other = match
            if number:
                token = Token(Token.NUMBER_TYPE, number, self.line_num)
            elif word:
                token = Token(Token.WORD_TYPE, word, self.line_num)
            elif special:
                token = Token(Token.SPECIAL_TYPE, special, self.line_num)
            else:
                sys.exit("Unrecognized token \"{}\" on line {}".format(other, self.line_num))
            self.token_buffer.append(token)
        self.line_num += 1
        return True

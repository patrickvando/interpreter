import re
import sys
from Common.Common import *
class Lexer:
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
        self.current += 1
        return self.current_token()

    def prev_token(self):
        self.current -= 1
        return self.current_token()

    def current_token(self):
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
        self.token_buffer = self.token_buffer[self.current + 1:]
        self.current = -1

    def match(self, expected_lexeme):
        ct = self.current_token()
        self.consume()
        if ct.lexeme != expected_lexeme:
            exit('Unexpected token "{}" on line {}.\nExpected token "{}"'.format(ct.lexeme, ct.line_num, expected_lexeme))
        self.next_token()

    def process_line(self):
        if self.f.closed:
            return False
        line = self.f.readline()
        if not line:
            self.f.close()
            return False
        token_pattern = "({})|({})|({})|(\S+)".format(Token.NUMBER_PATTERN, Token.WORD_PATTERN, Token.SPECIAL_PATTERN)
        for match in re.findall(token_pattern, line):
            number, word, special, other = match
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

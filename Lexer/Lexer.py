import re
import sys
class Token:
    number_type, number_pattern = "number", "[0-9]+"
    special_type, special_pattern = "special", "|".join(
            [re.escape(sp) for sp in
                ["++", "--", "==", "<=", ">=", "!=", "<", ">", "=",
                    "!", "+", "-", "/", "%", "}", "{", "]", "[", ")",
                    "(", ";", ","]])
    word_type, word_pattern = "word", "[a-zA-Z][a-zA-Z0-9_]*"
    end_type = "END"

    def __init__(self, type_, lexeme, line_num):
        self.type_ = type_
        self.lexeme = lexeme
        self.line_num = line_num

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
            return Token(Token.end_type, None, self.line_num)
        if self.current == -1:
            return None
        return self.token_buffer[self.current]

    def consume(self):
        self.token_buffer = self.token_buffer[self.current + 1:]
        self.current = -1

    def process_line(self):
        line = self.f.readline()
        if not line:
            return False
        token_pattern = "({})|({})|({})|(\S+)".format(Token.number_pattern, Token.word_pattern, Token.special_pattern)
        for match in re.findall(token_pattern, line):
            number, word, special, other = match
            if number:
                token = Token(Token.number_type, number, self.line_num)
            elif word:
                token = Token(Token.word_type, word, self.line_num)
            elif special:
                token = Token(Token.special_type, special, self.line_num)
            else:
                sys.exit("Unrecognized token \"{}\" on line {}".format(other, self.line_num))
            self.token_buffer.append(token)
        self.line_num += 1
        return True

lex = Lexer("fib.oats")
ct = lex.next_token()
while ct.type_ != Token.end_type:
    print(ct.lexeme)
    ct = lex.next_token()

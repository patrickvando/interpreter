from .Buffer import Buffer
from .Token import Token
from .Word_tokenizer import Word_tokenizer
from .Number_tokenizer import Number_tokenizer
from .Symbol_tokenizer import Symbol_tokenizer
class Lexer:
    def __init__(self, filename):
        self.buf = Buffer(filename)
        self.word = Word_tokenizer(self.buf)
        self.number = Number_tokenizer(self.buf)
        self.symbol = Symbol_tokenizer(self.buf)
        self.ct = None

    def current_token(self):
        return self.ct

    def next_token(self):
        c = self.buf.go_forward()
        while c.isspace():
            c = self.buf.go_forward()
        self.buf.go_backward()
        if c.isalpha():
            token = self.word.extract()
        elif c.isdigit():
            token = self.number.extract()
        elif c in Symbol_tokenizer.acceptable_symbols:
            token = self.symbol.extract()
        elif c == '':
            token = Token("END")
        self.buf.consume()
        self.ct = token
        return token

    def print_token(self, token):
        print("Token type: {} \t Attributes: {}".format(token.kind, token.attributes))


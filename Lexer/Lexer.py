from .Buffer import Buffer
from .Token import Token
from .Word_tokenizer import Word_tokenizer
from .Number_tokenizer import Number_tokenizer
from .Symbol_tokenizer import Symbol_tokenizer
class Lexer:
    """The Lexer class is used to break the raw text of the NRJ source file into "tokens".
    
    All of the raw text in a valid NRJ source file can be broken into
    word, number, or symbol tokens. The Lexer class is responsible for
    streaming these tokens to the Parser class, one at a time. The
    Lexer class stores tokens until they are "consumed", which
    allows previous tokens to be put back into the stream.""" 

    def __init__(self, filename):
        self.buf = Buffer(filename)
        self.word = Word_tokenizer(self.buf)
        self.number = Number_tokenizer(self.buf)
        self.symbol = Symbol_tokenizer(self.buf)
        self.current = -1
        self.token_buffer = []

    def current_token(self):
        """Return the current token in the stream."""
        self.current = max(-1, self.current)
        if self.current == -1:
            return None
        else:
            return self.token_buffer[self.current]

    def prev_token(self):
        """Return the previous token in the stream."""
        self.current -= 1
        return self.current_token()

    def next_token(self):
        """Return the next token in the stream."""
        self.current += 1
        if self.current < len(self.token_buffer):
            return self.current_token()
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
            token = Token()
            token.typ = "END"
        self.buf.consume()
        self.token_buffer.append(token)
        return token

    def consume(self):
        """Remove all previous tokens up to and including the current token from the stream."""
        self.token_buffer = self.token_buffer[self.current + 1:]
        self.current = -1

    def print_token(self, token):
        """Print a token. For debugging purposes."""
        print("Token type: {} \t Lexeme: {} \t Attributes: {}".format(token.typ, token.lexeme, token.attributes))


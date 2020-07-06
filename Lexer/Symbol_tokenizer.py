from .Token import Token
class Symbol_tokenizer:
    """The Symbol_tokenizer class processes symbols into tokens."""
    # + - { } != || && == <= => ++ -- / *
    acceptable_symbols = set("+-{}!|&=<>/*[]();,%")
    acceptable_operators = set(["+", "-", "{", "}", "!", "||", "&&", "==", "<=", ">=", "++", "--", "/", "*", "!=", "[", "]", "(", ")", ";", "=", ',', '<', '>', '%'])
    def __init__(self, buf):
        self.buf = buf

    def extract(self):
        """Return a symbol token."""
        val = ""
        a = self.buf.go_forward()
        b = self.buf.go_forward()
        res = Token()
        res.typ = "symbol"
        if b != "" and a + b in self.acceptable_operators:
            res.lexeme = a + b
            return res
        elif a in self.acceptable_operators:
            res.lexeme = a
            self.buf.go_backward()
            return res
        else:
            raise Exception("Invalid symbol token")

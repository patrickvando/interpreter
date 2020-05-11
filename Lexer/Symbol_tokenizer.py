from .Token import Token
class Symbol_tokenizer:
    # + - { } != || && == <= => ++ -- / *
    acceptable_symbols = set("+-{}!|&=<>/*[]();")
    acceptable_operators = set(["+", "-", "{", "}", "!", "||", "&&", "==", "<=", ">=", "++", "--", "/", "*", "!=", "[", "]", "(", ")", ";", "="])
    def __init__(self, buf):
        self.buf = buf

    def extract(self):
        val = ""
        a = self.buf.go_forward()
        b = self.buf.go_forward()
        if b != "" and a + b in self.acceptable_operators:
            return Token(a + b)
        elif a in self.acceptable_operators:
            self.buf.go_backward()
            return Token(a)
        else:
            raise Exception("Invalid symbol token")

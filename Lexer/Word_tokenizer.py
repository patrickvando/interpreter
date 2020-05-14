from .Token import Token
class Word_tokenizer:
    def __init__(self, buf):
        self.buf = buf

    def extract(self):
        c = self.buf.go_forward()
        val = ""
        while c.isalpha() or c.isdigit() or c == "_":
            val += c
            c = self.buf.go_forward()
        self.buf.go_backward()
        res = Token()
        res.typ = "word"
        res.lexeme = val
        return res

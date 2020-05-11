from .Token import Token
class Number_tokenizer:
    def __init__(self, buf):
        self.buf = buf

    def extract(self):
        def getDigits():
            c = self.buf.go_forward()
            val = ""
            while c.isdigit():
                val += c
                c = self.buf.go_forward()
            return val, c
        
        val, c = getDigits()
        if c == ".":
            after_decimal, c = getDigits()
            if after_decimal == "":
                raise Exception("Invalid number token")
            val += "." + after_decimal
        self.buf.go_backward()

        res = Token("float")
        res.attributes["val"] = val
        return res

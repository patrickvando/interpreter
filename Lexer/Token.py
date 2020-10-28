import re
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


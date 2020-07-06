class Token:
    """The Token class is used to represent word, symbol or number tokens."""
    def __init__(self):
        self.typ = None # Type - "symbol", "word", "double" or "int"
        self.lexeme = "" # The text of the token
        self.value = None # The value of the token (numerical value for number tokens)
        self.attributes = {} # Other information about the token

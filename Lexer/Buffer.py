class Buffer:
    """The Buffer class is used to process raw text.
    
    The Buffer class streams characters to the Lexer class.
    characters are stored until they are "consumed", allowing
    text to be put back into the stream."""
    
    def __init__(self, filename):
        self.text = ""
        self.f = open(filename)
        self.chunk_size = 64
        self.current = -1 
    
    def go_forward(self):
        """Return the next character in the stream."""
        self.current += 1
        if self.current == len(self.text):
            self.text += self.f.read(self.chunk_size)
        if self.current == len(self.text):
            self.current = len(self.text)
            return ""
        return self.text[self.current]

    def go_backward(self):
        """Return the previous character in the stream."""
        self.current -= 1
        if self.current == -1:
            return ""
        else:
            return self.text[self.current]

    def consume(self):
        """Remove all previous characters up to and including
        the current character from the stream."""
        self.text = self.text[self.current + 1:]
        self.current = -1

class Buffer:
    """The Buffer class is used to process text from a file.
    
    The Buffer class streams characters to the Lexer class.
    Characters are stored until they are "consumed", allowing
    text to be put back into the stream."""
    
    def __init__(self, filename):
        self.text = ""
        self.f = open(filename)
        self.chunk_size = 64
        self.current = -1 
    
    def forward(self):
        """Return the next character in the stream.
        If there are no characters remaining in the stream, return None."""
        self.current += 1
        if self.current == len(self.text):
            self.text += self.f.read(self.chunk_size)
        if self.current == len(self.text):
            self.current = len(self.text)
            return None 
        return self.text[self.current]

    def backward(self):
        """Return the previous character in the stream.
        If there are no previous characters in the stream, return None."""
        self.current -= 1
        if self.current < 0:
            return None 
        else:
            return self.text[self.current]

    def consume(self):
        """Remove all previous characters up to and including the current character from the stream."""
        self.text = self.text[self.current + 1:]
        self.current = -1

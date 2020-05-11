class Buffer:
    def __init__(self, filename):
        self.text = ""
        self.f = open(filename)
        self.chunk_size = 64
        self.current = -1 
    
    def go_forward(self):
        self.current += 1
        if self.current == len(self.text):
            self.text += self.f.read(self.chunk_size)
        if self.current == len(self.text):
            self.current = len(self.text)
            return ""
        return self.text[self.current]

    def go_backward(self):
        self.current -= 1
        if self.current == -1:
            return ""
        else:
            return self.text[self.current]

    def consume(self):
        self.text = self.text[self.current + 1:]
        self.current = -1

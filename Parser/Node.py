class Node():
    def __init__(self):
        self.typ = None
        self.attributes = {}
        self.children = []

    def add_child(self, node):
        self.children.append(node)

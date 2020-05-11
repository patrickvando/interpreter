class Node():
    def __init__(self):
        self.kind = None
        self.attributes = {}
        self.children = []

    def add_child(self, node):
        self.children.append(node)

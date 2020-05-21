class Node():
    def __init__(self):
        self.typ = None
        self.attributes = {}
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def copy(self):
        copy_node = Node()
        copy_node.typ = self.typ
        for key in self.attributes:
            copy_node.attributes[key] = self.attributes[key]
        return copy_node

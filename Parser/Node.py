class Node():
    """The Node class is used to represent nodes in the Abstract Syntax Tree (AST) produced by the Parser."""
    def __init__(self):
        self.typ = None
        self.attributes = {}
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def copy(self):
        copy_node = Node()
        copy_node.typ = self.typ
        copy_node.attributes = self.copy_attributes()
        return copy_node

    def copy_attributes(self):
        copy_attributes = {}
        for key in self.attributes:
            copy_attributes[key] = self.attributes[key]
        return copy_attributes

    def __str__(self):
        self.st = ""
        def recurse(root, indent):
            st = "\t"*indent + " " + root.typ
            if root.attributes:
                st += " Attributes: {}".format(root.attributes)
            self.st += st + "\n"
            for child in root.children:
                recurse(child, indent + 1)
        recurse(self, 0)
        return self.st

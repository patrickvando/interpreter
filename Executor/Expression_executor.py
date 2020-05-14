class Expression_executor:
    def execute_expression(self, root):
        if not root.children:
            return root.attributes["val"]
        if root.typ == "+":
            return self.execute_add(root)
        elif root.typ == "-":
            return self.execute_subtract(root)
        elif root.typ == "/":
            return self.execute_divide(root)
        elif root.typ == "*":
            return self.execute_multiply(root)
        elif root.typ == "%":
            return self.execute_modulus(root)
        elif root.typ == "&&":
            return self.execute_and(root)
        elif root.typ == "||":
            return self.execute_or(root)
        elif root.typ == "==":
            return self.execute_eq(root)
        elif root.typ == "<=":
            return self.execute_lte(root)
        elif root.typ == ">=":
            return self.execute_gte(root)
        elif root.typ == "!=":
            return self.execute_ne(root)
        elif root.typ == ">":
            return self.execute_ge(root)
        elif root.yp == "<":
            return self.execute_le(root)

    def execute_add(self, root):
        if len(root.children) == 1:
            return self.execute_expression(root.children[0])
        else:
            left = self.execute_expression(root.children[0])
            right = self.execute_expression(root.children[1])
            return left + right

    def execute_subtract(self, root):
        if len(root.children) == 1:
            return -1 * self.execute_expression(root.children[0])
        else:
            left = self.execute_expression(root.children[0])
            right = self.execute_expression(root.children[1])
            return left - right

    def execute_divide(self, root):
        left = self.execute_expression(root.children[0])
        right = self.execute_expression(root.children[1])
        return left / right

    def execute_multiply(self, root):
        left = self.execute_expression(root.children[0])
        right = self.execute_expression(root.children[1])
        return left * right

    def execute_modulus(self, root):
        left = self.execute_expression(root.children[0])
        right = self.execute_expression(root.children[1])
        return left % right

    def execute_and(self, root):
        left = self.execute_expression(root.children[0])
        right = self.execute_expression(root.children[1])
        return left and right

    def execute_or(self, root):
        left = self.execute_expression(root.children[0])
        right = self.execute_expression(root.children[1])
        return left or right

    def execute_eq(self, root):
        left = self.execute_expression(root.children[0])
        right = self.execute_expression(root.children[1])
        return left == right

    def execute_lte(self, root):
        left = self.execute_expression(root.children[0])
        right = self.execute_expression(root.children[1])
        return left <= right

    def execute_gte(self, root):
        left = self.execute_expression(root.children[0])
        right = self.execute_expression(root.children[1])
        return left >= right

    def execute_le(self, root):
        left = self.execute_expression(root.children[0])
        right = self.execute_expression(root.children[1])
        return left < right

    def execute_ge(self, root):
        left = self.execute_expression(root.children[0])
        right = self.execute_expression(root.children[1])
        return left > right

    def execute_ne(self, root):
        left = self.execute_expression(root.children[0])
        right = self.execute_expression(root.children[1])
        return left != right

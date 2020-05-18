class Expression_executor:
    def __init__(self, st_stack):
        self.st_stack = st_stack

    def execute_function(self, root):
        entry = self.st_stack.get(root.attributes["identifier"])
        function = entry["function"]
        expected_args = function.children[0].children
        function_body = function.children[1]
        given_args = root.children[0].children
        self.st_stack.push_table()
        for k in range(len(expected_args)):
            arg_val = self.execute_expression(given_args[k])
            arg_identifier = expected_args[k].attributes["identifier"]
            self.st_stack.insert(arg_identifier, {"val": arg_val})
        stat_executor = Statement_executor(self.st_stack)
        return_val = stat_executor.execute_statement_list(function_body)
        self.st_stack.pop_table() 
        return return_val

    def execute_expression(self, root):
        if root.typ == "CONSTANT":
                return root.attributes["val"]
        elif root.typ =="VARIABLE":
                entry = self.st_stack.get(root.attributes["identifier"])
                return entry["val"]
        elif root.typ == "FUNCTION_CALL":
                return self.execute_function(root)
        elif root.typ == "+":
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
        elif root.typ == "<":
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

from .Statement_executor import Statement_executor
from .Symbol_table import Symbol_table_stack

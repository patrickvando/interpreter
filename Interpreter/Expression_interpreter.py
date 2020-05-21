class Expression_interpreter:
    def __init__(self, st_stack):
        self.st_stack = st_stack

    def interpret_function(self, root):
        func_identifier = root.attributes["identifier"]
        given_arg_node = root.children[0]
        given_args = []
        for arg in given_arg_node.children:
            given_args.append(self.interpret_expression(arg))
        if func_identifier in Built_ins.funcs:
            return Built_ins.interpret_func(func_identifier, given_args)
        entry = self.st_stack.get(func_identifier)
        function = entry["function"]
        expected_arg_node = function.children[0]
        function_body = function.children[1]
        self.st_stack.push_table()
        expected_args = [arg.attributes["identifier"] for arg in expected_arg_node.children]
        for arg_pair in zip(expected_args, given_args):
            arg_identifier, arg_val = arg_pair
            self.st_stack.insert(arg_identifier, {"val": arg_val})
        stat_interpreter = Statement_interpreter(self.st_stack)
        return_val = stat_interpreter.interpret_statement_list(function_body)
        self.st_stack.pop_table() 
        return return_val

    def interpret_expression(self, root):
        if root.typ == "CONSTANT":
                return root.attributes["val"]
        elif root.typ =="VARIABLE":
                entry = self.st_stack.get(root.attributes["identifier"])
                return entry["val"]
        elif root.typ == "FUNCTION_CALL":
                return self.interpret_function(root)
        elif root.typ == "+":
            return self.interpret_add(root)
        elif root.typ == "-":
            return self.interpret_subtract(root)
        elif root.typ == "/":
            return self.interpret_divide(root)
        elif root.typ == "*":
            return self.interpret_multiply(root)
        elif root.typ == "%":
            return self.interpret_modulus(root)
        elif root.typ == "&&":
            return self.interpret_and(root)
        elif root.typ == "||":
            return self.interpret_or(root)
        elif root.typ == "==":
            return self.interpret_eq(root)
        elif root.typ == "<=":
            return self.interpret_lte(root)
        elif root.typ == ">=":
            return self.interpret_gte(root)
        elif root.typ == "!=":
            return self.interpret_ne(root)
        elif root.typ == ">":
            return self.interpret_ge(root)
        elif root.typ == "<":
            return self.interpret_le(root)
        elif root.typ == "++":
            return self.interpret_increment(root)
        elif root.typ == "--":
            return self.interpret_decrement(root)

    def interpret_add(self, root):
        if len(root.children) == 1:
            return self.interpret_expression(root.children[0])
        else:
            left = self.interpret_expression(root.children[0])
            right = self.interpret_expression(root.children[1])
            return left + right
    
    def interpret_increment(self, root):
        var = root.children[0]
        entry = self.st_stack.get(var.attributes["identifier"])
        val = entry["val"]
        self.st_stack.update(var.attributes["identifier"], {"val": val + 1})
        if root.attributes["pre"]:
            return val + 1
        else:
            return val 

    def interpret_decrement(self, root):
        var = root.children[0]
        entry = self.st_stack.get(var.attributes["identifier"])
        val = entry["val"]
        self.st_stack.update(var.attributes["identifier"], {"val": val - 1})
        if root.attributes["pre"]:
            return val - 1
        else:
            return val 

    def interpret_subtract(self, root):
        if len(root.children) == 1:
            return -1 * self.interpret_expression(root.children[0])
        else:
            left = self.interpret_expression(root.children[0])
            right = self.interpret_expression(root.children[1])
            return left - right

    def interpret_divide(self, root):
        left = self.interpret_expression(root.children[0])
        right = self.interpret_expression(root.children[1])
        return left / right

    def interpret_multiply(self, root):
        left = self.interpret_expression(root.children[0])
        right = self.interpret_expression(root.children[1])
        return left * right

    def interpret_modulus(self, root):
        left = self.interpret_expression(root.children[0])
        right = self.interpret_expression(root.children[1])
        return left % right

    def interpret_and(self, root):
        left = self.interpret_expression(root.children[0])
        right = self.interpret_expression(root.children[1])
        return left and right

    def interpret_or(self, root):
        left = self.interpret_expression(root.children[0])
        right = self.interpret_expression(root.children[1])
        return left or right

    def interpret_eq(self, root):
        left = self.interpret_expression(root.children[0])
        right = self.interpret_expression(root.children[1])
        return left == right

    def interpret_lte(self, root):
        left = self.interpret_expression(root.children[0])
        right = self.interpret_expression(root.children[1])
        return left <= right

    def interpret_gte(self, root):
        left = self.interpret_expression(root.children[0])
        right = self.interpret_expression(root.children[1])
        return left >= right

    def interpret_le(self, root):
        left = self.interpret_expression(root.children[0])
        right = self.interpret_expression(root.children[1])
        return left < right

    def interpret_ge(self, root):
        left = self.interpret_expression(root.children[0])
        right = self.interpret_expression(root.children[1])
        return left > right

    def interpret_ne(self, root):
        left = self.interpret_expression(root.children[0])
        right = self.interpret_expression(root.children[1])
        return left != right

from .Statement_interpreter import Statement_interpreter
from .Symbol_table import Symbol_table_stack
from .Built_ins import Built_ins

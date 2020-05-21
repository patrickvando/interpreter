class Construct_interpreter:
    def __init__(self, st_stack):
        self.st_stack = st_stack

    def interpret_construct(self, root):
        if root.typ == "IF":
            return self.interpret_if(root)
        elif root.typ == "WHILE":
            return self.interpret_while(root)
        elif root.typ == "FOR":
            return self.interpret_for(root)

    def interpret_if(self, root):
        exp_interpreter = Expression_interpreter(self.st_stack)
        stat_interpreter = Statement_interpreter(self.st_stack)
        for option_node in root.children:
            condition, body = option_node.children
            res = exp_interpreter.interpret_expression(condition)
            if res:
                return stat_interpreter.interpret_statement_list(body)

    def interpret_while(self, root):
        exp_interpreter = Expression_interpreter(self.st_stack)
        stat_interpreter = Statement_interpreter(self.st_stack)
        res = exp_interpreter.interpret_expression(root.children[0])
        while res != False:
            return_value = stat_interpreter.interpret_statement_list(root.children[1])
            if return_value:
                return return_value
            res = exp_interpreter.interpret_expression(root.children[0])

    def interpret_for(self, root):
        exp_interpreter = Expression_interpreter(self.st_stack)
        stat_interpreter = Statement_interpreter(self.st_stack)
        stat_interpreter.interpret_statement(root.children[0])
        res = exp_interpreter.interpret_expression(root.children[1])
        while res != False:
            return_value = stat_interpreter.interpret_statement_list(root.children[3])
            if return_value:
                return return_value
            stat_interpreter.interpret_statement(root.children[2])
            res = exp_interpreter.interpret_expression(root.children[1])

from .Expression_interpreter import Expression_interpreter
from .Statement_interpreter import Statement_interpreter

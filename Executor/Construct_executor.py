class Construct_executor:
    def __init__(self, st_stack):
        self.st_stack = st_stack

    def execute_construct(self, root):
        if root.typ == "IF":
            return self.execute_if(root)
        elif root.typ == "WHILE":
            return self.execute_while(root)
        elif root.typ == "FOR":
            return self.execute_for(root)

    def execute_if(self, root):
        exp_executor = Expression_executor(self.st_stack)
        res = exp_executor.execute_expression(root.children[0])
        if res == False:
            return
        stat_executor = Statement_executor(self.st_stack)
        return stat_executor.execute_statement_list(root.children[1])

    def execute_while(self, root):
        exp_executor = Expression_executor(self.st_stack)
        stat_executor = Statement_executor(self.st_stack)
        res = exp_executor.execute_expression(root.children[0])
        while res != False:
            return_value = stat_executor.execute_statement_list(root.children[1])
            if return_value:
                return return_value
            res = exp_executor.execute_expression(root.children[0])

    def execute_for(self, root):
        exp_executor = Expression_executor(self.st_stack)
        stat_executor = Statement_executor(self.st_stack)
        stat_executor.execute_statement(root.children[0])
        res = exp_executor.execute_expression(root.children[1])
        while res != False:
            return_value = stat_executor.execute_statement_list(root.children[3])
            if return_value:
                return return_value
            stat_executor.execute_statement(root.children[2])
            res = exp_executor.execute_expression(root.children[1])

from .Expression_executor import Expression_executor
from .Statement_executor import Statement_executor

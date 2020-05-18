class Statement_executor():
    def __init__(self, st_stack):
        self.st_stack = st_stack

    def execute_statement_list(self, root):
        for child in root.children:
            res = self.execute_statement(child)
            if res:
                return res
        return None
 
    def execute_statement(self, root):
        if root.typ == "RETURN":
            return self.execute_return_statement(root)
        elif root.typ == "ASSIGN":
            self.execute_variable_assignment(root)
        elif root.typ == "VARIABLE_DECLARATION":
            self.execute_variable_declaration(root)
        elif root.typ in Data_types.constructs:
            con_executor = Construct_executor(self.st_stack)
            return con_executor.execute_construct(root)
        elif root.typ == "FUNCTION":
            self.execute_function_declaration(root)
        return None

    def execute_function_declaration(self, root):
        self.st_stack.insert(root.attributes["identifier"], {"function": root}) 
    
    #need to keep declare variable -> declared inside scope should be different from declared outside scope, one overwrites prev, one doesnt
    def execute_variable_declaration(self, root):
        var = root.children[0]
        exp_executor = Expression_executor(self.st_stack)
        res = exp_executor.execute_expression(root.children[1])
        self.st_stack.insert(var.attributes["identifier"], {"val": res}) 

    def execute_variable_assignment(self, root):
        var = root.children[0]
        exp_executor = Expression_executor(self.st_stack)
        res = exp_executor.execute_expression(root.children[1])
        self.st_stack.update(var.attributes["identifier"], {"val": res})

    def execute_return_statement(self, root):
        exp_executor = Expression_executor(self.st_stack)
        return exp_executor.execute_expression(root.children[0])

from .Data_types import Data_types
from .Expression_executor import Expression_executor
from .Construct_executor import Construct_executor

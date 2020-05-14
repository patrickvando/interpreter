from .Expression_executor import Expression_executor
from .Symbol_table import Symbol_table_stack
class Statement_executor():
    def __init__(self, st_stack):
        self.exp_executor = Expression_executor()
        self.st_stack = st_stack
       
    def execute_statement_list(self, root):
        for child in root.children:
            self.execute_statement(child)

    def execute_statement(self, root):
        if root.typ == "ASSIGN":
            self.execute_variable_assignment(root)
        elif root.typ == "DECLARE":
            self.execute_variable_declaration(root)

    def execute_function_declaration(self):
        pass

    def execute_function_call(self):
        pass
    
    #need to keep declare variable -> declared inside scope should be different from declared outside scope, one overwrites prev, one doesnt
    def execute_variable_declaration(self, root):
        var = root.children[0]
        res = self.exp_executor.execute_expression(root.children[1])
        identifier = var.attributes["identifier"]
        self.st_stack.insert(identifier, res)

    def execute_variable_assignment(self, root):
        var = root.children[0]
        res = self.exp_executor.execute_expression(root.children[1])
        identifier = var.attributes["identifier"]
        self.st_stack.update(identifier, res)

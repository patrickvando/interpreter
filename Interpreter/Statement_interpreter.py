class Statement_interpreter():
    def __init__(self, st_stack):
        self.st_stack = st_stack

    def interpret_statement_list(self, root):
        for child in root.children:
            res = self.interpret_statement(child)
            if res:
                return res
        return None
 
    def interpret_statement(self, root):
        if root.typ == "RETURN":
            return self.interpret_return_statement(root)
        elif root.typ == "ASSIGN":
            self.interpret_variable_assignment(root)
        elif root.typ == "VARIABLE_DECLARATION":
            self.interpret_variable_declaration(root)
        elif root.typ in Data_types.constructs:
            con_interpreter = Construct_interpreter(self.st_stack)
            return con_interpreter.interpret_construct(root)
        elif root.typ == "FUNCTION":
            self.interpret_function_declaration(root)
        elif root.typ == "++" or "--":
            exp_interpreter = Expression_interpreter(self.st_stack)
            exp_interpreter.interpret_expression(root)
        if root.typ == "PRINT":
            self.interpret_print_statement(root)
        return None

    def interpret_function_declaration(self, root):
        self.st_stack.insert(root.attributes["identifier"], {"function": root}) 
    
    #need to keep declare variable -> declared inside scope should be different from declared outside scope, one overwrites prev, one doesnt
    def interpret_variable_declaration(self, root):
        var = root.children[0]
        exp_interpreter = Expression_interpreter(self.st_stack)
        res = exp_interpreter.interpret_expression(root.children[1])
        self.st_stack.insert(var.attributes["identifier"], {"val": res}) 

    def interpret_variable_assignment(self, root):
        var = root.children[0]
        exp_interpreter = Expression_interpreter(self.st_stack)
        res = exp_interpreter.interpret_expression(root.children[1])
        self.st_stack.update(var.attributes["identifier"], {"val": res})

    def interpret_return_statement(self, root):
        exp_interpreter = Expression_interpreter(self.st_stack)
        rv = exp_interpreter.interpret_expression(root.children[0])
        return rv;

from .Data_types import Data_types
from .Expression_interpreter import Expression_interpreter
from .Construct_interpreter import Construct_interpreter

from Common.Common import *
class ConstructInterpreter:
    def __init__(self, symbol_table):
        self.sym_tab = symbol_table

    def interpret_construct(self, node):
        if node.type_ == Node.FUNC_DEF_TYPE:
            self.interpret_func_def(node)
        else:
            illegal_node(node)
        return None

    def interpret_if(self, node):
        pass

    def interpret_for(self, node):
        pass

    def interpret_while(self, node):
        pass

    def interpret_func_def(self, node):
        self.sym_tab[-1][(node.type_, node.value)] = node

from Interpreter.ExpressionInterpreter import ExpressionInterpreter
from Interpreter.StatementInterpreter import StatementInterpreter

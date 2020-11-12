from Common.Common import *

class StatementInterpreter:
    def __init__(self, symbol_table=[]):
        self.sym_tab = symbol_table
        if not self.sym_tab:
            self.sym_tab.append(dict())

    def interpret_statement_list(self, node):
        for child in node.children:
            if child.type_ == Node.ASSIGN_TYPE:
                self.interpret_assignment(child)
            elif child.type_ == Node.FUNC_CALL_TYPE:
                einterpreter = ExpressionInterpreter(self.sym_tab)
                einterpreter.interpret_expression(child)
            elif child.type_ in Node.CONSTRUCT_TYPES:
                cinterpreter = ConstructInterpreter(self.sym_tab)
                ret_val = cinterpreter.interpret_construct(child)
                if ret_val != None:
                    self.pop_symbol_table()
                    return ret_val
            elif child.type_ == Node.RETURN_TYPE:
                ret_val = self.interpret_return(child)
                self.pop_symbol_table()
                return ret_val
            else:
                illegal_node(child)
        return None

    def interpret_assignment(self, node):
        variable_node, expression_node = node.children
        einterpreter = ExpressionInterpreter(self.sym_tab)
        self.sym_tab[-1][(variable_node.type_, variable_node.value)] = einterpreter.interpret_expression(expression_node)

    def interpret_return(self, node):
        expression_node = node.children[0]
        einterpreter = ExpressionInterpreter(self.sym_tab)
        return einterpreter.interpret_expression(expression_node)

    def pop_symbol_table(self):
        self.sym_tab.pop()
        if not self.sym_tab:
            exit(0)

from Interpreter.ConstructInterpreter import ConstructInterpreter
from Interpreter.ExpressionInterpreter import ExpressionInterpreter

from Common.Common import *
class ConstructInterpreter:
    def __init__(self, symbol_table):
        self.sym_tab = symbol_table

    def interpret_construct(self, node):
        if node.type_ == Node.FUNC_DEF_TYPE:
            ret_val = self.interpret_func_def(node)
        elif node.type_ == Node.IF_TYPE:
            ret_val = self.interpret_if(node)
        elif node.type_ == Node.FOR_TYPE:
            ret_val = self.interpret_for(node)
        elif node.type_ == Node.WHILE_TYPE:
            ret_val = self.interpret_while(node)
        else:
            illegal_node(node)
        return ret_val

    def interpret_if(self, node):
        ret_val = None
        einterpreter = ExpressionInterpreter(self.sym_tab)
        for k in range(0, len(node.children), 2):
            condition_node = node.children[k]
            body_node = node.children[k + 1]
            if einterpreter.interpret_expression(condition_node) != 0:
                sinterpreter = StatementInterpreter(self.sym_tab)
                ret_val = sinterpreter.interpret_statement_list(body_node)
                break
        return ret_val

    def interpret_for(self, node):
        ret_val = None
        einterpreter = ExpressionInterpreter(self.sym_tab)
        sinterpreter = StatementInterpreter(self.sym_tab)
        assignment_node = node.children[0]
        condition_node = node.children[1]
        change_node = node.children[2]
        body_node = node.children[3]
        sinterpreter.interpret_assignment(assignment_node)
        while einterpreter.interpret_expression(condition_node) != 0:
            ret_val = sinterpreter.interpret_statement_list(body_node)
            if ret_val != None:
                break
            sinterpreter.interpret_assignment(change_node)
        return ret_val

    def interpret_while(self, node):
        ret_val = None
        einterpreter = ExpressionInterpreter(self.sym_tab)
        sinterpreter = StatementInterpreter(self.sym_tab)
        condition_node = node.children[0]
        body_node = node.children[1]
        while einterpreter.interpret_expression(condition_node) != 0:
            ret_val = sinterpreter.interpret_statement_list(body_node)
            if ret_val != None:
                break
        return ret_val

    def interpret_func_def(self, node):
        self.sym_tab[-1][(node.type_, node.value)] = node

from Interpreter.ExpressionInterpreter import ExpressionInterpreter
from Interpreter.StatementInterpreter import StatementInterpreter

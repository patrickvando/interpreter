from Common.Common import *

class StatementInterpreter:
    """The StatementInterpreter is used to execute the statements in an Abstract Syntax Tree.
    
    The StatementInterpreter specifically executes assignment and return statements. Execution of function declarations and loops is handed off to the ConstructInterpreter. Execution of function calls is handed off to the ExpressionInterpreter. """
    def __init__(self, symbol_table):
        self.sym_tab = symbol_table

    def interpret_statement_list(self, node):
        """Execute all the child nodes of a statement list node.
        
        If one of the child nodes is found to have a return value when executed, execution of further child nodes is cut short and that return value is passed up."""
        ret_val = None
        for child in node.children:
            if child.type_ == Node.ASSIGN_TYPE:
                self.interpret_assignment(child)
            elif child.type_ == Node.FUNC_CALL_TYPE or child.type_ in Node.BUILT_IN_TYPES:
                einterpreter = ExpressionInterpreter(self.sym_tab)
                einterpreter.interpret_expression(child)
            elif child.type_ in Node.CONSTRUCT_TYPES:
                cinterpreter = ConstructInterpreter(self.sym_tab)
                ret_val = cinterpreter.interpret_construct(child)
                if ret_val != None:
                    break
            elif child.type_ == Node.RETURN_TYPE:
                ret_val = self.interpret_return(child)
                break
            else:
                illegal_node(child)
        return ret_val

    def interpret_assignment(self, node):
        """Execute an assignment node.

        An assignment node has two children: a variable node, and an expression node. The expression node is evaluated and associated with the variable node in the symbol table."""
        var_to_exp_result = []
        einterpreter = ExpressionInterpreter(self.sym_tab)
        for k in range(0, len(node.children), 2):
            variable_node, expression_node = node.children[k], node.children[k + 1]
            var_to_exp_result.append([variable_node, einterpreter.interpret_expression(expression_node)])
        for variable_node, expr_result in var_to_exp_result:
            self.sym_tab[-1][(variable_node.type_, variable_node.value)] = expr_result 

    def interpret_return(self, node):
        """Execute a return statement.
        
        A return node has an expression node as its only child. This expression node is evaluated and the result is returned."""
        expression_node = node.children[0]
        einterpreter = ExpressionInterpreter(self.sym_tab)
        return einterpreter.interpret_expression(expression_node)

from Interpreter.ConstructInterpreter import ConstructInterpreter
from Interpreter.ExpressionInterpreter import ExpressionInterpreter

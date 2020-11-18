from Common.Common import *
class ConstructInterpreter:
    """The ConstructInterpreter is used to execute the constructs in an Abstract Syntax Tree.

    The ConstructInterpreter specifically executes for/while loops, if/elseif/else statements, and function declarations."""
    def __init__(self, symbol_table):
        self.sym_tab = symbol_table

    def interpret_construct(self, node):
        """Execute a construct node.
        
        All construct nodes will have a return value of None, unless the body of the construct node contains a return statement."""
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
        """Execute an if node.
        
        An if node has an even number of children, and has at least two children. Every subsequent pair of children consists of an expression node and a statement list node. The expression node corresponds to the condition, and the statement list node corresponds to the body of that if, elseif, or else statement."""
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
        """Execute a for node.

        A for node has four children: An assignment node, an expression node, a statement list node, and an assignment node. The first assignment node represents the initial assignment step of a traditional for loop, and is only executed once. The expression node represents the loop condition. If the loop condition evaluates to a nonzero result, then the statement list node representing the body of the loop is executed. Then the last assignment node, representing the increment/decrement step of a traditional for loop, is executed. The process then repeats, until the loop condition evaluates to zero."""
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
        """Execute a while node.

        A while node has two children: An expression node and a statement list node. The expression node, representing the loop condition, is evaluated, and if the result is not equal to 0, the statement list node representing the body of the loop is executed. The process then repeats."""
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
        """Execute a function definition.

        Stores the function definition node in the symbol table."""
        self.sym_tab[-1][(node.type_, node.value)] = node

from Interpreter.ExpressionInterpreter import ExpressionInterpreter
from Interpreter.StatementInterpreter import StatementInterpreter

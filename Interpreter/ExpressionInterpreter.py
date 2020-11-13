from Common.Common import *
class ExpressionInterpreter:
    def __init__(self, symbol_table):
        self.sym_tab = symbol_table

    def interpret_expression(self, node):
        if len(node.children) == 2:
            left, right = node.children
        elif len(node.children) == 1:
            left = node.children[0]
        if node.type_ == Node.VARIABLE_TYPE:
            return self.interpret_variable(node)
        elif node.type_ == Node.FUNC_CALL_TYPE:
            return self.interpret_func_call(node)
        elif node.type_ == Node.ADD_TYPE:
            return self.interpret_expression(left) + self.interpret_expression(right)
        elif node.type_ == Node.SUB_TYPE:
            if len(node.children) == 1:
                return -self.interpret_expression(left)
            else:
                return self.interpret_expression(left) - self.interpret_expression(right)
        elif node.type_ == Node.MULT_TYPE:
            return self.interpret_expression(left) * self.interpret_expression(right)
        elif node.type_ == Node.DIV_TYPE:
            return self.interpret_expression(left) // self.interpret_expression(right)
        elif node.type_ == Node.MOD_TYPE:
            return self.interpret_expression(left) % self.interpret_expression(right)
        elif node.type_ == Node.AND_TYPE:
            return (self.interpret_expression(left) != 0) * (self.interpret_expression(right) != 0)
        elif node.type_ == Node.OR_TYPE:
            return int((self.interpret_expression(left) != 0) + (self.interpret_expression(right) != 0) != 0) 
        elif node.type_ == Node.NOT_TYPE:
            return int(self.interpret_expression(left) == 0)
        elif node.type_ == Node.EQ_TYPE:
            return int(self.interpret_expression(left) == self.interpret_expression(right))
        elif node.type_ == Node.NEQ_TYPE:
            return int(self.interpret_expression(left) != self.interpret_expression(right))
        elif node.type_ == Node.LT_TYPE:
            return int(self.interpret_expression(left) < self.interpret_expression(right))
        elif node.type_ == Node.GT_TYPE:
            return int(self.interpret_expression(left) > self.interpret_expression(right))
        elif node.type_ == Node.LTE_TYPE:
            return int(self.interpret_expression(left) <= self.interpret_expression(right))
        elif node.type_ == Node.GTE_TYPE:
            return int(self.interpret_expression(left) >= self.interpret_expression(right))
        elif node.type_ == Node.NUMBER_TYPE:
            return int(node.value)
        elif node.type_ == Node.PRINT_TYPE:
            return self.interpret_print(node)
        elif node.type_ == Node.READ_TYPE:
            return self.interpret_read(node)
        else:
            illegal_node(node)

    def interpret_variable(self, node):
        ind = len(self.sym_tab) - 1
        while ind >= 0 and (node.VARIABLE_TYPE, node.value) not in self.sym_tab[ind]:
            ind -= 1
        if ind < 0:
            uninitialized_variable(node)
        return self.sym_tab[ind][(node.VARIABLE_TYPE, node.value)]

    def interpret_func_call(self, node):
        ind = len(self.sym_tab) - 1
        while ind >= 0 and (node.FUNC_DEF_TYPE, node.value) not in self.sym_tab[ind]:
            ind -= 1
        if ind < 0:
            uninitialized_function(node)
        func_def_node = self.sym_tab[ind][(node.FUNC_DEF_TYPE, node.value)]
        param_node, slist_node = func_def_node.children
        if len(param_node.children) != len(node.children):
            argument_length_mismatch(node)
        arg_vals = []
        einterpreter = ExpressionInterpreter(self.sym_tab)
        for expr in node.children:
            arg_vals.append(einterpreter.interpret_expression(expr))
        self.sym_tab.append(dict(zip([(param.type_, param.value) for param in param_node.children], arg_vals)))
        sinterpreter = StatementInterpreter(self.sym_tab)
        ret_val =  sinterpreter.interpret_statement_list(slist_node)
        self.sym_tab.pop()
        if ret_val == None:
            return 0
        return ret_val

    def interpret_print(self, node):
        einterpreter = ExpressionInterpreter(self.sym_tab)
        e_results = []
        for expr in node.children:
            e_results.append(einterpreter.interpret_expression(expr))
        print(", ".join([str(result) for result in e_results]))
        return 0

    import re
    def interpret_read(self, node):
        einterpreter = ExpressionInterpreter(self.sym_tab)
        vars_ = []
        for var in node.children:
            res = input()
            while not re.match('^-?[0-9]+', res):
                print("Please input a valid integer.")
                res = input()
            self.sym_tab[-1][(Node.VARIABLE_TYPE, var.value)] = int(res)
        return 0

from Interpreter.StatementInterpreter import StatementInterpreter

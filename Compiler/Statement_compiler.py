class Statement_compiler:
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table

    def compile_statement_list(self, root):
        res = []
        res += self.allocate_variables(root)
        cc = Construct_compiler(self.symbol_table)
        for statement in root.children:
            if statement.typ in cc.CONSTRUCTS:
                res += cc.compile_construct(statement)
            else:
                res += self.compile_standalone_statement(statement)
        return res

    def compile_standalone_statement(self, root):
        res = []
        ec = Expression_compiler(self.symbol_table)
        if root.typ == "VARIABLE_DECLARATION" or root.typ == "ASSIGN":
            res += self.compile_assignment(root)
        elif root.typ in ec.STANDALONE_EXPRESSIONS:
            res += ec.compile_expression(root)
        return res

    def compile_assignment(self, root):
        res = []
        variable = root.children[0]
        expression = root.children[1]
        ec = Expression_compiler(self.symbol_table)
        res += ec.load_variable_location(variable)
        res += ec.compile_expression(expression)
        res += instr.pop(instr.R2)
        res += instr.pop(instr.R1)
        res += instr.mov(instr.memloc(instr.R1), instr.R2)
        return res

    def allocate_variables(self, root):
        res = []
        st = ""
        offset = 0
        variables = []
        for statement in root.children:
            if statement.typ == "VARIABLE_DECLARATION":
                info = {}
                variable = statement.children[0]
                variables.append(variable.attributes)
        for variable in variables:
            offset += 8
            variable["offset"] = offset
            self.symbol_table.insert(variable["identifier"], variable)
        #allocate space for variables
        res += instr.sub(instr.SP, offset)
        return res

from .Instructions import Instructions as instr
from .Expression_compiler import Expression_compiler
from .Construct_compiler import Construct_compiler

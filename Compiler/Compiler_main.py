class Compiler_main:
    def __init__(self, filename):
        self.symbol_table = Symbol_table_stack()
        self.symbol_table.push_table()
        self.output_file = open(filename, 'w')
        self.ec = Expression_compiler(self.symbol_table)

    def compile_ast(self, root):
        res = []
        res += instr.HEADER
        res += instr.push(instr.BP)
        res += instr.mov(instr.BP, instr.SP)
        res += self.compile_statement_list(root)
        res += instr.mov(instr.SP, instr.BP)
        res += instr.pop(instr.BP)
        res += instr.FOOTER
        self.write_instructions(res)

    def write_instructions(self, instructions):
        for instruction in instructions:
            self.output_file.write(instruction + "\n")

    def compile_statement_list(self, root):
        res = []
        res += self.allocate_variables(root)
        for statement in root.children:
            if statement.typ == "VARIABLE_DECLARATION" or statement.typ == "VARIABLE_ASSIGNMENT":
                res += self.compile_assignment(statement)
        return res

    def compile_assignment(self, root):
        res = []
        variable = root.children[0]
        expression = root.children[1]
        res += self.load_variable_location(variable)
        res += self.ec.compile_expression(expression)
        res += instr.pop(instr.R2)
        res += instr.pop(instr.R1)
        res += instr.mov(instr.memloc(instr.R1), instr.R2)
        return res

    #pushes the memory location of the variable onto the stack
    def load_variable_location(self, variable):
        res = []
        variable, depth = self.symbol_table.get(variable.attributes["identifier"])
        #assume depth 0 right now
        res += instr.mov(instr.R1, instr.BP)
        res += instr.sub(instr.R1, variable["offset"])
        res += instr.push(instr.R1)
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

from .Symbol_table import Symbol_table_stack
from .Instructions import Instructions as instr
from .Expression_compiler import Expression_compiler

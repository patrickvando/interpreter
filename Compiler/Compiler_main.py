class Compiler_main:
    def __init__(self, filename):
        self.symbol_table = Symbol_table_stack()
        self.output_file = open(filename, 'w')

    def compile_ast(self, root):
        st = Statement_compiler(self.symbol_table)
        res = []
        res += instr.HEADER
        res += instr.push(instr.BP)
        res += instr.mov(instr.BP, instr.SP)
        res += st.compile_statement_list(root)
        res += instr.mov(instr.SP, instr.BP)
        res += instr.pop(instr.BP)
        res += instr.FOOTER
        res += instr.define_print()
        self.write_instructions(res)

    def write_instructions(self, instructions):
        for instruction in instructions:
            self.output_file.write(instruction + "\n")


from .Symbol_table import Symbol_table_stack
from .Instructions import Instructions as instr
from .Statement_compiler import Statement_compiler

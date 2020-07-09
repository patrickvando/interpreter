class Compiler_main:
    """The Compiler_main class turns an Abstract Syntax Tree (AST) into an assembly file.

    The Compiler_main class calls other classes in the Compiler that are
    responsible for descending down branches of the AST and translating
    the values and structure of the tree into NASM assembly
    instructions that are then written to .asm file."""
    def __init__(self, filename):
        self.symbol_table = Symbol_table_stack()
        self.output_file = open(filename, 'w')

    def compile_ast(self, root):
        """Translate the AST to a set of instructions and write those instructions to the output file."""
        st = Statement_compiler(self.symbol_table)
        res = []
        res += instr.HEADER
        res += self.load_print()
        res += instr.push(instr.BP)
        res += instr.mov(instr.BP, instr.SP)
        res += st.compile_statement_list(root)
        res += instr.mov(instr.SP, instr.BP)
        res += instr.pop(instr.BP)
        res += instr.FOOTER
        self.write_instructions(res)

    def write_instructions(self, instructions):
        """Write a set of instructions to the output file."""
        for instruction in instructions:
            self.output_file.write(instruction + "\n")

    def load_print(self):
        """Create a built-in "print" routine by adding a pre-written set of NASM constructions."""
        res = []
        function_label = self.symbol_table.next_label()
        continue_label = self.symbol_table.next_label()
        res += instr.jmp(continue_label)
        res += instr.addlabel(function_label)
        res += ["""push rbp
mov rbp, rsp
push rax
push rcx
mov rdi,fmt
mov rsi, [rbp + 16]
xor rax, rax
call printf
pop rcx
pop rax
pop rbp
ret"""]
        res += instr.addlabel(continue_label)
        function = {}
        function["label"] = function_label
        self.symbol_table.insert("print", function)
        return res

from .Symbol_table import Symbol_table_stack
from .Instructions import Instructions as instr
from .Statement_compiler import Statement_compiler

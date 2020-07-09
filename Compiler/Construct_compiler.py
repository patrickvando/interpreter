class Construct_compiler:
    """The Construct_compiler class descends down all construct nodes in the AST and turns them into sequences of instructions.

    For loops, while loops, and if-elseif-else constructs are all 
    represented as construct nodes."""

    CONSTRUCTS = ["IF", "WHILE", "FOR"]
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table

    def compile_construct(self, root):
        """Return a sequence of assembly instructions, given a construct node."""
        res = []
        if root.typ == "IF":
            res += self.compile_if(root)
        elif root.typ == "WHILE":
            res += self.compile_while(root)
        elif root.typ == "FOR":
            res += self.compile_for(root)
        return res

    def compile_if(self, root):
        """Return a sequence of assembly instructions, given an if node."""
        res = []
        continue_label = self.symbol_table.next_label()
        next_label = self.symbol_table.next_label()
        sc = Statement_compiler(self.symbol_table)
        ec = Expression_compiler(self.symbol_table)
        for option in root.children:
            condition = option.children[0]
            statement_list = option.children[1]
            res += ec.compile_expression(condition)
            res += instr.pop(instr.R1)
            res += instr.mov(instr.R2, 1)
            res += instr.cmp(instr.R1, instr.R2)
            res += instr.jne(next_label)
            res += sc.compile_statement_list(statement_list)
            res += instr.jmp(continue_label)
            res += instr.addlabel(next_label)
            next_label = self.symbol_table.next_label()
        res += instr.addlabel(continue_label)
        return res

    def compile_for(self, root):
        """Return a sequence of assembly instructions, given a for node."""
        res = []
        loop_label = self.symbol_table.next_label()
        continue_label = self.symbol_table.next_label()
        sc = Statement_compiler(self.symbol_table)
        ec = Expression_compiler(self.symbol_table)
        initial = root.children[0]
        condition = root.children[1]
        increment = root.children[2]
        body = root.children[3]
        res += sc.compile_standalone_statement(initial)
        res += instr.addlabel(loop_label)
        res += ec.compile_expression(condition)
        res += instr.pop(instr.R1)
        res += instr.mov(instr.R2, 1)
        res += instr.cmp(instr.R1, instr.R2)
        res += instr.jne(continue_label)
        res += sc.compile_statement_list(body)
        res += sc.compile_standalone_statement(increment)
        res += instr.jmp(loop_label)
        res += instr.addlabel(continue_label)      
        return res

    def compile_while(self, root):
        """Return a sequence of assembly instructions, given a while node."""
        res = []
        loop_label = self.symbol_table.next_label()
        continue_label = self.symbol_table.next_label()
        sc = Statement_compiler(self.symbol_table)
        ec = Expression_compiler(self.symbol_table)
        condition = root.children[0]
        body = root.children[1]
        res += instr.addlabel(loop_label)
        res += ec.compile_expression(condition)
        res += instr.pop(instr.R1)
        res += instr.mov(instr.R2, 1)
        res += instr.cmp(instr.R1, instr.R2)
        res += instr.jne(continue_label)
        res += sc.compile_statement_list(body)
        res += instr.jmp(loop_label)
        res += instr.addlabel(continue_label)
        return res

from .Instructions import Instructions as instr
from .Statement_compiler import Statement_compiler
from .Expression_compiler import Expression_compiler

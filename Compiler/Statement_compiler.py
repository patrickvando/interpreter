class Statement_compiler:
    """The Statement_compiler class descends down all statement nodes in the AST and turns them into sequences of assembly instructions.

    Variable assignments, function definitions, function calls, 
    increment/decrement and return statements are all represented as
    statement nodes."""

    def __init__(self, symbol_table):
        self.symbol_table = symbol_table

    def compile_statement_list(self, root):
        """Return a sequence of assembly instructions, given a statement_list node."""
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
        """Return a sequence of assembly instructions, given a statement node."""
        res = []
        ec = Expression_compiler(self.symbol_table)
        if root.typ == "VARIABLE_DECLARATION" or root.typ == "ASSIGN":
            res += self.compile_assignment(root)
        elif root.typ in ec.STANDALONE_EXPRESSIONS:
            res += ec.compile_expression(root)
        elif root.typ == "FUNCTION":
            res += self.compile_function_definition(root)
        elif root.typ == "RETURN":
            res += self.compile_function_return(root)
        return res

    def compile_assignment(self, root):
        """Return a sequence of assembly instructions, given an assignment node."""
        res = []
        variable = root.children[0].copy_attributes()
        expression = root.children[1]
        ec = Expression_compiler(self.symbol_table)
        res += ec.load_variable_location(variable)
        res += ec.compile_expression(expression)
        res += instr.pop(instr.R2)
        res += instr.pop(instr.R1)
        res += instr.mov(instr.memloc(instr.R1), instr.R2)
        return res

    def allocate_variables(self, root):
        """Return a sequence of instructions that moves the stack pointer to allocate space for all variables in the current scope."""
        res = []
        st = ""
        def recurse(root, offset):
            if root.typ == "VARIABLE_DECLARATION":
                variable = root.children[0].copy_attributes()
                offset -= 8
                variable["offset"] = offset
                self.symbol_table.insert(variable["identifier"], variable)
            else:
                for child in root.children:
                    offset = recurse(child, offset)
            return offset
        offset = recurse(root, 0)
        # allocate space for variables
        res += instr.add(instr.SP, offset)
        return res

    def compile_function_definition(self, root):
        """Return a sequence of instructions, given a function definition node."""
        res = []
        function = {}
        function["label"] = self.symbol_table.next_label()
        self.symbol_table.insert(root.attributes["identifier"], function)
        self.symbol_table.push_table()
        arguments = root.children[0]
        body = root.children[1]
        ec = Expression_compiler(self.symbol_table)
        sc = Statement_compiler(self.symbol_table)
        continue_label = self.symbol_table.next_label()
        res += instr.jmp(continue_label)
        res += instr.addlabel(function["label"])
        res += instr.push(instr.BP)
        res += instr.mov(instr.BP, instr.SP)
        offset = 0
        #load the arguments
        for argument in arguments.children:
            variable = argument.copy_attributes()
            offset += 8
            variable["offset"] = 8 + offset
            self.symbol_table.insert(variable["identifier"], variable)
        res += sc.compile_statement_list(body)
        res += instr.mov(instr.SP, instr.BP)
        res += instr.pop(instr.BP)
        res += instr.mov(instr.R1, 0) # default return value of 0
        res += instr.ret()
        res += instr.addlabel(continue_label)
        self.symbol_table.pop_table()
        return res

    def compile_function_return(self, root):
        """Return a sequence of instructions, given a return call."""
        res = []
        return_value = root.children[0]
        ec = Expression_compiler(self.symbol_table)
        res += ec.compile_expression(return_value)
        res += instr.pop(instr.R1) # Store the return value in R1
        res += instr.mov(instr.SP, instr.BP)
        res += instr.pop(instr.BP)
        res += instr.ret()
        return res

from .Instructions import Instructions as instr
from .Expression_compiler import Expression_compiler
from .Construct_compiler import Construct_compiler

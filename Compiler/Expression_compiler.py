class Expression_compiler:
    """The Expression_compiler class descends down all expression nodes in the AST and turns them into sequences of assembly instructions.

    Expression nodes are nodes that evaluate to some result. Examples
    of expressions include arithmetic expressions, like (1*2)+(3/4),
    and function calls that return a number."""
 
    STANDALONE_EXPRESSIONS = ["FUNCTION_CALL", "++", "--"]
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table
   
    def compile_expression(self, root):
        """Return a sequence of instructions, given an expression node.
        
        The value corresponding to the expression result is pushed
        onto the stack."""
        res = []
        if root.typ == "CONSTANT":
            if root.attributes["type"] == "int":
                res += self.compile_int(root)
            elif root.attributes["type"] == "bool":
                res += self.compile_boolean(root)
        elif root.typ == "+":
            res += self.compile_add(root)
        elif root.typ == "-":
            res += self.compile_subtract(root)
        elif root.typ == "/":
            res += self.compile_divide(root)
        elif root.typ == "*":
            res += self.compile_multiply(root)
        elif root.typ == "||":
            res += self.compile_or(root)
        elif root.typ == "&&":
            res += self.compile_and(root)
        elif root.typ == "%":
            res += self.compile_modulus(root)
        elif root.typ == "==":
            res += self.compile_relational(root, instr.je)
        elif root.typ == "<":
            res += self.compile_relational(root, instr.jl)
        elif root.typ == ">":
            res += self.compile_relational(root, instr.jg)
        elif root.typ == "<=":
            res += self.compile_relational(root, instr.jle)
        elif root.typ == ">=":
            res += self.compile_relational(root, instr.jge)
        elif root.typ == "!=":
            res += self.compile_relational(root, instr.jne)
        elif root.typ == "++":
            res += self.compile_inc_dec(root, instr.add)
        elif root.typ == "--":
            res += self.compile_inc_dec(root, instr.sub)
        elif root.typ == "FUNCTION_CALL":
            res += self.compile_function_call(root)
        elif root.typ == "VARIABLE":
            variable = root.copy_attributes()
            res += self.load_variable_location(variable)
            res += instr.pop(instr.R2)
            res += instr.mov(instr.R1, instr.memloc(instr.R2))
            res += instr.push(instr.R1)
        return res

    def compile_int(self, root):
        """Return a sequence of instructions, given a constant boolean node.
        
        The resulting value is pushed onto the stack."""
        res = []
        res += instr.mov(instr.R1, root.attributes["val"])
        res += instr.push(instr.R1)
        return res

    def compile_boolean(self, root):
        """Return a sequence of instructions, given a constant boolean node.
        
        The resulting value is pushed onto the stack."""
        res = []
        if root.attributes["val"] == True:
            res += instr.mov(instr.R1, 1)
        else:
            res += instr.mov(instr.R1, 0)
        res += instr.push(instr.R1)
        return res

    def compile_inc_dec(self, root, op):
        """Return a sequence of instructions, given an increment/decrement node.
        
        The resulting value is pushed onto the stack."""
        res = []
        variable = root.children[0].copy_attributes()
        res += self.load_variable_location(variable)
        res += instr.pop(instr.R1)
        res += instr.mov(instr.R2, instr.memloc(instr.R1))
        if not root.attributes["pre"]:
            res += instr.push(instr.R2)
        res += op(instr.R2, 1)
        res += instr.mov(instr.memloc(instr.R1), instr.R2)
        if root.attributes["pre"]:
            res += instr.push(instr.R2)
        return res

    def compile_relational(self, root, op):
        """Return a sequence of instructions, given an relational operator node.
        
        The resulting value is pushed onto the stack."""
        res = []
        res += self.load_operands(root)
        next_label = self.symbol_table.next_label()
        res += instr.mov(instr.R3, 1)
        res += instr.cmp(instr.R1, instr.R2)
        res += op(next_label)
        res += instr.mov(instr.R3, 0)
        res += instr.addlabel(next_label)
        res += instr.push(instr.R3)
        return res


    def load_operands(self, root):
        """Return a sequence of instructions that processes two child expression nodes and then loads the corresponding results into the working registers."""
        res = []
        res += self.compile_expression(root.children[0])
        res += self.compile_expression(root.children[1])
        res += instr.pop(instr.R2)
        res += instr.pop(instr.R1)
        return res

    def compile_divide(self, root):
        """Return a sequence of instructions, given a division node.
        
        The resulting value is pushed onto the stack."""
        res = []
        res += self.load_operands(root)
        res += instr.mov(instr.R3, 0)
        res += instr.div(instr.R2)
        res += instr.push(instr.R1)
        return res

    def compile_modulus(self, root):
        """Return a sequence of instructions, given a modulus node.
        
        The resulting value is pushed onto the stack."""
        res = []
        res += self.load_operands(root)
        res += instr.mov(instr.R3, 0)
        res += instr.div(instr.R2)
        res += instr.push(instr.R3)
        return res

    def compile_multiply(self, root):
        """Return a sequence of instructions, given a multiply node.
        
        The resulting value is pushed onto the stack."""
        res = []
        res += self.load_operands(root)
        res += instr.mov(instr.R3, 0)
        res += instr.mul(instr.R2)
        res += instr.push(instr.R1)
        return res

    def compile_and(self, root):
        """Return a sequence of instructions, given an and node.
        
        The resulting value is pushed onto the stack."""
        res = []
        res += self.load_operands(root)
        res += instr.and_(instr.R1, instr.R2)
        res += instr.push(instr.R1)
        return res

    def compile_or(self, root):
        """Return a sequence of instructions, given an or node.
        
        The resulting value is pushed onto the stack."""
        res = []
        res += self.load_operands(root)
        res += instr.or_(instr.R1, instr.R2)
        res += instr.push(instr.R1)
        return res

    def compile_add(self, root):
        """Return a sequence of instructions, given an addition node.
        
        The resulting value is pushed onto the stack."""
        res = []
        if len(root.children) == 1:
            res += self.compile_expression(root.children[0])
        else:
            res += self.load_operands(root)
            res += instr.add(instr.R1, instr.R2)
            res += instr.push(instr.R1)
        return res

    def compile_subtract(self, root):
        """Return a sequence of instructions, given a subtraction node.
        
        The resulting value is pushed onto the stack."""
        res = []
        if len(root.children) == 1:
            res += self.compile_expression(root.children[0])
            res += instr.pop(instr.R1)
            res += instr.neg(instr.R1)
            res += instr.push(instr.R1)
        else:
            res += self.load_operands(root)
            res += instr.sub(instr.R1, instr.R2)
            res += instr.push(instr.R1)
        return res

    def compile_function_call(self, root):
        """Return a sequence of instructions, given a function call node.
        
        The resulting value is pushed onto the stack."""
        res = []
        res += instr.xor(instr.R1, instr.R1)
        function, depth = self.symbol_table.get(root.attributes["identifier"])
        arguments = root.children[0]
        for arg in reversed(arguments.children):
            res += self.compile_expression(arg)
        res += instr.call(function["label"])
        for arg in arguments.children:
            res += instr.pop(instr.R2)
        res += instr.push(instr.R1) # store result of function
        return res

    def load_variable_location(self, variable):
        """Return a sequence of instructions that pushes the location of a variable in the current scope or in a containing scope onto the stack. """
        res = []
        variable, depth = self.symbol_table.get(variable["identifier"])
        res += instr.mov(instr.R1, instr.BP)
        for k in range(depth):
            res += instr.mov(instr.R1, instr.memloc(instr.R1))
        res += instr.add(instr.R1, variable["offset"])
        res += instr.push(instr.R1)
        return res

from .Instructions import Instructions as instr

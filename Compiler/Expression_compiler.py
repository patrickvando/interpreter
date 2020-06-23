class Expression_compiler:
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table
   
    #compile expression and place onto stack
    def compile_expression(self, root):
        res = []
        if root.typ == "CONSTANT":
            res += instr.mov(instr.R1, root.attributes["val"])
            res += instr.push(instr.R1)
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
        elif root.typ == "FUNCTION_CALL":
            res += self.compile_function_call(root)
        elif root.typ == "VARIABLE":
            res += self.load_variable_location(root)
            res += instr.pop(instr.R2)
            res += instr.mov(instr.R1, instr.memloc(instr.R2))
            res += instr.push(instr.R1)
        return res

    def compile_divide(self, root):
        res = []
        res += self.compile_expression(root.children[0])
        res += self.compile_expression(root.children[1])
        res += instr.mov(instr.R3, 0)
        res += instr.pop(instr.R2)
        res += instr.pop(instr.R1)
        res += instr.div(instr.R2)
        res += instr.push(instr.R1)
        return res

    def compile_modulus(self, root):
        res = []
        res += self.compile_expression(root.children[0])
        res += self.compile_expression(root.children[1])
        res += instr.mov(instr.R3, 0)
        res += instr.pop(instr.R2)
        res += instr.pop(instr.R1)
        res += instr.div(instr.R2)
        res += instr.push(instr.R3)
        return res

    def compile_multiply(self, root):
        res = []
        res += self.compile_expression(root.children[0])
        res += self.compile_expression(root.children[1])
        res += instr.mov(instr.R3, 0)
        res += instr.pop(instr.R2)
        res += instr.pop(instr.R1)
        res += instr.mul(instr.R2)
        res += instr.push(instr.R1)
        return res

    def compile_and(self, root):
        res = []
        res += self.compile_expression(root.children[0])
        res += self.compile_expression(root.children[1])
        res += instr.pop(instr.R2)
        res += instr.pop(instr.R1)
        res += instr.and_(instr.R1, instr.R2)
        res += instr.push(instr.R1)
        return res

    def compile_or(self, root):
        res = []
        res += self.compile_expression(root.children[0])
        res += self.compile_expression(root.children[1])
        res += instr.pop(instr.R2)
        res += instr.pop(instr.R1)
        res += instr.or_(instr.R1, instr.R2)
        res += instr.push(instr.R1)
        return res

    def compile_add(self, root):
        res = []
        if len(root.children) == 1:
            res += self.compile_expression(root.children[0])
        else:
            res += self.compile_expression(root.children[0])
            res += self.compile_expression(root.children[1])
            res += instr.pop(instr.R2)
            res += instr.pop(instr.R1)
            res += instr.add(instr.R1, instr.R2)
            res += instr.push(instr.R1)
        return res

    def compile_subtract(self, root):
        res = []
        if len(root.children) == 1:
            res += self.compile_expression(root.children[0])
            res += instr.pop(instr.R1)
            res += instr.neg(instr.R1)
            res += instr.push(instr.R1)
        else:
            res += self.compile_expression(root.children[0])
            res += self.compile_expression(root.children[1])
            res += instr.pop(instr.R2)
            res += instr.pop(instr.R1)
            res += instr.sub(instr.R1, instr.R2)
            res += instr.push(instr.R1)
        return res

    def compile_function_call(self, root):
        res = []
        res += instr.xor(instr.R1, instr.R1)
        function_name = root.attributes["identifier"]
        arguments = root.children[0]
        for arg in arguments.children:
            res += self.compile_expression(arg)
        res += instr.call(function_name)
        for arg in arguments.children:
            res += instr.pop(instr.R2)
        #store result of function
        res += instr.push(instr.R1)
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

from .Instructions import Instructions as instr

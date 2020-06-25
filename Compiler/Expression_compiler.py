class Expression_compiler:
    STANDALONE_EXPRESSIONS = ["FUNCTION_CALL", "++", "--"]
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table
   
    #compile expression and place onto stack
    def compile_expression(self, root):
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
        res = []
        res += instr.mov(instr.R1, root.attributes["val"])
        res += instr.push(instr.R1)
        return res

    def compile_boolean(self, root):
        res = []
        if root.attributes["val"] == True:
            res += instr.mov(instr.R1, 1)
        else:
            res += instr.mov(instr.R1, 0)
        res += instr.push(instr.R1)
        return res

    def compile_inc_dec(self, root, op):
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


    #loads operands into R1 and R2
    def load_operands(self, root):
        res = []
        res += self.compile_expression(root.children[0])
        res += self.compile_expression(root.children[1])
        res += instr.pop(instr.R2)
        res += instr.pop(instr.R1)
        return res

    def compile_divide(self, root):
        res = []
        res += self.load_operands(root)
        res += instr.mov(instr.R3, 0)
        res += instr.div(instr.R2)
        res += instr.push(instr.R1)
        return res

    def compile_modulus(self, root):
        res = []
        res += self.load_operands(root)
        res += instr.mov(instr.R3, 0)
        res += instr.div(instr.R2)
        res += instr.push(instr.R3)
        return res

    def compile_multiply(self, root):
        res = []
        res += self.load_operands(root)
        res += instr.mov(instr.R3, 0)
        res += instr.mul(instr.R2)
        res += instr.push(instr.R1)
        return res

    def compile_and(self, root):
        res = []
        res += self.load_operands(root)
        res += instr.and_(instr.R1, instr.R2)
        res += instr.push(instr.R1)
        return res

    def compile_or(self, root):
        res = []
        res += self.load_operands(root)
        res += instr.or_(instr.R1, instr.R2)
        res += instr.push(instr.R1)
        return res

    def compile_add(self, root):
        res = []
        if len(root.children) == 1:
            res += self.compile_expression(root.children[0])
        else:
            res += self.load_operands(root)
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
            res += self.load_operands(root)
            res += instr.sub(instr.R1, instr.R2)
            res += instr.push(instr.R1)
        return res

    def compile_function_call(self, root):
        res = []
        res += instr.xor(instr.R1, instr.R1)
        function, depth = self.symbol_table.get(root.attributes["identifier"])
        arguments = root.children[0]
        for arg in reversed(arguments.children):
            res += self.compile_expression(arg)
        res += instr.call(function["label"])
        for arg in arguments.children:
            res += instr.pop(instr.R2)
        #store result of function
        res += instr.push(instr.R1)
        return res

    #pushes the memory location of the variable onto the stack
    def load_variable_location(self, variable):
        res = []
        variable, depth = self.symbol_table.get(variable["identifier"])
        #assume depth 0 right now
        res += instr.mov(instr.R1, instr.BP)
        for k in range(depth):
            res += instr.mov(instr.R1, instr.memloc(instr.R1))
        res += instr.add(instr.R1, variable["offset"])
        res += instr.push(instr.R1)
        return res

from .Instructions import Instructions as instr

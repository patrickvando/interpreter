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
        return res

    def compile_add(self, root):
        res = []
        if len(root.children) == 1:
            res += self.compile_expression(root.children[0])
        else:
            res += self.compile_expression(root.children[0])
            res += self.compile_expression(root.children[1])
            res += instr.pop(instr.R1)
            res += instr.pop(instr.R2)
            res += instr.add(instr.R1, instr.R2)
            res += instr.push(instr.R1)
        return res

    def compile_sub(self, root):
        res = []
        if len(root.children) == 1:
            res += self.compile_expression(root.children[0])
            res += instr.pop(instr.R1)
            res += instr.neg(instr.R1)
            res += instr.push(instr.R1)
        else:
            res += self.compile_expression(root.children[0])
            res += self.compile_expression(root.children[1])
            res += instr.pop(instr.R1)
            res += instr.pop(instr.R2)
            res += instr.sub(instr.R1, instr.R2)
            res += instr.push(instr.R1)
        return res

    def print(self, root):
        pass

from .Instructions import Instructions as instr

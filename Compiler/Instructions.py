class Instructions:
    R1 = "rax"
    R2 = "rcx"
    R3 = "rdx"
    ARG1 = "rdi"
    SP = "rsp"
    BP = "rbp"
    HEADER = ["extern printf",
"section .data",
'fmt:    db "%d", 10, 0',
"section .text",
"global main",
"main:",]
    FOOTER = ["ret"]

    def xor(a, b):
        return ["xor " + str(a) + ", " + str(b)]

    def call(a):
        return ["call " + str(a)]

    def jmp(a):
        return ["jmp " + str(a)]

    def sub(a, b):
        return ["sub " + str(a) + ", " + str(b)]

    def neg(a):
        return ["neg " + str(a)]

    def add(a, b):
        return ["add " + str(a) + ", " + str(b)]

    def div(a):
        return ["div " + str(a)]

    def and_(a, b):
        return ["and " + str(a) + ", " + str(b)]

    def or_(a, b):
        return ["or " + str(a) + ", " + str(b)]

    def mul(a):
        return ["mul " + str(a)]

    def push(a):
        return ["push " + str(a)]

    def pop(a):
        return ["pop " + str(a)]

    def mov(a, b):
        return ["mov " + str(a) + ", " + str(b)]

    def memloc(a, offset=None):
        a = str(a)
        if offset:
            if offset < 0:
                return "[" + a + str(offset) + "]"
            return "[" + a + "+" + str(offset) + "]"
        return  "[" + a + "]"

    def addlabel(a):
        return [str(a) + ":"]

    def je(a):
        return ["je " + str(a)]

    def jne(a):
        return ["jne " + str(a)]

    def jg(a):
        return ["jg " + str(a)]

    def jge(a):
        return ["jge " + str(a)]

    def jl(a):
        return ["jl " + str(a)]

    def jle(a):
        return ["jle  " + str(a)]

    def cmp(a, b):
        return ["cmp " + str(a) + ", " + str(b)]

    def jmp(a):
        return ["jmp " + str(a)]

    def define_print():
        res = ["""print:
push rbp
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
        return res
    

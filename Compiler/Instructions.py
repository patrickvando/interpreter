class Instructions:
    R1 = "rax"
    R2 = "rcx"
    SP = "rsp"
    BP = "rbp"
    HEADER = ["extern printf",
"section .data",
'fmt:    db "%u", 10, 0',
"section .text",
"global main",
"main:",]
    FOOTER = ["ret"]
    def sub(a, b):
        return ["sub " + str(a) + ", " + str(b)]

    def neg(a):
        return ["neg " + str(a)]

    def add(a, b):
        return ["add " + str(a) + ", " + str(b)]

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

class Built_ins:
    funcs = ["print"]

    def execute_func(func_name, args):
        if func_name == "print":
            Built_ins.print_func(args)

    def print_func(args):
        st = ""
        for arg in args:
            st += str(arg) + ","
        print(st[:-1])

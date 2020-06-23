class Symbol_table:
    def __init__(self):
        self.table = {}

    def update(self, key, value):
        self.table[key] = value

    def get(self, key):
        if key in self.table:
            return self.table[key]
        else:
            return None

    def __str__(self):
        res = ""
        for key in self.table:
            res += "{}: {}\n".format(key, self.table[key])
        return res

class Symbol_table_stack:
    def __init__(self):
        self.stack = []
        self.push_table()

    def push_table(self):
        self.stack.append(Symbol_table())

    def pop_table(self):
        self.stack.pop()

    def get(self, key):
        for k in reversed(range(len(self.stack))):
            res = self.stack[k].get(key)
            if res:
                return res, k
        return None

    def insert(self, key, value):
        self.stack[-1].update(key, value)

    def __str__(self):
        res = ""
        for k in reversed(range(len(self.stack))):
            res += "Symbol Table #{}\n".format(k)
            res += str(self.stack[k])
        return res

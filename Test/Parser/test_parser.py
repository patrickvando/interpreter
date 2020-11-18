import unittest
from Common.Common import *
from Lexer.Lexer import Lexer
from Parser.StatementParser import StatementParser

class TestParser(unittest.TestCase):
    def setUp(self):
        self.lex = Lexer("Test/Examples/gcd.oats")
        self.sparser = StatementParser(self.lex)
        self.expected_nodes = [Node(Node.STATEMENT_LIST_TYPE),
                Node(Node.FUNC_DEF_TYPE, "gcd"),
                Node(Node.PARAMETER_LIST_TYPE),
                Node(Node.VARIABLE_TYPE, "x"),
                Node(Node.VARIABLE_TYPE, "y"),
                Node(Node.STATEMENT_LIST_TYPE),
                Node(Node.IF_TYPE),
                Node(Node.LT_TYPE),
                Node(Node.VARIABLE_TYPE, "x"),
                Node(Node.VARIABLE_TYPE, "y"),
                Node(Node.STATEMENT_LIST_TYPE),
                Node(Node.ASSIGN_TYPE),
                ]

    def tearDown(self):
        self.lex.f.close()

    def testParser(self):
        """Verify the correctness of the Abstract Syntax Tree produced by the Parser for the "gcd.oats" test file."""
        root = self.sparser.parse_main()
        stack = [root]
        for expected_node in self.expected_nodes:
            current = stack.pop()
            self.assertEqual(current.type_, expected_node.type_)
            self.assertEqual(current.value, expected_node.value)
            for child in reversed(current.children):
                stack.append(child)

if __name__ == '__main__':
    unittest.main()

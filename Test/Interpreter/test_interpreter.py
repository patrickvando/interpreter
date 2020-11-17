import unittest
from Common.Common import *
from Lexer.Lexer import Lexer
from Parser.StatementParser import StatementParser
from Interpreter.StatementInterpreter import StatementInterpreter
from Interpreter.ExpressionInterpreter import ExpressionInterpreter
from unittest.mock import patch
from io import StringIO

class TestInterpreterMethods(unittest.TestCase):
    def setUp(self):
        lex = Lexer("Test/Examples/fibonnaci.oats")
        sparser = StatementParser(lex)
        self.root = sparser.parse_main()
        lex.f.close()
        sym_tab = [dict()]
        self.sinterpreter = StatementInterpreter(sym_tab)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', return_value="10")
    def testInterpretStatementList(self, mock_input, mock_output):
        self.sinterpreter.interpret_statement_list(self.root)
        self.assertEqual(mock_output.getvalue(), "55\n")

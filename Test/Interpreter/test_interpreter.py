import unittest
from Common.Common import *
from Lexer.Lexer import Lexer
from Parser.StatementParser import StatementParser
from Interpreter.StatementInterpreter import StatementInterpreter
from Interpreter.ExpressionInterpreter import ExpressionInterpreter
from unittest.mock import patch
from io import StringIO

class TestInterpreter(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input')
    def testInterpreterFib(self, mock_input, mock_output):
        """Verify the correctness of the fibonnaci.oats program (The 20th fibonnaci number is 6765)."""
        mock_input.side_effect = ["20"]
        lex = Lexer("Test/Examples/fibonnaci.oats")
        sparser = StatementParser(lex)
        root = sparser.parse_main()
        sym_tab = [dict()]
        sinterpreter = StatementInterpreter(sym_tab)
        sinterpreter.interpret_statement_list(root)
        self.assertEqual(mock_output.getvalue(), "6765\n")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input')
    def testInterpreterGCD(self, mock_input, mock_output):
        """Verify the correctness of the gcd.oats program (The gcd of 1071 and 462 is 21)."""
        mock_input.side_effect = ["1071", "462"]
        lex = Lexer("Test/Examples/gcd.oats")
        sparser = StatementParser(lex)
        root = sparser.parse_main()
        sym_tab = [dict()]
        sinterpreter = StatementInterpreter(sym_tab)
        sinterpreter.interpret_statement_list(root)
        self.assertEqual(mock_output.getvalue(), "21\n")
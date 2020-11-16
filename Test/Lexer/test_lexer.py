import unittest
from Common.Common import *
from Lexer.Lexer import Lexer

class TestLexerMethods(unittest.TestCase):
    def setUp(self):
        self.lex = Lexer("Test/Examples/gcd.oats")
        self.expected_tokens = [
                Token("special", "func", 1),
                Token("word", "gcd", 1),
                Token("special", "(", 1),
                Token("word", "x", 1), Token("special", ",", 1), Token("word", "y", 1), Token("special", ")", 1), Token("special", "{", 1),
                ]

    def tearDown(self):
        self.lex.f.close()

    def test_next_token(self):
        ct = self.lex.next_token()
        def checkEquivalent(token1, token2):
            self.assertEqual(token1.type_, token2.type_)
            self.assertEqual(token1.lexeme, token2.lexeme)
        for k in range(len(self.expected_tokens)):
            checkEquivalent(self.expected_tokens[k], ct)
            ct = self.lex.next_token()

    def test_prev_token(self):
        ct = self.lex.next_token()
        def checkEquivalent(token1, token2):
            self.assertEqual(token1.type_, token2.type_)
            self.assertEqual(token1.lexeme, token2.lexeme)
        for k in range(len(self.expected_tokens)):
            ct = self.lex.next_token()
        for k in reversed(range(len(self.expected_tokens))):
            ct = self.lex.prev_token()
            checkEquivalent(self.expected_tokens[k], ct)


if __name__ == '__main__':
    unittest.main()

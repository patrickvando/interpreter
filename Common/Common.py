import re

def check_valid_name(token):
    if token in RESERVED_WORDS:
        illegal_token(token, "This is a reserved word.")

def illegal_token(token, error_message):
    exit('Illegal token "{}" on line {}.\n{}'.format(token.lexeme, token.line_num, error_message))

def match_lexeme(lex, expected_lexeme):
    ct = lex.current_token()
    if ct.lexeme != expected_lexeme:
        exit('Unexpected token "{}" on line {}.\nExpected token "{}"'.format(ct.lexeme, ct.line_num, expected_lexeme))
    lex.next_token()

FUNC_LEXEME, WHILE_LEXEME, FOR_LEXEME, IF_LEXEME, ELSE_LEXEME, ELSEIF_LEXEME, RETURN_LEXEME, PRINT_LEXEME, GET_LEXEME = "func", "while", "for", "if", "else", "elseif", "return", "print", "get"
RESERVED_WORDS = [FUNC_LEXEME, WHILE_LEXEME, FOR_LEXEME, IF_LEXEME, ELSE_LEXEME, ELSEIF_LEXEME, RETURN_LEXEME, PRINT_LEXEME, GET_LEXEME]
CONSTRUCT_LEXEMES = [FUNC_LEXEME, WHILE_LEXEME, FOR_LEXEME, RETURN_LEXEME, IF_LEXEME]

LT_LEXEME, LTE_LEXEME, GT_LEXEME, GTE_LEXEME, EQ_LEXEME, NEQ_LEXEME = "<", "<=", ">", ">=", "==", "!="
EXP_LEXEMES = [LT_LEXEME, LTE_LEXEME, GT_LEXEME, GTE_LEXEME, EQ_LEXEME, NEQ_LEXEME]

ADD_LEXEME, SUB_LEXEME, OR_LEXEME = "+", "-", "or"
SIMPLE_EXP_LEXEMES = [ADD_LEXEME, SUB_LEXEME, OR_LEXEME]

MULT_LEXEME, DIV_LEXEME, MOD_LEXEME, AND_LEXEME = "*", "/", "%", "and"
TERM_LEXEMES = [MULT_LEXEME, DIV_LEXEME, MOD_LEXEME, AND_LEXEME]

NOT_LEXEME, NEG_LEXEME = "!", "-"
FACTOR_LEXEMES = [NOT_LEXEME, NEG_LEXEME]
class Token:
    NUMBER_TYPE, NUMBER_PATTERN = "number", "[0-9]+"
    SPECIAL_TYPE, SPECIAL_PATTERN = "special", "|".join(
            [re.escape(sp) for sp in
                ["++", "--", "==", "<=", ">=", "!=", "<", ">", "=",
                    "!", "+", "-", "*", "/", "%", "}", "{", "]", "[", ")",
                    "(", ";", ","]])
    WORD_TYPE, WORD_PATTERN = "word", "[a-zA-Z][a-zA-Z0-9_]*"
    END_TYPE = "END"
    def __init__(self, type_, lexeme, line_num):
        self.type_ = type_
        self.lexeme = lexeme
        self.line_num = line_num

class Node:
    VARIABLE_TYPE, NUMBER_TYPE, STATEMENT_LIST_TYPE, ASSIGNMENT_TYPE, FUNC_CALL_TYPE, FUNC_DEF_TYPE, RETURN_TYPE, WHILE_TYPE, FOR_TYPE, IF_TYPE, ELSEIF_TYPE, PRINT_TYPE, GET_TYPE = "variable", "number", "statement_list", "assignment", "func_call", "func_def", "return", "while", "for", "if", "elseif", "print", "get";

    LT_TYPE, LTE_TYPE, GT_TYPE, GTE_TYPE, EQ_TYPE, NEQ_TYPE = "LT", "LTE", "GT", "GTE", "EQ", "NEQ"
    EXP_TYPES = [LT_TYPE, LTE_TYPE, GT_TYPE, GTE_TYPE, EQ_TYPE, NEQ_TYPE]

    ADD_TYPE, SUB_TYPE, OR_TYPE = "ADD", "SUB", "OR"
    SIMPLE_EXP_TYPES = [ADD_TYPE, SUB_TYPE, OR_TYPE]

    MULT_TYPE, DIV_TYPE, MOD_TYPE, AND_TYPE = "MULT", "DIV", "MOD", "AND" 
    TERM_TYPES = [MULT_TYPE, DIV_TYPE, MOD_TYPE, AND_TYPE]

    NOT_TYPE, NEG_TYPE = "NOT", "NEG"
    FACTOR_TYPES = [NOT_TYPE, NEG_TYPE]
    
    LEXEME_TO_TYPE = dict(zip(EXP_LEXEMES + SIMPLE_EXP_LEXEMES + FACTOR_LEXEMES + TERM_LEXEMES, EXP_TYPES + SIMPLE_EXP_TYPES + FACTOR_TYPES + TERM_TYPES))

    def __init__(self, type_, value=None, token=None):
        self.type_ = type_
        self.value = value
        self.token = token
        self.children = []

    def __str__(self):
        def recurse(current, level):
            st = "\t"*level + "Type: {} Value: {}\n".format(current.type_, current.value)
            for child in current.children:
                st += recurse(child, level + 1)
            return st       
        return recurse(self, 0)



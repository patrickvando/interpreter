import re

class Lexeme:
    FUNC, WHILE, FOR, IF, ELSE, ELSEIF, RETURN, PRINT, GET = "func", "while", "for", "if", "else", "elseif", "return", "print", "get"
    RESERVED = [FUNC, WHILE, FOR, IF, ELSE, ELSEIF, RETURN, PRINT, GET]
    CONSTRUCTS = [FUNC, WHILE, FOR, RETURN, IF]
    
    LT, LTE, GT, GTE, EQ, NEQ = "<", "<=", ">", ">=", "==", "!="
    EXPS = [LT, LTE, GT, GTE, EQ, NEQ]
    
    ADD, SUB, OR = "+", "-", "or"
    SIMPLE_EXPS = [ADD, SUB, OR]
    
    MULT, DIV, MOD, AND = "*", "/", "%", "and"
    TERMS = [MULT, DIV, MOD, AND]
    
    NOT = "!"
    FACTORS = [NOT]

    OPEN_BRACE, CLOSE_BRACE, OPEN_PAREN, CLOSE_PAREN, OPEN_BRACKET, CLOSE_BRACKET, SEMICOLON, COMMA, EQUALS = "{", "}", "(", ")", "[", "]", ";", ",", "="
    DELIMS = [OPEN_BRACE, CLOSE_BRACE, OPEN_PAREN, CLOSE_PAREN, OPEN_BRACKET, CLOSE_BRACKET, SEMICOLON, COMMA, EQUALS]

class Token:
    NUMBER_TYPE, NUMBER_PATTERN = "number", "[0-9]+"
    """
    SPECIAL_TYPE, SPECIAL_PATTERN = "special", "|".join(
            [re.escape(sp) for sp in
                ["++", "--", "==", "<=", ">=", "!=", "<", ">", "=",
                    "!", "+", "-", "*", "/", "%", "}", "{", "]", "[", ")",
                    "(", ";", ","]])
    """
    SPECIAL_TYPE, SPECIAL_PATTERN = "special", "|".join(
            [re.escape(sp) for sp in
                Lexeme.EXPS + Lexeme.SIMPLE_EXPS + Lexeme.TERMS + Lexeme.FACTORS + Lexeme.DELIMS])

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

    NOT_TYPE  = "NOT" 
    FACTOR_TYPES = [NOT_TYPE]
    
    LEXEME_TO_TYPE = dict(zip(Lexeme.EXPS + Lexeme.SIMPLE_EXPS + Lexeme.FACTORS + Lexeme.TERMS, EXP_TYPES + SIMPLE_EXP_TYPES + FACTOR_TYPES + TERM_TYPES))

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

def check_valid_name(token):
    if token in Lexeme.RESERVED:
        illegal_token(token, "This is a reserved word.")

def illegal_token(token, error_message):
    exit('Illegal token "{}" on line {}.\n{}'.format(token.lexeme, token.line_num, error_message))

def illegal_statement(token):
    exit('Illegal statement on line {}.'.format(token.line_num))

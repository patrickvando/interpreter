FUNC_LEXEME, WHILE_LEXEME, FOR_LEXEME, IF_LEXEME, ELSE_LEXEME, ELSEIF_LEXEME, RETURN_LEXEME, PRINT_LEXEME, GET_LEXEME = "func", "while", "for", "if", "else", "elseif", "return", "print", "get"
RESERVED_WORDS = [FUNC_LEXEME, WHILE_LEXEME, FOR_LEXEME, IF_LEXEME, ELSE_LEXEME, ELSEIF_LEXEME, RETURN_LEXEME, PRINT_LEXEME, GET_LEXEME]
CONSTRUCT_LEXEMES = [FUNC_LEXEME, WHILE_LEXEME, FOR_LEXEME, RETURN_LEXEME, IF_LEXEME]

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

class Node:
    VARIABLE_TYPE, NUMBER_TYPE, STATEMENT_LIST_TYPE, ASSIGNMENT_TYPE, FUNC_CALL_TYPE, FUNC_DEF_TYPE, RETURN_TYPE, WHILE_TYPE, FOR_TYPE, IF_TYPE, ELSEIF_TYPE, PRINT_TYPE, GET_TYPE = "variable", "number", "statement_list", "assignment", "func_call", "func_def", "return", "while", "for", "if", "elseif", "print", "get";
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


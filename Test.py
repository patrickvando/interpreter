from Lexer.Buffer import Buffer
from Lexer.Lexer import Lexer
from Parser.Parser import Parser

def testBuffer():
    print("Testing Buffer")
    buf = Buffer("empty.toy")

    c = buf.go_forward()
    while c != "":
        print("c: " + c)
        c = buf.go_forward()
    
    c = buf.go_backward()
    while c != "":
        print("c: " + c)
        c = buf.go_backward()
    print("Done testing Buffer")

def testLexer():
    print("Testing Lexer")
    lex = Lexer("example.toy")
    token = lex.next_token()
    while token.kind != "END":
        token = lex.next_token()
        lex.print_token(token)
        print(token.kind)
    print("Done testing Lexer")

def testParser():
    print("Testing Parser")
    lex  = Lexer("simple.toy")
    parser = Parser(lex)
    parser.parse()
    print("Done testing Parser")

testParser()

# NRJ Compiler

## About

This is a compiler for the [NRJ language (a made-up language)](#NRJ-Language-Specifications). NRJ supports recursive functions, for/while/if-elseif constructs, and integer arithmetic. Well-formed NRJ file goes into the compiler, 64-bit assembly code comes out. 

To compile `filename.nrj` into `filename.asm`, use:  `python nrj_compiler.py filename.nrj`

To run `filename.asm`, use:  `run filename`

See the file `gcd.nrj` for an example implementation of the Euclidean Algorithm.

See the file `fib.nrj` for an example implementation of a Fibonnaci number generator.

See the file `isprime.nrj` for an example implementation of a prime number checker. 

## Dependencies

- Python
- NASM 
- GCC

The compiler is written in Python. NASM is used to compile the `.asm` file output by the compiler into a `.o` file, GCC is used to turn the `.o` file into an executable. 

## Background

This was a learning project for me. I learned a lot about compilers and assembly. I also learned about managing complexity in a project that is larger/more complex than I was used to as a student. Compilers are fascinating and I have still have much to learn. 

This compiler has three stages:

- Lexer stage turns source `.nrj` file into a sequence of tokens (tokens for symbols, tokens for numbers, token for 'words')
- Parser stage turns sequence of tokens into an Abstract Syntax Tree (intermediate representation of source code)
- Compiler stage travels through the AST and turns it into NASM instructions that are written to the `.asm` file

## Features

placeholder

## NRJ Language Specifications

placeholder

## Why?

## Implemented Features

## Planned Features


## NRJ Language Specification

## Overview

I am writing this project for the sake of learning more about compilers. Currently this project is a simple interpreter written in Python that interprets the made-up ".simple" language. This is an ongoing project, and I plan to further develop it into a full compiler. 

Right now, the interpreter supports functions, integer/boolean operations, and if-else/while/for constructs. The included example file `gcd.simple` is a recursive implementation of the Euclidean Algorithm in the ".simple" language that demonstrates some of these capabilites.

For further details on what features have and have not been implemented in the interpreter, see the *Current State* section. For details on the language specifications of the ".simple" language, see the *".simple" Language Specifications* section.

## Current State

Right now, the interpreter consists of a three stage process (each with a corresponding directory in the project): the lexical analysis stage (Lexer), the semantic analysis stage (Parser) and the interpreter stage (Interpreter). 

The lexical analysis stage breaks the source text file into "symbol", "number", or "word" tokens. Further division of the "word" tokens into keywords (like "int") and identifiers ("myvar") is left to the semantic analysis stage. String support has yet to be implemented.

The semantic analysis stage uses a top-down recursive-descent parser to fit the various tokens into the ".simple" language grammar. The various tokens are assembled into "statements" (variable declarations, function declarations, etc), "expressions" (+, ||, function calls, etc) or "constructs" (if-else, while, for). These statements, expressions, and constructs are then represented in an intermediate parse tree. Type checking and error recovery (both very important parts of a compiler/interpreter) have yet to be implemented. 

The interpreter stage evaluates the parse tree recursively. Arithmetic/boolean operations are represented in the parse tree with a node for the operand and the children as operators, so evaluating them is straightforward. Evaluating variable and function declarations involves evaluating an expression and attaching the result to an identifier that is then added to the the "symbol table" at the top of the "stack". Calling a function involves pushing a new "symbol table" onto the stack, which is popped when the function has ended or a return statement has executed. Constructs like "for" involve executing statements and evaluating an expression to determine whether or not the statements in the "body" of the construct should be executed. 

## ".simple" Language Specifications

### Supported Operators

#### Binary Operators

| Operator   | Symbol   |
| ---------- | :------: |
| Add        | +        |
| Subtract   | -        |
| Multiply   | *        |
| Divide     | /        |
| Modulus    | %        |
| Or         | ||       |
| And        | &&       |
| EQ         | ==       |
| NE         | !=       |
| LT         | <        |
| GT         | >        |
| LTE        | <=       |
| GTE        | >=       | 

#### Unary Operators

| Operator               | Symbol     |
| ---------------------- | :--------: |
| Negate Variable        | -var       |
| Positive Variable      | +var       |
| Preincrement Variable  | ++var      |
| Predecrement Variable  | --var      |
| Postincrement Variable | var++      |
| Postdecrement Variable | var--      |

### Variable Declarations

Variable declarations take the following form:

`type identifier = expression;`

For example, 

`int x = 1 * (2 + 3);`

### Function Declarations

Functions declarations take the following form:

```
type identifier ( type arg1, type arg2, type arg3) {<br/>
    *body*
}
```

For example:

```
int fib(int num) {
    if ((num == 1) || (num == 2)){
        return 1;
    } else {
        return fib(num - 1) + fib(num - 2);
    }
}
```

### Function Calls

Function Calls take the following form:

`identifier(arg1, arg2, ...);`

For example:

`fib(9);`

### Constructs

#### If-Elseif-Else

*if-elseif-else* constructs take the following form:

```
if (expression) {
    *body*
} elseif (expression) {
    *body*
} else {
    *body*
}
```

For example,

```
int x = 1;
if ( x == 1) {
    print(1);
} elseif (x == 2) {
    print(2);
} else {
    print(3);
}
```

#### While

*while* constructs take the following form:

```
while (expression) {
    *body*
}
```

For example,
```
int x = 1;
while (x < 1){
    x++;
}
```

#### For

*for* constructs take the following form:

```
for (statement; expression; statement) {
    *body*
}
```

For example,
```
int total = 0;
for(int k = 0; k < 10; k++){
    total += k; 
}
```


### Built-Ins

The ".simple" interpreter supports a *print* function that can be used for simple output.

The *print* function takes the following form:

```
print(arg1, arg2, ...);
```

For example,
```
int a = 1;
int b = 2;
int c = 3;
print(a, b, c);
```

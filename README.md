# NRJ Compiler

## About

This is a compiler for the [NRJ language (a made-up Java-like language)](#NRJ-Language-Specifications). NRJ supports recursive functions, for/while/if-elseif constructs, and integer arithmetic. Well-formed NRJ file goes into the compiler, 64-bit assembly code comes out. 

To compile `filename.nrj` into `filename.asm`, use:  `python nrj_compiler.py filename.nrj`

To run `filename.asm`, use:  `. run filename`

See the file `gcd.nrj` for an example implementation of the Euclidean Algorithm.

See the file `fib.nrj` for an example implementation of a Fibonnaci number generator.

See the file `isprime.nrj` for an example implementation of a prime number checker. 

## Background

This was a learning project for me. I learned a lot about compilers and assembly. I also learned about managing complexity in a larger personal project. Compilers are fascinating and I have still have much to learn. I plan to continue on expanding the features available in this compiler.

## Dependencies

- Python
- NASM 
- GCC

The compiler is written in Python. NASM is used to compile the `.asm` file output by the compiler into a `.o` file, GCC is used to turn the `.o` file into an executable. 

## How it Works

This compiler has three stages:

- Lexer stage turns source `.nrj` file into a sequence of tokens (tokens for symbols, tokens for numbers, token for 'words')
- Parser stage turns sequence of tokens into an Abstract Syntax Tree (intermediate representation of source code)
- Compiler stage travels through the AST and turns it into NASM instructions that are written to a `.asm` file

## Features

| Implemented Features |
| -------------------- |
| Integer arithmetic |
| If-elseif-else branching |
| While loops |
| For loops |
| Functions |
| Recursion |

## NRJ Language Specifications

### Supported Operators

#### Binary Operators

| Operator   | Symbol   |
| ---------- | :------: |
| Add        | +        |
| Subtract   | -        |
| Multiply   | *        |
| Divide     | /        |
| Modulus    | %        |
| Or         | \|\|       |
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
    total = total + k; 
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

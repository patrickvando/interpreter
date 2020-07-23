# NRJ Compiler

## What does it do?

I made up a programming language that I call NRJ.

This is a compiler that turns NRJ into assembly.

Here is an example. The compiler takes in `gcd.nrj`, and spits out `gcd.asm`.

<table>
<tr>
<th>
gcd.nrj
</th>
<th>
gcd.asm
</th>
</tr>
<tr>
<td style="vertical-align: top;">
<pre>
int a = 1071;
int b = 462;
int gcd(int a, int b){
    if (a > b){
        int c = a;
        a = b;
        b = c;
    }
    if (b % a == 0){
        return a;
    } else {
        return gcd(b % a, a);
    }
}
int greatest_common_divisor = gcd(a, b);
print(greatest_common_divisor);
</pre>
</td>
<td>
<pre>
extern printf
section .data
fmt:    db "%d", 10, 0
section .text
global main
main:
jmp __2
__1:
push rbp
mov rbp, rsp
push rax
push rcx
mov rdi,fmt
mov rsi, [rbp + 16]
xor rax, rax
call printf
pop rcx
pop rax
pop rbp
ret
__2:
push rbp
mov rbp, rsp
add rsp, -32
mov rax, rbp
add rax, -8
push rax
mov rax, 1071
push rax
pop rcx
pop rax
mov [rax], rcx
mov rax, rbp
add rax, -16
push rax
mov rax, 462
push rax
pop rcx
pop rax
mov [rax], rcx
jmp __4
__3:
push rbp
mov rbp, rsp
add rsp, -8
mov rax, rbp
add rax, 16
push rax
pop rcx
mov rax, [rcx]
push rax
mov rax, rbp
add rax, 24
push rax
pop rcx
mov rax, [rcx]
push rax
pop rcx
pop rax
mov rdx, 1
cmp rax, rcx
jg __7
mov rdx, 0
__7:
push rdx
pop rax
mov rcx, 1
cmp rax, rcx
jne __6
add rsp, -8
mov rax, rbp
add rax, -8
push rax
mov rax, rbp
add rax, 16
push rax
pop rcx
mov rax, [rcx]
push rax
pop rcx
pop rax
mov [rax], rcx
mov rax, rbp
add rax, 16
push rax
mov rax, rbp
add rax, 24
push rax
pop rcx
mov rax, [rcx]
push rax
pop rcx
pop rax
mov [rax], rcx
mov rax, rbp
add rax, 24
push rax
mov rax, rbp
add rax, -8
push rax
pop rcx
mov rax, [rcx]
push rax
pop rcx
pop rax
mov [rax], rcx
jmp __5
__6:
__5:
mov rax, rbp
add rax, 24
push rax
pop rcx
mov rax, [rcx]
push rax
mov rax, rbp
add rax, 16
push rax
pop rcx
mov rax, [rcx]
push rax
pop rcx
pop rax
mov rdx, 0
div rcx
push rdx
mov rax, 0
push rax
pop rcx
pop rax
mov rdx, 1
cmp rax, rcx
je __11
mov rdx, 0
__11:
push rdx
pop rax
mov rcx, 1
cmp rax, rcx
jne __10
add rsp, 0
mov rax, rbp
add rax, 16
push rax
pop rcx
mov rax, [rcx]
push rax
pop rax
mov rsp, rbp
pop rbp
ret
jmp __9
__10:
mov rax, 1
push rax
pop rax
mov rcx, 1
cmp rax, rcx
jne __12
add rsp, 0
xor rax, rax
mov rax, rbp
add rax, 16
push rax
pop rcx
mov rax, [rcx]
push rax
mov rax, rbp
add rax, 24
push rax
pop rcx
mov rax, [rcx]
push rax
mov rax, rbp
add rax, 16
push rax
pop rcx
mov rax, [rcx]
push rax
pop rcx
pop rax
mov rdx, 0
div rcx
push rdx
call __3
pop rcx
pop rcx
push rax
pop rax
mov rsp, rbp
pop rbp
ret
jmp __9
__12:
__9:
mov rsp, rbp
pop rbp
mov rax, 0
ret
__4:
mov rax, rbp
add rax, -32
push rax
xor rax, rax
mov rax, rbp
add rax, -16
push rax
pop rcx
mov rax, [rcx]
push rax
mov rax, rbp
add rax, -8
push rax
pop rcx
mov rax, [rcx]
push rax
call __3
pop rcx
pop rcx
push rax
pop rcx
pop rax
mov [rax], rcx
xor rax, rax
mov rax, rbp
add rax, -32
push rax
pop rcx
mov rax, [rcx]
push rax
call __1
pop rcx
push rax
mov rsp, rbp
pop rbp
ret

</pre>
</td>
</tr>
</table>

## About

This is a compiler for the [NRJ language (a made-up Java-like language)](#NRJ-Language-Specifications). NRJ supports recursive functions, for/while/if-elseif constructs, and integer arithmetic. Well-formed NRJ file goes into the compiler, 64-bit assembly code comes out. 

To compile `filename.nrj` into `filename.asm`, use:  `python nrj_compiler.py filename.nrj`

To run `filename.asm`, use:  `. run filename`

See the file `Examples/gcd.nrj` for an example implementation of the Euclidean Algorithm in NRJ.

See the file `Examples/fib.nrj` for an example implementation of a Fibonnaci number generator in NRJ.

See the file `Examples/isprime.nrj` for an example implementation of a prime number checker in NRJ.

## Background

This was a learning project for me. My goal was to make a compiler capable of turning a traditionally structured high level language into low level assembly. I learned a lot about compilers and assembly in the process of making this project, but it remains very bare-bones in terms of functionality. Recursive functions, loops, and integer operations are enough to make a number of fun programs (see the included examples) - but of course any complete compiler would also include support for strings, doubles, arrays, classes (and more).  

There are also still many areas of compiler design that I am continuing to learn about; error recovery, type-checking, and instruction/register optimization are all interesting and important areas of compiler design that this project does not address in its current implementation. I hope to continue learning about compilers and expanding this project!

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

This NRJ compiler supports a *print* function that can be used for simple output.

The *print* function takes the following form:

```
print(arg1);
```

For example,
```
int a = 1;
print(a);
```

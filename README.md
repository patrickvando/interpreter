
# NRJ Compiler

## What does it do?

I made up a programming language and named it "NRJ". The syntax of NRJ is very similar to that of Java.
This project is a compiler that translates NRJ source code into assembly code.

Let's look at an example. `gcd.nrj` is an NRJ file that calculates the greatest common divisor of 1071 and 462 using the Euclidean Algorithm.

If the compiler takes `gcd.nrj` as input, it will output`gcd.asm`. Then when `gcd.asm` is run, the answer (21) will be printed to the std out.


<table>
    <tr>
        <th>gcd.nrj</th>
        <th>gcd.asm</th>
    </tr>
    <tr>
        <td>
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
<!--I couldn't think of a better way to format this table :( please read in markdown-->
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
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

Currently this compiler does not perform any optimization on the code that it generates. As a result, the generated `nrj.asm` code is lengthy and inefficient; there are lots of consecutive `push` and `pop` operations on the same registers, intermediates are saved on the stack instead of being left in registers, etc. 

An equivalent hand-written assembly file that implements the Euclidean Algorithm might look like this:

<table>
    <tr>
        <th>handwritten_gcd.asm</th>
    </tr>
    <tr>
        <td>
<pre>
        extern  printf
        section .data
a:      dd  1071
b:      dd  462
fmt:    db "%d", 10, 0 
        section .text
        global main
main:               
    mov eax, [b]
    cmp eax, [a]
    jg noswap
    mov eax, [a]
    mov ecx, [b]
    jmp gcd
noswap:
    mov ecx, [a]
gcd:
    xor edx, edx
    div ecx
    cmp edx, 0
    je print
    mov eax, ecx
    mov ecx, edx
    jmp gcd
print:
    mov rdi,fmt
    movsx rcx, ecx
    mov rsi, rcx
    xor rax, rax
    call    printf
</pre>
        </td>
    </tr>
</table>

As you can see, there's a big gap between the `gcd.asm` file automatically generated by the compiler and the hand coded `handwritten_gcd.asm` file.

## Why
I made this project because I wanted to learn more about compilers. I had fun learning about how to take a high level source language through the various stages of a compiler (tokenizing the source file; parsing the tokens into an abstract syntax tree; translating the AST into assembly). I also had fun learning about how aspects of coding languages like loops, functions, and recursion are implemented on the assembly level.

There are a number of features that this compiler lacks that would be present in a full-fledged compiler. There is no error recovery, no support for classes and other OOP structures, no support for any data types other than integers, and no assembly optimization. It is possible that at some point I will return to this project and implement some of these features.

## How to run

To compile `filename.nrj` into `filename.asm`, use:  `python nrj_compiler.py filename.nrj`

To run `filename.asm`, use:  `. run filename`

See the file `Examples/gcd.nrj` for an example implementation of the Euclidean Algorithm in NRJ.

See the file `Examples/fib.nrj` for an example implementation of a Fibonnaci number generator in NRJ.

See the file `Examples/isprime.nrj` for an example implementation of a prime number checker in NRJ.

## Dependencies

- Python
- NASM 
- GCC

The compiler is written in Python. NASM is used to compile the `.asm` file output by the compiler into a `.o` file, GCC is used to turn the `.o` file into an executable. 



## NRJ Language Specifications

### Features

| Implemented Features |
| -------------------- |
| Integer arithmetic |
| If-elseif-else branching |
| While loops |
| For loops |
| Functions |
| Recursion |

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

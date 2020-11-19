# Oats Programming Language and Interpreter

Oats is a procedural programming language that allows you to write simple programs to manipulate integers.

`gcd.oats` is a good example of an Oats program:
```
# Calculate the greatest common divisor of two numbers using Euclid's algorithm
func gcd(x, y){
    if (x < y){
        x, y = y, x;
    }
    if (x % y == 0){
        return y;
    }
    return gcd(y, x % y);
}
print(gcd(read(), read()));
```
`gcd.oats` can be run using the Oats interpreter:
```
$ python oats.py gcd.oats
input an integer: 1071
input an integer: 462
21
```
`gcd.oats`, along with other example files, can be found in the `Test/Examples` folder. 

## Overview

Oats is a programming language stripped down to the essentials. It includes the most important features of procedural programming - conditionals, loops, functions, and recursion - and discards the rest. The only allowed data type is integers. For I/O, Oats includes built in `read` and `print` functions.

Syntactically, Oats is like a hybrid of Java and Python, but without the constant verbosity of the former or the occasional abstruseness of the latter.

## How to run

`$ python oats.py your_file_here.oats`

# Oats Language Specifications

## Binary Operators
| Operator   | Lexeme   |
| ---------- | :------: |
| Add        | +        |
| Subtract   | -        |
| Multiply   | *        |
| Divide     | /        |
| Modulus    | %        |
| Or         | or       |
| And        | and       |
| EQ         | ==       |
| NE         | !=       |
| LT         | <        |
| GT         | >        |
| LTE        | <=       |
| GTE        | >=       | 

## Unary Operators

| Operator | Lexeme |
| -------- | :----: |
| Not       | not   |
| Negation  | -     |

## Variable Declarations

Variable declarations take the following form:

`identifier = expression;`

For example, 

`x = 1 * (2 + 3);`

## Function Declarations

Function declarations take the following form:

```
func identifier (arg1, arg2, arg3) {
    *body*
}
```

For example:

```
func factorial (x){
    if(x < 0 ){
        return -1;
    } elseif(x == 0){
        return 1;
    } else {
        return x * factorial(x - 1);
    }
}
```

## Function Calls

Function calls take the following form:

`identifier(arg1, arg2, ...);`

For example:

`factorial(9);`

## Conditionals

Conditionals take the following form:

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
x = 1;
if ( x == 1) {
    print(1);
} elseif (x == 2) {
    print(2);
} else {
    print(3);
}
```

## Loops

### While Loops

*while* loops take the following form:

```
while (expression) {
    *body*
}
```

For example,
```
int x = 1;
while (x < 1){
    x = x + 1;
}
```

### For Loops

*for* loops take the following form:

```
for (assignment; expression; assignment) {
    *body*
}
```

For example,
```
total = 0;
for(k = 0; k < 10; k = k + 1){
    total = total + k; 
}
```


## Built-Ins

Oats has two built in functions: *print* and *read*.

### Print

The *print* function takes in some number of arguments and prints those arguments to stdout, separating them with commas. The *print* function takes the following form:

```
print(arg1, arg2, ...);
```

For example,
```
a, b, c = 1, 2, 3;
print(a, b, c);
```

### Read

The *read* function automatically prints the prompt `input an integer:` to stdout, and then reads from stdin until a valid integer is input, which it then returns. The *read* function takes the following form:

`read();`

For example,

`a = read();`

## Comments

Single line comments can be made in Oats using `#`.

For example,

```
# Print the sum of x and y.
print(x + y);
```

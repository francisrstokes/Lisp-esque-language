# Lisp-esque language (Lel)

Lel is a lisp like programming language. It is not meant for practical purposes, but more as a tool to learn how to write a programming language.

## Language features

- Primitive types:
  - Number
  - String
  - Boolean
  - Function
- Lexical scoping of functions and variables
- Functions form closures
- Call by reference for functions
- Conditionals

### Keywords

The standard language implements a range of functionality.

#### Variables

Variables are declared with the `let` keyword, and are immutable.

```lisp
(let x 10)
```

They can of course be assigned as the result of a function:

```lisp
(let x (+ 4 6))
```

#### Functions

Functions are declared with the `function` keyword. The last statement in a function body is the final return value.

```lisp
(function add1 (x)
  (+ x 1))
```

Functions exist in both the scope they were declared in, and a separate execution scope for running instance. A function declared inside a function FIXXXXXXXX

## Tokeniser and Parser

The lel tokeniser and parser are both written in javascript, as is the interpreter.

```lisp
(let theAnswer
  (+ 18
    (* 12 2)))

(print
  "Life the universe and everything = " theAnswer "\n")
```

becomes

```javascript
[
  [
    { isToken: true, type: 'IDENTIFIER', value: 'let' },
    { isToken: true, type: 'IDENTIFIER', value: 'theAnswer' },
    [
      { isToken: true, type: 'IDENTIFIER', value: '+' },
      { isToken: true, type: 'NUMBER', value: 18 },
      [
        { isToken: true, type: 'IDENTIFIER', value: '*' },
        { isToken: true, type: 'NUMBER', value: 12 },
        { isToken: true, type: 'NUMBER', value: 2 }
      ]
    ]
  ],
  [
    { isToken: true, type: 'IDENTIFIER', value: 'print' },
    { isToken: true, type: 'STRING', value: 'Life the universe and everything = ' },
    { isToken: true, type: 'IDENTIFIER', value: 'theAnswer' },
    { isToken: true, type: 'STRING', value: '\n' }
  ]
]
```

Which evaluates to: `Life the universe and everything = 42`.


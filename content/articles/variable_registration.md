title: Variable/Function Hoisting in Javascript 
date: 2020-06-08 11:00
author: Punit Jain
Category: Javascript
Slug: variable Hoisting in Javascript
Summary: variable/function Hoisting in Javascript
Tags: Javascript
Authors: Punit Jain
Status: published

# Variable Hoisting

Variable/Function hoisting is a common term in javascript and important concept to understand flow of program.
Javascript being a dynamic language, executes statements line by line and jump around using control flow statements.
However if you notice in javascript, functions can be called prior to declaration.
This is due to the fact javascript execution happens in 2 phases:

1. In first phase, javascript goes through the code and registers all functions and variables in the current lexical environment.
2. In second phase javascript code actually runs and executes statements. In this phase no registration happens.

Lets take an example to understand this is detail:

```javascript
func()
function func() {
  console.log('I am executed')
}
```
In the above code func() is referenced before it is declared which is fine as:
1. In first phase func is added to lexical environment of the program which is global at the moment.
2. Then in second phase actual execution starts and since reference of func is already available in lexical environment it is executed.

This concept is called hoisting. Basically all variables and function declarations are lifted to top of their functional/local scope.
This excludes function expression.

* **Hoisting and var**

Variables declared with var are hoisted to the top of enclosing function scope.
If variable is accessed before declaration, it gets evaluated to undefined.
lets look by example:

```javascript
function func(num) {
  console.log(variable); // => undefined
  var variable;
  return num;
}
func(3); // => 3
```

Here 'variable' is moved to to of function as a part of hoisting.
It is then assigned undefined.

* **Hoisting and let**

let is also hoisted to top of block. Unlike var, let scope is restricted by block in which it is declared.
When variable is accessed, which is declared with let, javascript throws 'ReferenceError'.
Below is an example:
```javascript
function check(value) {
  var variable = 1;
  if (value) {
    // Throws ReferenceError: variable is not defined
    console.log(variable);
    let variable = 2;
    console.log(variable); // 2 is printed
  }
  return false;
}
check(1);
```
If you see above 'variable' declared with let is scoped inside if block. So it is moved to top of block as a process of hoisting.
In declared state let variable cannot be used so raises a ReferenceError. So the best practice is declare let variable and then use it.

* **Hoisting and const**

const are also registered at top of the block like let.
referencing before assignment raises an ReferenceError just like in case of let.

```javascript
function func(num) {
   console.log(VALUE); // ReferenceError
   const VALUE = 2;
   return num * VALUE;
}
func(2); // => 4
```
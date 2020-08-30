title: Function Invocations in Javascript 
date: 2020-06-18 12:00
author: Punit Jain
Category: Javascript
Slug: Function Invocations in Javascript
Summary: Function Invocations in Javascript
Tags: Javascript
Authors: Punit Jain
Status: published


# Different ways to invoke functions

There are various ways to invoke functions in javacript:

* **As a function**

Function can be invoked as a function. This is what common way to use functions:

a. As a function using function declaration
```javascript
function test(name) {
  console.log(name)
}
test('punit')
```
If a line starts with a function keyword then it is a function declaration.

b. As a function expression
```javascript
(function (who) {console.log(who)})('punit');
```
If a line doesnot start with function keyword then it might be a function expression.
Sounds wierd right ? but this is the way we differentiate between function declaration and rest of the ways to define function.


* **As a method**

```javascript
var test = {
  demo: function() {console.log('hello punit')};
};

test.demo()
```

* **As a constructor**

Function can be invoked as a constructor to create a new object by using keyword new.
Example is as below:

```javascript
function Demo() {
  this.obj = function() {
    return this;
  }
};

d = new Demo();
```
Note here function name is starting with a capital letter unlike in while calling as a regular function where we use a camelcase.

* **IIFE**

IIFE(Immediately invoked function expressions), as the name suggest are function expressions which are immediately invoked.
These were pre-dominant in ECMA 5 and earlier to define local scopes, however with invent of modules, they are sparingly used.

```javascript
var greet = function hello() {
    console.log(hello); //[Function: hello]
    return 'good morning';
}

console.log(greet());
```
Here since function keyword doesnot start the line so it is a function expression and not function declaration.
Also since it is a function expression and it is not asssigned to any global variable, so no global property is being created,
so it preserves the scope of variables declared inside the IIFE.
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

b. As a function expression
```javascript
(function (who) {console.log(who)})('punit');
```

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

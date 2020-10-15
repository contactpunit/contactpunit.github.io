title: instanceof checks in Javascript 
date: 2020-07-04 13:20
author: Punit Jain
Category: Javascript
Slug: instanceof checks in Javascript
Summary: instanceof checks in Javascript 
Tags: Javascript
Authors: Punit Jain
Status: published

# instanceof in Javascript

The most common use of instanceof operator in Javascript is to check whether an instance was created from a particular function constructor.
However if you are aware of how the instanceof works, you can very well conclude that instanceof checks whether the prototype of right side function is in the prototype chain of object on the left side.
Lets take an example to understand in detail:

```javascript
function Demo() {}
function SubDemo() {}
SubDemo.prototype = new Demo();
subdemoobj = new SubDemo();
console.log(subdemoobj instanceof SubDemo); //true
console.log(subdemoobj instanceof Demo); //true
}
```

Here if you see subdemoobj object returns true for instance check for class frm which it is instantiated as well as prototype class as Demo is in prototype chain of subemoclass.

however if we look at below example:

```javascript
function Demo() {};
let obj = new Demo();
Demo.prototype = {}; // changed prototype of demo constructor function
console.log(obj instanceof Demo); // false
```
If you see the result is 'false'. The reason being, we created object form Demo function and later we changed the prototype of Demo constructor to point to diff object.
so on change of prototype, right side of instanceof ie. Demo here has a prototype {} which is not in prototype chain of obj ( which has Demo in its prototype change as it was created prior to making prototype change ).

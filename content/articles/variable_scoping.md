title: Variable Scoping in Javascript 
date: 2020-06-02 10:00
author: Punit Jain
Category: Javascript
Slug: variable scoping in Javascript
Summary: variable scoping in Javascript
Tags: Javascript
Authors: Punit Jain
Status: published

# keywords supported for Variables

Javascript supports 3 keywords of variables definition:
1. const
2. var
3. let

Prior to ES6, only var was supported. With addition of const and let, there has been great improvement in the way variable are scoped and inline with support of keywords in other languages.

* **Const**

As the name suggests const keyword allows for initialization of variable at the time of declaration.
Once a variable is initialized using its value cannot be changed.

```javascript
const variable1 = 10;
try {
  variable1 = 20;
} catch(e) {
  console.log('An exception raised on trying to change a const variable')
}
```

However, there are some caveats you should be aware of :

```javascript
const obj = {};
obj['a'] = 1;
```
In above case we are not changing reference to const variable rather assigning key to object which is allowed.
Same holds for array as well

```javascript
const anArray = [];
anArray[0] = 'hello';
```

Now that we have seen const, the second keyword is var

* **var**

var has been a keyword since the beginning in javascript and has always been a point of bugs inside the program.
For people new to javascript and not really clear with scoping rules which holds for various keywords, its a potential source of bugs and errors.

variable scoping is defined based on lexical environments they create.
For var, variable is defined in the closest function or global lexical environment.
lets understand with an example below:

```javascript
var globalVar = 'global';
function func() {
  var funcVar = 10;
  for (var i=0; i<2; i++) {
      var innerVar = funcVar + i;
  }
  console.assert(i === 2 && funcVar === 10);
}
func();
console.assert(typeof innerVar === 'undefined' &&
         typeof funcVar === 'undefined')
```

If you see in above program var innerVar is still accessible outside the for loop and the scope of innerVar is defind by nearest function and in this case func.

* **let**

let is a recent addition in ES6 and solves the probem of scoping.

```javascript
var globalVar = 'global';
function func() {
  var funcVar = 10;
  for (let i=0; i<2; i++) {
      let innerVar = funcVar + i;
  }
  console.assert(typeof innerVar === 'undefined');
}
func();
console.assert(typeof innerVar === 'undefined' &&
         typeof funcVar === 'undefined')
```

here we have replaced var with let for variable innerVar.
This restricts the scope of innerVar to for loop itself.

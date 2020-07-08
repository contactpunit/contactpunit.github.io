title: use strict in Javascript 
date: 2020-06-16 14:10
author: Punit Jain
Category: Javascript
Slug: strict in Javascript
Summary: use strict in Javascript
Tags: Javascript
Authors: Punit Jain
Status: published

# Always use strict

It is always recommended to use 'strict' while you create javascript programs to avoid unexpected results.
Lets see below example to understand one of the use-case:

```javascript
function fullname(firstname, lastname) {
  arguments[1] = 'dummy';
  return firstname + ' ' + lastname;
}

console.log(fullname('punit', 'jain'))
>>> punit dummy

```
If you see in the above example, the value of lastname has been changed inside the function by overriding value of arguments alias.
arguments is an alias to the values passed inside a function. You can treat it as an array but they are not array to be precise.
 Inside this example I am changing value of arguments[1] alias which causes original variable lastname to be changed.
 
 This can be avoided by using strict as in example below:
 
 ```javascript
"use strict";
function fullname(firstname, lastname) {
  arguments[1] = 'dummy';
  return firstname + ' ' + lastname;
}

console.log(fullname('punit', 'jain'))
>>> punit jain
```
Here by using strict we are avoiding any surprises that could happen.
title: Prototypes in Javascript 
date: 2020-07-05 18:20
author: Punit Jain
Category: Javascript
Slug: Prototypes in Javascript
Summary: Prototypes in Javascript 
Tags: Javascript
Authors: Punit Jain
Status: published

# Prototype in Javascript

In javascript, prototype is used to implement inheritence.
Taking an example below

```javascript
let obj = { 'name': 'hello', 'value': 'punit'}; // object obj has name ans value as its own properties. 
let subobj = {'profession': 'engineer'};
let other = {'place': 'IN'};

console.log('name' in obj) // true
console.log('profession' in obj) // false

```
Here we have created 3 different objects (obj, subobj, subsubobj). Each object has access to its own properties assigned while creating objects.
If we try to access 'profession' from obj, we get false as it has no property named 'profession'.
We can create a inheritence relationship by setting prototype using setPrototypeOf method.

```javascript
Object.setPrototypeOf(obj, subobj);
console.log('profession' in obj) // true
```

This sets subobj as the prototype for obj.



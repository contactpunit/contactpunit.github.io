title: Spread operator in Javascript 
date: 2020-08-09 19:22
author: Punit Jain
Category: Javascript
Slug: spread operator in Javascript
Summary: spread operator in Javascript
Tags: Javascript
Authors: Punit Jain
Status: published

# Spread operator in Javascript

The spread operator (...) is special in a way, it converts any iterable into an array.
The way it works is:
1. spread operator determines the default iterator on an object on which is is applied.
like in case of map it is entries(), incase of set values() etc.
2. Once it determines the default iterator, it reads all values rom iterators and fills in, inside an array

This can be explained with example below:

```javascript
let m = new Map([['name', 'punit'], ['age', 42]]);
let mapArray = [...m]
console.log(mapArray) // calls default iterator entries() on map.


let arr = [1,2,3,4];
let array = [...arr]
console.log(array);

let set = new Set([1,2,3,4,6,6,6,4]);
let setArray = [...set];
console.log(setArray);

//output
[ [ 'name', 'punit' ], [ 'age', 42 ] ]
[ 1, 2, 3, 4 ]
[ 1, 2, 3, 4, 6 ]
```
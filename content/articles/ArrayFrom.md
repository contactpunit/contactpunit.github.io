title: Array.from in Javascript 
date: 2020-11-08 19:54
author: Punit Jain
Category: Javascript
Slug: Arrayfrom in Javascript
Summary: Array.from in Javascript
Tags: Javascript
Authors: Punit Jain
Status: published

# Array.from method in Javascript

ECMA 6 introduced a new method Array.from which can be used to traverse over any iterable or array like object,
to convert it into an array.

Earlier user had to use Array prototype method as below:

```javascript
function convertToArray() {
    return Array.prototype.slice.call(arguments)
}

```
In the above code method convertToArray is used to convert array like objects ( like arguments or NodeList ),
to an array.

This does work, however ECMA6 introduced a new method on Array prototype called 'from' which works on any iterable
and converts it to an Array, using its default iterator.

The last statement 'using its default iterator' is important to understand, so I will explain it in more detail.
Lets take few examples below:

```javascript
let m = new Map([['a', 1], ['b', 2]]);
console.log(Array.from(m))

//  [ 'a', 1 ], [ 'b', 2 ] ]

let n = new Set([1, 3, 5, 7]);
console.log(Array.from(n))

// [ 1, 3, 5, 7 ]

```
In first case map is an iterable object and is passed to Array.from.
Array.from will use map's default iterator, which is entries().
So Array.from() will call entries() on map and convert it to array.

In second case set, which is an iterable is passed to Array.from.
Array.from will use default iterator for Set, which is values() and 
create an array from it.

Now let's consider some custom object as below:

```javascript
let p = {
    items: [1, 4, 6, 8, 10, 12, 14],
    [Symbol.iterator]() {
        return this.values()
    },
    values: function* (items) {
        for (let i of this.items) {
            yield i
        }
    }
}

console.log(Array.from(p))

//[ 1,  4,  6, 8, 10, 12, 14 ]

```
In the above example we have created a custom iterable which returns values() as default iterator.
As a result o/p is an Array using values() iterator on calling Array.from().

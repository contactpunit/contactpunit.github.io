title: Custom Iterator in Javascript Example
date: 2020-06-12 23:11
author: Punit Jain
Category: Javascript
Slug: Custom Iterator in Javascript Example
Summary: Custom Iterator in Javascript Example
Tags: Javascript
Authors: Punit Jain
Status: published

# Custom Iterators

One important point to note about iterators in javascript which we discussed in earlier article was 
that custom object iterators can be created using [Symbol.iterator] method.

Ideally if you see inner working of any collection whether array, set or maps, they use Symbol.iterator method to
return an iterator.

For the build-in collections which include :
1. Sets
2. Arrays
3. Maps

These return specific iterators which further create an abstraction layer.
The build-in iterators returned are any one of the following, unless explicitly specified:
1. keys()
2. values()
3. entries()

So we already know in case of Arrays and Sets values() is returned, 
however in case of Maps entries() is returned which means if we traverse over the collections
using for...of loop, sets and arrays use values() as iterator by default and maps use entries.

What if you want to create custom iterator for your object. Let's understand this with an example:

* **Below custom object**

```javascript
let obj = {
    items: [1, 4, 6, 8, 10, 12, 14],
    itemsmap: new Map([['name', 'punit'], ['age', 25], ['profession', 'engineer']]),
    [Symbol.iterator]() {
        return this.entries()
    },
    values: function *(items) {
        for (let i of this.items) {
            yield i
        }
    },
    entries: function *(itemsmap) {
        for (let k of this.itemsmap) {
            yield k
        }
    }
}

for (let o of obj) {
    console.log(o)
}

// [ 'name', 'punit' ]
// [ 'age', 25 ]
// [ 'profession', 'engineer' ]
```
If we see the above code, [Symbol.iterator] specifies entries as an iterator and calls it whenever obj object is traversed using for...of loop.

Steps to explain above code execution:
1. when 'let o of obj' is called, [Symbol.iterator] method of obj method is checked for its presence to check if this object is iterable.
2. It then calls [Symbol.iterator] which further calls entries() generator function to return generator object.
3. This generator object is then traversed using for...of loop which traverses over itemsmap map using entries and yields item on each traversal.

If we modify the code as below:

```javascript
let obj = {
    items: [1, 4, 6, 8, 10, 12, 14],
    itemsmap: new Map([['name', 'punit'], ['age', 25], ['profession', 'engineer']]),
    [Symbol.iterator]() {
        return this.values()
    },
    values: function *(items) {
        for (let i of this.items) {
            yield i
        }
    },
    entries: function *(itemsmap) {
        for (let k of this.itemsmap) {
            yield k
        }
    }
}

for (let o of obj) {
    console.log(o)
}

// 1
// 4
// 6
// 8
// 10
// 12
// 14
```

It then behaves as an array as values() is called to return array iterator.

This way you can customize your custom object to behave as per your requirement.




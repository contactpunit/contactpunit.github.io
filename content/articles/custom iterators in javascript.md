title: Iterators in Javascript 
date: 2020-08-15 14:32
author: Punit Jain
Category: Javascript
Slug: Custom iterators in Javascript
Summary:  Custom iterators in Javascript
Tags: Javascript
Authors: Punit Jain
Status: published

# Custom iterators in Javascript

we have seen in our earlier post how iteration works in javascript and how builtin collections offer functionality for javascript to loop over.
However we can create our custom objects and make them iterable too. By default custom collections are not iterable.
There are various ways to do that, however the easiest way to achieve this is using composition.
This is something you might have seen in other languages as well like in python defining your own objects with certain methods like iter etc.
When creating a custom object in javacript we include a property which is predefined in javascript and is iterable.
So basically we piggy-back on existing iterable to use its functionality.

There are rule for creating your own iterables:
1. define Symbol.iterator property containing a generator.

```javascript
let collection = {
    items: [1,2,3,4],
    *[Symbol.iterator]() {
        for (let item of this.items) {
            yield item;
        }
    }
};

for(let x of collection) {
    console.log(x)
}
// output
1
2
3
4
```
if you see above example we have created custom iterable traverses already defined iterable items.

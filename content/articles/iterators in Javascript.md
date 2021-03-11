title: Iterators in Javascript 
date: 2020-08-16 16:19
author: Punit Jain
Category: Javascript
Slug: Iterators in Javascript
Summary: Iterators in Javascript Explained
Tags: Javascript
Authors: Punit Jain
Status: published

# Iterators in Javascript

Iterators are objects with interface that supports iteration.
Question comes is what are iterators. Any object that can be traversed and produces values one by one are iterators.
However, in javascript terms iterators should follow some rules:
1. Iterators have next() method which when called generates an object.
2. The object returned has 2 properties 'value' and 'done.'
3. 'value' property gives the next value from the iterator
4. 'done' property tells if there are any more values still remaining to be returned.
5. Iterator can be traversed only once. Once completed, it cannot be restarted.
6. If all values are returned, 'value' of undefined is returned going forward.

We can create an iterator manually as well. Below is an example of one of the iterators:

```javascript

function iterators(items) {
    var i = 0;
    return {
        next: function() {
            var done = (i >= items.length);
            var value = !done ? items[i++] : undefined;
            return {
                value,
                done
            };
        }
    }
}
let sampleIterator = iterators([1,2,3,4]);
console.log(sampleIterator.next());
console.log(sampleIterator.next());
console.log(sampleIterator.next());
console.log(sampleIterator.next());
console.log(sampleIterator.next());

// output
{ value: 1, done: false }
{ value: 2, done: false }
{ value: 3, done: false }
{ value: 4, done: false }
{ value: undefined, done: true }

```
As you see above creating an iterator with hand is not straight forward, so javascript already gave a mechanism to mke this process easy.
This is done using a generator. Generator returns and iterator.

# Generators

Generator is a function that returns an iterator which can then be traversed using next() method on the iterator.
Generator is created using an * between function keyword and name of function.
also a 'yield' keyword inside the function body marks a function as a generator.
Generators have sme rules similar to iterators:
1. They have yield statement inside the function body
2. Generator function on execution returns iterator which is later traversed to produce vaules.
3. Iterator returned from generator function, doesnot produce all values at once.
4. Each value is produced on call to next() method, after which generator object goes to sleep untill it is called again.

ets take previous example where we created iterator with hand and convert it to use generator.
The simplest approach is :
```javascript
function * generator() {
    yield 1;
    yield 2;
    yield 3;
    yield 4;
}

let iterator = generator();
console.log(iterator.next());
console.log(iterator.next());
console.log(iterator.next());
console.log(iterator.next());
console.log(iterator.next());

//output
{ value: 1, done: false }
{ value: 2, done: false }
{ value: 3, done: false }
{ value: 4, done: false }
{ value: undefined, done: true }
```
Same as previous example, however here we have hardcoded values to be produced inside the generator function.
Lets try passing items as input like in first example.

```javascript
function * generator(items) {
    for(let i=0; i < items.length; i++) {
        yield items[i]
    }
}

let iterator = generator([1,2,3,4]);
console.log(iterator.next());
console.log(iterator.next());
console.log(iterator.next());
console.log(iterator.next());
console.log(iterator.next());

// output
{ value: 1, done: false }
{ value: 2, done: false }
{ value: 3, done: false }
{ value: 4, done: false }
{ value: undefined, done: true }
```
# Generator Function Expressions

function expressions can be used to create generators as well.

```javascript
let gen = function * generator(items) {
    for(i=0; i < items.length; i++) {
        yield items[i]
    }
}

let iterator = gen([1,2,3,4]);
console.log(iterator.next());
console.log(iterator.next());
console.log(iterator.next());
console.log(iterator.next());
console.log(iterator.next());
```
However there is one problem with this approach if you see.
We are calculating length of iterable inside the loop. Generators are meant to traverse infinite iterators and dont need to know length of an iterable.
This approach is not productive as imagine if we have a million item inside items array, to calculate the length of items, items will need to be loaded in memory which defeats the purpose.
One approach is to look for done property each time we traverse the loop and when done is true we break out, like below:

```javascript
function * generator() {
    yield 1;
    yield 2;
    yield 3;
    yield 4;
}

let iterator = generator()
while(true) {
    result = iterator.next();
    if (result.done) {
        break;
    }
    console.log(result);
}

// output
{ value: 1, done: false }
{ value: 2, done: false }
{ value: 3, done: false }
{ value: 4, done: false }

```
However using while loop and everytime checking for value of done property, as well as creating an iterator first from generator function is cumbersome process.
Javascript provides a syntactic sugar for this problem and abstracts all this 'for - of' loop.

# for-of loop

An iterable as we discussed earlier is an object from which iterator is created.
All collection objects like arrays, map, sets are by default iterable.
There are some characterstics of iterable which you should be aware of: 
1. An iterable has Symbol.iterator property. 
2. when we use for-of loop, it calls Symbol.iterator method on iterable to retrieve an iterator.
3. Then iterator.next() method is called and done property is checked if it is false or true. 
4. If false iterator.next() is caled until true is returned for done property. That's when loop stops execution. 

```javascript
var items = [1,2,2,3,4];
for ( let i of items) {
    console.log(i)
}
// output
1
2
2
3
4
```

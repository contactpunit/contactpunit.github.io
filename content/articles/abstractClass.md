title: Abstract Classes in Javascript
date: 2020-11-14 10:38
author: Punit Jain
Category: Javascript
Slug: Abstract Classes in Javascript
Summary: Abstract Classes in Javascript
Tags: Javascript
Authors: Punit Jain
Status: published

# Abstract classes in Javascript

ECMA 6 introduced a new keyword to create classes like they are created in other languages.
The syntax and inner details of classes is discussed in a separate post altogether, as it a big subject on its own,
however here we will discuss on how to create an abstract base class in javascript.

An abstract base class is a class which cannot be instantiated, however can be inherited.
Objects are created from inherited class.

The way to create abstract class is as below:

```javascript
class Car {
    constructor(numTypres, numWindows) {
        this.numTypres = numTypres;
        this.numWindows = numWindows;
        if (new.target === Car) {
            throw new Error('base class cannot be instantiated')
        }
    }
}

class Ford extends Car {
    constructor(numTypres, numWindows) {
        super(numTypres, numWindows);
    }
}

const c = new Car(4, 6)

// throw new Error('base class cannot be instantiated')
            ^
//Error: base class cannot be instantiated

const f = new Ford(4, 6)
console.log(f)

// Ford { numTypres: 4, numWindows: 6 }
```
In the above code Car is created as a base class. Under constructor function we are checking for
new.target, which is added in ecma6 to determine how the class is being invoked.

new.target is mostly used to make sure class is instantiated using new operator and target of new is 
one against which test is being performed.

In the first case when base class (Car), is called with new, it throws as error
as the new.target matches 'Car'.

Then class Ford is derived from Car using extends.
When an instance of Ford is created, it succeeds, as new.target in that case
matches Ford.

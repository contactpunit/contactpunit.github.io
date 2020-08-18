title: Objects in Javascript 
date: 2020-08-18 12:58
author: Punit Jain
Category: Javascript
Slug: Objects in Javascript
Summary: Objects in Javascript
Tags: Javascript
Authors: Punit Jain
Status: published

# Objects in Javascript

There are multiple ways to create object in javascript.
1. Using object literals
2. Using constructor functions
3. Using Object.create method

## Using Object literal

Using object literal is the most common way of creating an object in javascript.
See below example:
```javascript
let person = {
    firstName: 'Punit',
    lastName: 'Jain'
};
```
here person object is created by assigning values to properties of an object.
These are kind of static. This object can be changed later by adding / removing/ modifying existing object like below:

```javascript
person.age = 24;
person.speak = function() {
    return 'speaks english';
}
```
This adds properties to the object. We can inspect it py printing various property values:
```javascript
onsole.log(person.firstName); // Punit
console.log(person.speak()) // speaks english
```

However if we need to create multiple objects it is not feasible to create all objects manually.
We need a kind of a blueprint to create objects.
This brings us to creating objects using constructor functions.

## Using Constructor Functions

Constructor functions is another way to create objects in javascript.
```javascript
function Person(firstName, lastName, age) {
    this.firstName = firstName,
    this.lastName = lastName,
    this.age = age,
    function speak () {
        return 'speaks english';
    };
}

let person1 = new Person('Punit', 'Jain', 24);
let person2 = new Person('Jack', 'Taylor', 28);

console.log(person1.firstName); // Punit
console.log(person2.firstName); // Jack
``` 
As you can see above we created object using new operator and notice properties are created on tis object using this. this always refer to an object in the context of the code you are executing at that time.
Also new creates a new empty javascript object and sets the context of this to that new object and then calls the constructor function which is Person in this case.

## Using Object.create()

Earlier 2 ways of creating an object in javascript are syntactic sugar of creating an object using Object.create method.
Let us see how we can achieve the same using Object.create.

```javascript
let person = Object.create(Object.prototype,
    {
        firstName: {value: 'Punit', enumerable: true, writable: true, configurable: true},
        lastName: {value: 'Jain', enumerable: true, writable: true, configurable: true},  
    }
    );
```
In above example we have used Object.create method to create same object.
The first parameter to Object.create is prototype to be used for new object, then followed by various property descriptors for each of the property on this object.
However if you see this is far more complex way of creating an object than using syntactic sugar provided.

title: Titbits in Javascript 
date: 2020-07-25 19:27
author: Punit Jain
Category: Javascript
Slug: Titbits in Javascript
Summary: Titbits in Javascript
Tags: Javascript
Authors: Punit Jain
Status: published

# Important Titbits

This blog discusses on important titbits in javascript that you might find helpful

 # Titbit 1 - Default parameter values
 
 It is possible to specify default values for any arguments to function and it can appear before positional arguments as well.
 This is unlike in other languages like Python were positional params should come before named params.
 
 ```javascript
function getResponse(url, timeout=10, callback) {
  // function body defined here
}

getResponse('/', 20, function() {});
```

# Titbit 2 - undefined as default value
We can pass 'undefined' as default value for named parameter.
```javascript
function getResponse(url, timeout=10, callback) {
  // function body defined here
}

getResponse('/', undefined, function() {});
```
In above example timeout is assigned default value of 10.

# Titbit 3 - passing function as default value

For the case below:
```javascript
let variable  = 1;

function return_default_value() {
    return 10;
}
function printvalue(inputvalue=return_default_value()) {
    return inputvalue;
}

// function call
printvalue(20); //value passed to named param
printvalue(); //causes return_default_value to be called and value returned assigned to inputvalue param

```
In the above example first call to printvalue with an input param, assigns 20 to inputvalue.
In second case without any parameter passed return_default_value function is called to get value to be assigned to inputvalue.
Important point to note here is that function return_default_value is only called when no input parameter is passed.

# Titbit 4 - Triple equals operator

Comparing below equality:
```javascript
console.log('1' == 1); // true
console.log('1' === 1); // false
```

Note that '==' double equals does a type coercion to do comparison. Always use triple equals to do equality checks.

# Titbit 5 - isNaN check

Below code:
```javascript
a = NaN;
console.log(a == NaN); // false
console.log(a === NaN); // false
console.log(isNaN(a)); // true
```
use isNaN to check for NaN property.

# Titbit 6 - Object.is method

ECMA6 introduces Object.is method which solves lot of equality issues in prior versions:
```javascript
a = NaN;
console.log(Object.is(a, NaN));     // true
console.log(Object.is(5 == '5'));   // false
console.log(Object.is(NaN, NaN));  // true
```

Object.is method returns true if the type as well as value is same for comparison.

# Titbit 7 - Removing duplicates from an Array

In ECMA6 there is pretty easy way to remove duplicates from an array
```javascript
let duplicatearray = [1,4,3,4,2,2,2,7];
function removeDuplicates(items) {
    return [...new Set(items)]
}
let finalarray = removeDuplicates(duplicatearray);
console.log(finalarray) // [1,4,3,2,7]
```
Here we have used Set to remove duplicates and then passed the set output to array using spread operator.

# Titbit 8 - Default parameter expression

As we are aware in EMA 6 we can provide a default variable declaration as below:

```javascript
function add(first, second=10) {
  return first + second;
}
```
Here if second is not provided, default value of 10 is taken.
However the default value can also be a function call like below:

```javascript
function returnvalue() {
  return 5;
}
function add(first, second=returnvalue()) {
  return first + second;
}
```
Here whatever value is returned from returnvalue function execution is assigned to second as default.
Note here that the function call doesnot happen when function decleration is first parsed, rather it is called when returnvalue() is called.

This brings us an important point to watch out for.
```javascript
function add(first=second, second) {
  return first + second;
}
```
Here above if we have first argument dependent on later argument ( in this case second), would result in an undefined being set for first, rather than value of second.
so calling add(undefined, 2) raises an error.
This again brings us to interesting question.
What happens when we call: 
```javascript
  console.log(add(undefined, 2)); // throws an error
  console.log(add(null, 2)) // 2
```
This comparison tells that null doesnot account for no value being passed, rather null is taken as a value, which is different than passing undefined.

# Titbit 9 - Returning object from arrow function

To return an object from an arrow function use below syntax:

```javascript
let arrfunction = () => ({name: 'John', age: 42})
console.log(arrfunction());
```

Note the use of parenthesis around the arrow function.

# Titbit 10 - nested object destructuring

In ECMA6, it is possible to destructure a nested object, like below:

```javascript
let userAddress = {
    address: {
      house: "grand victoria",
      street: "3rd cross",
      city: "bangalore"
    }
  }
  
  let {address: { house }} = userAddress;
  console.log(house) // grand victoria
```
# Titbit 11 - Swap values

In older version of javascript, to swap 2 variable values a temporary variable was required.
However in ECMA6 it is easier and uses variable de-structuring to swap variable values.

```javascript
let a = 10;
let b = 20;
[a, b] = [b, a]
console.log(a,b) // 20 10
```
Make sure there is some value in variable as object destructuring throws error if the right side of destructuring as null or undefined in variable.

# Titbit 11 - Destructuring nested arrays

Just like destructuring nested objects, we can also destructure nested arrays as well.

let colors = [ 'red', ['skyblue', 'pink'] ]
let [darkcolor, [lightcolor]] = colors;
console.log(darkcolor, lightcolor) // red skyblue

# Titbit 12 - cloning an array

rest items can be used to clone an array

```javascript
let names = ['john', 'peter', 'andrew']
let [...cloneNames] = names; 
```

# Titbit 13 - forEach in Sets Arrays and Maps

forEach method in different datatypes:

```javascript
let arr = [1,2, 3, 4];
arr.forEach(function(elem) {
    console.log(elem);
})

let set = new Set([1,3,3,3,2,4,7]);
set.forEach(function(elem) {
    console.log(elem);
})

let m = new Map([['name', 'punit'], ['age', 25]])
m.forEach(function(k, v) {
    console.log(k, v); // value, key of a map
})

```

# Titbit 14 - for-of loop

we already know how for-of loop works. We also know how default iterator are used for builtin collections when for-of loop is used.
like :
array - default iterator is values()
set - default iterator is values()
map - default iterator is entries()
this feature can be used in destructuring of maps as below:
```javascript
let m = new Map([['name', 'punit'], ['age', 42]]);
for (let [k, v] of m) {
    console.log(k, v)
}
```

if you see above example, we have not used m.entries() as entries is default iterator for map.
this returns an array which is destructured in to [k, v] to capture key and corresponding value.


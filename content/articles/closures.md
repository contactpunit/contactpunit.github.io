title: Closures in Javascript 
date: 2020-06-10 10:00
author: Punit Jain
Category: Javascript
Slug: Closures in Javascript
Summary: Closures in Javascript
Tags: Javascript
Authors: Punit Jain
Status: published

# Closures

Understanding closures is key to understanding scoping in javascript.
A closure allows a function to access and manipulate variables which are external to that function.
This helps to call the declared function even after the scope in which it was declared has already gone.

Lets look different uses of closures with examples below:

* **Maintain Private variables**

```javascript
function Counter() {
  var counts = 0;
  this.getCounts = function () {
    return counts;
  };
  this.incrementValue = function() {
    counts++;
  };
}

var counterObject = new Counter();
counterObject.incrementValue();
var counterObject = new Counter();
counterObject.incrementValue();
console.assert(counterObject.counts === undefined);
console.assert(counterObject.getCounts() === 1);
counterObject.incrementValue();
console.assert(counterObject.getCounts() === 2);
```
If we see the above code, we create a function Counter to act like a constructor.
Inside the constructor we define private variable counts whose scope is limited to inside the function.
We then define a getter function getCounts which will get the current value of counts.
Note that closure here allows the count to maintain its state inside the method without letting it be directly accessed.

* **Using closures wih callbacks**

  Closures can also be used with callbacks. Normally defining a function inside another function creates a closure.
  In such cases inner function frequently accesses the outer function data. Lets understand this with an example.
  Imagine you are defining a script element inside DOM as below:
  
```javascript
function cityLocation() {
	var city = 'Delhi';
	return {
		get: function() { console.log(city); },
		set: function(newcity) {city = newcity; }
	};
}

var location = cityLocation();
location.get();
location.set('pune');
location.get();
```
In the above code inner function has reference to city variable even when the outer function cityLocation is called and long gone.
The reference to variable helps to modify the variable inside inner function. The variable remains in scope due to closure.





title: Functions in Javascript 
date: 2020-06-15 12:00
author: Punit Jain
Category: Javascript
Slug: Functions in Javascript
Summary: Functions in Javascript
Tags: Javascript
Authors: Punit Jain
Status: published

# Functions are first class citizens

Functions are first class citizens in Javascript just like Python. What does this mean ?
Well this means functions should obey below rules to be treated as first clas citizens:

* Functions can be created as literals
```javascript
function hello() {}
```
* Functions can be assigned to variables
```javascript
var hello = function() {}
```
* Functions can be passed to other functions and can be returned as a return value
```javascript
function test(hello) {
  return hello()
}
function hello() {};
result = test(hello)
```
* Function can be assigned properties
```javascript
var f = function() {};
f.alternateName = 'demo'
```

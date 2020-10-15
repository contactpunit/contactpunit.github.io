title: Variable declaration question in Javascript 
date: 2020-07-25 19:27
author: Punit Jain
Category: Javascript
Slug: Variable declaration question in Javascript
Summary: Variable declaration question in Javascript
Tags: Javascript
Authors: Punit Jain
Status: published

# Question

Below is a program and guess what will be the output without looking into answer.
```javascript
var count = 30;
let count = 10;
```

Any idea what will be the output ?
Answer - When you run it it gives below error:

```javascript
error: unknown: Identifier 'count' has already been declared (2:4)
```
So any idea why it generates this error ?
Here we are declaring count with var and later once again using let.
As let will not redefine a variable which already exists and is defined in same scope, an error is thrown.

However if we make changes to our script and run as below:

```javascript
var count = 10;
var total = 0;
if(total === 0) {
  let count = 20; // this works
}
```
The above program works as expected as inner if loop defines a new block scope and the variable defined inside the if loop shadows the global count.
title: Interesting Callables in Python 
date: 2020-05-12 11:30 
author: Punit Jain
Category: Python
Slug: Interesting Callables in Python
Summary: Callables you should know
Tags: Python
Authors: Punit Jain
Status: published

# Callables you should know

In our earlier post we already saw what callables are, but did you ever wondered what callables are already provided as part of language? Well know all in-built functions, methods are callables but there are 2 who I find really useful using them in my daily coding practices.

1. Decorators
2. Partials

# Decorators

Simple defined decorators are callables which accept a callable (could be function, class, method, object) and returns back a callable. In mot cases decorators dont modify the original callable which is passed to decorator, rather add functionality, before and after the function.

Taking an example:


```python
from functools import wraps
import time

def timing(f):
    """A simple timer decorator"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f'Start time {f.__name__}: {start}')
        result = f(*args, **kwargs)
        end = time.time()
        print(f'End time {f.__name__}: {end}')
        duration = end - start
        print(f'Elapsed time {f.__name__}: {duration}')
        return duration, result
    return wrapper

@timing
def sleep_interval(interval):
    time.sleep(interval)
    return interval

sleep_interval(10)

admins-MacBook-Pro:ds admin$ python ds/speed_up.py 
Start time sleep_interval: 1589273520.217406
End time sleep_interval: 1589273530.217633
Elapsed time sleep_interval: 10.000226974487305

```
If you see here we created a decorator timing which is applied on sleep_interval function. Decorator takes sleep_interval as an argument and return another function which is reassigned to sleep_interval. So basically above decorator can also be applied as :

sleep_interval = timing(sleep_interval)

With new syntax of applying decorator, its clear for a reader to understand whats going on. The old syntax we just talked about might be missed by some readers and requires deep reading to understand.

# Partial

Partials are another interesting callables which take a callable as an input and return a callable.
The most common use of partials is when we already know few arguments in advance, long before function is called. In such cases partials help with eventually calling final function with less number of arguments.

partial can be imported from functools module.
Lets take an example:

Lets suppose you want to multiple numbers with 5. The orginal function looks like this:

```python
from functools import partial
def multiply(a, b):
    return a * b

>>> multiply(2, 5)
10

However using partial

def multiply(a, b):
    return a * b

multiply5 = partial(multiply, 5)
>>> multiply5(7)
35
```

If you see here partial takes a callable ie multiply function and returns a callable which is finally called with one argument.

title: Concepts you should know, to understand Decorators well
date: 2020-05-10 15:45
author: Punit Jain
Category: Python
Slug: Concepts you should know, to understand Decorators well
Summary: Pre-requisites in understanding Decorators
Tags: Python
Status: published

# Pre-requisites in understanding Decorators

In order to understand what decorators are, you should understand below concepts which are centric to decorators.

1. Callables
2. Closures

# Callables

In python everything is an object. An object is callable, if it can be called like a function/method. The easiest way to check if an object can be called is by passing object to built-in callable function and get a return value as True. Lets take few examples:

```python
x = 3
>>> print(callable(x))
False
```
x is a variable and not a callable.No surprise here.

```python
def print_name(name):
    print(f'Good Morning {name}')

>>> print(callable(print_name))
True
```

```python
class Demo:
  pass
>>> print(callable(Demo))
True
```

Do you notice both function and class return True and are callable ? What makes them callable.
Well there is a special dunder method which is invoked when a function or a class is called.
This special method is `__call__`. This means a callable object do have `__call__` method defined underlying.

Lets check ourselves:

```python
>>> dir(print_name)
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
```

Do you see __call__ method defined for function class ?

Lets check for custom useless class we created

```python
>>> dir(Demo)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>>> 
```

Again we can see `__call__` method being available. 

In my next blog I will explain what closures are.

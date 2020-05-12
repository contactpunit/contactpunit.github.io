title: issubclass and isinstance
date: 2020-05-12 16:00
author: Punit Jain
Category: Python

# Relation between issubclass and isinstance

Normally for type checking most developers use type() function. The result of type function is matched with a hardcoded string. However it is recommended to use issubclass and isinstance to check if object is inherited fromma  particular class or a class has descended from another class.

Interestingly both issubclass and isinstance are related.

```python

class Shape:
    pass


class Square(Shape):
    def __init__(self, **args):
        super().__init__()
        self.length = args['length']

    def __repr__(self):
        return f'square with length {self.length}'

>>> s = Square(length=10)
>>> s
square with length 10
>>> assert isinstance(s, Square)
>>> assert issubclass(Square, Shape)

```

One thing to note how issubclass is related to isinstance as below:

```python
isinstance(s, Square) is same as issubclass(s.__class__, Square)
```

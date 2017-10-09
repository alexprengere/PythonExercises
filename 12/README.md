## Exercise 10

### Problem

Sara wants to know how fast things are going, for example when a function is called, she wants to know how much time it took.
For this task, we want to create a decorator called `measure`, who will print the time spent when the decorated function is called.

```python
import time

@measure
def long_function():
    time.sleep(1)

long_function()  #  prints the time spent in long_function, probably around 1s ;)
```

### Help

To get the current time in Python, you can use:

```python
from datetime import datetime

datetime.now()
```

### Going further

3 possible improvements on the `measure` decorator:

+ it can work on any function, regardless of the function arguments
+ it takes an argument to run the decorated function multiple times, to get a more accurate measurement (useful for fast functions), like `@measure(N=10)`
+ it will make sure the decorated function keeps the function metadata, like `long_function.__name__`, see [the doc](https://docs.python.org/2/library/functools.html#functools.wraps)

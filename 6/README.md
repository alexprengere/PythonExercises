## Exercise 6

### Problem

For this sixth exercise, we want to manipulate class inheritance.
We are going to use the `Runner` class from the previous exercise.

Create a class `Swimmer` and a class `Biker` following the same rules as `Runner`.
Then, using (multiple) inheritance, create a class `Triathlete` who is able to run triathlons:
```python
>>> t = Triathlete(swim_speed=3, bike_speed=20, run_speed=15)
>>> t.go(swim_distance=1.5, bike_distance=40, run_distance=10)
# total triathlon time, hours
```

### Bonus

Write a unit test in a separate file `test.py`. It may be interesting to use `doctest` also.

### Help

When using multiple inheritance, you can directly call the exact constructor you want from the parent classes using, for example: `Swimmer.__init__(self, ...)`.


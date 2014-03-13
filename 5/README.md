## Exercise 5

### Problem

For this fifth exercise, we want to manipulate classes.

We would like to create a class `Runner` representing a runner.
```python
>>> r = Runner(run_speed=20) # km/h
>>> r.run(distance=10)       # km
0.5 # time, hours
```

The `Runner` class should be able to handle:
* comparisons between runners (we must be able to compare runners with `runner_1 < runner_2`)
* a nice display (with `print runner`)

Now, create a class `Swimmer` and a class `Biker` with the same concepts.
Then, using multiple inheritance, create a class `Triathlete` who is able to run triathlons:
```python
>>> t = Triathlete(swim_speed=3, bike_speed=20, run_speed=15)
>>> t.go(swim_distance=1.5, bike_distance=40, run_distance=10)
# total triathlon time, hours
```

### Bonus

Write a unit test in a separate file `test.py`.

### Help

When using multiple inheritance, you can directly call the exact constructor you want from the parent classes using, for example: `Swimmer.__init__(self, ...)`.


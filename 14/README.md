## Exercise 14

### Problem

For this exercise, we want to code a program `pandemic.py` that simulates a pandemic.

The program should work as follow:

```bash
$ python pandemic.py
```

The program should display a turn by turn evolution of a pandemic where:

+ people are represented by random 2D points in [0, 1], at the beginning a single random person is infected
+ each turn new people can get infected based on a model of your choosing, depending on the distance between points (at least)
+ each turn some people may recover or die from the disease based on a model of your choosing, depending on how long they had the disease (at least)
+ people who recovered may not be infected again
+ the simulation stops when nothing changes between turns

You may implement the following:

+ people change position each turn, simulating movements
+ vaccines: after a few turns, some people may become immune without having contracted the disease
+ add new parameters to each person, like age, to have better models
+ improve the representation of points by moving from random to a more accurate representation of population density

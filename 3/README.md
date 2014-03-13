## Exercise 3

### Problem 1

For this third exercise, we want to manipulate dates in Python.

The program should read two dates in format `DD-MM-YYYY` and display the number of days between these two dates.
```bash
$ python delta.py "15-01-2011" "19-01-2011"
4
```

### Bonus

It may be interesting to display also some additional information regarding the two dates given as input, like the day of the week (*tuesday*), or the month name (*January*).

### Help

In Python, you can get the rest of the division of an integer by another one with `%`:
```python
5 % 3 # returns 2
4 % 2 # returns 0 because 2 divides 4 ;)
```
In Python, the `datetime` package is used to manipulate dates. More particularly, `datetime.strptime()` is very useful to parse dates with different formats...


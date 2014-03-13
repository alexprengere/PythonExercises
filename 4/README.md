## Exercise 4

### Problem

For this fourth exercise, we want to manipulate regular expressions in Python.

The program should work as follow. It has to read a sentence and returns a phone number, if a phone number was found in the sentence.
We will suppose that phone numbers are always in the format `NN NN NN NN NN`, where `N` is a digit.
```bash
$ python phone.py "My phone number is 06 11 12 13 14 15. Call me?"
('06', '11', '12', '13', '14')
$ python phone.py "Today is 2014-01-04 and my number is 06 11 12 13 14 15."
('06', '11', '12', '13', '14')
$ python phone.py "Today is 2014-01-04."
# nothing, no phone number found
```

### Bonus

No bonus here.

### Help

In Python, the `re` module is used to manipulate regular expressions. More particularly, `re.search()` could be useful...


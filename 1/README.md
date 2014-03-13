
# Problem

For this first exercise, we want to code a program counting the words of a text file, without case.

The program should work as follow:
```bash
$ python count.py file.txt
```

If `file.txt` has those three lines:
```bash
$ cat file.txt
Apple banana
apple
Salad
```

The program should give:
```bash
$ python count.py file.txt
apple 2
banana 1
salad 1
```

# Bonus

Write the words with a relevant order, for example in alphabetical order, or by frequency.

# Help

To access command-line arguments from Python:
```python
import sys
sys.argv
```

## Exercise 13

### Problem

For this exercise, we want to code a program `sudoku.py` that solves a Sudoku game.

The program should work as follow:

```bash
$ python sudoku.py examples/simple.txt
```

If `simple.txt` has those lines:

```bash
$ cat examples/simple.txt
53. .7. ...
6.. 195 ...
.98 ... .6.

8.. .6. ..3
4.. 8.3 ..1
7.. .2. ..6

.6. ... 28.
... 419 ..5
... .8. .79
```

The program should give:

```bash
$ python sudoku.py examples/simple.txt
534 678 912
...
... the Sudoku solved! ...
```

### Help

Start by writing some code that checks the validity of a solution.

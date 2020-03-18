## Exercise 13

### Problem

For this exercise, we want to code a program `sudoku.py` that solves a Sudoku game.

The program should work as follow:

```bash
$ python sudoku.py file.txt
```

If `file.txt` has those three lines:

```bash
$ cat file.txt
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
$ python sudoku.py file.txt
... the Sudoku solved! ...
```

### Bonus

It might be interesting to know if several solutions are possible, or if none are possible.

### Help

Start by writing some code that checks the validity of a solution.

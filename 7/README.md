## Exercise 7

### Problem

For this exercise, we want to learn manipulate file paths, in a portable way.
We are going to build a super `ls`, displaying all kind of information.

Suppose you create some files with `touch`, and some directories with `mkdir`.
```bash
$ touch toto.pdf titi # we just created two empty files!
$ mkdir tutu          # and also one empty directory ;)
$ ls                  # "ls" lists the content of the current directory
titi  toto.pdf  tutu/
```
Now we are going to build a Python script `details.py` that reads a list of file names,
and print details on those files, like path, extension, size...
The script will read the names on its standard input,
so it will be easy to integrate it with `ls`.
```bash
$ ls > filenames # we store the list of names in the "filenames" file
$ cat filenames
titi
toto.pdf
tutu/
$ cat filenames | python details.py # details.py reads from its standard input
<type> <name>   <absolutepath>    <extension> <size> <anyotheridea>
file   toto.pdf /path/to/toto.pdf PDF         1Kb    ...
file   titi     /path/to/titi     None        1Kb    ...
dir    tutu     /path/to/tutu     None        1Kb    ...
```
Of course, we can directly connect `ls` and `details.py` together:
```bash
$ ls | ./details.py # if details.py is executable, we call it directly
...
```

### Help

Reading from `stdin` in Python is pretty much like reading from a file in Python.
```python
from sys import stdin

for row in stdin:
    print row.rstrip() # rstrip() removes the newline character at the end of the row
```

All operations on files should use the `os.path` module, to be portable across systems.
The [official documentation](https://docs.python.org/2/library/os.path.html) may be useful.
The common way to use `os.path` is to import it with an alias like this:
```python
import os.path as op

# Useful functions ;)
# op.exists
# op.realpath
# op.dirname
# op.basename
# op.isfile
# op.isdir
# op.getsize
```

### Bonus

Add last access time to files in the output.


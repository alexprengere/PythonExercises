## Exercise 7

### Problem

For this exercise, we want to learn manipulate file paths, in a portable way.
We are going to build a super `ls`, displaying all kind of information.

Create a `details.py` script that is executable (use `chmod`). This script
must be able to read a list of files on `stdin`, and output details on `stdout`:
```python
$ touch toto.pdf titi
$ mkdir tutu
$ ls
toto.pdf titi tutu details.py
$ ls | ./details.py
<type> <name>   <absolutepath>    <extension> <size> <anyotheridea>
file   toto.pdf /path/to/toto.pdf PDF         1Kb    ...
...
```

### Help

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
# os.isdir
```

### Bonus

Add last access time to files in the output.


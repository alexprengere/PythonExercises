## Exercise 8

### Problem

In this problem we want to build an English Scrabble helper.
We are going to build a Python script that gives the best possible
words from a list of letters.

```bash
$ python scrabble.py sserhoq
1. horses  6   15
2. horse   5   14
...
```

The output must contain the top 10 words with their length, sorted by points (see [here](http://en.wikipedia.org/wiki/Scrabble_letter_distributions#English) for English Scrabble points).

### Help

A few hints:
* Linux distributions usually have a list of all existing words in a local file:
  ```
  /usr/share/dict/words
  ```
  The algorithm should just open this file and look for the best possible words.

* It will be helpful to structure the code in functions to keep it clean and readable.
  Functions like `compute_points(word)` and `is_possible(word, letters)` are expected.

* It may be a good idea to store the Scrabble points of the letters in a separate file (csv for example).
  So in the future, you may build easily versions for other languages by just adding new files ;).


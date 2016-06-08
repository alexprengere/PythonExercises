#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement, print_function
import sys
try:
    from collections import Counter
except ImportError:
    print('You should use Python 2.7')
    exit(1)


def main(letters, dictionary):
    with open(dictionary) as words:
        matches = []
        for word in words:
            word = word.strip().lower()
            if not Counter(word) - Counter(letters):
                matches.append(word)

        matches.sort(key=len)
        for word in matches:
            print("{0}\t{1}".format(len(word), word))
        print('{0} matches, best has {1} letters'.format(len(matches), len(matches[-1])))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("python {0} totoa /usr/share/dict/words".format(sys.argv[0]))
        exit(1)

    if len(sys.argv) < 3:
        dictionary = "/usr/share/dict/words"
    else:
        dictionary = sys.argv[2]

    main(letters=sys.argv[1], dictionary=dictionary)

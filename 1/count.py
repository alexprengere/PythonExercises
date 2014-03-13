#/usr/bin/env python

import sys

def count_words(fl):
    """Reads a file-like and returns the word count.
    """
    words = []
    count = {}

    for row in fl:
        for word in row.rstrip().split():
            word = word.lower()

            if word not in count:
                count[word] = 0
                words.append(word)
            count[word] += 1

    return count, words


def display_words(count, words, sort=None):
    """Display the word count.
    """
    print 'Sort by {}'.format(sort)

    if sort == 'alphabet':
        ordered_words = sorted(words)

    elif sort == 'frequency':
        # .items() returns a list of (k, v)
        # we then sort on the value v using the key parameter
        sorted_items = sorted(count.items(),
                              key=lambda (k, v): v,
                              reverse=True)
        # Finally we keep only the word
        ordered_words = [k for (k, _) in sorted_items]

    else:
        ordered_words = words

    for word in ordered_words:
        print '{}\t{}'.format(word, count[word])


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print "Need exactly one argument!"
        exit(1)

    with open(sys.argv[1]) as fl:
        count, words = count_words(fl)
        display_words(count, words)
        display_words(count, words, sort='alphabet')
        display_words(count, words, sort='frequency')


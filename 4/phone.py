#!/usr/bin/env python

import sys
import re


def is_number(n):
    """This is an implementation of `is_number` and is not needed in this exercise ;).

    >>> is_number('44')
    True
    >>> is_number('44.0') # tricky :D
    False
    >>> is_number('44.5')
    False
    >>> is_number('not a number')
    False
    """
    try:
        int(n)
    except ValueError:
        return False
    else:
        return True


def _test():
    """Run doctests."""
    import doctest
    doctest.testmod()


if __name__ == '__main__':

    _test()

    if len(sys.argv) != 2:
        print 'Usage: python %s "a phone number xx xx xx xx xx"' % sys.argv[0]
        exit(1)

    match_obj = re.search(r'(\d\d\s){4}(\d\d)', sys.argv[1])

    if not match_obj:
        print "No phone number found"
    else:
        phone =  match_obj.group().strip()
        print tuple(p for p in phone.split())


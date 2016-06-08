#!/usr/bin/env python

import sys
from datetime import datetime


def parse_date(date, dt_format='%d-%m-%Y'):
    """Parse date d in dt_format.

    >>> parse_date("15-01-2014", '%d-%m-%Y')
    datetime.datetime(2014, 1, 15, 0, 0)

    This returns `None`, parsing fails here.

    >>> parse_date("xxxx")
    "xxxx" was not in format "%d-%m-%Y"
    """
    try:
        dt = datetime.strptime(date, dt_format)
    except ValueError:
        print '"%s" was not in format "%s"' % (date, dt_format)
        return
    else:
        return dt


def _test():
    """Run doctests."""
    from doctest import testmod
    testmod()


if __name__ == '__main__':

    _test()

    if len(sys.argv) != 3:
        print 'Usage: python %s DD-MM-YYYY DD-MM-YYYY' % sys.argv[0]
        exit(1)

    d1 = parse_date(sys.argv[1])
    d2 = parse_date(sys.argv[2])

    if d1 is not None and d2 is not None:
        # We print the day of the week,the month and the year for both dates
        print "Date %s was a %s in %s of %s" % (d1, d1.strftime('%A'), d1.strftime('%B'), d1.strftime('%Y'))
        print "Date %s was a %s in %s of %s" % (d2, d1.strftime('%A'), d2.strftime('%B'), d2.strftime('%Y'))

        # We print the number of days between both dates
        print "%s days between those two dates" % abs((d2 - d1).days)


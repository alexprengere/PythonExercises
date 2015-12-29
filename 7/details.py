#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import os.path as op


def main():
    for row in sys.stdin:
        name = row.rstrip()
        if not op.exists(name):
            print('{0} does not exist'.format(name))
        else:
            print('\t'.join([
                'dir' if op.isdir(name) else 'file',
                '{0:15s}'.format(name),
                op.splitext(name)[-1],
                str(op.getsize(name)),
                op.realpath(name),
            ]))


if __name__ == '__main__':
    main()


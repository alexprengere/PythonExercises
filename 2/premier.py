#!/usr/bin/env python

import sys


def is_prime(n):
    """Returns True is n is prime, False otherwise.

    >>> is_prime(4)
    False
    >>> is_prime(7)
    True
    """
    if n <= 1:
        return False

    for i in xrange(2, n):
        if n % i == 0:
            # i divides n, n is not prime
            return False

    return True


def yield_prime_factors(n, primes):
    """Yields the prime factors for n. Primes are second argument.

    >>> primes = [2, 3, 5, 7]
    >>> list(yield_prime_factors(12, primes))
    [2, 2, 3]
    >>> list(yield_prime_factors(7, primes))
    [7]
    """
    # n is divided by its own factors
    for prime in primes:
        if prime > n:
            break
        while n % prime == 0:
            yield prime
            n = n / prime


def _test():
    """Test comments."""
    import doctest
    doctest.testmod()


if __name__ == '__main__':

    _test()

    if len(sys.argv) != 3:
        print 'Usage: python %s inf sup' % sys.argv[0]
        exit(1)

    inf = int(sys.argv[1])
    sup = int(sys.argv[2])

    # List of prime numbers <= sup, e.g. [2, 3, 5, ...]
    primes = [p for p in xrange(1 + sup) if is_prime(p)]

    # Dict of prime factors: {12 : [2, 2, 3], ...}
    factors = {}
    for p in xrange(inf, sup + 1):
        factors[p] = list(yield_prime_factors(p, primes))

    print "Prime numbers between %s and %s:" % (inf, sup)
    print '\n'.join([str(p) for p in primes if inf <= p <= sup])

    for p in sorted(factors.keys()):
        if len(factors[p]) > 1:
            # p is not prime
            print "Prime factors of number %s are %s" % (p, factors[p])


#!/usr/bin/env python


class Runner(object):
    """A runner
    """
    def __init__(self, name, run_speed):
        self.name = name
        self.run_speed = run_speed

    def __str__(self):
        return "I am %s, I run at %d km/h" % (self.name, self.run_speed)

    def __cmp__(self, other):
        """
        Here we just use the __cmp__ function of the run_speed attribute.
        This only works for Python2. Python3 removes the support for __cmp__,
        and forces to implement __lt__, __le__, __gt__, __ge__ (<, <=, >, >=).
        However in Python3, the total_ordering decorator helps you do that,
        you can implement one of the above and __eq__ (==), then the rest
        will be automatically implemented.

        ```
            from functools import total_ordering

            @total_ordering
            class Runner(object):
                ...
        ```
        """
        return self.run_speed.__cmp__(other.run_speed)

    def run(self, distance):
        return distance / float(self.run_speed)


if __name__ == '__main__':

    # First runner
    sara = Runner(name='Sara', run_speed=20)
    print sara

    # Second runner
    alex = Runner(name='Alex', run_speed=18)
    print alex

    # Testing run function
    d = 10 # km
    print "%s takes %.2f hours to run %dkm" % (sara.name, sara.run(d), d)

    # Testing comparison functions
    print 'alex <  sara: ', alex < sara
    print 'alex <= sara: ', alex <= sara
    print 'alex == sara: ', alex == sara
    print 'alex >= sara: ', alex >= sara
    print 'alex >  sara: ', alex > sara

    # Playing
    print '\nTraining time!'
    sara.run_speed += 1
    print sara


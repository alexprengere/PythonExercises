#!/usr/bin/env python

"""
This comment will be checked by the tests. This is called a doctest,
the test runner will verify that the output of the following lines
is correct.

>>> s = Triathlete(swim_speed=3, bike_speed=20, run_speed=15)
>>> s.go(swim_distance=1.5, bike_distance=40, run_distance=10)
3.16...
"""


class Runner(object):
    """
    Here we only keep the necessary methods in Runner class.
    """
    def __init__(self, run_speed):
        self.run_speed = run_speed

    def __str__(self):
        return "I am a runner, I run at %d km/h" % self.run_speed

    def run(self, distance):
        return distance / float(self.run_speed)


class Swimmer(object):
    def __init__(self, swim_speed):
        self.swim_speed = swim_speed

    def __str__(self):
        return "I am a swimmer, I swim at %d km/h" % self.swim_speed

    def swim(self, distance):
        return distance / float(self.swim_speed)


class Cyclist(object):
    def __init__(self, bike_speed):
        self.bike_speed = bike_speed

    def __str__(self):
        return "I am a cyclist, I ride at %d km/h" % self.bike_speed

    def ride(self, distance):
        return distance / float(self.bike_speed)


class Triathlete(Swimmer, Cyclist, Runner):
    def __init__(self, swim_speed, run_speed, bike_speed):
        Swimmer.__init__(self, swim_speed)
        Cyclist.__init__(self, bike_speed)
        Runner.__init__(self, run_speed)

    def __str__(self):
        return '\n'.join([
            Swimmer.__str__(self),
            Cyclist.__str__(self),
            Runner.__str__(self),
        ])

    def go(self, swim_distance=0, bike_distance=0, run_distance=0):
        return self.swim(swim_distance) + \
               self.ride(bike_distance) + \
               self.run(run_distance)


if __name__ == '__main__':

    alex = Swimmer(swim_speed=2)
    print 'Alex:'
    print alex

    sara = Triathlete(swim_speed=2, bike_speed=40, run_speed=15)
    print 'Sara:'
    print sara

    print '\nTriathlon:'
    print sara.go(swim_distance=1.5, bike_distance=40, run_distance=10)


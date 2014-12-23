#!/usr/bin/python

import unittest
import doctest

import triathlete


class TriathleteTest(unittest.TestCase):
    """This is the unittest for the Triathlete class.
    """
    def setUp(self):
        self.triathlete = triathlete.Triathlete(swim_speed=2, bike_speed=40, run_speed=15)

    def test_go(self):
        self.assertEquals(self.triathlete.go(0, 0, 0), 0)

        # The Triathlete class has default values 0 for the go() method
        self.assertEquals(self.triathlete.go(), 0)

        # We use assertAlmostEquals because we would have to write an infinite
        # number of digits otherwise: 2.416666666...
        self.assertAlmostEquals(self.triathlete.go(1.5, 40, 10), 2.416, places=2)


def generate_test_suite():
    """We generate a test suite manually
    """
    s = unittest.TestSuite()

    # We add the tests from the TriathleteTest class
    s.addTests(unittest.makeSuite(TriathleteTest))

    # This adds tests based on the comments of the triathlete module
    s.addTests(doctest.DocTestSuite(triathlete, optionflags=doctest.ELLIPSIS))

    # This adds tests based on the comments in the README file
    s.addTests(doctest.DocFileSuite('README.md', optionflags=doctest.ELLIPSIS))

    return s


if __name__ == '__main__':
    unittest.main(defaultTest='generate_test_suite', verbosity=2)


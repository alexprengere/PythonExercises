#!/usr/bin/python

import unittest
import runner


class RunnerTest(unittest.TestCase):
    """This is the unittest for the Runner class.
    """
    def setUp(self):
        """This is executed once at the beginning.
        """
        self.runner_1 = runner.Runner(name='Sara', run_speed=20)
        self.runner_2 = runner.Runner(name='Alex', run_speed=18)

    def test_run(self):
        self.assertEquals(self.runner_1.run(10), 0.5)
        self.assertEquals(self.runner_2.run(9), 0.5)

    def test_comparison(self):
        self.assertLess(self.runner_2, self.runner_1)


if __name__ == '__main__':
    unittest.main(verbosity=2)


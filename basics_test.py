import get_column_stats
import os
import random
import statistics
import unittest


class TestGetColumnStats(unittest.TestCase):

    def test_mean(self):
        for i in range(0, 500):
            V = []
            for j in range(0, 500):
                V.append(random.randint(-1000, 1000))

            self.assertAlmostEqual(
                get_column_stats.getMean(V),
                statistics.mean(V))

    def test_stdev(self):
        for i in range(0, 500):
            V = []
            for j in range(0, 500):
                V.append(random.randint(-1000, 1000))

            self.assertAlmostEqual(
                get_column_stats.getStDev(V),
                statistics.pstdev(V))

    def test_mean_error(self):
        V = []
        self.assertRaises(ZeroDivisionError, get_column_stats.getMean, V)

    def test_stdev_error(self):
        V = []
        self.assertRaises(ZeroDivisionError, get_column_stats.getStDev, V)


if __name__ == '__main__':
    unittest.main()

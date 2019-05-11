#! /usr/bin/env python3
import unittest, math


def is_prime(n):
    for x in range(2, n):
        if x**2 > n:
            break
        elif n % x == 0:
            return False
    return True


def trial_division(n):
    count = 0
    candidate = 1
    while count < n:
        candidate += 1
        if is_prime(candidate):
            count += 1
    return candidate
    


class Test(unittest.TestCase):
    def test_trial_division(self):
        self.assertEqual(trial_division(1), 2)
        self.assertEqual(trial_division(2), 3)
        self.assertEqual(trial_division(3), 5)
        self.assertEqual(trial_division(4), 7)
        self.assertEqual(trial_division(10000), 104729)
        # self.assertEqual(trial_division(100000), 1299709)


if __name__ == "__main__":
    unittest.main(verbosity=2)
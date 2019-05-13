#! /usr/bin/env python3
import unittest

def calculate_sum(limit, factors):
    return sum([sum([(factor * i) for i in range((limit // factor) + 1)]) for factor in factors])

class Test(unittest.TestCase):
    def test_calculate_sum(self):
        self.assertEqual(calculate_sum(49, [7]), 196)

if __name__ == "__main__":
    unittest.main(verbosity=2)
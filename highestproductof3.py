#! /usr/bin/env python3
import unittest

def product(*args):
    bal = 1
    for x in args:
        bal = bal * x
    return bal

def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise Exception('not enough ints')

    hpo2 = product(*list_of_ints[:2])
    highest = max(list_of_ints[:2])
    lpo2 = product(*list_of_ints[:2])
    lowest = min(list_of_ints[:2])
    hpo3 = product(*list_of_ints[:3])
    
    
    for i in range(2, len(list_of_ints)):
        current = list_of_ints[i]
        hpo3 = max(hpo3, product(hpo2, current), product(lpo2, current))
        hpo2 = max(hpo2, product(highest, current), product(lowest, current))
        lpo2 = min(lpo2, product(highest, current), product(lowest, current))
        highest = max(highest, current)
        lowest = min(lowest, current)
    
    return hpo3


class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])

if __name__ == '__main__':
    unittest.main(verbosity=2)
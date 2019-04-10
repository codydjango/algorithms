#! /usr/bin/env python3
import unittest

def reverselist(arr):
    l = 0
    r = arrlen = len(arr) - 1

    while l < r:
        r = arrlen - l
        arr[l], arr[r] = arr[r], arr[l]
        l += 1

    return arr

class Test(unittest.TestCase):
    def test_passes_easy(self):
        actual = [1,2,3,4,5,6]
        expected = [6,5,4,3,2,1]
        
        self.assertEqual(reverselist(actual), expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
#! /usr/bin/env python3

import unittest

# runs in O(log n), not in place though...
def merge_halves(arr1, arr2):
    tmp = []

    while len(arr1) and len(arr2):
        if arr1[0] <= arr2[0]:
            tmp.append(arr1.pop(0))
        else:
            tmp.append(arr2.pop(0))
    
    if len(arr1) > 0:
        tmp.extend(arr1)
    
    if len(arr2) > 0:
        tmp.extend(arr2)

    return tmp

# runs in O(log n) but space complexity kinda sucks because of all the temp arrays
# but since it only uses the temp arrays at different times throughout the algorithm lifecycle, it's not so bad.
def mergesort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr

    m = len(arr) // 2

    return merge_halves(mergesort(arr[:m]), mergesort(arr[m:]))


class Test(unittest.TestCase):
    def test_mergesort(self):
        self.assertEqual(mergesort([1,4,3,2,5,9,8,7,6]), [1,2,3,4,5,6,7,8,9])

if __name__ == '__main__':
    unittest.main(verbosity=2)

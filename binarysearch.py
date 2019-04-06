#! /usr/bin/env python3

import unittest
# also known as chopsearch, binary chop, logarithmnic search, half-interval search.
# this is good for sorted arrays, or arrays that have seen a rotation.
# search by repeated diving the search in half
# worst case is O(log n)
# constant space
def binarysearch_bad(arr, needle, l, r):
    if l == r:
        return -1
    
    if r - l == 1:
        if arr[l] == needle:
            return l
        else:
            return -1
        
    mid = l + ((r - l) // 2)

    if (arr[mid] == needle):
        return mid

    if arr[mid] > needle:
        return binarysearch(arr, needle, l, mid)
    
    if arr[mid] < needle:
        return binarysearch(arr, needle, mid, r)

# this is nicer recursion. implemented with slices, which are references to original array so no increase in space complexity and
# reduced logic complexity.
def binarysearchrecursive(arr, needle):
    target = len(arr) // 2

    if (len(arr) == 1 and arr[0] != needle):
        raise Exception('{0} not in list'.format(needle))

    if arr[target] == needle:
        return target
    elif arr[target] > needle:
        return binarysearchrecursive(arr[:target], needle)
    else:
        return target + binarysearchrecursive(arr[target:], needle)


# Iterative approach, no recursion
# time complexity of O(nlogn), time complexity of O(n)
def binarysearch(arr, needle):
    left = -1 
    right = len(arr)

    while left + 1 < right:
        distance = right - left
        guess = left + (distance // 2)

        if arr[guess] == needle:
            return guess
        elif arr[guess] > needle:
            right = guess
        else:
            left = guess
    return -1 # not found


class Test(unittest.TestCase):
    def test_notfound(self):
        self.assertEqual(binarysearch([1,2,3,4,5,6,7,8,9,10], 0), -1)

    def test_found(self):
        self.assertEqual(binarysearch([1,2,3,4,5,6,7,8,9,10], 3), 2)

    def test_notfoundrecursive(self):
        self.assertRaises(Exception, binarysearchrecursive, [1,2,3,4,5,6,7,8,9,10], 0)

    def test_foundrecursive(self):
        self.assertEqual(binarysearchrecursive([1,2,3,4,5,6,7,8,9,10], 3), 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)

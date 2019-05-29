#! /usr/bin/env python3
from heapq import heappush, heappop
import unittest

def peek(hp):
    try:
        return hp[0]
    except IndexError:
        return 0

def get_median(mnhp, mxhp):
    if len(mnhp) > len(mxhp):
        return peek(mnhp)
    
    if len(mxhp) > len(mnhp):
        return 0 - peek(mxhp)
    
    try:
        return (peek(mnhp) + (0 - peek(mxhp))) / 2.0
    except ZeroDivisionError:
        return 0

def rebalance(mnhp, mxhp):
    if abs(len(mnhp) - len(mxhp)) == 2:
        if len(mnhp) > len(mxhp):
            heappush(mxhp, 0 - heappop(mnhp))
        else:
            heappush(mnhp, 0 - heappop(mxhp))

def running_medium(vals):
    mnhp = []
    mxhp = []

    median = get_median(mnhp, mxhp)
    results = []

    for val in vals:
        if val > median:
            heappush(mnhp, val)
        elif val < median:
            heappush(mxhp, 0 - val)
        else:
            heappush(mxhp, 0 - val)
        
        rebalance(mnhp, mxhp)
        
        median = get_median(mnhp, mxhp)

        results.append(median)
    
    return results


class Test(unittest.TestCase):
    def test_mxheap(self):
        hp = []
        heappush(hp, -5)
        heappush(hp, -2)
        heappush(hp, -10)

        self.assertEqual(0 - hp[0], 10)
    
    def test_mnheap(self):
        hp = []
        heappush(hp, 5)
        heappush(hp, 2)
        heappush(hp, 10)

        self.assertEqual(hp[0], 2)
    
    def test_running_medium1(self):
        actual = running_medium([0])
        expects = [0]
        self.assertEqual(actual, expects)
    
    def test_running_medium2(self):
        actual = running_medium([2])
        expects = [2]
        self.assertEqual(actual, expects)
    
    def test_running_medium3(self):
        actual = running_medium([2, 1])
        expects = [2, 1.5]
        self.assertEqual(actual, expects)

    def test_running_medium4(self):
        actual = running_medium([2, 1, 5])
        expects = [2, 1.5, 2]
        self.assertEqual(actual, expects)
    
    def test_running_medium5(self):
        actual = running_medium([2, 1, 5, 7])
        expects = [2, 1.5, 2, 3.5]
        self.assertEqual(actual, expects)
    
        actual = running_medium([2, 1, 5, 7, 2, 0, 5])
        expects = [2, 1.5, 2, 3.5, 2, 2, 2]
        self.assertEqual(actual, expects)

if __name__ == '__main__':
    unittest.main(verbosity=2)
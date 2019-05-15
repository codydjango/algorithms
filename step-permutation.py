#! /usr/bin/env python3
import unittest

# using heaps algorithm (decrease and conquer)
# def generate(l, s, e, perms=[]):
#     if s == e:
#         perms.append(l)
#     else:    
#         for i in range(s, e + 1):
#             ll = l[:]
#             ll[s], ll[i] = ll[i], ll[s]
#             generate(ll, s + 1, e, perms)
    
#     return perms

def generate(n, l, s, e):
    perms = []

    if sum(perms) == n:
        return perms
    
    for i in range(len(n)):
        for j in l:
            while sum(perms) < 4:
                pass
    return perms

def step_permutation(n, l):
    print('step_permutation', n, l)
    # first get all permutations of list
    # then contrain to limit
    
    perms = generate(n, l, 0, len(l) - 1)
    print('perms', perms)


# recursion
def fib_rec(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    if n == 2:
        return 1

    return fib_rec(n - 2) + fib_rec(n - 1)
        
# no recursion
def fib_iter(n):
    if n == 0:
        return 0

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fib_offset(n):
    if n == 0:
        return 1

    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
    return a

# no cache
# def staircase(n, X):
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     elif n in X:
#         return 1 + sum(staircase(n - x, X) for x in X if x < n)
#     else:
#         return sum(staircase(n - x, X) for x in X if x < n)

# dynamic staircase with cache
# https://dailycodingproblem.com/blog/staircase-problem/
def staircase(n, X):
    cache= [0 for _ in range(n + 1)]
    cache[0] = 1

    for i in range(n + 1):
        cache[i] += sum(cache[i - x] for x in X if (i - x) > 0)
        cache[i] += 1 if i in X else 0
    
    print(cache)
    return cache[-1]


class Test(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib_rec(0), 0)
        self.assertEqual(fib_iter(0), 0)
        self.assertEqual(fib_rec(1), 1)
        self.assertEqual(fib_iter(1), 1)
        self.assertEqual(fib_rec(2), 1)
        self.assertEqual(fib_iter(2), 1)
        self.assertEqual(fib_rec(3), 2)
        self.assertEqual(fib_iter(3), 2)
        self.assertEqual(fib_rec(4), 3)
        self.assertEqual(fib_iter(4), 3)
        self.assertEqual(fib_rec(5), 5)
        self.assertEqual(fib_iter(5), 5)
        self.assertEqual(fib_rec(6), 8)
        self.assertEqual(fib_iter(6), 8)
        self.assertEqual(fib_rec(7), 13)
        self.assertEqual(fib_iter(7), 13)
    
    def test_fib_offset(self):
        self.assertEqual(fib_offset(1), 1)
        self.assertEqual(fib_offset(2), 2)
        self.assertEqual(fib_offset(3), 3)
        self.assertEqual(fib_offset(4), 4)
        self.assertEqual(fib_offset(5), 8)
        self.assertEqual(fib_offset(6), 13)
        self.assertEqual(fib_offset(7), 17)

    def test_fib_offset(self):
        # use cases:
        # staircase(1, [1,2]) = [[1]]                           # 1
        # staircase(2, [1,2]) = [[1, 1], [2]]                   # 2
        # staircase(3, [1,2]) = [[1, 2], [1, 1, 1], [2, 1]]     # 3
        # staircase(4, [1,2]) = [[1, 2, 1], [1, 1, 1, 1], [2, 1, 1], [1, 1, 2], [2, 1, 1]] # 5

        self.assertEqual(fib_offset(1), 1)
        self.assertEqual(fib_offset(2), 2)
        self.assertEqual(fib_offset(3), 3)
        self.assertEqual(fib_offset(4), 5)
        self.assertEqual(fib_offset(5), 8)
        self.assertEqual(fib_offset(6), 13)
        self.assertEqual(fib_offset(7), 21)

    def test_staircase(self):
        self.assertEqual(staircase(1, [1, 2]), 1)
        self.assertEqual(staircase(2, [1, 2]), 2)
        self.assertEqual(staircase(3, [1, 2]), 3)
        self.assertEqual(staircase(4, [1, 2]), 5)
        self.assertEqual(staircase(5, [1, 2]), 8)
        self.assertEqual(staircase(6, [1, 2]), 13)
        self.assertEqual(staircase(7, [1, 2]), 21)
    
    def test_staircase_mult(self):
        self.assertEqual(staircase(1, [1, 3, 5]), 1)
        self.assertEqual(staircase(2, [1, 3, 5]), 1)
        self.assertEqual(staircase(3, [1, 3, 5]), 2)
        self.assertEqual(staircase(4, [1, 3, 5]), 3)
        self.assertEqual(staircase(5, [1, 3, 5]), 5)
        self.assertEqual(staircase(6, [1, 3, 5]), 8)
        self.assertEqual(staircase(7, [1, 3, 5]), 12)
        self.assertEqual(staircase(8, [1, 3, 5]), 19)
        self.assertEqual(staircase(9, [1, 3, 5]), 30)


if __name__ == "__main__":
    unittest.main(verbosity=2)
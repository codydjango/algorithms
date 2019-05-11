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
    

def sieve_of_eratosthenes(n):
    # hard coded because can't generate limit of log(log(1))
    if n == 1:
        return 2

    # the nth number is upper-bound at approximately n * log(n) + n * log(log(n)). 
    # It's not perfect but ok. Works well for n > 3, hence adding 3.
    # https://proofwiki.org/wiki/Approximate_Value_of_Nth_Prime_Number
    limit = 3 + math.ceil((n * math.log(n)) + (n * math.log(math.log(n))))

    sieve = [True] * limit
    count = 0
    # start at 2, since 0 and 1 index are not prime
    for i in range(2, limit):
        if not sieve[i]:
            continue

        count += 1

        if count == n:
            return i

        # mark all multiples as composite
        # start range at prime * prime as an optimization, since composites
        # less than i*i that are divisible by i are already marked earlier.
        for multiple in range(i * i, limit, i):
            sieve[multiple] = False # mark as composite
    

class Test(unittest.TestCase):
    def x_test_trial_division(self):
        self.assertEqual(trial_division(1), 2)
        self.assertEqual(trial_division(2), 3)
        self.assertEqual(trial_division(3), 5)
        self.assertEqual(trial_division(4), 7)
        self.assertEqual(trial_division(10000), 104729)              # test in 0.889s

    def test_sieve(self):
        self.assertEqual(sieve_of_eratosthenes(1), 2)
        self.assertEqual(sieve_of_eratosthenes(2), 3)
        self.assertEqual(sieve_of_eratosthenes(3), 5)
        self.assertEqual(sieve_of_eratosthenes(4), 7)
        self.assertEqual(sieve_of_eratosthenes(5), 11)
        self.assertEqual(sieve_of_eratosthenes(6), 13)
        self.assertEqual(sieve_of_eratosthenes(10), 29)
        self.assertEqual(sieve_of_eratosthenes(10000), 104729)        # test in 0.021s
        self.assertEqual(sieve_of_eratosthenes(100000), 1299709)      # test in 0.278s
        self.assertEqual(sieve_of_eratosthenes(1000000), 15485863)    # test in 3.879s

if __name__ == "__main__":
    unittest.main(verbosity=2)


    # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
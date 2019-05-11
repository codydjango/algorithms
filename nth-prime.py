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

    if n == 1:
        return 2
    elif n == 2:
        return 3
    elif n == 3:
        return 5

    # the nth number is upper-bound at approximately n * log(n) + n * log(log(n)). 
    # It's not perfect but ok.
    # https://proofwiki.org/wiki/Approximate_Value_of_Nth_Prime_Number
    limit = math.ceil((n * math.log(n)) + (n * math.log(math.log(n))))
    sieve = [None] * limit

    prime = 0
    count = 0

    # mark first two spots as not primes, since 0 and 1 are not prime
    sieve[0] = False
    sieve[1] = False

    # loop until we hit all our target kth prime
    while count < n:
        # find next unmarked index and mark it as a prime.
        try:
            while sieve[prime] != None:
                prime += 1
            
            multiple = prime
            sieve[prime] = True # mark as prime
            count += 1
        except IndexError:
            # no more unmarked indexes, exit.
            break

        # mark all multiples
        while (multiple + prime) < limit:
            multiple += prime
            sieve[multiple] = False # mark as composite

    return prime
    

class Test(unittest.TestCase):
    def x_test_trial_division(self):
        self.assertEqual(trial_division(1), 2)
        self.assertEqual(trial_division(2), 3)
        self.assertEqual(trial_division(3), 5)
        self.assertEqual(trial_division(4), 7)
        self.assertEqual(trial_division(10000), 104729)
    #     # self.assertEqual(trial_division(100000), 1299709)

    def test_sieve(self):
        # Ran 1 test in 0.048s
        self.assertEqual(sieve_of_eratosthenes(1), 2)
        self.assertEqual(sieve_of_eratosthenes(2), 3)
        self.assertEqual(sieve_of_eratosthenes(3), 5)
        self.assertEqual(sieve_of_eratosthenes(4), 7)
        self.assertEqual(sieve_of_eratosthenes(10), 29)
        self.assertEqual(sieve_of_eratosthenes(10000), 104729)
        # self.assertEqual(sieve_of_eratosthenes(100000), 1299709)

if __name__ == "__main__":
    unittest.main(verbosity=2)


    # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
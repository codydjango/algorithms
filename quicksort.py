#! /usr/bin/env python3

import random
import sys

# Could be improved to be sorted in place, rather than using extra space
# O(n) time complexity
# o(2n + 1) space complexity
def partition(arr, pivot):
    low = []
    mid = []
    high = []
    for x in range(len(arr)):
        if arr[x] < pivot:
            low.append(arr[x])
        elif arr[x] > pivot:
            high.append(arr[x])
        else:
            mid.append(arr[x])
    return low, mid, high

# This is a recursive version of quicksort that runs in O(n log n).
# Unfortuantely the space complexity is higher in worse case, as space is tied up until the
# Recursion tail resolves.
def quicksort(arr):	
    if not arr: 
        return []

    pivot  = random.choice(arr)
    low, mid, high = partition(arr, pivot)
    return quicksort(low) + mid + quicksort(high)


if __name__ == '__main__':
    print(quicksort([1,5,2,3,5,6,3,6,2,55,22,33,54,33,21,64,85,8,5,43,56,75]))
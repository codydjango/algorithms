#! /usr/bin/env python3

# this is a very slow algorithm. 
# O(n) passes through the array, and each pass is O(n) time, which means worst case is 0(n^2), running in 
# exponential time.
def bubblesort(arr):	
    if not arr: 
        raise Exception('no provided array')

    i = swapped = 0

    while True:
        if i == len(arr) - 1:
            if not swapped: break
            else: i = swapped = 0
        
        if (arr[i] <= arr[i + 1]):
            i += 1
            continue
        
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        swapped = 1


if __name__ == '__main__':
    arr = [1,5,2,3,5,6,3,6,2,55,22,33,54,33,21,64,85,8,5,43,56,75]
    bubblesort(arr)
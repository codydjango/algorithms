#! /usr/bin/env python3

# runs in O(log n)
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


if __name__ == '__main__':
    arr = [1,4,3,2,5,9,8,7,6]
    print('original', arr)
    print('sorted', mergesort(arr))
#! /usr/bin/env python3

# also known as chopsearch, binary chop, logarithmnic search, half-interval search.
# this is good for sorted arrays, or arrays that have seen a rotation.
# search by repeated diving the search in half
# worst case is O(log n)
# constant space
def binarysearch(arr, needle, l, r):
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

# this is nicer. implemented with slices, which are references to original array so no increase in space complexity and
# reduced logic complexity
def binarysearch2(arr, needle):
    target = len(arr) // 2

    if (len(arr) == 1 and arr[0] != needle):
        raise Exception('{0} not in list'.format(needle))

    if arr[target] == needle:
        return target
    elif arr[target] > needle:
        return binarysearch2(arr[:target], needle)
    else:
        return target + binarysearch2(arr[target:], needle)

if __name__ == '__main__':
    print(binarysearch2([1,2,3,4,5,6,7,8,9,10], 0))

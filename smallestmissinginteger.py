#! /usr/bin/env python3

def getInt(i):
    while True:
        yield i
        i += 1

# return the smallest positive integer (greater than 0) that does not occur in A
def smallestmissinginteger(arr=[]):
    if not arr:
        return 1

    # sort it
    arr.sort()
    getI = getInt(0)
    t = next(getI)

    # if the whole thing is negative, throw it out
    if arr[-1] < 0: 
        return 1
    
    for x in arr:
        if x <= 0:
            continue
        elif x == t:
            continue
        else:
            t = next(getI)
            if x == t:
                continue
            else:
                return t
    else:
        t = next(getI)
        return t

def smallestmissinginteger2(arr):
    x = set(arr)
    i = 0
    while True:
        i += 1
        if i in x:
            continue
        return i

if __name__ == '__main__':
    print(smallestmissinginteger2(), 1)
    print(smallestmissinginteger2([]), 1)
    print(smallestmissinginteger2([-1]), 1)
    print(smallestmissinginteger2([0]), 1)
    print(smallestmissinginteger2([1]), 2)
    print(smallestmissinginteger2([2]), 1)
    print(smallestmissinginteger2([1, 3, 6, 4, 1, 2]), 5)
    print(smallestmissinginteger2([1, 2, 3]), 4)
    print(smallestmissinginteger2([-1, -3]), 1)
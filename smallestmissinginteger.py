#! /usr/bin/env python3

def getInt():
    i = 0
    while True:
        i += 1
        yield i

# return the smallest positive integer (greater than 0) that does not occur in A
def smallestmissinginteger(arr):
    # sort it
    arr.sort()
    getI = getInt()
    t = next(getI)

    # if the whole thing is negative, throw it out
    if arr[-1] < 0: 
        return 1
    
    for x in arr:
        if x <= 0:
            continue
        elif x == t:
            # found t, next
            continue
        else:
            # didn't find t, so check next t:
            t = next(getI)
            if x == t:
                continue
            else:
                return t
    else:
        return t


if __name__ == '__main__':
    print(smallestmissinginteger([1, 3, 6, 4, 1, 2]), 5)
    print(smallestmissinginteger([1, 2, 3]), 4)
    print(smallestmissinginteger([-1, -3]), 1)
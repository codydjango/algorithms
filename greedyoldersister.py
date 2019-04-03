#! /usr/bin/env python3


# each item in array represents a candy, with the int value representing the type of candy.
# the older sister is forced to share half with her younger brother, but wants to make sure she
# gets as many different kinds as possible.
def greedyoldersister(arr=[]):
    numeach = len(arr) // 2
    setarr = set(arr)
    sister = []
    brother = []


    for x in setarr:
        sister.append(arr.pop(arr.index(x)))

    # give the rest to brother
    brother = arr

    # equalize out
    if len(brother) > len(sister):
        cut = numeach - len(sister)
        sister.extend(brother[:cut])
        brother = brother[cut:]
    
    elif len(sister) > len(brother):
        cut = numeach - len(brother)
        brother.extend(sister[:cut])
        sister = sister[cut:]

    return len(list(set(sister)))

if __name__ == '__main__':
    assert(greedyoldersister([80, 80, 80, 40, 12, 1, 2, 4, 4, 50]) == 5)
    assert(greedyoldersister([1, 1, 1, 2, 2, 2, 7, 8]) == 4)
    assert(greedyoldersister([1, 1, 1, 2, 2, 3, 7, 8]) == 4)
    assert(greedyoldersister([1, 1, 1, 2, 2, 3, 7, 7]) == 4)
    assert(greedyoldersister([1, 2, 3, 4, 5, 6, 7, 8]) == 4)
    assert(greedyoldersister([1, 1, 2, 2, 3, 3, 4, 4]) == 4)
    assert(greedyoldersister([1, 1, 1, 2, 2, 2, 3, 3]) == 3)
    assert(greedyoldersister([1, 1, 1, 1, 2, 3, 4, 5]) == 4)
    assert(greedyoldersister([1, 1, 1, 1, 1, 1, 1, 1]) == 1)
    assert(greedyoldersister([1, 1, 1, 1, 1, 1, 1, 2]) == 2)
    assert(greedyoldersister([1, 1, 1, 1, 1, 2, 2, 2]) == 2)
    assert(greedyoldersister([1, 1, 1, 1, 1, 1, 2, 3]) == 3)
    assert(greedyoldersister([1, 1, 1, 1, 1, 2, 3, 4]) == 4)
    assert(greedyoldersister([1, 2, 3, 4, 5, 6, 7, 8]) == 4)
    assert(greedyoldersister([1, 1, 3, 4, 5, 6, 7, 8]) == 4)
    assert(greedyoldersister([1, 1, 1, 4, 5, 6, 7, 8]) == 4)
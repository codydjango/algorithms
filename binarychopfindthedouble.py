#! /usr/bin/env python3
import unittest, random



def randomize_in_place(longlist):
    arrlen = len(longlist)
    for i in range(arrlen):
        r = random.randrange(i, arrlen)
        longlist[i], longlist[r] = longlist[r], longlist[i]

def find_first_double(list_of_ints):
    if len(list_of_ints) < 2:
        raise Exception('not enough ints')


    # it's gonna keep trying until we find it
    # I'm gonna try "pidgeonholing", to narrow down the chops until
    # we find the chop with the duplicate.
    # to find the chop with the duplicate, we have to look at 
    # the number of items in the chop, and the number of distinct elements in the chop.
    # if the number of distinct elements in the chop is larger than the number of items, we've
    # found the duplicate.

    l = 1
    r = len(list_of_ints) - 1

    # loop through all possibilities of numbers, narrowing the window
    # of numbers that could possibly be used, using the chop method.
    while l < r:
        mid = l + (r - l) // 2

        ll, lr = l, mid
        ul, ur = mid + 1, r


        # get number of items in lower range
        num_of_items = 0
        for item in list_of_ints:
            if item >= ll and item <= lr:
                num_of_items += 1

        # get distinct in the chop
        distinct = lr - ll + 1

        # print('l & r', l, r)
        # print('num_of_items', num_of_items)
        # print('distinct', distinct)

        if num_of_items > distinct:
            l, r = ll, lr
        else:
            l, r = ul, ur
    
    # return the repeating number
    return l

testlist = [84, 76, 43, 58, 42, 94, 67, 15, 87, 49, 86, 34, 97, 99, 40, 66, 31, 83, 79, 55, 85, 27, 71, 3, 45, 16, 69, 61, 73, 62, 26, 32, 24, 80, 17, 41, 36, 70, 78, 5, 57, 95, 81, 8, 6, 92, 46, 28, 9, 21, 91, 12, 54, 77, 29, 39, 53, 44, 11, 60, 63, 88, 10, 100, 20, 96, 38, 7, 72, 25, 18, 13, 2, 93, 14, 68, 51, 35, 82, 23, 37, 48, 22, 19, 50, 59, 98, 56, 1, 89, 52, 4, 90, 47, 33, 30, 64, 65, 74, 75]

class Test(unittest.TestCase):

    # def test_make_random_longlist(self):
    #     longlist = [x for x in range(1, 101)]
    #     randomize_in_place(longlist)
    #     sortedlist = sorted(longlist)
    #     print(longlist)
    #     print(sortedlist)
    
    def test_binarychopofdouble1(self):
        testlist = [84, 76, 43, 58, 42, 94, 67, 15, 87, 49, 86, 34, 97, 99, 40, 66, 31, 83, 79, 55, 85, 27, 71, 3, 45, 16, 69, 61, 73, 62, 26, 32, 24, 80, 17, 41, 36, 70, 78, 5, 57, 95, 81, 8, 6, 92, 46, 28, 9, 21, 91, 12, 54, 77, 29, 39, 53, 44, 11, 60, 63, 88, 10, 100, 20, 96, 38, 7, 72, 25, 18, 13, 2, 93, 14, 68, 51, 35, 82, 23, 37, 48, 22, 19, 50, 59, 98, 56, 1, 89, 52, 4, 90, 47, 33, 30, 64, 65, 74, 75]
        testlist.insert(12, 33)

        self.assertEqual(find_first_double(testlist), 33)

    def test_binarychopofdouble2(self):
        testlist = [1, 1]

        self.assertEqual(find_first_double(testlist), 1)
    
    def test_binarychopofdouble3(self):
        testlist = [1, 2, 2, 3]

        self.assertEqual(find_first_double(testlist), 2)

    def test_binarychopofdouble4(self):
        testlist = [83, 1, 2, 2, 3, 4, 5, 4]

        self.assertEqual(find_first_double(testlist), 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
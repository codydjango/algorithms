#! /usr/bin/env python3

import unittest

# Ranges are for booking a room, with a start end end time for each range.
# Merge all touching or overlapping ranges so we know when the room is free.

# Tuples are immutable
# Don't assume ranges are in order: sort by start key
# Runs in O(n), plus the sort. Python uses timsort for sort, which has 
# a time complexity of O(nlogn). So in total, we have O(n + nlogn), drop
# the constants, O(nlogn).
def merge_ranges(meetings):
    # sort list by start key
    meetings = sorted(meetings, key=lambda e:e[0])

    # pop the first range and set it as the first
    # potentially extendable range.
    merged = [meetings.pop(0)]
    
    for meeting_start, meeting_end in meetings:
        open_start, open_end = merged[-1]
        if open_end >= meeting_start:
            merged[-1] = (open_start, max(open_end, meeting_end))
        else:
            merged.append((meeting_start, meeting_end))
    
    return merged


class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
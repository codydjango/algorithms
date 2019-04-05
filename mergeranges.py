#! /usr/bin/env python3

import unittest

# Ranges are for booking a room, with a start end end time for each range.
# Merge all touching or overlapping ranges so we know when the room is free.

# Tuples are immutable
# Don't assume ranges are in order: sort by start key
def merge_ranges(meetings):
    # sort list by start key
    meetings = sorted(meetings, key=lambda e:e[0])

    # cast list of tuples into a list of mutable lists
    meetings = [list(x) for x in meetings]

    # pop the first range and set it as the first
    # potentially extendable range.
    merged = [meetings.pop(0)]
    
    for meeting in meetings:
        if merged[-1][1] >= meeting[0]:
            if meeting[1] > merged[-1][1]:
                merged[-1][1] = meeting[1]
        else:
            merged.append(meeting)
    
    # cast back to list of tuples
    return [tuple(x) for x in merged]


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
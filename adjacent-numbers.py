#! /usr/bin/env python3
import unittest

def find_step(grid, target, col, row):
    if col < 0 or row < 0:
        return (False, None, None)

    try:
        if grid[col][row] == target:
            return (True, col, row)
        return (False, None, None)
    except IndexError:
        return (False, None, None)


def find_path_for(grid, start, col, row, current_path, cache):
    target = start + 1

    results = list(filter(lambda f: f[0], [find_step(grid, target, p_col, p_row) for p_col, p_row in [
        (col, row - 1),
        (col + 1, row),
        (col, row + 1),
        (col - 1, row)]]))

    if results:
        if target in cache.keys():
            return current_path + cache[target]

        current_path.append(target)
        return find_path_for(grid, start + 1, results[0][1], results[0][2], current_path, cache)

    cache[current_path[0]] = current_path
    return cache[current_path[0]]

def solve(grid):
    longest_path = []
    current_path = []
    cache = {}

    col_len = len(grid)
    row_len = len(grid[0])

    for col in range(col_len):
        for row in range(row_len):
            start = grid[col][row]
            current_path = find_path_for(grid, start, col, row, [start], cache)
            if len(current_path) > len(longest_path):
                longest_path = current_path
    
    return longest_path


class Test(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve([
            [2, 3, 5, 9],
            [1, 4, 8, 7],
            [6, 10, 12, 11]
        ]), [1, 2, 3, 4])

        self.assertEqual(solve([
            [2, 3,  5,  9,  13, 18],
            [1, 4,  8,  7,  14, 17],
            [6, 10, 12, 11, 15, 16]
        ]), [13, 14, 15, 16, 17, 18])

        self.assertEqual(solve([
            [2, 3,  5,  9,  13, 18, 19],
            [1, 4,  8,  7,  14, 17, 21],
            [6, 10, 12, 11, 15, 16, 20]
        ]), [13, 14, 15, 16, 17, 18, 19])





if __name__ == "__main__":
    unittest.main(verbosity=2)
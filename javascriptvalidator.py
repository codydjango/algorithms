#! /usr/bin/env python3
import unittest

# O(n)
def javascriptvalidator(string):
    open_to_close = {
        "{": "}",
        "[": "]",
        "(": ")"
    }

    openers = set(open_to_close.keys())
    closers = set(open_to_close.values())
    stack = []

    for char in string:
        if char in openers:
            stack.append(open_to_close[char])
        elif char in closers:
            try:
                if stack.pop() != char:
                    return 0
            except IndexError:
                return 0
        else:
            pass
    return 1


class Test(unittest.TestCase):
    def test_passes_easy(self):
        actual = javascriptvalidator("[{[]}]")
        expected = 1
        self.assertEqual(actual, expected)
    
    def test_passes_hard(self):
        actual = javascriptvalidator("""[{foo: "bar", baz: [{bat:[1,2]}, 3, 4]}]""")
        expected = 1
        self.assertEqual(actual, expected)
    
    def test_fails_easy(self):
        actual = javascriptvalidator("[]}")
        expected = 0
        self.assertEqual(actual, expected)

    def test_fails_hard(self):
        actual = javascriptvalidator("""{foo: "bar", baz: [{bat:[1,2]}, 3, 4]}]""")
        expected = 0
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
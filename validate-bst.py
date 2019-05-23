#! /usr/bin/env python3

import unittest
import sys
from collections import deque

# The BST property is that every node on the left subtree has to be smaller than the 
# current node and every every node on the right subtree has to be larger than the current node.
# 
# The we can't simply validate with an inorder traversal because it wont take into account
# that the left subtree is greater than the grandfather, which is the BST property.
#
# The correct solution is to be passing along a context range that shrinks with each iteration
# or recursion. That context enables us to check that the subtree is always according to the
# BST property.

# Runtime: 52 ms, faster than 89.79% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 15.6 MB, less than 67.36% of Python3 online submissions for Validate Binary Search Tree.
def validate_bst_recursive(node, min_value=None, max_value=None):
    if not (min_value and max_value):
        min_value = -sys.maxsize-1
        max_value = sys.maxsize

    if node == None:
        return True
    
    if node.value <= min_value or node.value >= max_value:
        return False
    
    return validate_bst(node.left_node, min_value, node.value) and validate_bst(node.right_node, node.value, max_value)

# Runtime: 48 ms, faster than 97.72% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 15.6 MB, less than 75.85% of Python3 online submissions for Validate Binary Search Tree.
def validate_bst_iterative(node, min_value=None, max_value=None):
    if not (min_value and max_value):
        min_value = -sys.maxsize-1
        max_value = sys.maxsize

    nodes = deque()
    nodes.append((node, min_value, max_value))

    while len(nodes) > 0:
        node, min_value, max_value = nodes.popleft()

        if node == None:
            continue
        
        if node.value <= min_value or node.value >= max_value:
            return False
        
        nodes.append((node.left_node, min_value, node.value))
        nodes.append((node.right_node, node.value, max_value))
    
    return True


validate_bst = validate_bst_iterative

class Node():
    def __init__(self, value):
        self.left_node = None
        self.right_node = None
        self.value = value
    
    def add_right_node(self, value):
        self.right_node = Node(value)
        return self.right_node
    
    def add_left_node(self, value):
        self.left_node = Node(value)
        return self.left_node
    
    def __str__(self):
        return "{}".format(self.value)


class Test(unittest.TestCase):
    def test_validate(self):
        root = Node(10)
        self.assertTrue(validate_bst(root))

    def test_validate2(self):
        root = Node(10)
        root.add_left_node(12)
        self.assertFalse(validate_bst(root))
    
    def test_validate3(self):
        root = Node(10)
        root.add_left_node(5)
        self.assertTrue(validate_bst(root))
    
    def test_validate4(self):
        root = Node(10)
        root.add_left_node(5)
        root.add_left_node(15)
        self.assertFalse(validate_bst(root))

    def test_validate5(self):
        root = Node(10)
        node = root.add_left_node(5)
        node.add_left_node(6)
        self.assertFalse(validate_bst(root))
    
    def test_validate6(self):
        root = Node(10)
        node = root.add_left_node(5)
        node.add_left_node(4)
        node.add_right_node(6)
        root.add_right_node(11)
        self.assertTrue(validate_bst(root))
    
    def test_validate7(self):
        root = Node(10)
        node = root.add_left_node(5)
        right_node = root.add_right_node(25)
        right_node = right_node.add_right_node(27)
        right_node = right_node.add_left_node(24)
        self.assertFalse(validate_bst(root))
    
    def test_validate8(self):
        root = Node(1)
        root.add_left_node(1)
        self.assertFalse(validate_bst(root))

    
if __name__ == "__main__":
    unittest.main(verbosity=2)
#! /usr/bin/env python3

import unittest
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
    
    def addChild(self, val):
        if not hasattr(self, 'left'):
            if val:
                self.left = TreeNode(val)
            else:
                self.left = None
            return self.left
        else:
            if val:
                self.right = TreeNode(val)
            else:
                self.right = None
            
            return self.right
    
    def isFull(self):
        return hasattr(self, 'left') and hasattr(self, 'right')


def inorder_recursive(node: TreeNode, nodes=[]):
    if node == None:
        return nodes
    
    inorder_recursive(node.left, nodes)
    nodes.append(node.val)
    inorder_recursive(node.right, nodes)
    
    return nodes


def inorder_iterative(root: TreeNode):
    to_process = []
    ordered_traversal = []
    
    if root:
        to_process.append((root, True))        
    
    while len(to_process) > 0:
        node, left_branch = to_process.pop()
        
        while node:
            # traverse down left side and queue those we pass
            if left_branch and node.left:
                to_process.append((node, False))
                node = node.left
                continue
            
            # capture the inorder value
            ordered_traversal.append(node.val)
            
            # move to right node. if it doesn't exist the loop breaks and
            # we process next in the queue
            if node.right:
                to_process.append((node.right, True))
            break
    
    return ordered_traversal



def build_tree(nodelist):
    nl = deque(nodelist)
    root = TreeNode(nl.popleft())

    queue = deque([root])
    node = queue.popleft()

    root.all_nodes = [root]

    while len(nl):
        val = nl.popleft()

        if node.isFull():
            node = queue.popleft()

        child = node.addChild(val)
        if child:
            queue.append(child)
            root.all_nodes.append(child)
    
    for node in root.all_nodes:
        if not hasattr(node, 'left'):
            node.left = None
        if not hasattr(node, 'right'):
            node.right = None

    return root


class Test(unittest.TestCase):
    def test_build_tree(self):
        root = build_tree([2, 3, 1])

        self.assertEqual(root.val, 2)
        self.assertEqual(root.left.val, 3)
        self.assertEqual(root.right.val, 1)

        root = build_tree([2, 3, None, 1])

        self.assertEqual(len(root.all_nodes), 3)
        self.assertEqual(root.val, 2)
        self.assertEqual(root.left.val, 3)
        self.assertEqual(root.right, None)
        self.assertEqual(root.left.left.val, 1)

        root = build_tree([3, 2, 4, None, None, 1])

        self.assertEqual(root.val, 3)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 4)
        self.assertEqual(root.left.left, None)
        self.assertEqual(root.left.right, None)
        self.assertEqual(root.right.left.val, 1)
        

    def test_inorder_recursive(self):
        self.assertEqual(inorder_recursive(build_tree([2, 3, 1]), []), [3, 2, 1])
        self.assertEqual(inorder_recursive(build_tree([2, 3, None, 1]), []), [1, 3, 2])
        self.assertEqual(inorder_recursive(build_tree([2, None, 3, 1]), []), [2, 1, 3])
        self.assertEqual(inorder_recursive(build_tree([2, None, 3, None, 1]), []), [2, 3, 1])
        self.assertEqual(inorder_recursive(build_tree([3, 2, 4, None, None, 1]), []), [2, 3, 1, 4])
    
    def test_inorder_iterative(self):
        self.assertEqual(inorder_iterative(build_tree([2, 3, 1])), [3, 2, 1])
        self.assertEqual(inorder_iterative(build_tree([2, 3, None, 1])), [1, 3, 2])
        self.assertEqual(inorder_iterative(build_tree([2, None, 3, 1])), [2, 1, 3])
        self.assertEqual(inorder_iterative(build_tree([2, None, 3, None, 1])), [2, 3, 1])
        self.assertEqual(inorder_iterative(build_tree([3, 2, 4, None, None, 1])), [2, 3, 1, 4])

if __name__ == "__main__":
    unittest.main(verbosity=2)
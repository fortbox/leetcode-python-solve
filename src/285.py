#  Copyright (c) 2020
#  @Author: xiaoweixiang

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        res = None
        while root:
            if root.val > p.val:
                res = root
                root = root.left
            else:
                root = root.right
        return res

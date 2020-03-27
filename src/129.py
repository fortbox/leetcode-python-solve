#  Copyright (c) 2020
#  @Author: xiaoweixiang

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        """
        dfs pre order
        :param root:
        :return:
        """
        res = []

        def dfs(node: TreeNode, ll: List[int]):
            if not node:
                return
            if not node.left and not node.right:
                res.append(ll)
                return
            ll.append(node.val)
            dfs(node.left, ll[:])
            dfs(node.right, ll[:])

        dfs(root, [])
        n = 0
        for r in res:
            print(r)
            s = ""
            for rr in r:
                print(rr)
                s += str(rr)
            n += int(s)
        return n

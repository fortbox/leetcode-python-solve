#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        """
        递归，树的题不用递归都不好意思
        :param N: 
        :return: 
        """
        res = []
        if N == 1: return [TreeNode(0)]
        if not N % 2: return []
        left_n = 1
        right_n = N - 2
        while right_n > 0:
            left = self.allPossibleFBT(left_n)
            right = self.allPossibleFBT(right_n)

            for l in left:
                for r in right:
                    root = TreeNode(0)
                    root.left = l
                    root.right = r
                    res.append(root)
            left_n += 2
            right_n -= 2
        return res

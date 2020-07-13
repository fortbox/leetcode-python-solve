#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        """
        根据前序和后序的特性，来组合
        :param pre:
        :param post:
        :return:
        """
        if not pre: return None
        root = TreeNode(pre[0])
        if len(pre) == 1: return root
        leftLength = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1: leftLength + 1], post[:leftLength])
        root.right = self.constructFromPrePost(pre[leftLength + 1:], post[leftLength:-1])
        return root

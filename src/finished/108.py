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
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        '''
        把中序遍历用bfs打印出来
        很简单
        :param nums:
        :return:
        '''

        if not nums:
            return None
        else:
            mid = len(nums) / 2
            node = TreeNode(nums[mid]);
            nums_left = nums[1:mid]
            nums_right = nums[mid + 1:]
            node.left = self.sortedArrayToBST(nums_left)
            node.right = self.sortedArrayToBST(nums_right)
        return node

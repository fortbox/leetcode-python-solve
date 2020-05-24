#  Copyright (c) 2020
#  @Author: xiaoweixiang

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        '''
        参考官方解题，树的题目就是需要从大局观上来分析
        :param root:
        :return:
        '''

        def max_gain(node: TreeNode):
            nonlocal max_sum
            if not node:
                return 0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            price_newpath = node.val + left_gain + right_gain
            max_sum = max(max_sum, price_newpath)
            return node.val + max(left_gain, right_gain)

        max_sum = float("-inf")
        max_gain(root)
        return max_sum

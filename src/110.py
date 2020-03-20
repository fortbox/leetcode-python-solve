#  Copyright (c) 2020
#  @Author: xiaoweixiang


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        '''
        首先计算左子树的高度，然后计算右子树的高度。然后比较差。
        然后递归判断左子树和右子树，是否是平衡二叉树。
        :param root:
        :return:
        '''
        if not root:
            return True
        return abs(self.calculateHeight(root.right) - self.calculateHeight(root.left)) < 2 \
               and self.isBalanced(root.left) \
               and self.isBalanced(root.right)

    def calculateHeight(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.calculateHeight(root.left), self.calculateHeight(root.right))

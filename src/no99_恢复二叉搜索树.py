#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        """
        先找到错误的那个节点，然后遍历所有节点，来判断交换后是否满足二叉搜索树
        """
        l = self.inorder(root)
        x, y = self.findTwoSwapped(l)
        print(x)
        print(y)

        def re(r: TreeNode) -> None:
            if not r:
                return
            re(r.left)
            if r.val == x:
                r.val = y
            elif r.val == y:
                r.val = x
            re(r.right)

        re(root)

    def inorder(self, r: TreeNode) -> List[int]:
        if r:
            return self.inorder(r.left) + [r.val] + self.inorder(r.right)
        else:
            return []

    def findTwoSwapped(self, nums: List[int]) -> (int, int):
        n = len(nums)
        x = y = -1
        k = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                if k == 0:
                    x = nums[i]
                    y = nums[i + 1]
                    k += 1
                elif k == 1:
                    y = nums[i + 1]
                    break
        return x, y

    def isValidBST(self, root: TreeNode) -> bool:
        """
        验证二叉搜索树，最简单的方法是用中序排序
        :param root:
        :return:
        """

        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not helper(node.left, lower, val):
                return False
            if not helper(node.right, val, upper):
                return False
            return True

        return helper(root)

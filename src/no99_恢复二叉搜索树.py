#  Copyright (c) 2020
#  @Author: xiaoweixiang
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

    def isValidBST(self, root: TreeNode) -> bool:
        '''
        验证二叉搜索树，最简单的方法是用中序排序
        :param root:
        :return:
        '''

#  Copyright (c) 2020
#  @Author: xiaoweixiang


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        """
        题目没看明白。
        左节点-》根节点，根节点-》右节点，右节点-》左节点
        :param root:
        :return:
        """
        parent = parent_right = None
        while root:
            root_left = root.left
            root.left = parent_right
            parent_right = root.right
            root.right = parent
            parent = root
            root = root_left
        return parent

#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
        只想到了重新建立二叉搜索树
        :param root:
        :return:
        """
        all_val = []

        def getAllVal(node: TreeNode) -> None:
            nonlocal all_val
            if not node: return
            getAllVal(node.left)
            all_val.append(node.val)
            getAllVal(node.right)

        def buildTree(ll: List[int]) -> TreeNode:
            if not ll: return None
            index = len(ll) // 2
            node = TreeNode(ll[index])
            node.left = buildTree(ll[:index])
            node.right = buildTree(ll[index + 1:])
            return node

        getAllVal(root)
        return buildTree(all_val)

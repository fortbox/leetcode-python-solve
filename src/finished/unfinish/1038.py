#  Copyright (c) 2020
#  @Author: xiaoweixiang

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        """
        获取总和，然后获取当前节点的左节点的和+（如果是右节点，则加上父节点和父节点的左节点的和）
        :param root:
        :return:
        """

        def getSum(node: TreeNode) -> int:
            if not node: return 0
            return getSum(node.left) + node.val + getSum(node.right)

        all_sum = getSum(root)

        def in_order(node: TreeNode) -> None:
            nonlocal all_sum
            if not node:
                return
            in_order(node.left)
            tmp = node.val
            node.val = all_sum
            all_sum -= tmp
            in_order(node.right)

        in_order(root)
        return root

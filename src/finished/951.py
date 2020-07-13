#  Copyright (c) 2020
#  @Author: xiaoweixiang
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        """
        首先根节点相等，然后1的左子树对2的左子树，1的左子树对2的右子树。
        两种情况都可以.
        :param root1:
        :param root2:
        :return:
        """
        if not root1 and not root2: return True
        if root1 and not root2: return False
        if not root1 and root2: return False
        if root1.val != root2.val: return False
        if self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right):
            return True
        if self.flipEquiv(root1.right, root2.left) and self.flipEquiv(root1.left, root2.right):
            return True
        return False

#  Copyright (c) 2020
#  @Author: xiaoweixiang
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        if root1 is None: return False

        def findVal(node: TreeNode, val: int) -> bool:
            if not node: return False
            return node.val == val or findVal(node.left, val) or findVal(node.right, val)

        if findVal(root2, target - root1.val): return True
        return self.twoSumBSTs(root1.left, root2, target) or self.twoSumBSTs(root1.right, root2, target)

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
    def generateTrees(self, n: int) -> List[TreeNode]:
        """
        其实很多树的问题，归根结底是dfs和bfs。通用解法
        :param n:
        :return:
        """
        if n == 0:
            return []

        def build_trees(left, right) -> List[TreeNode]:
            all_trees = []
            if left > right:
                return [None]
            for i in range(left, right + 1):
                left_trees = build_trees(left, i - 1)
                right_trees = build_trees(i + 1, right)
                for l in left_trees:
                    for r in right_trees:
                        cur_tree = TreeNode(i)
                        cur_tree.left = l
                        cur_tree.right = r
                        all_trees.append(cur_tree)

            return all_trees

        res = build_trees(1, n)
        return res


if __name__ == '__main__':
    s = Solution()
    r = s.generateTrees(10)
    print(len(r))

#  Copyright (c) 2020
#  @Author: xiaoweixiang

# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        用bfs，然后用一个来维护正序、反序
        :param root:
        :return:
        """
        if not root:
            return []
        level = 0
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            tmp = []
            lens = len(queue)
            for i in range(lens):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2 == 0:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
            level += 1
        return res

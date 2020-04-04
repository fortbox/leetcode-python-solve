#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from queue import Queue


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        还是比较清晰的思路，用一个队列来bfs
        :param root:
        :return:
        """
        q = Queue()
        l = []
        if not root:
            return l
        q.put(root)
        while not q.empty():
            n = q.qsize()
            print("n:", n)
            for i in range(n):
                tmp = q.get()
                if tmp.left:
                    q.put(tmp.left)
                if tmp.right:
                    q.put(tmp.right)
                if i == n - 1:
                    print(tmp.val)
                    l.append(tmp.val)
        return l

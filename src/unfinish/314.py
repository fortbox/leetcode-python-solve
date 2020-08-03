#  Copyright (c) 2020
#  @Author: xiaoweixiang
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        # 自己没思路，参考了powcai的思路
        from collections import deque, defaultdict
        if not root: return []
        queue = deque([(0, root)])
        my_dict = defaultdict(list)
        while len(queue) > 0:
            idx, node = queue.pop()
            my_dict[idx].append(node.val)
            if node.left:
                queue.appendleft((idx - 1, node.left))
            if node.right:
                queue.appendleft((idx + 1, node.right))
        return [val for idx, val in sorted(my_dict.items(), key=lambda x: x[0])]

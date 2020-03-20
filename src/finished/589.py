#  Copyright (c) 2020
#  @Author: xiaoweixiang


# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        redList = []
        if not root:
            return redList
        redList.append(root.val)
        for node in root.children:
            redList.extend(self.preorder(node))
        return redList

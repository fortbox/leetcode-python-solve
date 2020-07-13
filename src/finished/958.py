#  Copyright (c) 2020
#  @Author: xiaoweixiang
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from queue import Queue


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        """
        记录节点和它的序号，看看序号是否连续
        :param root: 
        :return: 
        """
        q = Queue()
        q.put([root, 0])
        dep = 0
        while q.qsize() > 0:
            sz = q.qsize()
            tmp = []
            for _ in range(sz):
                t = q.get()
                if t[0].left:
                    q.put([t[0].left, t[1] * 2])
                if t[0].right:
                    q.put([t[0].right, t[1] * 2 + 1])
                tmp.append(t[1])
            print("tmp:", tmp)
            if q.qsize() == 0:
                if tmp[0] != 0: return False
                for i in range(1, len(tmp)):
                    if tmp[i] != tmp[i - 1] + 1:
                        return False
            else:
                if len(tmp) != 2 ** dep: return False
            dep += 1
        return True

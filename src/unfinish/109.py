#  Copyright (c) 2020
#  @Author: xiaoweixiang
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        pass

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """
        获取中间的结点作为root，然后左右递归
        :param head:
        :return:
        """
        if not head:
            return None
        mid = self.findMiddle(head)
        node = TreeNode(mid.val)

        if head == mid:
            return node
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node

    def findMiddle(self, head: ListNode) -> ListNode:
        pre = None
        slow = head
        fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        if pre:
            pre.next = None
        return slow

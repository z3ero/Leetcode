# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return False
            fast, slow = fast.next.next, slow.next
            if fast==slow: break
        return True
        
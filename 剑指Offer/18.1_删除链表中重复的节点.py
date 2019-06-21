# -*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        ph=ListNode(0)
        ph.next=pHead
        pre=ph
        cur=ph.next
        while cur and cur.next:
            if cur.val==cur.next.val:
                while cur.next and cur.val==cur.next.val:
                    cur=cur.next
            else:
                pre.next=cur
                pre=pre.next
            cur=cur.next
        pre.next=cur
        return ph.next
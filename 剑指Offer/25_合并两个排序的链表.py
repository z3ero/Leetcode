# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    # 思路：不使用辅助空间
    def Merge(self, pHead1, pHead2):
        # write code here
        res = ListNode(0)
        p = res
        while pHead1 is not None and pHead2 is not None:
            if pHead1.val <= pHead2.val:   # 将小的放入辅助空间
                p.next = pHead1
                p = p.next
                pHead1 = pHead1.next
            else:
                p.next = pHead2
                p = p.next
                pHead2 = pHead2.next
                
        if pHead1 is None:
            p.next = pHead2
        if pHead2 is None:
            p.next = pHead1
        return res.next



# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    # 思路：递归解法
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        if pHead1.val <= pHead2.val:
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2
            
        
                
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 思路：
    # 1. 先判断是否存在环，若存在，返回一个环内节点
    def getNodeOfLoop(self, pHead):
        if pHead is None:
            return None
        # 两个指针，一快，一慢
        p_slow = pHead
        p_fast = p_slow.next
        while p_fast is not None: # 快指针没有到头
            if p_fast == p_slow:   # 找到相遇的节点
                return p_fast
            p_slow = p_slow.next  # 慢指针走一步
            p_fast = p_fast.next  # 快指针走两步
            if p_fast is not None:
                p_fast = p_fast.next
        return None
            
    # 2. 统计环内节点数目
    def CountNodeOfLoop(self, tmp_p):
        count = 1
        meet_node = tmp_p
        while tmp_p.next != meet_node:
            tmp_p = tmp_p.next
            count += 1
        return count
    # 3. 找到入口节点
    def EntryNodeOfLoop(self, pHead):
        meet_node = self.getNodeOfLoop(pHead)  # 返回环内节点
        if meet_node is None:
            return None
        num = self.CountNodeOfLoop(meet_node)  # 统计环内节点数目
        # 找入口节点: 两个节点，一个节点先走 n 步, 然后二者同样速度后移
        p_pre = pHead
        p_beh = pHead
        for i in range(num):
            p_pre = p_pre.next
        while p_beh != p_pre:
            p_pre = p_pre.next
            p_beh = p_beh.next
        return p_pre
#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = ListNode(0), ListNode(0)
        p1.next, p2.next = l1, l2
        carry_sign = 0
        while p1.next is not None and p2.next is not None:
            sum_val = p1.next.val + p2.next.val + carry_sign
            carry_sign = sum_val//10
            p1.next.val = sum_val % 10
            p1, p2 = p1.next, p2.next
        if p2.next is not None:
            p1.next = p2.next
        while carry_sign != 0:
            if p1.next is not None:
                sum_val = p1.next.val + carry_sign
                carry_sign = sum_val //10
                p1.next.val = sum_val%10
                p1 = p1.next            
            else:
                p1.next = ListNode(1)
                carry_sign = 0
        return l1

#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 思路: 先将对应节点相加，组成一个链表，然后再逐个处理
        res = ListNode(-1)
        l3 = res
        while True:
            l1.val += l2.val
            l3.next = l1
            
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
            if l1 is None:
                l3.next = l2
                break
            if l2 is None:
                l3.next = l1
                break
        # 对这个链表作单独的进位处理
        l3 = res
        carry = 0
        while l3.next is not None:
            l3.next.val += carry
            if l3.next.val >= 10:
                carry = 1
                l3.next.val -= 10
            else:
                carry = 0
            l3 = l3.next
        if carry > 0:
            l3.next = ListNode(1)
        return res.next   

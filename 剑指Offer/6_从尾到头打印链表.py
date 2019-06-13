# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 使用栈的方式
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        array_list = []
        ll = listNode
        while ll is not None:
            array_list.append(ll.val)
            ll = ll.next
        return array_list[::-1]
        # write code here

# 使用递归函数，速度和内存会更快些
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def recursion(self, ll, array_list):
        if ll is None:
            return;
        if ll.next is not None:
            self.recursion(ll.next, array_list)
        array_list.append(ll.val)
    def printListFromTailToHead(self, listNode):
        array_list = []
        self.recursion(listNode, array_list)
        return array_list
        # write code here
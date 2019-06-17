# [237] Delete Node in a Linked List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        tmp_node = node.next
        node.val = tmp_node.val
        node.next = tmp_node.next
        
# 前提： node 不是尾节点， 整个链表长度 > 2

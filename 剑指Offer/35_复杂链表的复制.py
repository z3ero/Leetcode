# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    # 思路1: 使用hash表空间换时间
    # 1. 先顺序遍历一遍建立 next 链表， 并且对复制节点建立hash表
    # 2. 再顺序遍历一遍，根据hash表 构建 random指针
    # 时间复杂度 O(n)
    def Clone(self, pHead):
        new_head = RandomListNode(-1)
        new_p = new_head
        p = pHead
        # 第一次遍历，只复制 节点值和next值, 并建立hash表
        node_dict = {None:None}
        while p is not None:  # p is not None
            new_p.next = RandomListNode(p.label) # 复制当前节点
            node_dict[p] = new_p.next
            new_p, p = new_p.next, p.next
        # 第二次遍历，构建 random链
        p = pHead
        new_p = new_head.next
        while p is not None:
            new_p.random = node_dict[p.random]
            new_p, p = new_p.next, p.next
        return new_head.next
        # write code here
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 思路:不使用额外的存储空间
    #     遍历两遍，第二遍正向找出第 n-k 个节点，即为倒数第k个节点
    # 考虑异常条件，这三种情况都返回 None
    # 1. k <= 0
    # 2. 链表为空
    # 3. 链表总长 < k
    def FindKthToTail(self, head, k):
        if head is None or k<=0:
            return None
        sum_count = 0
        p = head
        while p is not None:
            sum_count += 1
            p = p.next
        if sum_count < k:
            return None
        p = head
        for i in range(1, sum_count-k+1):
            p = p.next
        return p
        # write code here

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 思路: 只遍历一遍链表
    #     定义两个指针，指针 1 往前指向第k个节点，指针2 指向 头
    #     两个指针同时向后走，当指针1指向结尾，第二个指针即为倒数第 k 个节点
    # 考虑异常条件：
    # 1. 链表为空，K<=0
    # 2. 链表长度 < k
    def FindKthToTail(self, head, k):
        if head is None or k<=0:
            return None
        p1 = head;
        p2 = head;
        for index in range(k):
            if p1 is None:
                return None
            p1 = p1.next
        while p1 is not None:
            p1 = p1.next
            p2 = p2.next
        return p2
        # write code her
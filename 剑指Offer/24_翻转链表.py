class Solution:
    # 返回ListNode
    # 思路：不借助额外存储空间
    def ReverseList(self, pHead):
        # write code here
        if pHead is None:
            return pHead
        p0 = None
        p1 = pHead
        while p1 is not None:
            tmp = p1.next  # 获得下一个节点
            # 每次改变一个链接方向
            p1.next = p0
            # 都往后移动一个节点
            p0 = p1
            p1 = tmp
        return p0

# 思路特点总结: 步步为营，每次移动一个单位
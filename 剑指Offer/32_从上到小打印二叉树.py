# -*- coding:utf-8 -*-
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    # 思路: 使用堆
    def PrintFromTopToBottom(self, root):
        # 使用辅助list
        que_list = []
        res_list = []
        if root is None:
            return que_list
        index = 0
        que_list.append(root)
        while index < len(que_list):
            p = que_list[index]
            res_list.append(p.val)  # 取出队列头元素
            index += 1

            if p.left is not None:
                que_list.append(p.left)
            if p.right is not None:
                que_list.append(p.right)
        return res_list
        # write code here

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
print(sol.PrintFromTopToBottom(root))


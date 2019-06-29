# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsSame(self, R, pRoot2):
        if pRoot2 is None:   # 如果 pRoot2 先走完
            return True
        if R is None:  # 如果 R先走完
            return False
        if R.val == pRoot2.val:   # 根节点相等，才能继续走下去
            return self.IsSame(R.left, pRoot2.left) and self.IsSame(R.right,pRoot2.right)
        else:
            return False
            
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 is None or pRoot2 is None:
            return False
        # 思路:
        # 1. 找出 与 pRoot2 根节点相同的节点 R
        # 2. 判断 该 R 节点的子树是否与 pRoot2相等
        # 先根遍历——递归
        res = False
        if pRoot1.val == pRoot2.val:  # 根节点相同，进行下一步
            res = self.IsSame(pRoot1, pRoot2)
        if not res:
            res = self.HasSubtree(pRoot1.left, pRoot2)
        if not res:
            res = self.HasSubtree(pRoot1.right, pRoot2)
        return res
        # write code here
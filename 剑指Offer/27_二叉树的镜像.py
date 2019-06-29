# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 用递归实现二叉树的镜像
class Solution:
    # 返回镜像树的根节点
    # 思路：对每一棵子树使用递归
    def Mirror(self, root):
        # 递归终止条件： 到叶子节点 即节点为None
        if root is not None:
            root.left, root.right = root.right, root.left
            self.Mirror(root.left)
            self.Mirror(root.right)            
        # write code here

# 用循环实现二叉树的镜像
#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recurs(self, root, result):
        result.append(root.val)
        if root.left is not None:
            self.recurs(root.left, result)
        if root.right is not None:
            self.recurs(root.right, result)
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result = []
        self.recurs(root, result)
        return result

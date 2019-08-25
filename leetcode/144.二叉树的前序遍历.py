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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack = [root]
        result = []
        while len(stack)>0:
            tmp = stack.pop()
            result.append(tmp.val)
            if tmp.right is not None:
                stack.append(tmp.right)
            if tmp.left is not None:
                stack.append(tmp.left)
        return result


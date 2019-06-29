# -*- coding:utf-8 -*-
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    # 思路: 递归，对两个字数分别进行 根 左 右  和 根 右 左 遍历
    def fun(self, root1, root2):
        if root1 is None and root2 is None:  # 遍历到叶子节点
            return True
        if root1 is None or root2 is None:  # 其中有一个为 None
            return False
        
        if root1.val == root2.val: # 不是叶子节点, 但是相等
            return self.fun(root1.left, root2.right) and self.fun(root1.right, root2.left)
        else:
            return False    # 不对称
        
        
    def isSymmetrical(self, pRoot):
        if pRoot is None:   # 空指针情况
            return True
        return self.fun(pRoot.left, pRoot.right)
        # write code here

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
print(sol.isSymmetrical(root))
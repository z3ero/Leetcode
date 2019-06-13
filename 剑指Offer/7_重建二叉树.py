# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution:
    # 递归构建二叉树
    def construct(self, root, pre, tin):
        if len(pre)==0:
            return
        root.val = pre[0]
        if len(pre)==1:
            return
        for i, v in enumerate(tin):
            if v==root.val:
                if i>0:
                    root.left = TreeNode(-1)
                    self.construct(root.left, pre[1:i+1],tin[0:i])
                if i < len(tin)-1:
                    root.right = TreeNode(-1)
                    self.construct(root.right, pre[i+1:],tin[i+1:])
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        root = TreeNode(-1)
        self.construct(root, pre, tin)
        return root
        # write code here
'''


## 更简洁的代码
# -*- coding:utf-8 -*-
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    # 递归构建二叉树
    def construct(self, pre, tin):
        if len(pre) < 1:
            return None
        root = TreeNode(pre[0])
        for i, v in enumerate(tin):
            if v==root.val:
                root.left = self.construct(pre[1:i+1],tin[0:i])
                root.right = self.construct(pre[i+1:],tin[i+1:])
                break
        return root
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        return self.construct(pre, tin)
        # write code here
    
    
# -*- coding:utf-8 -*-
class Solution:
    # 二叉搜索树: 也成二叉排序树
    # 特点： 左子树 < 根 < 右子树
    # 思路: 
    # 1. 最后一个数是根，
    # 2. 前面的数中比根小的是根的左子树，比根大的是根的右子树
    def fun(self, sequence):
        seq_len = len(sequence)
        if seq_len < 1:
            return True
        # 根
        root = sequence[-1]
        index = 0
        left = []
        right = []
        # 左子树
        while index < seq_len-1 and sequence[index] < root:  # 左子树节点
            left.append(sequence[index])
            index += 1
        # 右子树
        while index < seq_len-1 and sequence[index] > root:  # 右子树节点
            right.append(sequence[index])
            index += 1
        # 出来后，如果没有走到尽头，说明右子树不符合规范
        if index != seq_len-1:
            return False
        else:
            return self.fun(left) and self.fun(right)
            
    def VerifySquenceOfBST(self, sequence):
        if len(sequence) < 1: # 空序列，不是二叉排序数
            return False
        if self.fun(sequence):
            return True
        else:
            return False
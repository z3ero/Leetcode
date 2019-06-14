# -*- coding:utf-8 -*-
# 两种解法
# 1. 识别最右边的1，不断右移，直到0 （负数易出现死循环）
# 2. < O(n) 的算法，有几个 1 执行几次循环
class Solution:
    def NumberOf1(self, n):
        if n<0:
            n&=0xffffffff
        count = 0
        while n!=0:
            n&=(n-1)
            count+=1
        return count
        # write code here
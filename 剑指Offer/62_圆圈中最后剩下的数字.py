# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 or m < 1:  # 异常情况
            return -1
        last = 0
        for i in range(2,n+1):    # 从2开始, 往回推n-1步骤
            last = (last+m)%i
        return last
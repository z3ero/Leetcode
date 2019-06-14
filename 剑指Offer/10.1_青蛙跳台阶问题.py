# 同上题斐波那契数列
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # 循环代码
        if number==0: return 1
        if number==1: return 1
        f_s, f_e = 1, 1
        for i in range(2,number+1):
            tmp = f_e
            f_e = f_e + f_s
            f_s = tmp
        return f_e
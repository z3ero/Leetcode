# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        if number==0: return 0
        if number==1: return 1
        if number==2: return 2
        f_s, f_e = 1, 2
        for i in range(3,number+1):
            tmp = f_e
            f_e = f_e + f_s
            f_s = tmp
        return f_e
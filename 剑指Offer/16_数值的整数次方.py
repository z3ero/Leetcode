# -*- coding:utf-8 -*-
# 常规做法
class Solution:
    def Power(self, base, exponent):
        if exponent==0: return 1
        negative_sign = False
        result = 1
        if exponent < 0: 
            negative_sign = True
            exponent = -exponent
        for i in range(0, exponent):
            result *= base
        if negative_sign:
            result = 1/result
        return result
# 高效做法，作 log(exponent) 次乘法
class Solution:
    def fun(self, base, e):
        if e == 0: return 1
        x = self.fun(base, e>>1)
        result = x*x
        if e & 1:
            result *= base
        return result
        
    def Power(self, base, exponent):
        if exponent<0:
            e = -exponent
            return 1.0/self.fun(base, e)
        else:
            e = exponent
            return self.fun(base, e)
        # write code here
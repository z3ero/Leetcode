# 思路：利用 位运算符 和 位移运算 求值
# 两数 与，可以得出哪些地方会进位
# eg: 5&7   101 & 111 = 101  在第1位和第3位进位，进位结果为 101<<1 = 1010
# 两数 异，可以得出哪些地方不进位
# eg: 5^7   101 ^ 111 = 010  第2位不进位，相加结果为 010
# ----- 将上述两个结果，重新看做两个数，重复这个过程，知道进位结果为0，此时异或结果即为最终结果

# -*- coding:utf-8 -*-
class Solution: 
    def Add(self, a, b):           
        while(b): 
           a,b = (a^b) & 0xFFFFFFFF,((a&b)<<1) & 0xFFFFFFFF
        return a if a<=0x7FFFFFFF else ~(a^0xFFFFFFFF)

# 使用 a<=0x7FFFFFFF 是判断是否为正数；因为32位整数，最高1位是负数，
# 如果 a 是负数，直接输出&过0xFFFFFFFF的a是一个很大的整数； 而 ^0xFFFFFFFF 再取反，才能输出真正的负数
# 综上： python 中 整数 & 0xFFFFFFFF 是一个转为无符号数的操作，
#       ^0xFFFFFFFF 再取反，是一个转为有符号数的操作
sol = Solution()
print(sol.Add(-5,-7))
    
1# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        # 思路:
        # 1. 首先找出两个只出现一次数字的异或
        # 边界条件
        if len(array)<2:
            return None
        xor_val = array[0]
        for val in array[1:]:
            xor_val ^= val
        # 2. 求出 xor_val 二进制的第一个n=1的位置
        # 不断右移, 直到遇到第一位 1
        index_bit = 0
        while xor_val & 1 == 0:
            xor_val = xor_val >> 1
            index_bit += 1
        # 3. 在遍历一遍: 这次将 后移index_bit 位为1 异或一次; 再将后移index_bit位为 0的异或一次 
        res_a, res_b = 0,0
        for each in array:
            if (each >> index_bit) & 1 == 0:
                res_a ^= each
            else:
                res_b ^= each
        return [res_a, res_b]
#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#
# 大数据相加问题，这里指明了非负整数
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1)>=len(num2):
            long_num, short_num = num1, num2
        else:
            long_num, short_num = num2, num1
        long_num, short_num = long_num[::-1], short_num[::-1]
        new_num = []
        carry = False
        for i in range(0, len(short_num)):
            tmp = int(long_num[i]) + int(short_num[i]) + carry
            carry = tmp >= 10
            new_num.append(str(tmp % 10))
        for i in range(len(short_num), len(long_num)):
            tmp = int(long_num[i]) + carry
            carry = tmp >= 10
            new_num.append(str(tmp % 10))
        if carry:
            new_num.append('1')
        return ''.join(new_num[::-1])
            

        


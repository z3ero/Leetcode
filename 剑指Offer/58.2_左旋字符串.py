# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # 思路: 将循环右移 取余
        #      1. 长度为 len 的字符串，左移 len 还是它本身
        #      2. 循环左移 n 相当于将 字符串 0-n的字符串 补 n-len的字符串后面
        str_len = len(s) # 字符串长度
        if str_len < 1: # 特殊情况，字符串为空
            return ""
        final_n = n%str_len
        return s[n:] + s[0:n]
        # write code here
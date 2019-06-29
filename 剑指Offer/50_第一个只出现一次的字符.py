# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        # 思路：采用 hash 表， 遍历两次，时间和空间复杂度均为O(n)
        c_map = {}
        for c in s:
            if c in c_map:
                c_map[c]+=1
            else:
                c_map[c]=1
        res = -1
        for index, c in enumerate(s):
            if c_map[c]==1:
                res = index
                break
        return res
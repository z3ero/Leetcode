# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if len(s)==1:
            return s
        res = ' '.join(s.split()[::-1])
        return res
sol = Solution()
s = " " 
print(sol.ReverseSentence(s)+'a')
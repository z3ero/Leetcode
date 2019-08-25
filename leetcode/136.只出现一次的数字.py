#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
from functools import reduce
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x,y:x^y, nums)


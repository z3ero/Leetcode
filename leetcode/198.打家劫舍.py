#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        pre_sum = 0
        pre_pre_sum = 0
        cur_sum = 0
        for each in nums:
            cur_sum = max(pre_sum, pre_pre_sum+each)
            pre_pre_sum = pre_sum
            pre_sum = cur_sum
        return pre_sum
        


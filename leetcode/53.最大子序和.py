#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
class Solution:
    # 思路1：从头到尾遍历累计，累计为负数时，从0开始重新加
    # 思路2:递推公式如下：
    #   f(i) = nums[i]    f(i-1) <= 0
    #   f(i) = f(i-1)+nums[i]  f(i-1) > 0
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return 0
        max_sum = nums[0]
        tmp_sum = 0
        for each in nums:
            if tmp_sum <= 0:
                tmp_sum = each
            else:
                tmp_sum += each
            # 保存最大序列和
            if tmp_sum > max_sum:
                max_sum = tmp_sum
        return max_sum


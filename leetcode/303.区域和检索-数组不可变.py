#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#
# 思路1：暴力求解，两层循环，O(n^2) 会超时
# 思路2：动态规划，只加1遍 保存0-(0~n)的所有累加
#      dp[i][j] = dp[0][j] - dp[0][i]
#  ===> res = dp[j] - dp[i]
class NumArray:

    def __init__(self, nums: List[int]):
        self.accu_list = [0]
        for each in nums:
            acc = self.accu_list[-1] + each
            self.accu_list.append(acc)

    def sumRange(self, i: int, j: int) -> int:
        return self.accu_list[j+1] - self.accu_list[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


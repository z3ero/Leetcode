#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
# 动态规划——递推公式如下
# f(i) = 0      f(i) <= pre_min   不卖
# f(i) = f(i)-pre_min f(i) > pre_min 卖
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 0:
            return 0

        max_pro = 0
        pre_min = prices[0]
        for each in prices:
            if each <= pre_min:
                pre_min = each
                pro = 0
            else:
                pro = each-pre_min
            
            if pro > max_pro:
                max_pro = pro
        return max_pro

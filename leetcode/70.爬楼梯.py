#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
class Solution:
    # 动态规划：递推公式
    # f(i) = f(i-1) + f(i-2)
    # 解释：爬到第 i 层的方法 = 爬到第i-1层的方法 + 爬到第i-2层的方法
    def climbStairs(self, n: int) -> int:
        # 1, 2 阶乘楼梯的 爬法 就是 1, 2
        if n <= 2:
            return n
        x, y = 1,2
        for i in range(3, n+1):
            x, y = y, x+y
        return y

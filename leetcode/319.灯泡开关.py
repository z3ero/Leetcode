#
# @lc app=leetcode.cn id=319 lang=python3
#
# [319] 灯泡开关
# 思路：
#   对于一个数，如果他不是完全平方数，那么他的因数必定是成对出现的，如8: 1和8，2和4
# 因此，只有完全平方数最后是亮着的
# 最后我们只需要求出 n 以内的完全平方数的个数
# math.floor 返回一个小于或者等于给定数字的最大整数，去尾法
class Solution:
    def bulbSwitch(self, n: int) -> int:
        import math
        num = math.floor(math.sqrt(n))
        return num

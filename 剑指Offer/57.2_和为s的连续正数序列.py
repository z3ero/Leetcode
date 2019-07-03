# -*- coding:utf-8 -*-
class Solution:
    # 找到 和为 tsum 的连续正数序列
    # 思路1: 从 1 这个序列开始，定义两个指针 A, B (头, 尾)
    #      1.  若 A+B = tsum 符合
    #      2.  若 A+B < tsum B往后
    #      3.  若 A+B > tsum A往后
    # 注意: 不要重复求序列和
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []     # 至少两个正数的序列, 和最小为3
        final_res = []
        head, tail = 1,2
        cur_sum = head + tail   # 当前和
        while head < tail:
            if cur_sum == tsum:
                final_res.append(list(range(head, tail+1)))
                tail += 1
                cur_sum += tail
            elif cur_sum < tsum:
                tail += 1
                cur_sum += tail
            else:
                cur_sum -= head
                head += 1
        return final_res
        # write code here
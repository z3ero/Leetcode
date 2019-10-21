#
# @lc app=leetcode.cn id=1124 lang=python3
#
# [1124] 表现良好的最长时间段
#

# @lc code=start
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # 1. 统计 hours 总体上，劳累天数 和 不劳累天数
        long_days = short_days = 0
        for h in hours:
            if h > 8: long_days += 1
            else: short_days += 1
        all_days = len(hours)
        if long_days > short_days:
            return all_days
        else:   # 从两头逐步减，使得 long_days > short_days, 选出最好的
            head_long_days = tail_long_days = long_days
            head_short_days = tail_short_days = short_days
            head_all_days = tail_all_days = all_days
            # 从头开始删
            index = 0
            while index < all_days and head_long_days <= head_short_days:
                if hours[index] > 8: head_long_days-=1
                else: head_short_days-=1
                head_all_days -= 1
                index += 1
            # 从尾开始删
            index = all_days-1
            while index >= 0 and tail_long_days <= tail_short_days:
                if hours[index] > 8: tail_long_days-=1
                else: tail_short_days-=1
                tail_all_days -= 1
                index -= 1         
            return max(head_all_days, tail_all_days)
    
# @lc code=end


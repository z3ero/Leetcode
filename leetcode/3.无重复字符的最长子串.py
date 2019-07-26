#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口思路
        start = max_length = 0
        used_dict = {}
        for index in range(len(s)):
            if s[index] in used_dict:
                start = max(start, used_dict[s[index]]+1)
            max_length = max(max_length, index-start+1)
            used_dict[s[index]] = index
        return max_length

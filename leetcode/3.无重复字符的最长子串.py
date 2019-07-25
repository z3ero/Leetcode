#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        usedChar = {}
        start = max_length = 0
        for index, char in enumerate(s):
            # 发现重复字符串，移动start, 生成新的候选最长不重复字符串
            if char in usedChar and start<=usedChar[char]:
                start = usedChar[char] + 1
            else:   # 未发现用过的字符串
                max_length = max(max_length, index-start+1)
            usedChar[char] = index
        return max_length

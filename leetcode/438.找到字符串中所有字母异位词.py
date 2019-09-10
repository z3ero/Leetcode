#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
class Solution:
    def findAnagrams(self, s: str, p: str):
        s_len, p_len = len(s), len(p)
        res_indexs = []
        if s_len < p_len:
            return res_indexs
        from collections import Counter
        p_counter = Counter(p)
        # 先匹配一个窗口
        for i in range(p_len):
            p_counter[s[i]] -= 1    # counter 本身就是一个 defaultdict
            if p_counter[s[i]]==0:
                p_counter.pop(s[i])
        # 滑动窗口，每次移动一个窗口
        for i in range(p_len, s_len):
            if not p_counter:
                res_indexs.append(i-p_len)  # p_counter 为空，说明匹配过一次
            if s[i] == s[i-p_len]:
                continue
            p_counter[s[i]] -= 1
            p_counter[s[i-p_len]] += 1
            if p_counter[s[i]] == 0:
                p_counter.pop(s[i])
            if p_counter[s[i-p_len]]==0:
                p_counter.pop(s[i-p_len])
        if not p_counter:
            res_indexs.append(s_len-p_len)
        return res_indexs

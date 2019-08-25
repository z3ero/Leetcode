#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 马拉车算法 O(n) 时间复杂度
        # 预处理
        s = '#'+'#'.join(s)+'#'
        # RL数组，存储以 i 为中心的回文半径，RL[i]-1 为原始回文字符串的长度
        # MaxRight 表示目前已知回文串所能触及的最右边界
        # pos 是 MaxRight 所对应的回文中心位置
        RL = [0]*len(s)
        MaxRight = 0
        pos = 0
        for i in range(len(s)):
            if i<MaxRight:
                RL[i] = min(RL[2*pos-i], MaxRight-i)
            else:
                RL[i] = 1
            # 尝试以 i 为中心，以目前已有的RL[i]半径，再次向外扩展
            while i-RL[i]>=0 and i+RL[i]<len(s) and s[i-RL[i]]==s[i+RL[i]]:
                RL[i]+=1
            # 更新MaxRight 和 pos
            if RL[i]+i-1 > MaxRight:
                MaxRight = RL[i]+i-1
                pos = i
        # 返回最长的RL[i]半径以及其索引
        max_pos = RL.index(max(RL))
        substring = ''.join(s[max_pos-RL[max_pos]+1: max_pos+RL[max_pos]])
        return substring.replace('#','')

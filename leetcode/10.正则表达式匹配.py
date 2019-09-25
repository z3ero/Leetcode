#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)
        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
        dp[0][0] = True
        for i in range(p_len):
            if p[i] == "*" and dp[0][i - 1]:
                dp[0][i + 1] = True

        for i in range(s_len):
            for j in range(p_len):
                if p[j] == s[i] or p[j] == ".":
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[j] == "*":
                    # 匹配0个
                    if p[j - 1] != s[i]:
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    # 匹配1个或者多个
                    if p[j-1] == s[i] or p[j-1] == ".":
                        dp[i+1][j+1] = (dp[i][j+1] or dp[i+1][j] or dp[i+1][j-1])
        return dp[-1][-1]

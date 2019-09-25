#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 思路： 动态规划
        n, m = len(word1), len(word2)
        dp_list = [[0]*(m+1) for i in range(n+1)]
        # 初始化 dp_list[:, 0] 和 dp_list[0,:] 分别表示：
        # 1. word1[0:0]——>word2[0:j]需要的步骤
        # 2. word1[0:i]——>word2[0:0]需要的步骤
        for i in range(n+1):
            dp_list[i][0]=i
        for j in range(m+1):
            dp_list[0][j]=j
        # 统计其余每个位置，如果执行更改操作，需要0步还是1步，字符相等，不需更改为0步
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1]!=word2[j-1]:
                    dp_list[i][j]=1
        # 统计 word1[0:i] ——> word2[0:j] 步数dp[i][j], dp[i][j] 可能会进行如下操作：
        # 1. 插入操作, dp[i][j] = dp[i][j-1] + 1   
        #       (dp[i][j-1]表示word1[0:i]转word2[0:j-1]需要多少步骤)
        # 2. 删除操作，dp[i][j] = dp[i-1][j] + 1
        # 3. 替换操作，dp[i][j] = dp[i-1][j-1] + 1 or 0  
        #       (word1[i]和word2[j]相等，则为+0)
        # dp[i][j] 取上述三种情况的最小值
        for i in range(1, n+1):
            for j in range(1, m+1):
                dp_list[i][j] = min(dp_list[i-1][j]+1, dp_list[i][j-1]+1, dp_list[i-1][j-1] + dp_list[i][j])
        return dp_list[n][m]



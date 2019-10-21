#
# @lc app=leetcode.cn id=1124 lang=python3
#
# [1124] 表现良好的最长时间段
#

# @lc code=start
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # 思路1: 暴力 + 二分查找 O(NlogN)
        # 思路，前缀和 + 单调栈 O(N)
        n = len(hours)
        score = [0]*n
        for i in range(n):
            if hours[i]>8: score[i]=1
            else: score[i]=-1
        # 前缀和
        presum = [0]*(n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + score[i-1]
        # 至此，原问题可以转化为，求presum两个索引i和j，使j-i最大，并且presum[j]-presum[i]>0
        ans = 0
        stack = []
        # 顺序生成单调栈，栈中元素从第一个元素开始严格单调递减，最后一个元素肯定是数组中的最小元素所在位置
        for i in range(n+1):
            if not stack or presum[stack[-1]] > presum[i]:
                stack.append(i)
        # stack 最终为 [0, 5, 6]
        # 倒序扫描数组，求最大长度坡
        i= n
        while i > ans:
            while stack and presum[stack[-1]] < presum[i]:
                ans = max(ans, i-stack[-1])
                stack.pop()
            i-=1
        return ans
# @lc code=end


#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
class Solution:
    # 思路：使用双向开口的队列
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 异常处理
        if len(nums) <= 0:
            return []
        from collections import deque
        max_list = []
        que = deque([])
        # 先将前 k 的数据入队, 并保持最大元素位于队头
        for i in range(k):
            while len(que) > 0 and nums[i] >= nums[que[-1]]: # 从后向前比我小的元素全部去掉
                que.pop()
            que.append(i)  # 下标入队
        # 滑动窗口，每次将最大的值输出
        for i in range(k, len(nums)):
            max_list.append(nums[que[0]])   # 取出队头下标代表的元素
            # 后面的元素入队，调整队列
            while len(que) > 0 and nums[i] >= nums[que[-1]]:
                que.pop()
            # 若是队中元素 大于 窗口 （队头和当前元素 > size）
            if len(que) > 0 and que[0] <= (i-k):
                que.popleft()
            que.append(i)
        max_list.append(nums[que[0]])
        return max_list


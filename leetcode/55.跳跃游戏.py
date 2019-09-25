#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
class Solution:
    def canJump(self, nums: List[int]) -> bool
        length = len(nums)
        if length==0:
            return True
        for i in range(length-1,-1,-1):
            if length-1-i <= nums[i]:
                if i==0:
                    return True
                else:
                    res = self.canJump(nums[0:i+1])
                    if res:
                        return True
        return False
sol = Solution()

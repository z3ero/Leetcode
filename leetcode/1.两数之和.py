#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 考虑重复元素: 
        # --- 不是一开始就建立好映射hash, 而是一边判断，一边建立hash
        mapper = {}
        length = len(nums)
        for i in range(length):
            result = target - nums[i]
            if result in mapper.keys():
                return [mapper[result], i]
            mapper[nums[i]] = i
        return []

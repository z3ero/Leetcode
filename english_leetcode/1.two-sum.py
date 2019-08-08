#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# 1
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                   return [i,j]
'''
# 2
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            k = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == k:
                    return [i,j]
'''

# 3. 遍历两遍 hash 表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # build key_indice map
        Map = {nums[i]: i for i in range(len(nums))}
        # traverse array to get result
        for each in nums:
            k = target - each
            if k in Map and k != each:
                return [Map[each], Map[k]]

# 4. 一遍 hash 表：将建表和查表集合在一起做   
# 废止：4 与 3 是同一量级的复杂度， 4 更难理解
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        indexs = range(len(nums))
        for i in indexs:
            k = target - nums[i]
            if k in Map:
                return [i, Map[k]]
            else:
                Map[nums[i]] = i
'''


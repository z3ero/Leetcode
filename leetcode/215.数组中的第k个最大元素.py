#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 思路：快排 partition
        start = 0
        end = len(nums)
        index = 0   # 以第一个元素为key进行一次partition
        # 使用 while True 配合 break 实现 do---while
        while True:
            key = nums[index]
            # 从前往后看，大的放左边
            while index+1 < end and nums[index+1] <= key:
                index += 1
            
            while 
            if index+1==K:  # partition后，发现index即第k大元素，则退出
                break
        return nums[index]
        


#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
class Solution:
    def findKthLargest(self, nums, k):
        # 思路：快排 partition
        start = 0
        end = len(nums)
        # 使用 while True 配合 break 实现 do---while
        while True:
            l, r = start, end-1
            key = nums[l] # 以第一个元素为key进行一次partition

            # 升序partition
            while l < r:
                # 从后往看，大的放后面
                while l < r and nums[r] >= key:
                    r -= 1
                nums[l] = nums[r]
                # 从前往后看，小的放前面
                while l < r and nums[l] <= key:
                    l += 1
                nums[r] = nums[l]
            nums[l] = key
            
            # 根据 l 与 k 的大小对数组 进行切片
            if end-l < k:  # 第 k 大数在前面 nums[start:l] 
                end = l   
                k -= end-l
            elif end-l > k: # 第 k 大数 在后面 nums[l+1:end]
                start = l
            else:
                return nums[l]    # 得到 第 k 大的数

nums = [3,2,1,5,6,4]
k = 2
sol = Solution()
print(sol.findKthLargest(nums, k))

#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
class Solution:
    def findKthLargest(self, nums, k):
        '''
        # 思路1：快排 partition 第一种写法
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
                k -= end-l 
                end = l   
            elif end-l > k: # 第 k 大数 在后面 nums[l+1:end]
                start = l+1
            else:
                return nums[l]    # 得到 第 k 大的数
        '''
        '''
        # 思路2: 堆排序，小顶堆: 先将k个元素入堆，堆顶即这k个元素的第k大元素
        # 后面的元素遍历：
        # 1. 小于堆顶的，必然不会是整个数组的第k大元素，不入堆
        # 2. 大于堆顶的，可能会改变 第 k 大元素值，入堆调整，改变堆顶
        import heapq
        return heapq.nlargest(k, nums)[-1]
        '''
        # 思路3：快排——第二种写法
        def partition(left, right):
            key = nums[right]   # 每次选定一个数字，找到它的位置， 本质上应该是随机选的，然后交换到right处
            index = left
            for i in range(left, right):
                if nums[i] < key:    # 小的放在 左边
                    nums[index], nums[i] = nums[i], nums[index]
                    index += 1
            # 一次快排后，index就是 key的最终位置
            nums[right], nums[index] = nums[index], nums[right]
            return index
        
        # 要选出第k小的元素
        def selectKth(left, right, k):
            index = partition(left, right)
            if index == k:   # index 是 第 k 小元素
                return nums[index]
            if index > k:  # 从 nums[left: index-1] 中找 第 k 小元素
                return selectKth(left, index-1, k)
            if index < k:  # 从 nums[index+1:right] 中找 第 k 小元素
                return selectKth(index+1, right, k)
        # 找 第 k 大元素即找 (n-k)th 小元素
        return selectKth(0, len(nums)-1, len(nums)-k)

'''
nums = [2, 1]
k = 1
sol = Solution()
print(sol.findKthLargest(nums, k))
'''                  

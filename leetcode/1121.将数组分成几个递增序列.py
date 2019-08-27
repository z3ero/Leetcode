class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], K:int)->bool:
        from collections import Counter
        nums_counter = Counter(nums)
        max_times = nums_counter.most_common(1)[1]
        if max_times * K > len(nums):
            return False
        else:
            return True
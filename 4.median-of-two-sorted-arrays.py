#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# 思路:
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        if l%2 == 1:
            return self.kth(nums1, nums2, l//2)
        else:
            return (self.kth(nums1, nums2, l//2) + self.kth(nums1, nums2, l//2-1))/2

    def kth(self, a, b, k):
        if len(a) < 1:
            return b[k]
        if len(b) < 1:
            return a[k]

        ia, ib = len(a)//2, len(b)//2
        va, vb = a[ia], b[ib]
        if ia+ib >= k:
            if va > vb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)
        else:
            if va > vb:
                return self.kth(a, b[ib+1:], k-ib-1)
            else:
                return self.kth(a[ia+1:], b, k-ia-1)


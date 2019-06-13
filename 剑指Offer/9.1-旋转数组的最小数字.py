# 二分查找的变形
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        head, tail = 0, len(rotateArray)-1
        while head < tail:
            mid = (head + tail)/2
            if rotateArray[mid] > rotateArray[tail]:
                head = mid+1
            else:
                tail = mid
        return rotateArray[head]
# 二分查找的变形
# -*- coding:utf-8 -*-
# 终止条件：
# 前后连个指针的相邻（程序中保证第一个指针总是在前面的递增序列，后面的指针总是在后面的递增序列）
# 最小元素是最终后面的指针
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        head, tail = 0, len(rotateArray)-1
        while tail-head > 1:     
            mid = (head + tail)/2
            if rotateArray[mid] > rotateArray[tail]:
                head = mid
            else:
                tail = mid
        return rotateArray[tail]
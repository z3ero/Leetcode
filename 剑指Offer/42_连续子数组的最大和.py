# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array) < 1 or not array:
            return None
        maxx = array[0]
        sumx = 0
        for each in array:
            if sumx <= 0:
                sumx = each
            else:
                sumx += each
            if sumx > maxx:
                maxx = sumx
        return maxx 
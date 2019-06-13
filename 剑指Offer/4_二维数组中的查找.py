# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        row_num, col_num = len(array), len(array[0])
        r = 0
        c = col_num-1
        sign = False
        while r < row_num and c >= 0:
            if array[r][c] < target:
                r += 1
            elif array[r][c] > target:
                c -= 1
            else:
                sign = True
                break
        return sign
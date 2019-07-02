# -*- coding:utf-8 -*-
class Solution:
    # 思路1:
    # 1. 建立hash表
    # 2. (s - hash) in hash
    # 时间和空间复杂度都是 O(n)
    def FindNumbersWithSum(self, array, tsum):
        val_dict = {}
        for each in array:
            if each in val_dict:
                val_dict[each] += 1
            else:
                val_dict[each] = 1
        res_list = []
        for key in val_dict:
            tmp_key = tsum - key
            if tmp_key > key and tmp_key in val_dict:  # 小的放在前面
                res_list.append([key, tmp_key])
            elif tmp_key == key and tmp_key in val_dict and val_dict[tmp_key]>1:
                res_list.append([key, tmp_key])
            else:
                continue
        # 输出乘积最小的一组数
        if len(res_list)>0:
            min_index = 0
            min_dot = res_list[0][0] * res_list[0][1]
            for i in range(1, len(res_list[1:])):
                dot = res_list[i][0]*res_list[i][1]
                if min_dot > dot:
                    min_dot = dot
                    min_index = i
            return res_list[min_index]
        else:
            return []     
        # write code here
# -*- coding:utf-8 -*-
from collections import defaultdict
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        # 思路1：字典统计
        result = 0
        length = len(numbers)
        if length <= 0:
            return result
        num_counter = defaultdict(int)
        for num in numbers:
            num_counter[num] += 1
            if num_counter[num] > length/2:
                result = num
                break
        return result

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        # 思路2: 累加计数 -- 记录两个数值: 数组中的值和出现的次数
        if not numbers:
            return 0
        result = numbers[0]
        times = 1
        for num in numbers:
            if times == 0:
                result = num
                times = 1
            else:
                if num == result:
                    times += 1
                else:
                    times -= 1
        times = 0
        for num in numbers:
            if num == result:
                times += 1
        if times > len(numbers)/2:
            return result
        else:
            return 0

# 评价
# 1. 看似思路2比思路1复杂，两者复杂度都是O(n),
# 2. 但是对于大数据来说，建立一个大字典是很占用空间的, 相比来说，思路1几乎不适用辅助空间
class Solution:
    def partition(self, numbers, start, end):
        key = numbers[start]
        while start < end:
            while start < end and key <= numbers[end]:
                end-=1
            numbers[start] = numbers[end]
            while start < end and key >= numbers[start]:
                start+=1
            numbers[end] = numbers[start]
        numbers[start] = key
        return start
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        # 思路2: 借助快排的partition
        if not numbers:
            return 0
        start, end = 0, len(numbers)-1
        middle = len(numbers)>>1
        index = self.partition(numbers, start, end)
        while index != middle:
            if index > middle:
                end = index - 1
                index = self.partition(numbers, start, end)
            else:
                start = index + 1
                index = self.partition(numbers, start, end)
        result = numbers[index]
        time = 0
        for num in numbers:
            if num==result:
                time += 1
        if time > middle:
            return result
        else:
            return 0

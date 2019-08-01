# -*- coding:utf-8 -*-
# 思路1：使用hash表，额外存储空间
'''
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        # 思路1： hash 表
        mapp = set()
        sign = False
        for each in numbers:
            if each in mapp:
                duplication[0]=each
                sign = True
                break
            else:
                mapp.add(each)
        return sign
'''

# 思路2: 交换数字，使用下标作为 key
# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        # 思路2： 数组下标为key
        length = len(numbers)
        for index in range(0, length):
            while index != numbers[index]:    # 每次交换都将 numbers[index] 放在正确的索引上
                if numbers[index] == numbers[numbers[index]]:
                    duplication[0] = numbers[index]
                    return True
                tmp_index = numbers[index]
                numbers[index], numbers[tmp_index] = numbers[tmp_index], numbers[index]
        return False
    
sol = Solution()
print(sol.duplicate([2,3,1,0,2,5,3], [-1,-2]))


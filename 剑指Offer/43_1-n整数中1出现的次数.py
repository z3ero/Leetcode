# -*- coding:utf-8 -*-
# 思路 1： 对每一个数字通过取余得到它的 1 的位数
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        for i in range(1, n+1):
            tmp = i
            while tmp:
                if tmp % 10 == 1:
                    count += 1
                tmp = tmp // 10
        return count

# -*- coding:utf-8 -*-
# 思路2: 从低到高，每次计算1个位上1出现的个数
# 1. 个位: 每经过10，个位出现1。个位1的个数: n//10 + (1 if n%10>=1 0)
# 2. 十位: 每经过100，出现1，重复10次，十位1: n//100*10 + （3 种类情况）
#    2.1: (n%100)%10 > 1: 十位上数大于1，则为 n//100*10 + 10    如 520
#    2.2: (n%100)%10 == 1: 十位上数 =1, 则为 n//100*10 + n%10 + 1 如514
#    2.3: (n%100)%10 < 1: 十位上数小于1, 则为 n//100*10 + 0 如509
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        if n<1: return 0
        count = 0
        base = 1
        roundd = n
        while roundd > 0:
            weight = roundd % 10
            roundd = roundd // 10
            count += roundd * base
            if weight == 1:
                count += (n%base)+1
            elif weight > 1:
                count += base
            base *= 10
        return count
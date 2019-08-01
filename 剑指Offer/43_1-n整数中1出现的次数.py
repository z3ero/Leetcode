import math
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        sum_one = 0
        count = 0  # 经历了几次循环
        while n//10:
            tmp_sum = (n-1)//10 + 1   # 从1开始，每经过一个10，个位上必定有一个1
            sum_one += tmp_sum*int(math.pow(10, count))
            n //= 10
            count += 1
        # 最高位上出现的 1 单独考虑
        if n > 1:   # 若 最高位上的数 > 1, 则最高位上1出现的次数为 1*(10^count)
            sum_one += int(math.pow(10, count))
        else:  # 若最高位上数 == 1，则最高位1 出现的次数为 n % (10^count)
            sum_one += n
        return sum_one


    def baoli(self, n):
        sum_one = 0
        for i in range(n+1):
            j = i
            while j:
                if j%10 == 1:
                    sum_one += 1
                j/=10
        return sum_one

sol = Solution()
print(sol.NumberOf1Between1AndN_Solution(21345))
print(sol.baoli(21345))
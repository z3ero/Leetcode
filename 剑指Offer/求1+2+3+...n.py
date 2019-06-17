# 短路求值，利用逻辑运算符求值
# 思路： 若 n == 0, 即 False, 不进行下一步运算
#       若 n > 0, 需要进行 n+f(n-1) 递归运算
class Solution:
    def Sum_Solution(self, n):
        # 短路求值，利用逻辑运算符求值
        sum = n and n+self.Sum_Solution(n-1)
        return sum

sol = Solution()
print(sol.Sum_Solution(5))
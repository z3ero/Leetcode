# 求斐波那切数列第 n 个数字
# 递归代码 ----- 计算时间复杂度太大,时间巨慢
'''
class Solution:
    def Fibonacci(self, n):
        if n == 0: return 0
        if n == 1: return 1
        return self.Fibonacci(n-2) + self.Fibonacci(n-1)
'''
# 循环代码
class Solution:
    def Fibonacci(self, n):
        # 循环代码
        if n==0: return 0
        if n==1: return 1
        f_s, f_e = 0, 1
        for i in range(2,n+1):
            tmp = f_e
            f_e = f_e + f_s
            f_s = tmp
        return f_e
# 基于矩阵公式+借助二分平方，可以时间复杂度降低到 O(logN)
sol = Solution()
print(sol.Fibonacci(9))
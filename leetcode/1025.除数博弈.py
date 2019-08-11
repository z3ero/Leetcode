#
# @lc app=leetcode.cn id=1025 lang=python3
#
# [1025] 除数博弈
#
# 思路：偶数先手必胜——先手为偶数的话，先手可以让自己每部都保持偶数
#     （只要让对方是奇数，奇数的因数必然是奇数，减去后，自己就是偶数）,
#       最终使得最后一轮自己是2，对方输
#       
class Solution:
    def divisorGame(self, N: int) -> bool:
        # 思路1: 先手偶数必胜思路
        '''
        if N%2==0:
            return True
        else:
            return False
        '''
        # 思路2：动态规划思路 f(N) = !f(N-x_1) || !f(N-x_2) ||...|| !f(N-x_i)
        dp_list = [False] * (N+1)
        for i in range(1, N+1):
            cur_data = i
            for j in range(1, i):
                if cur_data%j == 0 and not dp_list[cur_data-j]:
                    dp_list[cur_data] = True
                    break
        return dp_list[N]

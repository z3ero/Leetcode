#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
class Solution:
    # 思路：动态规划，递推公式
    # f(i) 表以第i个元素 为有效字符串结尾的 有效字符串的长度
    # 需要一个 n 长数组 保存f(0)~f(n-1)的长度
    # 需要一个 栈 保存遍历到的未匹配的 ( 的索引
    #  
    # 1. 若 nums[i] 为 '(' ====> f(i)=0, 索引入栈
    # 2. 若 nums[i] 为 ')', 且栈非空  ====> f(i)= i-出栈索引 +1 + f(出栈索引-1), 看看是否需要更改max_length
    # 3. 若 nums[i] 为 ')', 且栈空 =====> f(i)=0

    def longestValidParentheses(self, s: str) -> int:
        if len(s)<=0:
            return 0
        length_arr = [0]
        left_list = []
        for i in range(len(s)):
            length = 0
            if s[i]=='(':
                length_arr.append(0)
                left_list.append(i)
            if s[i]==')':
                if len(left_list)>0:
                    left_index = left_list.pop()
                    length = i+1-left_index+length_arr[left_index]
                    length_arr.append(length)
                else:
                    length_arr.append(0)
        return max(length_arr)


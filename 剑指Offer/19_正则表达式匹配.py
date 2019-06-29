# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    # 异常考虑考虑:
    # 1. pattern 第一个字符为 “*”
    # 2. s 与 pattern 为 None
    
    # 递归匹配
    def matchScore(self, s, s_index, pattern, pattern_index):
        # 终止条件: 两者有一个先结束
        # 1. pattern 结束是终止的前提条件 （s结束不能作为终止前提，因为可能出现 .*）
        #       pattern 结束: 若 s 也结束，匹配完成; 否则匹配失败
        if pattern_index == len(pattern):
            return s_index == len(s)

        # 考虑是否模式中存在 *，因为 * 影响当前位置
        if pattern_index + 1 < len(pattern) and pattern[pattern_index+1]=="*":
            # 如果当前位置可以匹配，有三种推进方式
            # 1. * 表示0， pattern 后移两位， s 不移动
            # 2. * 表示1， pattern 后移两位， s 后移1位
            # 3. * 表示2+, pattern 不移动，s后移1位 
            if s_index != len(s) and (pattern[pattern_index]=='.' or s[s_index]==pattern[pattern_index]): # 可以后移
                return self.matchScore(s, s_index, pattern, pattern_index+2) or self.matchScore(s, s_index+1, pattern, pattern_index+2) or self.matchScore(s, s_index+1, pattern, pattern_index)
            else:  # （s不能后移或者当前位置不能匹配）只能将 pattern 向后移动两位
                return self.matchScore(s, s_index, pattern, pattern_index+2)
        else:    # 不为 *
            # 匹配当前位置
            if s_index < len(s) and (pattern[pattern_index]=="." or s[s_index]==pattern[pattern_index]):
                return self.matchScore(s, s_index+1, pattern, pattern_index+1)
            # 不匹配
            else:
                return False
  
    def match(self, s, pattern):
        return self.matchScore(s, 0, pattern, 0)
        # write code here

sol = Solution()
print(sol.match("a",".*"))
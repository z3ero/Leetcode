#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
import functools
class Solution:
    @functools.lru_cache(None)
    def isMatch(self, s: str, p: str) -> bool:
        # p为空的时候
        if not p: return not s
        # p不为空时
        # 1. 若p有下一位且下一位是 * 时
        if len(p)>=2 and p[1]=='*':
            # 1.1 判断 s 是否为空
            if s and (s[0]==p[0] or p[0]=='.'):   # 1.1 非空且匹配: ‘*’ 匹配0次或一次或多次
                return self.isMatch(s[1:], p[2:]) or self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:  # 1.2 空或者不匹配, p移动两个
                return self.isMatch(s, p[2:])
        # 2. 若p无下一位，或者又下一位但不是 *
        else:
            if s and (s[0]==p[0] or p[0]=='.'):   # 2.1 若s非空且匹配
                return self.isMatch(s[1:], p[1:])
            else:  # 2.2 若s为空或者不匹配
                return False

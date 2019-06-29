# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isInt(self, s):
        # 整数判断：
        # 1. 为空
        # 2. +，- 或者 1-9 开头，后面取值全是0-9
        #   (2.1) + 或者 - 开头，后面需要有值
        #   (2.2) 1-9开头，后面可以无值
        if len(s)==0:
            return True
        
        if s[0]=='+' or s[0]=='-':
            if len(s) == 1:
                return True    # 只有一个 + - 不匹配
            else:
                s = s[1:]  # 进行下一步匹配
                
        if s[0] > '0' and s[0]<='9':   # 最高位不为 0
            sign = True
            for index in range(1, len(s)):
                if s[index]<'0' or s[index]>'9':
                    sign = False
                    break
            return sign
        elif s[0] == '0' and len(s)==1: # 最后是0，但是整数只有0
            return True
        else:
            return False

    def isFloat(self, s):
        # 1. 没有小数
        # 2. 以.开头, 后面是常规数字
        if len(s)==0:
            return True
        if s[0]=='.':
            if len(s)==1:
                return False
            else:
                # 判断小数点后的数字部分
                sign = True
                for index in range(1, len(s)):
                    if s[index]<'0' or s[index]>'9':
                        sign = False
                        break
                return sign
        else: # 没有以 '.' 开头
            return False
                
    def isIndex(self, s):
        # 指数部分
        if len(s)==0:
            return True
        if (s[0] == 'e' or s[0] == 'E') and len(s)>1:
            # 与判断整数逻辑大体相似
            return self.isInt(s[1:])
        else: # 不是以 e 开头
            return False
    
    def isNumeric(self, s):
        # 异常状态
        if s is None or s == "":
            return False
        # 分别找出整数，小数和指数部分
        start = index = 0
        s_len = len(s)
        while index<s_len and s[index]!='.' and s[index]!='e' and s[index]!='E':
            index += 1
        s1 = s[start:index] # 整数部分
        start = index
        while index<s_len and s[index]!='e' and s[index]!='E':
            index += 1
        s2 = s[start:index] # 小数部分
        start = index
        while index<s_len:
            index+=1
        s3 = s[start:index] # 指数部分
        
        ## 判断 s1, s2, s3 是否符合要求
        # 边界条件: 
        # 1. s1 不存在，s2 必须存在，且 s3 不能存在  
        # 2. s1 存在，但是只有 +-, s2 必须存在 且 s3不能存在
        if len(s1)==0 or (len(s1)==1 and (s1[0]=='+' or s[1]=='-')):  
            if len(s2) ==0 or len(s3)>0:
                return False
        # 判断整数部分，小数部分，指数部分是否都符合规范
        return self.isInt(s1) and self.isFloat(s2) and self.isIndex(s3)
        # write code here
sol = Solution()
positive_list = ['100', '+1.00', '-1.03', '0.123', '.123', '-1e2', '5E-3', '-.123']
negetive_list = ['100.e3', 'e3', '', '.e', '1.abc']
print([sol.isNumeric(each) for each in positive_list])
print([sol.isNumeric(each) for each in negetive_list])
# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # 思路1:
        # 分割字符串,反转
        res = ' '.join(s.split(' ')[::-1])
        return res

    # 思路2: 两次翻转
    # 1. 翻转整个句子: 定义两个指针, 从前往后，每次交换头尾指针的值, 直到两个指针遇见
    # 2. 翻转1结果中的每个单词: 对每个单词重复 1 过程
    
        
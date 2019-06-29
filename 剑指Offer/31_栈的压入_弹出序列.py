# -*- coding:utf-8 -*-
class Solution:
    # 借助一个辅助栈
    def IsPopOrder(self, pushV, popV):
        s = []
        # 压栈的 同时，遍历弹栈
        j = 0
        for p in popV:
            if len(s)>0 and s[-1]==p: # 顺序对应, 弹栈
                s.pop()
                continue
            # 若是里面没有数据，或者不相等。
            # 1. 继续压栈，直到相等
            # 2. 若压完栈后，还不相等，则不匹配
            sign = False
            while j < len(pushV):
                s.append(pushV[j])
                j += 1
                if p == s[-1]:
                    s.pop()
                    sign = True
                    break
            if sign == False:
                return False
        return True
        # write code here
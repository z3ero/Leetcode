# -*- coding:utf-8 -*-
class Solution:
    # 定义两个辅助栈, 其中s2是存储最小值栈
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def push(self, node):
        self.s1.append(node)
        if len(self.s2)==0 or node < self.s2[-1]:
            self.s2.append(node)
        else:
            self.s2.append(self.s2[-1])
        # write code here
    def pop(self):
        if len(self.s1)<=0 or len(self.s2)<=0:
            return None
        self.s1.pop()
        self.s2.pop()
        # write code here
    def top(self):
        if len(self.s1)<=0:
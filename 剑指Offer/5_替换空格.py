# -*-coing: utf-8 -*-
# give a string, replace the space in string with '%20'
class Solution:
    '''
    def replaceSpace(self, s):
        return '%20'.join(s.split(' '))
    '''
    # method_2 双指针
    def replaceSpace(self, s):
        s = list(s)
        num_space = 0
        for c in s:
            if c==' ':
                num_space += 1
        new_length = len(s) + 2*num_space  # 替换每个空格多了两个字符
        p1 = len(s)-1
        p2 = new_length-1
        new_s = s + [None]*(2*num_space)

        while p1 >=0 and p2 > p1:
            if s[p1]==' ':
                new_s[p2-2:p2+1] = '%20'
                p2 = p2-3
            else:
                new_s[p2] = s[p1]
                p2 = p2-1
            p1 = p1-1
        return ''.join(new_s)

s = ' hello io'
sol = Solution()
print(sol.replaceSpace(s))
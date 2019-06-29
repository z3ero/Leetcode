# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    # 思路：1. 找到循环终止条件: 由于打印开始点总是 行号 = 列号，所以循环终止条件为：
    #         row_len > start * 2 && col_len > start * 2 
    #      2. 打印每一圈的逻辑 和 边界条件 的考虑 
    #           每个循环里最多分四组输出
    def printEach(self, matrix, row_len, col_len, start):
        r_end = row_len - 1 - start
        c_end = col_len - 1 - start
        ll = []
        # 第一步 横着打印总是需要的
        ll += matrix[start][start:c_end+1]
        # 第二步 竖着打印只有 r_end > start 才被需要
        if r_end > start:
            for i in range(start+1, r_end+1):
                ll.append(matrix[i][c_end])
        # 第三步 反向横着打印 只有 r_end > start and c_end > start 才被需要
        if r_end > start and c_end > start:
            for i in range(c_end-1,  start-1, -1):
                ll.append(matrix[r_end][i])
        # 第四步 反向竖着打印 只有 r_end-1 > start and c_end > start 才被需要
        if r_end -1 > start and c_end > start:
            for i in range(r_end-1, start, -1):
                ll.append(matrix[i][start])
        return ll
                
    def printMatrix(self, matrix):
        # write code here
        row_len, col_len = len(matrix), len(matrix[0])
        start = 0
        res_list = []
        while row_len > start*2 and col_len > start*2:
            res_list += self.printEach(matrix, row_len, col_len, start)
            start += 1
        return res_list 

sol = Solution()
# array = [[1],[2],[3],[4],[5]]
array = [[1]]
print(sol.printMatrix(array))
# -*- coding:utf-8 -*-
class Solution:
    # 判断是否可以进入格子
    def check_into(self, threshold, r, c):
        sum = 0
        while r:
            sum += r%10
            r /= 10
        while c:
            sum += c%10
            c /= 10
        return sum <= threshold
    
    def move(self, count, threshold, rows, cols, visited, r, c):
        # 若是下标越界，直接返回count
        if r<0 or r>=rows or c<0 or c>=cols:
            return count
        # 若是访问过  或者 进不去，直接返回 count
        if visited[r*cols+c] or not self.check_into(threshold, r, c):
            return count
        count += 1
        visited[r*cols+c] = True
        count = self.move(count, threshold, rows, cols, visited, r-1, c)
        count = self.move(count, threshold, rows, cols, visited, r+1, c)
        count = self.move(count, threshold, rows, cols, visited, r, c-1)
        count = self.move(count, threshold, rows, cols, visited, r, c+1)
        return count
    
    def movingCount(self, threshold, rows, cols):
        visited = [False]*(rows*cols)
        count = 0
        count = self.move(count, threshold, rows, cols, visited, 0, 0)
        return count
        # write code here
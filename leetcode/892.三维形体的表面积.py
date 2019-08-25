#
# @lc app=leetcode.cn id=892 lang=python3
#
# [892] 三维形体的表面积
#
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        # 每个块 6 个面，总面数
        count = sum((sum(x) for x in grid))*6
        # z 轴 (即上下) 遮盖了多少面
        # 例如: 如果某个位置为 5, 则遮盖了 8=2*(5-4)面
        for line in grid:
            for h in line:
                if h>0:
                    count -= 2*(h-1)
        # x 轴 (即左右)遮盖了多少面 (将h也要纳入，因为高度上也有左右)
        for line in grid:
            for i in range(len(line)-1):
                count -= 2*min(line[i], line[i+1])
        # y 轴 (即前后)遮盖了多少面 (也将h纳入，高度上也有前后)
        for i in range(len(grid)-1):
            for j in range(len(grid)):
                if len(grid[i])> j and len(grid[i+1]) > j:
                    count -= 2*min(grid[i][j], grid[i+1][j])
        return count


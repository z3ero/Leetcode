# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    # 思路: 使用递归 + 路径数组
    # 下面分两种情况考虑:
    # 1. 深入: 未深入到叶子节点 且 sum < 目标值
    # 2. 匹配: 深入到叶子节点，且 sum = 目标值
    # 3. 其他的不作处理
    # 返回父函数, 注意本层操作撤销
    def __init__(self):
        self.res_paths = []   # 最终要返回的所有路径数组

    def fun(self, root, expectNumber, sum, path):
        sum += root.val
        path.append(root.val)
        # 1. 深入
        if sum < expectNumber:
            if root.left is not None:
                self.fun(root.left, expectNumber, sum, path)
            if root.right is not None:
                self.fun(root.right, expectNumber, sum, path)
            # 无法深入 pass
        # 2. 匹配
        if root.left is None and root.right is None and sum == expectNumber:
            tmp_path = [x for x in path]
            self.res_paths.append(tmp_path)
            # 匹配但是未到叶子节点, pass
        sum -= root.val
        path.pop()

    def FindPath(self, root, expectNumber):
        sum = 0
        path = []
        # 边界条件
        if root is None:
            return self.res_paths
        self.fun(root, expectNumber, sum, path)
        # 按照数组排序，默认升序，reverse=True ---- 降序
        self.res_paths = sorted(self.res_paths, key=lambda x: len(x), reverse=True)
        return self.res_paths
        # write code here

sol = Solution()
root = TreeNode(1)
ltree = TreeNode(2)
rtree = TreeNode(2)
root.left = ltree
root.right = rtree
print(sol.FindPath(root, 3))

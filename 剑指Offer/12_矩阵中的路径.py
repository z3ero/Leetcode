class Solution:
    # 寻找路径的递归函数  
    def search(self, matrix, rows, cols, path, path_ix, r, c, visited, path_len):
        if path_ix == path_len:
            return True
        sign = False
        if r>=0 and r<rows and c>=0 and c<cols and matrix[r*cols+c]==path[path_ix] and not visited[r*cols+c]:
            path_ix += 1
            visited[r*cols+c]=True
            b_1 = self.search(matrix, rows, cols, path, path_ix, r-1, c, visited, path_len)
            b_2 = self.search(matrix, rows, cols, path, path_ix, r+1, c, visited, path_len)
            b_3 = self.search(matrix, rows, cols, path, path_ix, r, c-1, visited, path_len)
            b_4 = self.search(matrix, rows, cols, path, path_ix, r, c+1, visited, path_len)
            sign = b_1 or b_2 or b_3 or b_4
            if not sign:
                path_ix -= 1
                visited[r*cols+c]=False
        return sign      
    def hasPath(self, matrix, rows, cols, path):
        visited = [False]*len(matrix)
        for r in range(rows):
            for c in range(cols):
                if self.search(matrix, rows, cols, path, 0, r, c, visited, len(path)):
                    return True
        return False

sol = Solution()
matrix = "ABCESFCSADEE"
rows = 3
cols = 4
path = "ABCCED"
print(sol.hasPath(matrix, rows, cols, path))

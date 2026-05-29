class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        max_area = 0

        def dfs(x, y):
            area = 1
            grid[x][y] = 0
            for i in range(4):
                nx, ny = x + delta[i][0], y + delta[i][1]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    area += dfs(nx, ny)
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area
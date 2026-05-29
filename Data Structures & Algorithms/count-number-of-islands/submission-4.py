class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(x, y):
            grid[x][y] = "0"
            for i in range(4):
                nx, ny = x + delta[i][0], y + delta[i][1]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                    dfs(nx, ny)
        
        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    num_islands += 1
        
        return num_islands
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def bfs(x, y):
            area = 0
            queue = deque([(x, y)])
            grid[x][y] = 0

            while queue:
                c_x, c_y = queue.popleft()
                area += 1
                for i in range(len(delta)):
                    n_x, n_y = c_x + delta[i][0], c_y + delta[i][1]
                    if 0 <= n_x < m and 0 <= n_y < n and grid[n_x][n_y] == 1:
                        queue.append((n_x, n_y))
                        grid[n_x][n_y] = 0
            
            return area
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, bfs(i, j))

        return res
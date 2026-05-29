from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0: return -1

        n = len(grid)
        queue = deque([(1, 0, 0)])
        delta = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

        while queue:
            dist, x, y = queue.popleft()
            grid[x][y] = dist
            if x == y == n - 1: return dist
            for i in range(len(delta)):
                nx, ny = x + delta[i][0], y + delta[i][1]
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                    queue.append((dist + 1, nx, ny))
        
        return -1
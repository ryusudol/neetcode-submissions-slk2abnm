from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        fresh_cnt = time = 0
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: fresh_cnt += 1
                elif grid[i][j] == 2: queue.append((0, i, j))

        while queue:
            for _ in range(len(queue)):
                time, cx, cy = queue.popleft()
                for i in range(len(delta)):
                    nx, ny = cx + delta[i][0], cy + delta[i][1]
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        queue.append((time + 1, nx, ny))
                        fresh_cnt -= 1
                        grid[nx][ny] = 2
        
        return time if fresh_cnt == 0 else -1
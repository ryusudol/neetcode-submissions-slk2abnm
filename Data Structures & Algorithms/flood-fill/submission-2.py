from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        original_color = image[sr][sc]
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque([(sr, sc)])
        visited = set((sr, sc))

        while queue:
            c_row, c_col = queue.popleft()
            image[c_row][c_col] = color
            for i in range(4):
                n_row, n_col = c_row + delta[i][0], c_col + delta[i][1]
                if 0 <= n_row < m and 0 <= n_col < n:
                    if (n_row, n_col) not in visited and image[n_row][n_col] == original_color:
                        queue.append((n_row, n_col))
                        visited.add((n_row, n_col))
        
        return image
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        original_color = image[sr][sc]
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()

        def dfs(x, y):
            image[x][y] = color
            visited.add((x, y))
            for i in range(4):
                n_x, n_y = x + delta[i][0], y + delta[i][1]
                if 0 <= n_x < m and 0 <= n_y < n:
                    if (n_x, n_y) not in visited and image[n_x][n_y] == original_color:
                        dfs(n_x, n_y)

        dfs(sr, sc)

        return image
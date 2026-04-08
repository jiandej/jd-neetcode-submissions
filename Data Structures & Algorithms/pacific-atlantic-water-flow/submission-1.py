class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = [[False]*n for _ in range(m)]
        atlantic = [[False]*n for _ in range(m)]
        
        def dfs(r: int, c: int, visited: list[list[bool]], prev_height: int):
            if (r < 0 or r >= m or c < 0 or c >= n or visited[r][c] or heights[r][c] < prev_height):
                return
            
            visited[r][c] = True
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                dfs(r+dr, c+dc, visited, heights[r][c])
        
        for i in range(m):
            dfs(i, 0, pacific, 0)
            dfs(i, n-1, atlantic, 0)

        for j in range(n):
            dfs(0, j, pacific, 0)
            dfs(m-1, j, atlantic, 0)
        
        return [[i, j] for i in range(m) for j in range(n) if pacific[i][j] and atlantic[i][j]]
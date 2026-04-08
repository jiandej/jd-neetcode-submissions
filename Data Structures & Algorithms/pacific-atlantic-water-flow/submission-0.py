class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        
        def dfs(r: int, c: int, visited: set[tuple[int]], prev_height: int):
            if ((r,c) in visited or r < 0 or r >= m or c < 0 or c >= n or heights[r][c] < prev_height):
                return
            
            visited.add((r, c))
            dfs(r-1, c, visited, heights[r][c])
            dfs(r+1, c, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
        
        for i in range(m):
            dfs(i, 0, pacific, 0)
            dfs(i, n-1, atlantic, 0)

        for j in range(n):
            dfs(0, j, pacific, 0)
            dfs(m-1, j, atlantic, 0)
        
        result = []

        for i in range(m):
            for j in range(n):
                if ((i, j) in pacific and (i, j) in atlantic):
                    result.append((i, j))
        
        return result
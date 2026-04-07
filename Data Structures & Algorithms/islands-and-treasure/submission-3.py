class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        EMPTY = 2147483647
        queue = collections.deque()

        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]

        # put treasures as starting points of BFS
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 0):
                    queue.append((i, j))
        
        while (len(queue) != 0):
            lens = len(queue)

            for _ in range(lens):
                x, y = queue.popleft()
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    
                    if (0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == EMPTY):
                        grid[new_x][new_y] = grid[x][y] + 1
                        queue.append((new_x, new_y))
                    
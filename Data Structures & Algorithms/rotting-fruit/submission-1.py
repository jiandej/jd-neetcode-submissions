class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if (not grid):
            return -1
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        total_fresh_fruit = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 2):
                    queue.append((i, j))
                elif (grid[i][j] == 1):
                    total_fresh_fruit += 1
        
        minutes = 0

        while (queue):
            length = len(queue)

            for _ in range(length):
                x,y = queue.popleft()
                for dx, dy in directions:
                    new_x, new_y = x+dx, y+dy

                    if (0<= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1):
                        grid[new_x][new_y] = 2
                        total_fresh_fruit -= 1
                        queue.append((new_x, new_y))
            if (queue):
                minutes += 1
        
        return minutes if total_fresh_fruit == 0 else -1
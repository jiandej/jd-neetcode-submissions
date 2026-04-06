class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        in_queued = set()

        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]

        # put treasures as starting points of BFS
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 0):
                    queue.append((i, j))
                    in_queued.add((i, j))
        
        print(len(queue))
        
        distance = 0
        while (len(queue) != 0):
            lens = len(queue)

            for _ in range(lens):
                x, y = queue.popleft()
                for direction in directions:
                    new_x = x + direction[0]
                    new_y = y + direction[1]

                    if ((new_x, new_y) in in_queued):
                        continue
                    
                    # out of boundary
                    if (new_x < 0 or new_y < 0 or new_x == m or new_y == n):
                        continue
                    if (grid[new_x][new_y] == -1):
                        continue
                    
                    if (grid[new_x][new_y] > distance + 1):
                        grid[new_x][new_y] = distance + 1
                    queue.append((new_x, new_y))
                    in_queued.add((new_x, new_y))
            
            distance += 1
                    
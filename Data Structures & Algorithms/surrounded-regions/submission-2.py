class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if (not board):
            return
        m, n = len(board), len(board[0])

        queue = collections.deque()
            
        # Only boundary is safe, adding boundary as starting points of BFS
        for r in range(m):
            if (board[r][0] == 'O'):
                queue.append((r, 0))
            if (board[r][n-1] == 'O'):
                queue.append((r, n-1))
        for c in range(n):
            if (board[0][c] == 'O'):
                queue.append((0, c))
            if (board[m-1][c] == 'O'):
                queue.append((m-1, c))
        
        while (queue):
            length = len(queue)

            for _ in range(length):
                r, c = queue.popleft()
                board[r][c] = 'S' # safe
                for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    new_r, new_c = r+dr, c+dc
                    if (0 <= new_r < m and 0 <= new_c < n and board[new_r][new_c] == 'O'):
                        queue.append((new_r, new_c))
        
        for r in range(m):
            for c in range(n):
                if (board[r][c] == 'S'):
                    board[r][c] = 'O'
                elif (board[r][c] == 'O'):
                    board[r][c] = 'X'
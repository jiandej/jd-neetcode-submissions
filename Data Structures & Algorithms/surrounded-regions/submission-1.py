class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if (not board):
            return
        m, n = len(board), len(board[0])

        def dfs(r: int, c: int):
            if (0 <= r < m and 0 <= c < n and board[r][c] == 'O'):
                board[r][c] = 'S' # safe
                dfs(r-1, c)
                dfs(r+1, c)
                dfs(r, c-1)
                dfs(r, c+1)
            
        # Only boundary is safe
        for r in range(m):
            if (board[r][0] == 'O'):
                dfs(r, 0)
            if (board[r][n-1] == 'O'):
                dfs(r, n-1)
        for c in range(n):
            if (board[0][c] == 'O'):
                dfs(0, c)
            if (board[m-1][c] == 'O'):
                dfs(m-1, c)
        
        for r in range(m):
            for c in range(n):
                if (board[r][c] == 'S'):
                    board[r][c] = 'O'
                elif (board[r][c] == 'O'):
                    board[r][c] = 'X'
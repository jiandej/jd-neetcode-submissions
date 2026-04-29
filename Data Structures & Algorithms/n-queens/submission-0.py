class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag = set()
        neg_diag = set()
        result = []
        board = [['.']*n for _ in range(n)]

        def backtracking(row: int):
            if row == n:
                copy = ["".join(r) for r in board]
                result.append(copy)
            
            for col in range(n):
                if col in cols or (row + col) in diag or (row - col) in neg_diag:
                    continue
                cols.add(col)
                diag.add(row + col)
                neg_diag.add(row - col)
                board[row][col] = 'Q'

                backtracking(row+1)

                cols.remove(col)
                diag.remove(row + col)
                neg_diag.remove(row - col)
                board[row][col] = '.'
        
        backtracking(0)
        return result


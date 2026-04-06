from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        for col in range(9):
            for row in range(9):
                if (board[col][row] == '.'):
                    continue
                if (board[col][row] in cols[col]
                    or board[col][row] in rows[row]
                    or board[col][row] in square[(col//3, row//3)]):
                    return False
                cols[col].add(board[col][row])
                rows[row].add(board[col][row])
                square[(col//3, row//3)].add(board[col][row])
        
        return True
                
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        n = len(matrix)

        # step 1: reverse matrix vertically
        for i in range(n//2):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]

        # step 2: tranpose the matrix

        for i in range(n):
            for j in range(i+1, n):
                if (i != j):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
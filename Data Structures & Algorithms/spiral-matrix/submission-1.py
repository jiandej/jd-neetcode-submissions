class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix:
            return result
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        
        while (top <= bottom and left <= right):
            # direction from left to right
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1

            # direction from top to bottom
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1

            # direction from right to left
            if (top <= bottom):
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # direction from bottom to top
            if (left <= right):
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result
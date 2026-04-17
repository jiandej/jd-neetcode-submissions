class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        total = m*n
        i, j = 0, 0
        visited = set()
        result = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_idx = 0

        while (len(visited) < total):
            result.append(matrix[i][j])
            visited.add((i, j))

            if (len(visited) == total):
                break

            new_i, new_j = i + directions[direction_idx][0], j + directions[direction_idx][1]

            while ((new_i, new_j) in visited or new_i == m or new_i < 0 or new_j == n or new_j < 0):
                direction_idx = (direction_idx+1)%4
                new_i, new_j = i + directions[direction_idx][0], j + directions[direction_idx][1]
            i, j = new_i, new_j

        
        return result
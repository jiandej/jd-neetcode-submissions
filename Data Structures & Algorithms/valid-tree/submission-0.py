class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if (len(edges) > n - 1):
            return False
        
        adj = [[] for _ in range(n)]
        indegrees = [0]*n

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        visited = set()
        queue = collections.deque([(0, -1)]) # (current, parent)
        visited.add(0)

        # BFS
        while (queue):
            node, parent = queue.popleft()

            for neighbor in adj[node]:
                if (neighbor == parent):
                    continue
                if (neighbor in visited):
                    return False
                queue.append((neighbor, node))
                visited.add(neighbor)
        return len(visited) == n
                
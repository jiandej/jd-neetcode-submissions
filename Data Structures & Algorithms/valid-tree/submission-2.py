class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if (len(edges) > n - 1):
            return False
        
        adj = [[] for _ in range(n)]
        visited = set()

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        # Option 1: BFS
        # queue = collections.deque([(0, -1)]) # (current, parent)
        # visited.add(0)

        # while (queue):
        #     node, parent = queue.popleft()

        #     for neighbor in adj[node]:
        #         if (neighbor == parent):
        #             continue
        #         if (neighbor in visited):
        #             return False
        #         queue.append((neighbor, node))
        #         visited.add(neighbor)
        # return len(visited) == n

        # Option 2: DFS
        def isCycle(node: int, parent: int) -> bool:
            visited.add(node)
            for neighbor in adj[node]:
                if (neighbor == parent):
                    continue
                if (neighbor in visited):
                    return True
                if (isCycle(neighbor, node)):
                    return True
            return False
        
        return isCycle(0, -1) == False and len(visited) == n

                
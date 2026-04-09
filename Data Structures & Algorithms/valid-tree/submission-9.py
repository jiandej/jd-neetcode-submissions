class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if (len(edges) != n - 1):
            return False
        
        parents = list(range(n))
        size = [1]*n
        def find(u: int) -> int:
            if (parents[u] == u):
                return u
            parents[u] = find(parents[u])
            return parents[u]
        def union(u: int, v: int) -> bool:
            pu = find(u)
            pv = find(v)

            if (pu == pv):
                return False # already having same root -> cycle
            
            if (size[pu] < size[pv]):
                pu, pv = pv, pu
            parents[pv] = pu
            size[pu] += size[pv]

            return True
        
        for u, v in edges:
            if (not union(u, v)):
                return False
        
        return True
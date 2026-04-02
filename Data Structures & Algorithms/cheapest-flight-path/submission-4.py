class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        for flight in flights:
            u, v, p = flight
            if (u not in graph):
                graph[u] = []
            graph[u].append((v, p))
        
        queue = collections.deque()
        if (src not in graph):
            return -1
        queue.append((src, 0))

        min_cost = [sys.maxsize]*n
        min_cost[src] = 0

        step = 0
        while (queue and step <= k):
            n = len(queue)
            for i in range(n):
                airport, curret_cost = queue.popleft()

                for v, p in graph[airport]:
                    cost = curret_cost + p

                    if (v == dst):
                        min_cost[dst] = min(min_cost[dst], cost)
                    else:
                        if (v in graph and cost < min_cost[dst] and cost < min_cost[v]):
                            min_cost[v] = cost
                            queue.append((v, cost))
            
            step+=1
        
        return min_cost[dst] if min_cost[dst] != sys.maxsize else -1
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            stone_1 = heapq.heappop_max(stones)
            print(stone_1)
            stone_2 = heapq.heappop_max(stones)
            remains = stone_1 - stone_2

            if remains != 0:
                heapq.heappush_max(stones, remains)
        
        return stones[0] if len(stones) else 0
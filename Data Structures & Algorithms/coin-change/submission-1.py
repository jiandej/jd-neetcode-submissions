import collections
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if (amount == 0):
            return 0
        queue = collections.deque()

        seen = set()

        for coin in coins:
            remains = amount-coin
            if (remains >= 0):
                queue.append(remains)
                seen.add(remains)
        
        # BFS
        num_coin = 1
        while (queue):
            n = len(queue)

            for _ in range(n):
                remains = queue.popleft()
                if (remains == 0):
                    return num_coin
                for coin in coins:
                    new_remains = remains - coin
                    if (new_remains >= 0 and new_remains not in seen):
                        queue.append(new_remains)
                        seen.add(new_remains)
            num_coin += 1
            
        return -1


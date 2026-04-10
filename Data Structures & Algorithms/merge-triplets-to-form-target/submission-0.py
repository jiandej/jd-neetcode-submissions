class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        eligible = [0]*3

        for a, b, c in triplets:
            if (a == target[0] and b <= target[1] and c <= target[2]):
                eligible[0] += 1
            if (a <= target[0] and b == target[1] and c <= target[2]):
                eligible[1] += 1
            if (a <= target[0] and b <= target[1] and c == target[2]):
                eligible[2] += 1
        
        return eligible[0] > 0 and eligible[1] > 0 and eligible[2] > 0
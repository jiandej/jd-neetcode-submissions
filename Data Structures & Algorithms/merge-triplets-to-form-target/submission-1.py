class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        satisfied_indices = set()

        for triplet in triplets:
            # the triplet only useful if the value is small or equal to the target (can be overrided)
            if (triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]):
                for i in range(3):
                    # The triplet that can use to generate the target
                    if (triplet[i] == target[i]):
                        satisfied_indices.add(i)
            
            if (len(satisfied_indices) == 3):
                return True
        
        return len(satisfied_indices) == 3
from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {}
        for idx, c in enumerate(s):
            last_idx[c] = idx
        
        result = []
        start = 0
        end = 0
        
        for idx, c in enumerate(s):
            end = max(end, last_idx[c])

            if (idx == end):
                result.append(end - start + 1)
                start = end + 1
        
        return result
            
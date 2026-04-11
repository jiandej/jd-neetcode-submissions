from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = Counter(s)

        result = []
        substring = []
        occur_set = set()
        for c in s:
            if (counts[c] > 0):
                substring.append(c)
                counts[c] -= 1
                occur_set.add(c)
            
            if (counts[c] == 0):
                occur_set.remove(c)
            
            if (len(occur_set) == 0):
                result.append(len(substring))
                substring = []
        
        return result
            
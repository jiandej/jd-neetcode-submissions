class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        for s in strs:
            # build map
            char_map = {}
            sorted_s = "".join(sorted(s))
            if (sorted_s not in cache):
                cache[sorted_s] = []
            cache[sorted_s].append(s)
        
        return list(cache.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        for s in strs:
            # build map
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')]+=1
            # hash_key = tuple(count)
            hash_key = ','.join([str(c) for c in count])
            if (hash_key not in cache):
                cache[hash_key] = []
            cache[hash_key].append(s)
        
        return list(cache.values())

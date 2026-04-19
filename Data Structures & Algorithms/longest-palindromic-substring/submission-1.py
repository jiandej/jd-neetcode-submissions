class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, max_len = 0, 1

        for i in range(len(s)):
            # odd
            l, r = i-1, i+1
            while (l >= 0 and r <len(s) and s[l] == s[r]):
                if (r - l + 1 > max_len):
                    start = l
                    max_len = r - l + 1
                l -=1
                r +=1
            # even
            l, r = i, i+1
            while (l >= 0 and r <len(s) and s[l] == s[r]):
                if (r - l + 1 > max_len):
                    start = l
                    max_len = r - l + 1
                l -=1
                r +=1
        
        return s[start:start+max_len]
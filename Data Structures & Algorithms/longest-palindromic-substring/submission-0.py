class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_substring = s[0]

        for i in range(len(s)):
            # even
            l, r = i-1, i+1
            while (l >= 0 and r <len(s) and s[l] == s[r]):
                if (r - l + 1 > len(max_substring)):
                    max_substring = s[l: r+1]
                l -=1
                r +=1
            # odd
            l, r = i, i+1
            while (l >= 0 and r <len(s) and s[l] == s[r]):
                if (r - l + 1 > len(max_substring)):
                    max_substring = s[l: r+1]
                l -=1
                r +=1
        
        return max_substring
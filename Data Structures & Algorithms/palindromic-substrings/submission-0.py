class Solution:
    def countSubstrings(self, s: str) -> int:
        total_counts = 0

        for i in range(len(s)):
            # odd
            total_counts += self.countPalindromic(s, i, i)
            # even
            total_counts += self.countPalindromic(s, i, i+1)
        
        return total_counts
        
    
    def countPalindromic(self, s: str, left: int, right: int) -> int:
        count = 0

        while (left >= 0 and right < len(s) and s[left] == s[right]):
            count += 1
            left -= 1
            right +=1
        
        return count
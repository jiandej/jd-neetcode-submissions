class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        prev = 1
        prev_prev = 0

        for i in range(n-1, -1, -1):
            val = int(s[i])

            if (val == 0):
                cur = 0
            else:
                cur = prev

            if (i < n-1 and 0 < val <= 2):
                combined_val = int(s[i:i+2])
                if (combined_val <= 26):
                    cur += prev_prev
            prev, prev_prev = cur, prev
        
        return cur
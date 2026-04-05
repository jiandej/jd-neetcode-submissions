class Solution:
    divider_char = "#"
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s))
            encoded_str += self.divider_char
            encoded_str += s
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        strs = []
        idx = 0
        while (idx < len(s)):
            lens_start = idx
            while (s[idx] != self.divider_char):
                idx += 1
            lens = int(s[lens_start:idx])
            idx += 1
            strs.append(s[idx:idx+lens])
            idx += lens
        
        return strs
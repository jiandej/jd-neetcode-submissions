class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = []
        for s in strs:
            encoded_str.append(f"{str(len(s))}#{s}")
        
        return "".join(encoded_str)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while (i < len(s)):
            j = i
            while (s[j] != "#"):
                j += 1
            length = int(s[i:j])
            j+=1
            strs.append(s[j:j+length])
            i = j+length
        
        return strs
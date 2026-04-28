class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        result = []
        self.backtracking(digits, 0, [], result, mapping)
        return result

    
    def backtracking(self, digits: str, idx: int, current: list[str], result: list[str], mapping: dict[str, list[str]]):
        if (idx == len(digits)):
            result.append("".join(current))
            return
        for char in mapping[digits[idx]]:
            current.append(char)
            self.backtracking(digits, idx+1, current, result, mapping)
            current.pop()
        
        return